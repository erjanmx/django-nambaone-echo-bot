import requests


class Bot:
    _response = {
        'code': 200,
        'success': True,
    }

    def __init__(self,
                 token,
                 base_url=None,
                 user_follow_handler=None,
                 user_unfollow_handler=None,
                 message_new_handler=None,
                 message_update_handler=None,
                 chat_new_handler=None):

        self._base_url = base_url or 'https://api.namba1.co'

        self._token = token

        self.handler = BotEventHandler(
            self,
            user_follow_handler,
            user_unfollow_handler,
            message_new_handler,
            message_update_handler,
            chat_new_handler
        )

    @property
    def response(self):
        self._response['success'] = self._response['code'] == 200
        return self._response

    @property
    def header(self):
        return {
            'X-Namba-Auth-Token': self._token
        }

    def run(self, request):
        event = str(request['event']).replace('/', '_')

        try:
            update = getattr(self.handler, 'event_{}'.format(event))(request['data'])
            self.__call_handler(event, update)
        except Exception as e:
            raise e
            self._response['code'] = 520

    def __call_handler(self, event, update):
        if hasattr(self.handler, event) and callable(getattr(self.handler, event)):
            getattr(self.handler, event)(self, update)

    def send_message(self, chat_id, content, content_type):
        params = {
            'type': content_type,
            'content': content,
        }
        url = '{}/chats/{}/write'.format(self._base_url, chat_id)

        response = requests.post(url, params, headers=self.header).json()

        return BotMessage.de_json(response['data'])

    def create_chat(self, user_id, name='', image=''):
        params = {
            'name': name,
            'image': image,
            'members[]': user_id,
        }
        url = '{}/chats/create'.format(self._base_url).json()

        response = requests.post(url, params)

        return BotChat.de_json(response['data'])

    def typing_start(self, chat_id):
        url = '{}/chats/{}/typing'.format(self._base_url, chat_id)

        return requests.get(url, headers=self.header)

    def typing_stop(self, chat_id):
        url = '{}/chats/{}/stoptyping'.format(self._base_url, chat_id)

        return requests.get(url, headers=self.header)


class BotEventHandler:
    def __init__(self,
                 bot,
                 user_follow_handler,
                 user_unfollow_handler,
                 message_new_handler,
                 message_update_handler,
                 chat_new_handler):

        self.bot = bot

        self.user_follow = user_follow_handler
        self.user_unfollow = user_unfollow_handler
        self.message_new = message_new_handler
        self.message_update = message_update_handler
        self.chat_new = chat_new_handler

    def add(self, event, handler):
        setattr(self, event, handler)

    @staticmethod
    def event_user_follow(request):
        user = BotUser(id=request['id'], name=request['name'], gender=request['gender'])

        return BotUpdate(user)

    @staticmethod
    def event_user_unfollow(request):
        user = BotUser(id=request['sender_id'])

        return BotUpdate(user)

    def event_message_new(self, request):
        chat = BotChat(id=request['chat_id'])
        user = BotUser(id=request['sender_id'])
        message = BotMessage(bot=self.bot, id=request['id'], type=request['type'], chat=chat,
                             status=request['status'], content=request['content'].strip())

        return BotUpdate(user, message, chat)

    @staticmethod
    def event_message_update(request):
        chat = BotChat(id=request['chat_id'])
        user = BotUser(id=request['sender_id'])
        message = BotMessage(bot=self.bot, id=request['id'], type=request['type'], chat=chat,
                             status=request['status'], content=request['content'].strip())

        return BotUpdate(user, message)

    @staticmethod
    def event_chat_new(request):
        user = BotUser(id=request['user']['id'], name=request['user']['name'], gender=request['user']['gender'])
        chat = BotChat(id=request['id'])

        return BotUpdate(user, chat)


class BotUpdate:

    def __init__(self, user=None, message=None, chat=None):
        self.user = user
        self.chat = chat
        self.message = message


class BotMessage:

    def __init__(self, id, chat, content, type, status=0, bot=None):
        self.id = id
        self.bot = bot
        self.chat = chat
        self.type = type
        self.status = status
        self.content = content

    def reply_typing(self):
        self.bot.typing_start(self.chat.id)

    def reply_text(self, content):
        self.bot.send_message(self.chat.id, content, 'text/plain')

    @staticmethod
    def de_json(data):
        chat = BotChat(id=data['chat_id'])
        message = BotMessage(id=data['id'], chat=chat, type=data['type'], content=data['content'])

        return message


class BotUser:

    def __init__(self, id, name='', gender=''):
        self.id = id
        self.name = name
        self.gender = gender


class BotChat:

    def __init__(self, id, name='', image=''):
        self.id = id
        self.name = name
        self.image = image

    @staticmethod
    def de_json(data):
        chat = BotChat(id=data['id'], name=data['name'], image=data['image'])

        return chat
