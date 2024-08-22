from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from src.auxiliary import EducationReader
from src.keyboard import *

education_router = Router()


@education_router.message(F.text == "📚Обучение руническому раскладу")
async def education_runes_handler(message: Message):
    content_page = EducationReader.read_page_1()
    await message.answer_photo(photo=content_page[1], caption=content_page[0], reply_markup=next_education_keyboard())


@education_router.callback_query(F.data.in_(["next", "variation"]))
async def next_education_handler(callback: CallbackQuery):
    if callback.data == "next":
        await callback.message.delete()
        await callback.message.answer(text=EducationReader.read_page_2(), reply_markup=layout_variation_keyboard())
    else:
        await callback.message.edit_text(text="Всего есть 7 вариаций раскладов на рунах, выберите любой или который "
                                              "больше подходит:", reply_markup=variation_keyboard())


@education_router.callback_query(F.data.in_(["0var", "1var", "2var", "3var", "4var", "5var", "6var"]))
async def unique_text_variation_handler(callback: CallbackQuery):
    content_for_variation = EducationReader.read_variation_content()

    if callback.data == "4var":
        await callback.message.edit_text(text=content_for_variation[0][4], reply_markup=behind_keyboard())
    else:
        await callback.message.delete()
        await callback.message.answer_photo(photo=content_for_variation[1][int(callback.data[0])],
                                            caption=content_for_variation[0][int(callback.data[0])],
                                            reply_markup=behind_keyboard())


@education_router.callback_query(F.data == "behind")
async def behind_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Всего есть 7 вариаций раскладов на рунах, выберите любой или который "
                                       "больше подходит:", reply_markup=variation_keyboard())
