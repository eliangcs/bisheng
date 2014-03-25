import re
try:
    import cString as StringIO
except ImportError:
    import StringIO


# CJK characters
CHAR_CJK = (u'\u3040-\u30FF\u3105-\u312C\u3200-\u33FF\u3400-\u4DBF'
            u'\u4E00-\u9FFF\uAC00-\uD7AF\uF900-\uFAFF')

CHAR_ENG_LEFT = (u'\u0021\u0023-\u0026\\\u0029-\u005A\\\u005C-\\\u005E\u0061-\u007A'
                 u'\\\u007C\\\u007D'
                 u'\u00A2-\u00AA\u00AE-\u00BE\u00C0-\u02AF\u0370-\u052F\u1D00-\u1DBF'
                 u'\u1E00-\u1FFF\u2010-\u2016\u2019\u201D\u2020-\u2023\u2027'
                 u'\u2030-\u2034\u203A\u203C\u203D\u2043\u2044\u2046-\u2049\u205E'
                 u'\u2070-\u20CF\u2100-\u218F')

CHAR_ENG_RIGHT = (u'\u0023-\u0026\\\u0028\\\u002A\\\u002B\\\u002D\u002F-\u0039\u003C-\u003E'
                  u'\u0040-\\\u005C\\\u005E\u0061-\\\u007C'
                  u'\u00A1-\u00A9\u00AB\u00AC\u00AE-\u00AF\u00B1\u00B5-\u00B8'
                  u'\u00BC-\u02AF\u0370-\u052F\u1D00-\u1D9A\u1E00-\u1FFF'
                  u'\u2010-\u2016\u2018\u201A-\u201C\u201E-\u2023\u2027'
                  u'\u2030\u2031\u2039\u2043-\u2045\u205E\u20A0-\u20CF\u2100-\u218F')


# Patterns
PATTERN_ENG_CJK = re.compile(u'([%s])([%s])' % (CHAR_ENG_LEFT, CHAR_CJK))
PATTERN_CJK_ENG = re.compile(u'([%s])([%s])' % (CHAR_CJK, CHAR_ENG_RIGHT))


def add_spaces(text, exclude=None):
    if exclude:
        patt_exclude = u'[%s]' % re.escape(exclude)
        eng_left = re.sub(patt_exclude, u'', CHAR_ENG_LEFT)
        eng_right = re.sub(patt_exclude, u'', CHAR_ENG_RIGHT)
        patt_eng_cjk = re.compile(u'([%s])([%s])' % (eng_left, CHAR_CJK))
        patt_cjk_eng = re.compile(u'([%s])([%s])' % (CHAR_CJK, eng_right))
    else:
        patt_eng_cjk = PATTERN_ENG_CJK
        patt_cjk_eng = PATTERN_CJK_ENG

    def add_space_func(index1, index2):
        def add_space(match):
            return u'%s %s' % (match.group(index1), match.group(index2))
        return add_space

    text = patt_cjk_eng.subn(add_space_func(1, 2), text)[0]
    text = patt_eng_cjk.subn(add_space_func(1, 2), text)[0]

    # XXX"YYY"XXX -> XXX "YYY" XXX
    # where X and Y are CJK charaters
    is_left_dquote = True
    is_left_squote = True
    out = StringIO.StringIO()
    for i in xrange(len(text)):
        prev_char = text[i - 1] if i > 0 else None
        cur_char = text[i]
        next_char = text[i + 1] if i < len(text) - 1 else None
        if cur_char == u'\"':
            if is_left_dquote:
                if _is_cjk(prev_char):
                    out.write(u' \"')
                else:
                    out.write(u'\"')
                is_left_dquote = False
            else:
                if _is_cjk(next_char):
                    out.write(u'\" ')
                else:
                    out.write(u'\"')
                is_left_dquote = True
        elif cur_char == u'\'':
            if is_left_squote:
                if _is_cjk(prev_char):
                    out.write(u' \'')
                else:
                    out.write(u'\'')
                is_left_squote = False
            else:
                if _is_cjk(next_char):
                    out.write(u'\' ')
                else:
                    out.write(u'\'')
                is_left_squote = True
        else:
            out.write(cur_char)
    text = out.getvalue()
    out.close()
    return text


def _is_cjk(c):
    return ((c >= u'\u4E00' and c <= u'\u9FFF') or
            (c >= u'\u3040' and c <= u'\u30FF') or
            (c >= u'\u3105' and c <= u'\u312C') or
            (c >= u'\u3200' and c <= u'\u33FF') or
            (c >= u'\u3400' and c <= u'\u4DBF') or
            (c >= u'\uF900' and c <= u'\uFAFF'))
