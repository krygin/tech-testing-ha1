import argparse
from unittest import TestCase
from source.lib import utils

__author__ = 'Ivan'


class TestParseCmdArgs(TestCase):
    def test_raised_exception_without_required_argument(self):
        description = 'description'
        args = '%s' % description
        self.assertRaises(SystemExit, utils.parse_cmd_args, (args, description))

    def test_all_full_name_argument_parsed(self):
        path = '/test/path'
        pid = 1
        description = 'description'
        args = ['--config', path, '--daemon', '--pid', str(pid)]
        result = utils.parse_cmd_args(args, description)
        self.assertEqual(result, argparse.Namespace(config=path, daemon=True, pidfile=str(pid)))

    def test_all_short_name_argument_parsed(self):
        path = '/test/path'
        pid = 1
        description = 'description'
        args = ['-c', path, '-d', '-P', str(pid)]
        result = utils.parse_cmd_args(args, description)
        self.assertEqual(result, argparse.Namespace(config=path, daemon=True, pidfile=str(pid)))

    def test_mixed_name_argument_parsed_without_daemon_flag(self):
        path = '/test/path'
        pid = 1
        description = 'description'
        args = ['-c', path, '--pid', str(pid)]
        result = utils.parse_cmd_args(args, description)
        self.assertEqual(result, argparse.Namespace(config=path, daemon=False, pidfile=str(pid)))