from unittest import TestCase
from source import lib

__author__ = 'Ivan'


class TestToStr(TestCase):
    def test_decoding(self):
        str = 'test str'
        unicode_str = u'test str'
        self.assertEqual(str, lib.to_str(unicode_str))