from ast import Lambda
import telebot


bot = telebot.TeleBot('5614902466:AAG5AcR0rd5Yrl-myulxQKQLJvR1n0O6ydI')
users = set()

@bot.message_handler(func=lambda message: not message.from_user.is_bot)
def on_message(message):
    print(message)
    bot.send_message(message.from_user.id, "Сообщение отправлено!")

    for user in users:
        if user != message.from_user.id:
            bot.send_message(message.from_user.id, message.text)

    users.add(message.from_user.id)

bot.polling(non_stop=True)
