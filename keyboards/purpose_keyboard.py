from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def mark():
    markup = ReplyKeyboardMarkup(True, True)
    item1 = KeyboardButton('Быстрое похудение')
    item2 = KeyboardButton('Умеренное похудение')
    item3 = KeyboardButton('Поддержание веса')
    item4 = KeyboardButton('Умеренный набор')
    item5 = KeyboardButton('Быстрый набор')
    markup.add(item1, item2, item3, item4, item5)
    return markup