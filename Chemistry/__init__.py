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


"""
This is the master __init__ file for the Chemistry repository.  File structure
should look something like

    Chemistry\
        docs\
            stuff
        molecules\
            test_molecules\
                *.cml
            *.cml
        parsing\
            __init__.py
            CheML.py
        reactions\
            __init__.py
            acid_base.py
        Testing\
            __init__.py
            test_*.py 
        LICENSE
        README.md
        element_list.csv
        __init__.py ## This file ##
        base_chemistry.py
        base_reactions.py
        compounds.py
        make_clean.py
        periodic_table.py
        runtests.py
        table_builder.py
        
There may be assorted *.txt *.log files lying around that just haven't been cleaned up yet
"""

__all__ = ['base_reactions', 'compounds', 'periodic_table', 'table_builder',
           'parsing', 'reactions']

__version__ = 0.0 ## pre-release

__author__ = ["Dan Obermiller"]