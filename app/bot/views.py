import json
from nambaone.bot import Bot
from django.http import JsonResponse
from bot_project.settings import NAMBA_ONE_API_TOKEN


def entry(request):
    bot = Bot(NAMBA_ONE_API_TOKEN)

    '''
    Add handlers
    Handlers will be called with bot instance and nambaone.update.Update object

    bot.handler.add('message_new', message_new)
    '''
    if request.method == 'POST':
        bot.run(json.loads(request.body))

    return JsonResponse(bot.response, status=bot.response['code'])
