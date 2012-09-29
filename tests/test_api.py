 # -*- coding: utf-8 -*-
import unittest
import bisheng


class APITest(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(bisheng.add_spaces(u'測試test'), u'測試 test')


if __name__ == '__main__':
    unittest.main()
