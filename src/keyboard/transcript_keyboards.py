from aiogram.utils.keyboard import InlineKeyboardBuilder


def dynamic_keyboard_transcript(page: int):
    pages = [["🧿Анзус", "🧿Феху", "🧿Кеназ", "🧿Райдо", "🧿Турисаз", "🧿Уруз"],
             ["🧿Йера", "🧿Гебо", "🧿Хагалас", "🧿Иса", "🧿Наутиз", "🧿Вуньо"],
             ["🧿Альгиз", "🧿Беркана", "🧿Эйваз", "🧿Перт", "🧿Соулу", "🧿Тейваз"],
             ["🧿Дагаз", "🧿Эваз", "🧿Ингуз", "🧿Лагуз", "🧿Манназ", "🧿Отал"]]

    builder = InlineKeyboardBuilder()
    builder.button(text="🔎Поиск руны по названию", callback_data="search")

    for i in pages[page]:
        builder.button(text=i[pages[page].index(i)], callback_data=f"{pages[page].index(i)}rune")

    if page == 0:
        builder.button(text="Далее", callback_data="continue")
        builder.adjust(1, 2, 2, 2, 1)
        return builder.as_markup()
    elif page == 3:
        builder.button(text="Назад", callback_data="behind_transcript")
        builder.adjust(1, 2, 2, 2, 1)
        return builder.as_markup()

    builder.button(text="Назад", callback_data="behind_transcript")
    builder.button(text="Далее", callback_data="continue")
    builder.adjust(1, 2, 2, 2, 2)

    return builder.as_markup()


def delete_message_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🗑 Удалить сообщение")
    return builder.as_markup()


def cancel_enter():
    builder = InlineKeyboardBuilder()
    builder.button(text="⛔️ Отмена ввода")
    return builder.as_markup()
