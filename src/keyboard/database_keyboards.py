from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.auxiliary import counting_users


def kb_actions_db():
    builder = InlineKeyboardBuilder()

    if counting_users() > 0:
        builder.button(text="Отчистить базу данных", callback_data="clear_data_base")
        builder.button(text="Сообщение пользователям", callback_data="message_users")

    return builder.as_markup()
