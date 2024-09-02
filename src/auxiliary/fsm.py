from aiogram.fsm.state import StatesGroup, State


class UserInfo(StatesGroup):
    name = State()
    date = State()


class Search(StatesGroup):
    rune_name = State()


class DataBase(StatesGroup):
    text = State()
    image = State()


class ChangeUsername(StatesGroup):
    old_username = State()
    new_username = State()

    @classmethod
    def change_username(cls, old_value, new_value):
        with open("text/free_layout.txt", "r", encoding="utf-8") as f:
            old_text = "".join(f.readlines())
        with open("text/free_layout.txt", "w", encoding="utf-8") as f:
            if old_value in old_text and old_value[0] == "@":
                new_text = old_text.replace(old_value, new_value)
                f.write(new_text)
            else:
                return False

        with open("text/congratulation.txt", "r", encoding="utf-8") as f:
            old_text = "".join(f.readlines())
        with open("text/congratulation.txt", "w", encoding="utf-8") as f:
            if old_value in old_text and old_value[0] == "@":
                new_text = old_text.replace(old_value, new_value)
                f.write(new_text)
            else:
                return False

        return True
