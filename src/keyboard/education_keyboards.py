from aiogram.utils.keyboard import InlineKeyboardBuilder


def next_education_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Далее ➡️", callback_data="next")
    return builder.as_markup()


def layout_variation_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🗃 Варианты расклада", callback_data="variation")
    return builder.as_markup()


def variation_keyboard():
    builder = InlineKeyboardBuilder()
    list_names = ["Расклад 'Крест'", "Расклад в пять рун", "Четырёх рунный расклад", "Метод трёх Норн",
                  "Случайная руна",  "Расклад в семь рун", "Шестирунный расклад"]

    for i in list_names:
        builder.button(text=i, callback_data=f"{list_names.index(i)}var")

    builder.adjust(1, repeat=True)
    return builder.as_markup()


def behind_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Назад", callback_data="behind")
    return builder.as_markup()
