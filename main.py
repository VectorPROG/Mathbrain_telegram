import random
import telebot
from telebot import types

bot = telebot.TeleBot('7092646647:AAGkXYVfQtXCyfZP6xxIABUMFUbos13mbTo')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Здесь будет информация для помощи')
@bot.message_handler(commands=['main'])
def start(message):
    bot.send_message(message.chat.id, 'MathBrain - это бот для Telegram, который поможет школьникам улучшить свои знания в таблице умножения. С помощью интерактивных заданий и игр, этот проект с открытым исходным кодом поможет вам легко и весело освоить основы математики. Никогда раньше учить таблицу умножения не было так просто и увлекательно!')
@bot.message_handler(commands=['site', 'website'])
def start(message):
    bot.send_message(message.chat.id, 'По этой команде будет открываться сайт проекта. Сейчас он в разработке')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('Сгенерировать пример')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "Привет, "+ message.from_user.first_name)
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
