from telebot.types import Message
from loader import bot
from states.user_info import UserInfo
from config.config import WELCOME_TEXT
from keyboards import gender_keyboard, purpose_keyboard, trainung_keyboard


@bot.message_handler(commands=['start'])
def send_welcome(message: Message) -> None:
    bot.send_message(message.from_user.id, WELCOME_TEXT)
    bot.set_state(message.from_user.id, UserInfo.name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['telegram_user_id'] = message.from_user.id


@bot.message_handler(state=UserInfo.name)
def get_name(message: Message) -> None:
    if ''.join(message.text.split()).isalpha():
        text = f'Приятно познакомиться, {message.text.title()}\n\nУточни свой пол:'
        bot.send_message(message.from_user.id, text, reply_markup=gender_keyboard.mark())
        bot.set_state(message.from_user.id, UserInfo.gender, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text
    else:
        text_error = 'Это не похоже на настоящее имя. ' \
                     'Однако спасибо за шутку. Мы с Дуровым посмеялись:)\n' \
                     'И все же, хотелось бы настоящее имя'
        bot.send_message(message.from_user.id, text_error)


@bot.message_handler(state=UserInfo.gender)
def get_gender(message: Message) -> None:
    text = f'Отлично.\n\nДля более правильного подсчета калорий, нужен твой возраст.'
    bot.send_message(message.from_user.id, text)
    bot.set_state(message.from_user.id, UserInfo.age, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['gender'] = message.text


@bot.message_handler(state=UserInfo.age)
def get_age(message: Message) -> None:
    if message.text.isdigit():
        text = f'Оказывается, мы с тобой ровесники. Нам явно будет о чем по болтать:)\n\nУкажи свой вес'
        bot.send_message(message.from_user.id, text)
        bot.set_state(message.from_user.id, UserInfo.weight, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['age'] = message.text
    else:
        text_error = ''
        bot.send_message(message.from_user.id, text_error)


@bot.message_handler(state=UserInfo.weight)
def get_weight(message: Message) -> None:
    if message.text.isdigit():
        text = 'Какой у тебя рост?'
        bot.send_message(message.from_user.id, text)
        bot.set_state(message.from_user.id, UserInfo.height, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['weight'] = message.text
    else:
        text_error = 'Странное значение. А можно в числах и с реальным значением?'
        bot.send_message(message.from_user.id, text_error)


@bot.message_handler(state=UserInfo.height)
def get_height(message: Message) -> None:
    if message.text.isdigit():
        text = f'Сколько раз в неделю ты собираешься ходить на тренировку?'
        bot.send_message(message.from_user.id, text, reply_markup=trainung_keyboard.mark())
        bot.set_state(message.from_user.id, UserInfo.training, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['height'] = message.text
    else:
        text_error = 'Странное значение. А можно в числах и с реальным значением?'
        bot.send_message(message.from_user.id, text_error)


@bot.message_handler(state=UserInfo.training)
def get_training(message: Message) -> None:
    if message.text:
        text = f'Какого результата ты ожидаешь?'
        bot.send_message(message.from_user.id, text, reply_markup=purpose_keyboard.mark())
        bot.set_state(message.from_user.id, UserInfo.purpose, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['training'] = message.text
    else:
        text_error = 'Странное значение. А можно в числах и с реальным значением?'
        bot.send_message(message.from_user.id, text_error)


@bot.message_handler(state=UserInfo.purpose)
def get_purpose(message: Message) -> None:
    if message.text:
        text = f'Я все записал'
        bot.send_message(message.from_user.id, text)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['purpose'] = message.text
    else:
        text_error = 'Странное значение. А можно в числах и с реальным значением?'
        bot.send_message(message.from_user.id, text_error)