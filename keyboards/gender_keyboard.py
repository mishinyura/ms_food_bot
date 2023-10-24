from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def mark():
    markup = ReplyKeyboardMarkup(True, True)
    item_men = KeyboardButton('Мужчина')
    item_women = KeyboardButton('Женщина')
    markup.add(item_men, item_women)
    return markup
