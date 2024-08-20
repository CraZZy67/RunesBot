from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from src import keyboard

start_router = Router(name=__name__)


@start_router.message(CommandStart(ignore_case=True))
async def start_command_handler(message: Message):
    with open("text/subconscious.txt", "r", encoding="utf-8") as f:
        start_text = "".join(f.readlines())

    photo = FSInputFile(path="image/subconscious.jpg")
    await message.answer_photo(photo, caption=start_text, reply_markup=keyboard.layout_keyboard())
