import random
import telebot
from telebot import types

bot = telebot.TeleBot('6368856712:AAEdMJgAWLdkT5ZI1fsBbeu08HucZ8d8huQ')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('Сгенерировать пример')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы сгенерировать пример умножения.", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def generate_question(message):
    if message.text == 'Сгенерировать пример':
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        question = f"Сколько будет {num1} * {num2}?"
        bot.send_message(message.chat.id, question)
        bot.register_next_step_handler(message, check_answer, num1, num2)


def check_answer(message, num1, num2):
    user_answer = message.text
    correct_answer = num1 * num2

    if user_answer == str(correct_answer):
        bot.send_message(message.chat.id, "Молодец! Правильно (Чтобы сгенерировать новый пример нажми на кнопку)")
    else:
        bot.send_message(message.chat.id, "Неправильно. Попробуй ещё(Нажми на кнопку)")

    # Генерация нового примера после проверки ответа
    generate_question(message)


bot.polling(none_stop=True)
