from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import src
from src.auxiliary import ChangeUsername

username_router = Router()


@username_router.message(F.text == "/change")
async def old_username(message: Message, state: FSMContext):
    await message.answer(text="Напишите старый никнейм который хотите заменить.")
    await state.set_state(ChangeUsername.old_username)
    src.main_logger.info(f"Админ {message.from_user.id} зашел в изменение никнейма.")


@username_router.message(ChangeUsername.old_username)
async def old_username(message: Message, state: FSMContext):
    await state.update_data(old_username=message.text)
    await message.answer(text="Теперь напишите новый никнейм на который хотите заменить.")
    await state.set_state(ChangeUsername.new_username)


@username_router.message(ChangeUsername.new_username)
async def old_username(message: Message, state: FSMContext):
    await state.update_data(new_username=message.text)
    data = await state.get_data()
    result = ChangeUsername.change_username(old_value=data["old_username"], new_value=data["new_username"])

    if not result:
        await message.answer(text="Скорее всего вы ввели не правильный старый username, попробуйте снова.")
        await state.clear()
    else:
        await message.answer(text="Никнейм был успешно изменен!")
        await state.clear()
