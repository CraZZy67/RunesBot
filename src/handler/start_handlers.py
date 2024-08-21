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
    texts_layout = Reader.read_combinations_txt()
    images_layout = Reader.read_combinations_image()

    await message.answer(text=texts_layout[4])
    await sleep(3.0)

    for i in range(0, 4):
        await message.answer_photo(photo=images_layout[i], caption=texts_layout[i])
        await sleep(0.5)

    await message.answer(text=texts_layout[5], reply_markup=keyboard.combination_choice_keyboard())


@start_router.message(F.text.in_(["Комбинация №1", "Комбинация №2", "Комбинация №3", "Комбинация №4"]))
async def layout_handler(message: Message):
    unique_texts = Reader.read_unique_combination_texts(number=message.text[-1])

    await message.answer(text=unique_texts[1], reply_markup=keyboard.main_menu_keyboard())
    await sleep(0.5)
    await message.answer(text=unique_texts[0], reply_markup=keyboard.free_layout_keyboard())

