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

import argparse
import StringIO as IO

import make_clean
import runtests


parser = argparse.ArgumentParser(description="Runs the Chemistry simulator")
parser.add_argument(
                '-t', '--runtests', dest='runtests', 
                default=False, action='store_true',
                help='Signals that the tests, not the program, should be run')       
parser.add_argument(
                '-d', '--debugging', dest='debug',
                default=False, action='store_true',
                help="'".join(['Signals that specific content I',
                               'm working on debugging should be run']))
args = parser.parse_args()

if args.runtests:                
    make_clean.make_clean()
    runtests.main()
elif args.debug: ## This is just whatever I'm debugging/playing with at the moment
    import Chemistry.parsing.mol.molv2000 as mol
    import json
    from copy import copy
    benzene = IO.StringIO(""" benzene
 ACD/Labs0812062058
 
  6  6  0  0  0  0  0  0  0  0  1 V2000
    1.9050   -0.7932    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.9050   -2.1232    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.7531   -0.1282    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.7531   -2.7882    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.3987   -0.7932    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.3987   -2.1232    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  2  1  1  0  0  0  0
  3  1  2  0  0  0  0
  4  2  2  0  0  0  0
  5  3  1  0  0  0  0
  6  4  1  0  0  0  0
  6  5  2  0  0  0  0
 M  END
""")
    a = mol.MolV2000(benzene)
    a.parse()
    d = copy(vars(a))
    d.pop('moldata')
    d.pop('other')
    print json.dumps(d, indent=4)
else:
    raise NotImplementedError("I don't have a functional program yet...")
