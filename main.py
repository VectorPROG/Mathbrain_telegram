import random
import telebot
from telebot import types

bot = telebot.TeleBot('6368856712:AAEdMJgAWLdkT5ZI1fsBbeu08HucZ8d8huQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('Сгенерировать пример')
    markup.row(itembtn)
    bot.send_message(message.chat.id, "Press the button to generate a random number between 1 and 9.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Сгенерировать пример':
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        bot.send_message(message.chat.id, f"Сгенерированный пример: {num1} * {num2}")

bot.polling()
