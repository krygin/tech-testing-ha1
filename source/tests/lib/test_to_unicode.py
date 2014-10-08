from unittest import TestCase
from source import lib

__author__ = 'Ivan'


class TestToUnicode(TestCase):
    def test_decoding(self):
        str = 'test str'
        unicode_str = u'test str'
        self.assertEqual(lib.to_unicode(str), unicode_str)