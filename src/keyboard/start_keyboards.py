from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardBuilder

import re


def layout_keyboard():
    start_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="⚡️ Расклад ⚡️")]], resize_keyboard=True)

    return start_keyboard


def combination_choice_keyboard():
    choice_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Комбинация №1"), KeyboardButton(text="Комбинация №2")],
        [KeyboardButton(text="Комбинация №3"), KeyboardButton(text="Комбинация №4")]]
        , resize_keyboard=True)

    return choice_keyboard


def main_menu_keyboard():
    main_menu_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🧿Все о рунах")],
        [KeyboardButton(text="ℹ️Расшифровка всех рун"), KeyboardButton(text="📚Обучение руническому раскладу")],
        [KeyboardButton(text="🤩Получить бесплатный расклад🤩")]]
        , resize_keyboard=True)

    return main_menu_kb


def free_layout_keyboard():
    builder = InlineKeyboardBuilder()

    pattern = r'@(\w+)'
    with open("text/free_layout.txt", "r", encoding="utf-8") as f:
        text = "".join(f.readlines())
        match = re.search(pattern, text)

    builder.button(text="🔮Получить рунический расклад", url=f"https://t.me/{match.group(0)[1:]}")
    return builder.as_markup()


def back_keyboard():
    back_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="👈Обратно")]], resize_keyboard=True,
                                  one_time_keyboard=True)

    return back_kb
