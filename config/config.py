import os
from dotenv import load_dotenv, find_dotenv

if find_dotenv():
    load_dotenv()
    token = os.getenv('TOKEN')
else:
    raise KeyError('Файл .env с TOKEN не найден')

DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Показать справку')
)

WELCOME_TEXT = 'Приветствую.\n\nЯ мастер подбора питания ' \
               'и готов делиться с тобой своими знаниями, ' \
               'а так же напоминать о предстоящих событиях\n' \
               'Однако, прежде чем мы начнем, мне нужно задать несколько вопросов...\n\n' \
               'Как тебя зовут?'
