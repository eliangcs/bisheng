# -*- coding: utf-8 -*-
import bisheng
import unittest


class AddSpacesTest(unittest.TestCase):

    def test_trad_chinese(self):
        self.assertEqual(bisheng.add_spaces(u'測試test'), u'測試 test')
        self.assertEqual(bisheng.add_spaces(u'Hello世界'), u'Hello 世界')
        self.assertEqual(bisheng.add_spaces(u'阿Q正傳'), u'阿 Q 正傳')

    def test_simp_chinese(self):
        self.assertEqual(bisheng.add_spaces(u'测试test'), u'测试 test')
        self.assertEqual(bisheng.add_spaces(u'Hello世界'), u'Hello 世界')
        self.assertEqual(bisheng.add_spaces(u'阿Q正传'), u'阿 Q 正传')

    def test_japanese(self):
        self.assertEqual(bisheng.add_spaces(u'樊隊じょtest'), u'樊隊じょ test')
        self.assertEqual(bisheng.add_spaces(u'Helloブケひゃ'), u'Hello ブケひゃ')
        self.assertEqual(bisheng.add_spaces(u'ブケひゃQちょ'), u'ブケひゃ Q ちょ')

    def test_korean(self):
        self.assertEqual(bisheng.add_spaces(u'듯하더니test'), u'듯하더니 test')
        self.assertEqual(bisheng.add_spaces(u'Hello바라보느냐'), u'Hello 바라보느냐')
        self.assertEqual(bisheng.add_spaces(u'김첨Q지는'), u'김첨 Q 지는')

    def test_fullwidth_punctuation(self):
        self.assertEqual(bisheng.add_spaces(u'hello，世界'), u'hello，世界')
        self.assertEqual(bisheng.add_spaces(u'hello。世界'), u'hello。世界')
        self.assertEqual(bisheng.add_spaces(u'hello！世界'), u'hello！世界')
        self.assertEqual(bisheng.add_spaces(u'hello「世界」'), u'hello「世界」')
        self.assertEqual(bisheng.add_spaces(u'hello（世界）'), u'hello（世界）')

    def test_halfwidth_punctuation(self):
        self.assertEqual(bisheng.add_spaces(u'hello,世界'), u'hello, 世界')
        self.assertEqual(bisheng.add_spaces(u'hello.世界'), u'hello. 世界')
        self.assertEqual(bisheng.add_spaces(u'hello!世界'), u'hello! 世界')
        self.assertEqual(bisheng.add_spaces(u'hello[世界]'), u'hello[世界]')
        self.assertEqual(bisheng.add_spaces(u'hello(世界)'), u'hello(世界)')

        self.assertEqual(bisheng.add_spaces(u'你好,世界'), u'你好, 世界')
        self.assertEqual(bisheng.add_spaces(u'你好.世界'), u'你好. 世界')
        self.assertEqual(bisheng.add_spaces(u'你好!世界'), u'你好! 世界')
        self.assertEqual(bisheng.add_spaces(u'你好[世界]'), u'你好 [世界]')
        self.assertEqual(bisheng.add_spaces(u'你好(世界)'), u'你好 (世界)')

    def test_double_quotes(self):
        self.assertEqual(bisheng.add_spaces(u'"hello"世界'), u'"hello" 世界')
        self.assertEqual(bisheng.add_spaces(u'hello"世界"'), u'hello"世界"')

    def test_single_quotes(self):
        self.assertEqual(bisheng.add_spaces(u"'hello'世界"), u"'hello' 世界")
        self.assertEqual(bisheng.add_spaces(u"hello'世界'"), u"hello'世界'")
        self.assertEqual(bisheng.add_spaces(u"你好'世界'"), u"你好 '世界'")
        self.assertEqual(bisheng.add_spaces(u"'hello'world'"), u"'hello'world'")

    def test_exclude(self):
        self.assertEqual(bisheng.add_spaces(u'方[括]孤'), u'方 [括] 孤')
        self.assertEqual(bisheng.add_spaces(u'方[括]孤', exclude='['), u'方[括] 孤')
        self.assertEqual(bisheng.add_spaces(u'方[括]孤', exclude='[]'), u'方[括]孤')

        self.assertEqual(bisheng.add_spaces(u'圓(括)孤方[括]孤'), u'圓 (括) 孤方 [括] 孤')
        self.assertEqual(bisheng.add_spaces(u'圓(括)孤方[括]孤', exclude='[)'), u'圓 (括)孤方[括] 孤')
        self.assertEqual(bisheng.add_spaces(u'圓(括)孤方[括]孤', exclude='[]()'), u'圓(括)孤方[括]孤')

        self.assertEqual(bisheng.add_spaces(u'雙"引"號'), u'雙 "引" 號')
        self.assertEqual(bisheng.add_spaces(u'雙"引"號', exclude='"'), u'雙"引"號')


class JianFanTest(unittest.TestCase):

    def test_to_simp(self):
        self.assertEqual(
            bisheng.to_simp(u'也最情大友安你然開物世需不書「活情」何，空會這天歡作臺。'),
            u'也最情大友安你然开物世需不书“活情”何，空会这天欢作台。')

    def test_to_trad(self):
        self.assertEqual(
            bisheng.to_trad(u'也最情大友安你然开物世需不书“活情”何，空会这天欢作台。'),
            u'也最情大友安你然開物世需不書「活情」何，空會這天歡作台。')


if __name__ == '__main__':
    unittest.main()
