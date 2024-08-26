from aiogram import Router, F
from aiogram.types import Message

import src
from src.keyboard import about_menu_keyboard, back_in_menu_keyboard, main_menu_keyboard
from src.auxiliary import AboutReader, Reader

about_router = Router()


@about_router.message(F.text == "🧿Все о рунах")
async def about_menu_handler(message: Message):
    await message.answer(text="🔮В данном меню Вы сможете узнать основную информацию про руны\n\n"
                              "👇Для продолжения, нажмите на любую из кнопок", reply_markup=about_menu_keyboard())
    src.main_logger.info(f"Пользователь {message.from_user.id} перешел в раздел о рунах")


@about_router.message(F.text.in_(["🧿 Для чего нужны руны?", "🧿 Что такое руны?"]))
async def buttons_handler_part1(message: Message):
    if message.text == "🧿 Для чего нужны руны?":
        await message.answer(text=AboutReader.read_about_runes()[2], reply_markup=back_in_menu_keyboard())
    else:
        await message.answer(text=AboutReader.read_about_runes()[6], reply_markup=back_in_menu_keyboard())


@about_router.message(F.text.in_(["🧿 Можно ли гадать на рунах?", "🧿 Какая руна символизирует здоровье?"]))
async def buttons_handler_part2(message: Message):
    if message.text == "🧿 Можно ли гадать на рунах?":
        await message.answer(text=AboutReader.read_about_runes()[4], reply_markup=back_in_menu_keyboard())
    else:
        await message.answer(text=AboutReader.read_about_runes()[3], reply_markup=back_in_menu_keyboard())


@about_router.message(F.text.in_(["🧿 Что можно увидеть на рунах?", "🧿 Какая разница между рунами и Таро?"]))
async def buttons_handler_part3(message: Message):
    if message.text == "🧿 Что можно увидеть на рунах?":
        await message.answer(text=AboutReader.read_about_runes()[5], reply_markup=back_in_menu_keyboard())
    else:
        await message.answer(text=AboutReader.read_about_runes()[0], reply_markup=back_in_menu_keyboard())


@about_router.message(F.text.in_(["🧿 Что означает пустая руна в раскладе?", "🧿 Какие виды рун бывают?"]))
async def buttons_handler_part4(message: Message):
    if message.text == "🧿 Что означает пустая руна в раскладе?":
        await message.answer(text=AboutReader.read_about_runes()[1], reply_markup=back_in_menu_keyboard())
    else:
        content = AboutReader.read_variation()
        await message.answer_photo(photo=content[1], caption=content[0], reply_markup=back_in_menu_keyboard())


@about_router.message(F.text == "🧿 Руна дня")
async def buttons_handler_part4(message: Message):
    content = AboutReader.read_day_runes()
    await message.answer_photo(photo=content[1], caption=content[0], reply_markup=back_in_menu_keyboard())


@about_router.message(F.text == "👈Назад")
async def buttons_handler_part4(message: Message):
    await message.answer(text="🔮В данном меню Вы сможете узнать основную информацию про руны\n\n"
                              "👇Для продолжения, нажмите на любую из кнопок", reply_markup=about_menu_keyboard())


@about_router.message(F.text == "👈 Обратно")
async def buttons_handler_part4(message: Message):
    await message.answer(text=Reader.read_greeting(), reply_markup=main_menu_keyboard())
