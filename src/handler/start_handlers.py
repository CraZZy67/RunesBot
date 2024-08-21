from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from asyncio import sleep

from src import keyboard
from src.auxiliary import Reader

start_router = Router(name=__name__)


@start_router.message(CommandStart(ignore_case=True))
async def start_command_handler(message: Message):
    with open("text/subconscious.txt", "r", encoding="utf-8") as f:
        start_text = "".join(f.readlines())

    photo = FSInputFile(path="image/subconscious.jpg")
    await message.answer_photo(photo, caption=start_text, reply_markup=keyboard.layout_keyboard())


@start_router.message(F.text == "⚡️ Расклад ⚡️")
async def layout_handler(message: Message):
    texts_layout = Reader.read_combination_txt()
    images_layout = Reader.read_combination_image()

    await message.answer(text=texts_layout[4])
    await sleep(3.0)

    for i in range(0, 4):
        await message.answer_photo(photo=images_layout[i], caption=texts_layout[i])
        await sleep(0.5)

    await message.answer(text=texts_layout[5], reply_markup=keyboard.combination_choice_keyboard())
