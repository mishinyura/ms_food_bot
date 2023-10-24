from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'help')