# -*- coding: utf-8 -*-
import bisheng
import unittest


class AddSpacesTest(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(bisheng.add_spaces(u'測試test'), u'測試 test')
        self.assertEqual(bisheng.add_spaces(u'Hello世界'), u'Hello 世界')
        self.assertEqual(bisheng.add_spaces(u'阿Q正傳'), u'阿 Q 正傳')

    def test_exclude(self):
        self.assertEqual(bisheng.add_spaces(u'方[括]孤'), u'方 [括] 孤')
        self.assertEqual(bisheng.add_spaces(u'方[括]孤', exclude='['), u'方[括] 孤')
        self.assertEqual(bisheng.add_spaces(u'方[括]孤', exclude='[]'), u'方[括]孤')


if __name__ == '__main__':
    unittest.main()
