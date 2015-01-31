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

__all__ = ['test_acid_base_reactions', 'test_base_reactions', 'test_CML', 
           'test_compounds', 'test_isomorphism', 'test_periodic_helpers']


def helper(globs, verbosity=1):
    import sys
    import types
    import unittest

    test_classes_to_run = [value for key, value in globs.items()
                           if (isinstance(value, (type, types.ClassType))
                               and issubclass(value, unittest.TestCase))]

    loader = unittest.TestLoader()
    big_suite = unittest.TestSuite(loader.loadTestsFromTestCase(test_class)
                                   for test_class in test_classes_to_run)

    runner = unittest.TextTestRunner(sys.stdout, verbosity=verbosity)
    runner.run(big_suite)


def stdout_capture():
    import contextlib
    import sys
    import io

    @contextlib.contextmanager
    def capture():
        oldout, olderr = sys.stdout, sys.stderr

        try:
            out=[io.StringIO(), io.StringIO()]
            sys.stdout, sys.stderr = out
            yield out

        finally:
            sys.stdout, sys.stderr = oldout, olderr
            out[0] = out[0].getvalue()
            out[1] = out[1].getvalue()
    return capture