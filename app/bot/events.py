
def event_message_new(bot, update):
    # echo everything
    bot.send_message(update.message.chat.id, update.message.content, update.message.type)

    # if content type does not matter simply call shortcut
    # update.message.reply_text(update.message.content)


def event_user_follow(bot, update):
    # create chat
    chat = bot.create_chat(update.user.id)

    # welcome new user
    bot.send_message(chat.id, 'Welcome, %s!' % update.user.name, 'text/plain')
