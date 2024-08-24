from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import src
from src.keyboard import dynamic_keyboard_transcript, delete_message_keyboard, cancel_enter
from src.auxiliary import TranscriptReader, Search


transcript_router = Router()


@transcript_router.message(F.text == "ℹ️Расшифровка всех рун")
async def transcript_menu_handler(message: Message):
    await message.answer(text="Выберите руну:", reply_markup=dynamic_keyboard_transcript(page=0))
    src.main_logger.info(f"Пользователь {message.from_user.id} перешел в расшифровку рун")


@transcript_router.callback_query(F.data == "behind_transcript")
async def transcript_behind_handler(callback: CallbackQuery):
    first_button = callback.message.reply_markup.inline_keyboard[1][0].text

    if "Йера" in first_button:
        await callback.message.edit_text(text="Выберите руну:",
                                         reply_markup=dynamic_keyboard_transcript(page=0))
    elif "Альгиз" in first_button:
        await callback.message.edit_text(text="Выберите руну:",
                                         reply_markup=dynamic_keyboard_transcript(page=1))
    elif "Дагаз" in first_button:
        await callback.message.edit_text(text="Выберите руну:",
                                         reply_markup=dynamic_keyboard_transcript(page=2))


@transcript_router.callback_query(F.data == "continue")
async def transcript_continue_handler(callback: CallbackQuery):
    first_button = callback.message.reply_markup.inline_keyboard[1][0].text

    if "Анзус" in first_button:
        await callback.message.edit_text(text="Выберите руну:",
                                         reply_markup=dynamic_keyboard_transcript(page=1))
    elif "Йера" in first_button:
        await callback.message.edit_text(text="Выберите руну:",
                                         reply_markup=dynamic_keyboard_transcript(page=2))
    elif "Альгиз" in first_button:
        await callback.message.edit_text(text="Выберите руну:",
                                         reply_markup=dynamic_keyboard_transcript(page=3))


# ДА, Я ПОКА НЕ УМЕЮ ДЕЛАТЬ ПАГИНАЦИИ, НО ОБЯЗАТЕЛЬНО НАУЧУСЬ
@transcript_router.callback_query(F.data.in_(["0rune", "1rune", "2rune", "3rune", "4rune", "5rune"]))
async def transcript_pages_handler(callback: CallbackQuery):
    first_button = callback.message.reply_markup.inline_keyboard[1][0].text

    if "Анзус" in first_button:
        content = TranscriptReader.read_pages_tr(number="one")
        await callback.message.answer_photo(photo=content[1][int(callback.data[0])],
                                            caption=content[0][int(callback.data[0])],
                                            reply_markup=delete_message_keyboard())
        await callback.answer()

    elif "Йера" in first_button:
        content = TranscriptReader.read_pages_tr(number="two")
        await callback.message.answer_photo(photo=content[1][int(callback.data[0])],
                                            caption=content[0][int(callback.data[0])],
                                            reply_markup=delete_message_keyboard())
        await callback.answer()

    elif "Альгиз" in first_button:
        content = TranscriptReader.read_pages_tr(number="three")
        await callback.message.answer_photo(photo=content[1][int(callback.data[0])],
                                            caption=content[0][int(callback.data[0])],
                                            reply_markup=delete_message_keyboard())
        await callback.answer()

    elif "Дагаз" in first_button:
        content = TranscriptReader.read_pages_tr(number="four")
        await callback.message.answer_photo(photo=content[1][int(callback.data[0])],
                                            caption=content[0][int(callback.data[0])],
                                            reply_markup=delete_message_keyboard())
        await callback.answer()


@transcript_router.callback_query(F.data == "delete_message")
async def delete_message_handler(callback: CallbackQuery):
    await callback.message.delete()


@transcript_router.callback_query(F.data == "search")
async def search_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Введите название руны для поиска 🔎:", reply_markup=cancel_enter())
    await state.set_state(Search.rune_name)


@transcript_router.message(Search.rune_name)
async def catch_search_name_handler(message: Message):
    part_1 = TranscriptReader.read_pages_tr(number="one")
    part_2 = TranscriptReader.read_pages_tr(number="two")
    part_3 = TranscriptReader.read_pages_tr(number="three")
    part_4 = TranscriptReader.read_pages_tr(number="four")

    images_list = part_1[1] + part_2[1] + part_3[1] + part_4[1]
    texts_list = part_1[0] + part_2[0] + part_3[0] + part_4[0]

    find = False

    for i in texts_list:
        if message.text in i:
            await message.answer_photo(photo=images_list[texts_list.index(i)], caption=i,
                                       reply_markup=delete_message_keyboard())
            find = True
            break

    if not find:
        await message.answer(text=f"Руна {message.text} не найдена. Попробуйте ещё раз",
                             reply_markup=delete_message_keyboard())


@transcript_router.callback_query(F.data == "cancel_enter")
async def clear_state_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(text="Выберите руну:", reply_markup=dynamic_keyboard_transcript(page=0))
