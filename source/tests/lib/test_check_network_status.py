import socket
from unittest import TestCase
import urllib2
import mock
from source.lib import utils

__author__ = 'Ivan'


class TestCheckNetworkStatus(TestCase):
    def test_valid_url(self):
        url = '/test/url'
        timeout = 10
        with mock.patch('urllib2.urlopen', mock.Mock()):
            self.assertTrue(utils.check_network_status(url, timeout))

    def test_socket_error(self):
        url = '/test/url'
        timeout = 10
        with mock.patch('urllib2.urlopen', mock.Mock(side_effect=socket.error)):
            self.assertFalse(utils.check_network_status(url, timeout))

    def test_value_error(self):
        url = '/test/url'
        timeout = 10
        with mock.patch('urllib2.urlopen', mock.Mock(side_effect=ValueError)):
            self.assertFalse(utils.check_network_status(url, timeout))

    def test_url_error(self):
        url = '/test/url'
        timeout = 10
        with mock.patch('urllib2.urlopen', mock.Mock(side_effect=urllib2.URLError(""))):
            self.assertFalse(utils.check_network_status(url, timeout))