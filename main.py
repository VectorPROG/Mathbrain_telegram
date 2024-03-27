import telebot
import webbrowser
from telebot import types




bot = telebot.TeleBot('7092646647:AAGkXYVfQtXCyfZP6xxIABUMFUbos13mbTo')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com/')
    bot.send_message(message.chat.id, 'Сайт запущен ')
@bot.message_handler(commands=['main'])
def main(message):
    bot.send_message(message.chat.id, '<b>MathBrain</b> - это бот для Telegram, который поможет школьникам улучшить свои знания в таблице умножения. С помощью интерактивных заданий и игр, этот проект с открытым исходным кодом поможет вам легко и весело освоить основы математики. Никогда раньше учить таблицу умножения не было так просто и увлекательно!', parse_mode='html')
@bot.message_handler(commands=['start', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Delete')
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> information', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Крутая фотка!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
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