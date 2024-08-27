import csv

from aiogram.types import Message, CallbackQuery
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramForbiddenError

import src
from src.auxiliary import counting_users, clear_db
from src.keyboard import kb_actions_db
from src.auxiliary import DataBase

router_for_db = Router()
valid_users = [5617141084, 1162899410, 5919006420]


@router_for_db.message(F.text == "/users")
async def users_actions(message: Message):
    if message.from_user.id in valid_users:
        await message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                             reply_markup=kb_actions_db())
    src.main_logger.info(f"Админ {message.from_user.id} зашел в меню рассылки")


@router_for_db.callback_query(F.data == "clear_data_base")
async def clear_data_base(callback: CallbackQuery):
    clear_db()
    await callback.message.answer("База данных отчищена")
    await callback.answer()
    await callback.message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                                  reply_markup=kb_actions_db())


@router_for_db.callback_query(F.data == "message_users")
async def set_state_message(callback: CallbackQuery, state: FSMContext):
    await state.set_state(DataBase.text)
    await callback.message.answer("Введите одним сообщением что хотите отправить.")
    await callback.answer()


@router_for_db.message(DataBase.text)
async def set_state_message(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(DataBase.image)
    await message.answer("Теперь отправьте изображение для этого текста.")


@router_for_db.message(DataBase.image)
async def catch_image(message: Message, state: FSMContext, bot: Bot):
    data = await state.update_data(image=message.photo[-1].file_id)
    banned_users = 0
    with open("data/users.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        reader.__next__()
        for i in reader:
            try:
                await bot.send_photo(chat_id=i[0], photo=data["image"], caption=data["text"], parse_mode="HTML")

            except TelegramForbiddenError:
                banned_users += 1

    await state.clear()
    await message.answer("Сообщение отправлено!")
    await message.answer(f"Пользователей с заблокированным ботом: {banned_users}")
    await message.answer(f"Количество пользователей в базе данных: {counting_users()}",
                         reply_markup=kb_actions_db())
