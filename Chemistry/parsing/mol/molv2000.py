#Copyright (c) 2014 Dan Obermiller
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
#You should have received a copy of the MIT License along with this program.
#If not, see <http://opensource.org/licenses/MIT>

try:
    import cStringIO as IO
except ImportError:
    try:
        import StringIO as IO
    except ImportError:
        import io as IO
finally:
    import re

    from Chemistry.exceptions.ParseErrors import ParsingException


class MolV2000(object):
    """Represents a molfile that follows the v2000 standard as a data structure
    in memory (instead of a text file/string)

    Lines 1-3 represent the header
      |  1: Title
      |  2: Software produced by
      |  3: Comment line
    Lines 4+ are the ctab block.  It can be split into a few sections:
      |  Counts line
      |  Atom block
      |  Bond block
      |  Atom list block
      |  Stext (structural text descriptor)
      |  Properties block

    Blank numerical values should be represented as `0`.  Spaces are significant
    and can indicate any of a number of things, such as:
        - absense of an entry
        - Empty character positions
        - Spaces between entries (single unless noted otherwise)
    """

    version = 'V2000'
    _counts_format = ('aaa', 'bbb', 'lll', 'fff', 'ccc', 'sss', 'xxx',
                      'rrr', 'ppp', 'iii', 'mmm', 'vvvvvv')

    count_meanings = {'aaa': 'number of atoms (max 255)',
                      'bbb': 'number of bonds (max 255)',
                      'lll': 'number of atom lists (max 30)',
                      'ccc': 'chiral flag. {0:chiral, 1:not_chiral}',
                      'sss': 'number of stext entries',
                      'mmm': ''.join(['number of lines of properties, ',
                                      'including `M END` (max 999)']),
                      'vvvvvv': 'the schema this obeys',
                      'fff': 'obsolete',
                      'xxx': 'obsolete',
                      'rrr': 'obsolete',
                      'ppp': 'obsolete',
                      'iii': 'obsolete'}

    def __init__(self, molfile, from_string=False):
        if from_string:
            self._moldata = IO.StringIO(molfile)
        elif isinstance(molfile, basestring):
            try:
                with open(molfile, 'r') as f:
                    self._moldata = IO.StringIO(f.read())
            except IOError:
                raise ParsingException(
                    ' '.join(["MolV2000 given {}, wasn't a valid file",
                               "\nIf you would like to parse a string",
                               "then pass the kwarg `from_string=True"])
                            .format(molfile))
        elif hasattr(molfile, "read"):
            self._moldata = IO.StringIO(molfile.read())
        else:
            raise TypeError(
                "MolV2000 must be given something it can read data from")

    def __getattr__(self, attr):
        return getattr(self._moldata, attr)

    def parse(self):
        """Parses the data.  Uses the MolV2000Parser wrapper to parse the data
        line by line and then add various instance variables to the current
        instance (not the parser object which just wraps this)
        """

        MolV2000Parser(self)
        self.other = {k:v for k, v in vars(self).iteritems()
                      if k not in ['atoms', 'bonds'] and
                      not k.startswith('_')}

    def __str__(self):
        if hasattr(self, "title"):
            return "MolV2000 data representing {}".format(self.title)
        else:
            return "MolV2000 data object"

    def __repr__(self):
        return str(self)


class MolV2000Parser(object):
    """Parser object for molfiles conforming to the V2000 standard. Is just a
    wrapper over the underlying molfile object
    """

    _molfile = None

    def __init__(self, molv2000):
        self.molfile = molv2000
        self.parse_file()

    @property
    def molfile(self):
        """The underlying molfile object of the parser"""

        return self._molfile

    @molfile.setter
    def molfile(self, molv2000):
        if not isinstance(molv2000, MolV2000):
            self._molfile = MolV2000(molv2000)
        else:
            self._molfile = molv2000

    def __getattr__(self, attr):
        return getattr(self.molfile, attr)

    def __setattr__(self, attr, value):
        if attr in ['_molfile', 'molfile']:
            exec("self.__dict__['{}'] = value".format(attr),
                 globals(),
                 locals())
        else:
            self._molfile.__setattr__(attr, value)

    def parse_file(self):
        """Parses the molfile."""

        lines = self.readlines()
        self._parse_header(lines[:3])
        self._parse_body(lines[3:])

    def _parse_header(self, lines):
        """Parses the header of the molfile.

        Expects three lines so don't cut off leading whitespace (sometimes the
        headers get truncated.  This is bad mkay).
        """

        if len(lines) != 3:
            raise ParsingException(
                "Header must have three lines, not {}".format(len(lines)))

        self.title = lines[0].strip()
        self.info = lines[1].strip()
        self.comments = (lines[2].strip() if lines[2].strip() else None)

    def _parse_body(self, lines):
        """Parses the body of the function."""

        line_start, line_end = 0, 1
        self._parse_counts_line(lines[0])

        line_start, line_end = line_end, line_end + int(self.counts['aaa'])
        self._parse_atom_block(lines[line_start:line_end])

        line_start, line_end = line_end, line_end + int(self.counts['bbb'])
        self._parse_bond_block(lines[line_start:line_end])

        line_start, line_end = line_end, line_end + int(self.counts['lll'])
        self._parse_atom_list_block(lines[line_start:line_end])

        line_start, line_end = line_end, line_end + int(self.counts['sss'])
        self._parse_stext_block(lines[line_start:line_end])

        line_start, line_end = line_end, line_end + int(self.counts['mmm'])
        self._parse_properties_block(lines[line_start:line_end])

    def _parse_counts_line(self, line):
        """The counts line has the general form of

        aaabbblllfffcccsssxxxrrrpppiiimmmvvvvvv

        Where:

            aaa -> number of atoms (max 255)
            bbb -> number of bonds (max 255)
            lll -> number of atom lists (max 30)
            ccc -> chiral flag. {0:chiral, 1:not_chiral}
            sss -> number of stext entries
            mmm -> number of lines of properties, including `M END` (max 999)
            vvvvvv -> schema this obeys
            fff, xxx, rrr, ppp, iii -> obsolete
        """

        self.counts = {}
        i = 0
        for sequence in MolV2000._counts_format:
            try:
                self.counts[sequence] = line[i:i+len(sequence)].strip()
            except IndexError:
                self.counts[sequence] = line[i:].strip()
                raise StopIteration
            i+= len(sequence)

        self.version = self.counts['vvvvvv']
        if not self.version == MolV2000.version:
            raise ParsingException(
                "{{}} file is in {} not {}".format(self.version,
                                                   MolV2000.version))

    def _parse_atom_block(self, lines):
        """Parses the atom block"""

        properly_formed = re.compile(r"""
                    (\s+[-.0-9]+){3} # matches the X, Y, and Z coordinates
                    \s+[A-Z]{1}[a-z]{,2} # matches the chemical symbol
                    (\s+[-.0-9]+){,12} # matches the series of values
                                      """, re.X)
        self.atoms = {}
        self._atoms = {}
        for i, line in enumerate(lines, 1):
            match = properly_formed.match(line)
            if match:
                atom = line.split()
                self.atoms['a{}'.format(i)] = {'coords':
                                                    map(float, [atom.pop(0),
                                                                atom.pop(0),
                                                                atom.pop(0)]),
                                               'symbol': atom.pop(0)}
                # I don't know what all this stuff means yet, so I won't
                # bother doing anything with it
                self._atoms['a{}'.format(i)] = atom
            else:
                raise ParsingException("Malformed atom text")

    def _parse_bond_block(self, lines):
        """Parses the bond block"""

        properly_formed = re.compile(r"(\s+[0-9]+){,7}")
        self.bonds = {}
        self._bonds = {}
        for i, line in enumerate(lines, 1):
            match = properly_formed.match(line)
            if match:
                bond = line.split()
                self.bonds['b{}'.format(i)] = ('a{}'.format(bond.pop(0)),
                                               'a{}'.format(bond.pop(0)),
                                               {'order': int(bond.pop(0)),
                                                'chirality': None})
                self._bonds['b{}'.format(i)] = bond
            else:
                raise ParsingException("Malformed bond text")

    def _parse_atom_list_block(self, lines):
        """Parses the atom list block.

        I don't really know what this is, yet
        """

        if lines:
            raise NotImplementedError("I don't know how to parse these")

    def _parse_stext_block(self, lines):
        """Parses the stext block

        I don't really know what this is yet
        """

        if lines:
            raise NotImplementedError("I don't know how to parse these")

    def _parse_properties_block(self, lines):
        """Parses the properties block.

        I haven't really seen an example of what this would look like
        """

        self.properties = {}
        line_end = re.compile(r"\s*M\s*END")
        for i, line in enumerate(lines, 1):
            if line_end.match(line):
                return
            else:
                self.properties['p{}'.format(i)] = line


class MolV2000Builder(object):

    def __init__(self):
        raise NotImplementedError

    @classmethod
    def from_Compound(cls, compound):
        raise NotImplementedError

    def __str__(self):
        return "MolV2000 Builder"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    pass
