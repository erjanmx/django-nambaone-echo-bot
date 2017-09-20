import json
from namba_one.bot import Bot
from django.http import JsonResponse
from namba_one.settings import NAMBA_ONE_API_TOKEN


def message_new(bot, update):
    update.message.reply_text('Hi, there!')


def entry(request):
    bot = Bot(NAMBA_ONE_API_TOKEN, message_new_handler=message_new)

    bot.handler.add('message_new', message_new)

    if request.method == 'POST':
        bot.run(json.loads(request.body))

    return JsonResponse(bot.response, status=bot.response['code'])
