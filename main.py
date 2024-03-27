import telebot
import webbrowser
import random
from telebot import types




bot = telebot.TeleBot('7092646647:AAGkXYVfQtXCyfZP6xxIABUMFUbos13mbTo')


def random_num():
    random_number = random.randint(1, 10)#первое число
    random_number2 = random.randint(1, 10)#второе число
    #bot.send_message(message.chat.id, str(random_number) + '*' + str(random_number2))
    random_number3 = random.randint(1, 3,)
    if random_number3 == 1:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(str(random_number*random_number2))
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton(str(random.randint(10, 100)))
        markup.row(btn2)
        btn3 = types.InlineKeyboardButton(str(random.randint(10, 100)))
        markup.row(btn3)
    elif random_number3 == 2:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(str(random.randint(10, 100)))
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton(str(random_number*random_number2))
        markup.row(btn2)
        btn3 = types.InlineKeyboardButton(str(random.randint(10, 100)))
        markup.row(btn3)
    else:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(str(random.randint(10, 100)))
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton(str(random.randint(10, 100)))
        markup.row(btn2)
        btn3 = types.InlineKeyboardButton(str(random_number*random_number2))
        markup.row(btn3)

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com/')
    bot.send_message(message.chat.id, 'Сайт запущен ')
@bot.message_handler(commands=['main'])
def main(message):
    bot.send_message(message.chat.id, '<b>MathBrain</b> - это бот для Telegram, который поможет школьникам улучшить свои знания в таблице умножения. С помощью интерактивных заданий и игр, этот проект с открытым исходным кодом поможет вам легко и весело освоить основы математики. Никогда раньше учить таблицу умножения не было так просто и увлекательно!', parse_mode='html')
@bot.message_handler(commands=['start', 'hello'])
def start(message):
    random_num()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> information', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    bot.reply_to(message, 'Крутая фотка!', reply_markup=markup)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'start' or message.text.lower() == 'hello' or message.text.lower() == 'старт':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'help':
        bot.send_message(message.chat.id, '<b>Help</b> information', parse_mode='html')
    elif message.text.lower() == 'site' or message.text.lower() =='website' or message.text.lower() == 'сайт' or message.text.lower() == 'вебсайт':
        webbrowser.open('https://www.google.com/')
        bot.send_message(message.chat.id, 'Сайт запущен ')
    elif message.text.lower() == 'основная информация' or message.text.lower() =='инфо' or message.text.lower() == 'инфа' or message.text.lower() == 'информация' or message.text.lower() == 'main' or message.text.lower() == 'info' or message.text.lower() == 'information':
        bot.send_message(message.chat.id, '<b>MathBrain</b> - это бот для Telegram, который поможет школьникам улучшить свои знания в таблице умножения. С помощью интерактивных заданий и игр, этот проект с открытым исходным кодом поможет вам легко и весело освоить основы математики. Никогда раньше учить таблицу умножения не было так просто и увлекательно!', parse_mode='html')
    elif message.text.lower() == 'help' or message.text.lower() == 'помощь' or message.text.lower() == 'помоги' or message.text.lower() == 'хелп':
        bot.send_message(message.chat.id, '<b>Help</b> information', parse_mode='html')

bot.infinity_polling()