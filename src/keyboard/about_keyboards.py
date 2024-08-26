from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def about_menu_keyboard():
    about_menu_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🧿 Для чего нужны руны?"), KeyboardButton(text="🧿 Что такое руны?")],
        [KeyboardButton(text="🧿 Руна дня"), KeyboardButton(text="🧿 Можно ли гадать на рунах?")],
        [KeyboardButton(text="🧿 Какие виды рун бывают?"), KeyboardButton(text="🧿 Какая руна символизирует здоровье?")],
        [KeyboardButton(text="🧿 Что можно увидеть на рунах?"), KeyboardButton(text="🧿 Какая разница между рунами и Таро?")],
        [KeyboardButton(text="🧿 Что означает пустая руна в раскладе?")],
        [KeyboardButton(text="👈 Обратно")]], resize_keyboard=True)

    return about_menu_kb


def back_in_menu_keyboard():
    back = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="👈Назад")]], resize_keyboard=True)
    return back
