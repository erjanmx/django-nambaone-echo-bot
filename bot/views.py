import json
import logging
from nambaone.bot import Bot
from django.http import JsonResponse
from bot_project.settings import NAMBA_ONE_API_TOKEN
from bot.events import event_user_follow, event_message_new

logger = logging.getLogger('bot')


def error(bot, e):
    logging.error('Event "%s" caused error "%s"' % (e['event'], e['error']),
                  exc_info=True)


def entry(request):
    bot = Bot(NAMBA_ONE_API_TOKEN, error_handler=error)

    '''
    Add handlers
    Handlers will be called with bot instance and nambaone.update.Update object
    '''
    bot.handler.add('user_follow', event_user_follow)
    bot.handler.add('message_new', event_message_new)

    if request.method == 'POST':
        bot.run(json.loads(request.body))

    return JsonResponse(bot.response, status=bot.response['code'])
