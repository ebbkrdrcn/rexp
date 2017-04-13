#!/usr/bin/python

import re

class Pattern(object):

    def escepable(self):
        return True

    def __call__(self, *args, **kwargs):
        return '' if not len(args) else re.escape(args[0])

class DateTimePattern(Pattern):

    def __call__(self, *args, **kwargs):
        return ''

class IPAddressPattern(Pattern):

    __V4_EXPR = r'\b([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\b'
    __V6_EXPR = r'\b((([0-9A-Fa-f]{1,4}:){1,6}:)|(([0-9A-Fa-f]{1,4}:){7}))([0-9A-Fa-f]{1,4})\b'

    def __call__(self, *args, **kwargs):
        if not len(args):
            raise ValueError('Invalid IP address type!')

        return self.__V6_EXPR if not (args[0] or '').lower() == 'v6' \
            else self.__V4_EXPR

class RegexPattern(Pattern):

    def escepable(self):
        return False

    def __call__(self, *args, **kwargs):
        return args[0]

class RegexGroupPattern(Pattern):

    def __call__(self, *args, **kwargs):
        is_negative = kwargs['is_negative'] or False
        return '[%s%s]' % ('^' if is_negative else '', args[0])

class RegexNotPattern(Pattern):

    def escepable(self):
        return False

    def __call__(self, *args, **kwargs):
        return '(?!%s)' % args[0]

class KeyValuePairPattern(Pattern):

    def escepable(self):
        return False

    def __call__(self, *args, **kwargs):
        sep = r'=' if not len(args) else args[0]
        esced = re.escape(sep)
        cn = kwargs['capture_name']
        return r'\b(?P<{1}key>[^{0}\s]+)\s*{0}\s*(?P<{1}value>[^{0}]+)[\b\,\;]'.format(
            sep if sep == esced else esced, '%s_' % cn if cn else '')


DEFAULT_PATTERN_SET = dict(
    RE=RegexPattern(),
    BEGIN=r'^',
    END=r'$',
    GR=RegexGroupPattern(),
    NOT=RegexNotPattern(),
    SPACE=r'\s',
    ANY=r'.',
    INT=r'\d+',
    NUM=r'(\d+([,\.]\d+)*)',
    CH="\w",
    STR=r'("["]+")|(\'[\'+]\')',
    WORD=r'\b\w+\b',
    WORDS=r'\b(\w+\s*)*\b',
    DATE=DateTimePattern(),
    IP=IPAddressPattern(),
    IP4='${IP(v4)}',
    IP6='${IP(v6)}',
    PAIR=KeyValuePairPattern()
)