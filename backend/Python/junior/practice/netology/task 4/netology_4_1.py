import telebot

token = ''

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def echo(message):
    msg = 'Ба! Знакомые все лица!' if 'Sam' in message.text else message.text
    bot.send_message(message.chat.id, msg)


bot.polling(none_stop=True)
