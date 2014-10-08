from unittest import TestCase
from mock import mock_open
import mock
from source.lib import utils

__author__ = 'Ivan'


class TestCreatePidfile(TestCase):
    def test_utils_open_called(self):
        pid = 1
        path = '/test/file'
        open = mock_open()
        with mock.patch('source.lib.utils.open', open, create=True) as utils_open_mock:
            with mock.patch('os.getpid', mock.Mock(return_value=pid)):
                utils.create_pidfile(path)
        utils_open_mock.assert_called_once_with(path, 'w')

    def test_write_called(self):
        pid = 1
        path = '/test/file'
        open = mock_open()
        with mock.patch('source.lib.utils.open', open, create=True):
            with mock.patch('os.getpid', mock.Mock(return_value=pid)):
                utils.create_pidfile(path)
        open().write.assert_called_once_with(str(pid))

    def test_os_getpid_called(self):
        pid = 1
        path = '/test/file'
        open = mock_open()
        with mock.patch('source.lib.utils.open', open, create=True):
            with mock.patch('os.getpid', mock.Mock(return_value=pid)) as os_getpid_mock:
                utils.create_pidfile(path)
        os_getpid_mock.assert_called_once_with()