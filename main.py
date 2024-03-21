import datetime


import telebot

from config import TOKEN
from dbAdmin import createdb, createdbchoice, createstattable

bot = telebot.TeleBot(TOKEN)

def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0<= current_time.hour <6:
        return 'Доброй ночи!'
    if 6<= current_time.hour <12:
        return 'Доброе утро!'
    if 12<= current_time.hour <18:
        return 'Добрый день!'
    else:
        return 'Добрый вечер!'

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'{get_welcome()} Я бот, который подготовил для тебя интересный опрос✏'

    bot.send_message(message.chat.id, text)




if __name__=='__main__':
    createstattable()
    createdbchoice()
    createdb()
    print ('Бот запущен')
    bot.infinity_polling()