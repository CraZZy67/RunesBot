from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def layout_keyboard():
    start_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="⚡️ Расклад ⚡️")]], resize_keyboard=True)

    return start_keyboard


def combination_choice_keyboard():
    choice_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Комбинация №1"), KeyboardButton(text="Комбинация №2")],
        [KeyboardButton(text="Комбинация №3"), KeyboardButton(text="Комбинация №4")]]
        , resize_keyboard=True)

    return choice_keyboard
