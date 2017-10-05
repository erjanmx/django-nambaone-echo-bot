from unittest import mock, TestCase
from unittest.mock import MagicMock
from bot.events import event_message_new, event_user_follow


class TestEvents(TestCase):

    def setUp(self):
        self.bot_mock = MagicMock()
        self.update_mock = MagicMock()

    def test_event_message_new(self):
        self.update_mock.message.chat.id = 1000
        self.update_mock.message.content = 'message'
        self.update_mock.message.type = 'text/plain'

        event_message_new(self.bot_mock, self.update_mock)

        self.bot_mock.send_message.assert_called_once_with(
            1000,
            'message',
            'text/plain'
        )

    def test_event_user_follow(self):
        chat_mock = MagicMock
        chat_mock.id = 1000

        self.update_mock.user.id = 1
        self.bot_mock.create_chat.return_value = chat_mock

        event_user_follow(self.bot_mock, self.update_mock)

        self.bot_mock.create_chat.assert_called_once_with(1)
        self.bot_mock.send_message.assert_called_once_with(
            1000, mock.ANY, 'text/plain'
        )
