# Copyright (c) 2014 Dan Obermiller
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# You should have received a copy of the MIT License along with this program.
# If not, see <http://opensource.org/licenses/MIT>

import argparse


parser = argparse.ArgumentParser(description="Runs the Chemistry simulator")
parser.add_argument('-c', '--clean', dest='clean',
                    default=False, action='store_true',
                    help='Signals that the directory should get cleaned up')
parser.add_argument('-g', '--gui', dest='gui', default=False, action='store_true',
                    help='Runs the GUI')
args = parser.parse_args()

if args.clean:
    from scripts.make_clean import make_clean
    from scripts.strip_whitespace import strip_whitespace

    make_clean()
    strip_whitespace()

if args.gui:
    import sys
    sys.argv = sys.argv[:1]   # kivy messes up if I don't do this
    from Chemistry import chemgui
    chemgui.main()
else:   # Whatever I'm trying at the moment
    pass
