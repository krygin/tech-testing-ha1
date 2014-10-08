import mock
import requests
from unittest import TestCase
from source import notification_pusher

__author__ = 'Ivan'


class TestNotificationWorker(TestCase):
    def test_task_put_into_queue_with_bury_if_request_exception_raised(self):
        url = '/test/url'
        task = mock.Mock()
        task.task_id = 1
        task.data = {
            'callback_url': url
        }
        task_queue = mock.Mock()
        task_queue.put = mock.Mock()
        with mock.patch('source.notification_pusher.requests.post', mock.Mock(side_effect=requests.RequestException)):
            with mock.patch('source.notification_pusher.logger', mock.Mock()):
                notification_pusher.notification_worker(task, task_queue)
        task_queue.put.assert_called_once_with((task, 'bury'))

    def test_task_put_into_queue_with_ack(self):
        url = '/test/url'
        task = mock.Mock()
        task.task_id = 1
        task.data = {
            'callback_url': url
        }
        task_queue = mock.Mock()
        task_queue.put = mock.Mock()
        with mock.patch('source.notification_pusher.requests.post', mock.Mock()):
            with mock.patch('source.notification_pusher.logger', mock.Mock()):
                notification_pusher.notification_worker(task, task_queue)
        task_queue.put.assert_called_once_with((task, 'ack'))