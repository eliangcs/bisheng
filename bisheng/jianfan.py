# Modified from Jianfan: https://code.google.com/p/python-jianfan/
#
# Copyright (c) Jianfan developers.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
#
#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#
#     3. Neither the name of Jianfan nor the names of its contributors may be used
#        to endorse or promote products derived from this software without
#        specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import codecs
import os


def _load_char_table(file_path):
    table = {}
    with codecs.open(file_path, 'r', 'utf-8') as f:
        for line in f:
            orig, replacement = line[0], line[1]
            table[orig] = replacement
    return table


dir_path = os.path.abspath(os.path.dirname(__file__))

S2T = _load_char_table(os.path.join(dir_path, 's2t.txt'))
T2S = _load_char_table(os.path.join(dir_path, 't2s.txt'))


def _translate(unistr, table):
    '''Replace characters using a table.'''
    if type(unistr) is str:
        try:
            unistr = unistr.decode('utf-8')
        # Python 3 returns AttributeError when .decode() is called on a str
        # This means it is already unicode.
        except AttributeError:
            pass
    try:
        if type(unistr) is not unicode:
            return unistr
    # Python 3 returns NameError because unicode is not a type.
    except NameError:
        pass

    chars = []
    for c in unistr:
        replacement = table.get(c)
        chars.append(replacement if replacement else c)
    return u''.join(chars)


def to_trad(text):
    '''Translate to traditional Chinese.'''
    return _translate(text, S2T)


def to_simp(text):
    '''Translate to simplified Chinese.'''
    return _translate(text, T2S)
