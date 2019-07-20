import telebot

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello there!")
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply(message, message.text)

bot.polling(none_stop=True)