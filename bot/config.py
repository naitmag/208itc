from datetime import datetime

import telebot

from environs import Env


env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
GROUP_ID = env.int('GROUP_ID')
API_WEATHER = env.str('API_WEATHER')
CITY = env.str('CITY')
WEATHER_TIME = env.str('WEATHER_TIME')
SCHEDULE_TIME = env.str('SCHEDULE_TIME')
CABINETS_CLEAR_TIME = env.str('CABINETS_CLEAR_TIME')

ADMIN_ID = env.int('ADMIN_ID')
PERMISSIONS = env.dict('PERMISSIONS')

bot = telebot.TeleBot(TOKEN)

cabinets_info = {"cabinets": [], "author": {}}

days = ("пн", "вт", "ср", "чт", "пт", "сб")

define_week = {
    0: "🫨 Понедельник",
    1: "☕️ Вторник",
    2: "🪩 Среда",
    3: "🌟 Четверг",
    4: "🍻 Пятница",
    5: "🛌 Суббота"
}

define_time = {
    0: "8:00",
    1: "9:35",
    2: "11:10",
    3: "13:00",
    4: "14:35"
}

pages = {
    "home":
        {
            0: f"<b>Добро пожаловать в бота <em>208itc</em>!</b>"
               f"\n<em>Персональный бот 208 группы ФКиСКД БГУКИ</em>\n",

            1: f"\n<b>ℹ️Что бот умеет?</b>\n"
               f"\n- <em>Отправлять расписание</em>"
               f"\n- <em>Записывать и присылать кабинеты</em>"
               f"\n- <em>Отправить список преподавателей</em>"
               f"\n- <em>Отправлять погоду с утра</em>"
               f"\n- <em>и многое другое..</em>"
        },

    "help": f"⚙️<b>Список команд</b>"
            f"\n\n<blockquote><b>Получить расписание</b>\n/schedule или /s</blockquote>"
            f"\n- Принимает <em>|неделя| |день|</em> в любом порядке"
            f"\n- Можно указать и только неделю"
            f"\n- Без аргументов отправит текущую неделю"
            f"\n- <b>Пример:</b> <code>/schedule 12 пн</code>"
            f"\n\n<blockquote><b>Управление кабинетами</b>\n/cabinets или /c или <u>каб</u></blockquote>"
            f"\n- Принимает <em>|кабинет| |кабинет|</em>.."
            f"\n- Максимальное количество кабинетов : 4"
            f"\n- Без аргументов отправит список кабинетов"
            f"\n- <b>Пример:</b> <code>/cabinets 508 800а</code>"
            f"\n\n<blockquote><b>Добавить занятие</b>\n/add</blockquote>"
            f"\n- Принимает <em>|период или неделя| |день недели| |номер пары| |название_пары|</em>.."
            f"\n- Опционально <em>|тип пары| |преподаватель| </em>"
            f"\n- Доступ имеют определенные пользователи"
            f"\n- <b>Пример:</b> <code>/add 2-14 ср 4 Компьютерная_графика сем. Иванов</code>"
            f"\n\n<blockquote><b>Узнать преподавателей</b>\n/teacher или /t</blockquote>"
            f"\n- Принимает <em>|предмет|</em> или <em>|фамилия|</em>"
            f"\n- Покажет список предметов и преподавателей"
            f"\n- <b>Пример:</b> <code>/teacher чт</code>"
            f"\n\n<blockquote><b>Получить погоду</b>\n/weather или /w</blockquote>"
            f"\n- Отправит погоду на данный момент в городе Минск"
            f"\n- <b>Пример:</b> <code>/weather</code>"
            f"\n\n<blockquote><b>Случайный элемент</b>\n/random или /r</blockquote>"
            f"\n- Принимает <em>|элемент1| |элемент2|</em>.."
            f"\n- Случайно выберет один элемент"
            f"\n- Отлично подойдет для распределения семинаров"
            f"\n- <b>Пример:</b> <code>/random @naitmag @BotFather</code>"
            f"\n\n<blockquote><b>Ваш ID</b>\n/id</blockquote>"
            f"\n- Отправит ваш ID в Telegram"
            f"\n- Подходит для распределения прав"
            f"\n- Команда для тех. части бота"
            f"\n- <b>Пример:</b> <code>/id</code>",

    "contacts": f"📇<b>Контакты:</b>\n"
                f"\n<i><u>Instagram</u></i>"
                f"\n- <a href='https://www.instagram.com/itinculture/'>Instagram кафедры</a>"
                f"\n- <a href='https://www.instagram.com/208itk'>Instagram группы</a>"
                f"\n\n<i><u>Обратная связь</u></i>:"
                f"\n- <a href='https://t.me/naitmag'>Создатель бота</a>"

}

START_LESSONS = datetime(2023, 9, 4)
