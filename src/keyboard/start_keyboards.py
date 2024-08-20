from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def layout_keyboard():
    start_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="⚡️ Расклад ⚡️")]], resize_keyboard=True)

    return start_keyboard
