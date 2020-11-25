from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "1312879248:AAEqJKttgVbftYDQvN6OvKmVlc4NuGswYWY"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
updater.start_polling()

# 대본
def handler(bot, update):
    text = update.message.text  # 메시지
    chat_id = update.message.chat_id    # 챗 아이디

    if '모해' in text:
        bot.send_message(chat_id=chat_id, text='너 생각')
    elif '아잉' in text:
        bot.send_message(chat_id=chat_id, text='아잉')
    else:
        bot.send_message(chat_id=chat_id, text='뭐라구?')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)