#!/usr/bin/env python2.7

import os
import sys
import unittest

source_dir = os.path.join(os.path.dirname(__file__), 'source')
sys.path.insert(0, source_dir)

from source.tests.lib.test_daemonize import TestDaemonize
from source.tests.lib.test_create_pidfile import TestCreatePidfile
from source.tests.lib.test_load_config_from_pyfile import TestLoadConfigFromPyfile
from source.tests.lib.test_parse_cmd_args import TestParseCmdArgs
from source.tests.lib.test_spawn_workers import TestSpawnWorkers
from source.tests.lib.test_check_network_status import TestCheckNetworkStatus
from source.tests.lib.test_get_redirect_history_from_task import TestGetRedirectHistoryFromTask
from source.tests.lib.test_worker import TestWorker
from source.tests.test_main_loop import TestMainLoop
from source.tests.test_main import TestMain
from source.tests.test_notification_worker import TestNotificationWorker
from source.tests.test_done_with_processed_tasks import TestDoneWithProcessedTasks
from source.tests.test_stop_handler import TestStopHandler
from source.tests.test_install_signal_handlers import TestInstallSignalHandlers

from source.tests.lib.test_to_unicode import TestToUnicode
from source.tests.lib.test_to_str import TestToStr
from source.tests.lib.test_get_counters import TestGetCounters
from source.tests.lib.test_check_for_meta import TestCheckForMeta
from source.tests.lib.test_fix_market_url import TestFixMarketUrl
from source.tests.lib.test_make_pycurl_request import TestMakePycurlRequest
from source.tests.lib.test_get_url import TestGetUrl
from source.tests.lib.test_get_redirect_history import TestGetRedirectHistory

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestDaemonize),
        unittest.makeSuite(TestCreatePidfile),
        unittest.makeSuite(TestLoadConfigFromPyfile),
        unittest.makeSuite(TestParseCmdArgs),
        unittest.makeSuite(TestSpawnWorkers),
        unittest.makeSuite(TestCheckNetworkStatus),
        unittest.makeSuite(TestGetRedirectHistoryFromTask),
        unittest.makeSuite(TestWorker),

        unittest.makeSuite(TestMainLoop),
        unittest.makeSuite(TestMain),

        unittest.makeSuite(TestNotificationWorker),
        unittest.makeSuite(TestDoneWithProcessedTasks),
        unittest.makeSuite(TestStopHandler),
        unittest.makeSuite(TestInstallSignalHandlers),

        unittest.makeSuite(TestToUnicode),
        unittest.makeSuite(TestToStr),
        unittest.makeSuite(TestGetCounters),
        unittest.makeSuite(TestCheckForMeta),
        unittest.makeSuite(TestFixMarketUrl),
        unittest.makeSuite(TestMakePycurlRequest),
        unittest.makeSuite(TestGetUrl),
        unittest.makeSuite(TestGetRedirectHistory),


    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
