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

import unittest

from Chemistry.base import table_builder as tb


class test_helpers(unittest.TestCase):

    def setUp(self): pass

    def tearDown(self): pass

    def test_convert_type1(self):
        self.assertEqual(tb.convert_type('1', int), 1)

    def test_convert_type2(self):
        self.assertEqual(tb.convert_type('1.0', float), 1.0)

    def test_convert_type3(self):
        self.assertEqual(tb.convert_type('Hello', str), 'Hello')

    def test_convert_type4(self):
        self.assertEqual(tb.convert_type('[1,2,3]', tb.str_to_list), [1, 2, 3])

    def test_convert_type_bad(self):
        self.assertIsNone(tb.convert_type('No Data', int))

    def test_str_to_list1(self):
        self.assertEqual(tb.str_to_list('[1,2,3]'), ['1', '2', '3'])

    def test_str_to_list2(self):
        self.assertEqual(tb.str_to_list('[1,2,3]', mapped=int), [1, 2, 3])

    def test_build_table(self):
        self.assertFalse(tb.build_table())


if __name__ == '__main__':
    from . import helper
    helper(globals())
