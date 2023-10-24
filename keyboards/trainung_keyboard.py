from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def mark():
    markup = ReplyKeyboardMarkup(True, True)
    item1 = KeyboardButton('Не планирую заниматься')
    item2 = KeyboardButton('1-2 раза в неделю')
    item3 = KeyboardButton('3 раза в неделю')
    item4 = KeyboardButton('5 раз в неделю')
    item5 = KeyboardButton('Каждый день')
    markup.add(item1, item2, item3, item4, item5)
    return markup