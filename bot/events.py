
def event_message_new(bot, update):
    # echo everything
    bot.send_message(
        update.message.chat.id,
        update.message.content,
        update.message.type
    )
    # if content type does not matter simply call shortcut
    # update.message.reply_text(update.message.content)


def event_user_follow(bot, update):
    # create chat
    chat = bot.create_chat(update.user.id)

    greeting_text = 'Привет, {}!\nЯ echo-bot, пример бота на Django \
запущеного на сервере Heroku, исходный код доступен на GitHub \
\nПовторяю все, что ты мне отправляешь.'

    # welcome new user
    bot.send_message(
        chat.id,
        greeting_text.format(update.user.name),
        'text/plain'
    )
