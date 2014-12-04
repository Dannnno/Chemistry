"""
Copyright (c) 2014 Dan Obermiller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

You should have received a copy of the MIT License along with this program.
If not, see <http://opensource.org/licenses/MIT>
"""

from Chemistry.parsing.exceptions import ParsingException


class MolV2000(object):
    """Represents a molfile that follows the v2000 standard
    
    Lines 1-3 represent the header
    1: Title
    2: Software produced by
    3: Comment line
    Lines 4: are the ctab block.  It can generally be split into a few sections:
        Counts line
        Atom block
        Bond block
        Atom list block
        Stext (structural text descriptor)
        Properties block
        
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
                      'mmm': 'number of lines of properties, including `M END` (max 999)',
                      'vvvvvv': 'schema this obeys',
                      'fff': 'obsolete',
                      'xxx': 'obsolete',
                      'rrr': 'obsolete',
                      'ppp': 'obsolete',
                      'iii': 'obsolete'}
    
    def __init__(self, molfile): pass
    
    def _parse_counts_line(self, line):
        """ The counts line has the general form of
        
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
            
        for key in MolV2000._counts_format:
            print "{}|{}|".format(key, self.counts[key])
        
        self._version = self.counts['vvvvvv']
        if not self._version == MolV2000.version:
            raise ParsingException(
                "{{}} file is in {} not {}".format(self._version,
                                                   MolV2000.version))
    
    
class MolV2000Parser(object):
    
    pass
    
    
class MolV2000Builder(object):
    
    pass


if __name__ == '__main__':
    a = MolV2000('')
    a._parse_counts_line('v30000')
