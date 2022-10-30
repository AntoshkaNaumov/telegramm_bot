from mimetypes import common_types
import telebot


bot = telebot.TeleBot('5742777204:AAH8RflW8JFx43DFqK54Spl2xx3JBe5_ViI')


def f(message):
    return message.text == '1'


#@bot.message_handler(func = lambda message: True)
#def start(message):
#    #bot.send_message(message.chat.id, 'Привет!')
#    bot.reply_to(message, 'Привет!')



@bot.message_handler(content_types=['photo', 'video'])
def answer(message):
    bot.send_message(message.chat.id, 'Cool!!!')


@bot.message_handler(commands =['start'])
def format_text(message):
    bot.send_message(message.chat.id, '<b>Какой-то</b> текст', parse_mode='HTML')


bot.polling()
