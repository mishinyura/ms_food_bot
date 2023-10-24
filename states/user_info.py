from telebot.handler_backends import State, StatesGroup


class UserInfo(StatesGroup):
    """
    Имя(name) – type str (любая строка)
    Пол(gender) – мужской или женский (выбор кнопкой)
    Возраст(age) – type int (от 6 до 130)
    Вес(weight) – type int
    Рост(height) – type int
    Тренировки(training) – 1(Не занимаюсь спортом), 2(1-2 раза в неделю тренируюсь),
    Цель(purpose) – Варианты: Быстрое похудение, умеренное похудение, поддержание веса, умеренный набор, быстрый набор (5 вариантов)
    """
    name = State()
    gender = State()
    age = State()
    weight = State()
    height = State()
    training = State()
    purpose = State()
