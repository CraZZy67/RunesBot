import csv

import src


def add_user(user_id: str):
    with open("data/users.csv", "r", encoding="utf-8") as file:
        len_csv = len(list(csv.reader(file, delimiter=",")))

    if len_csv == 0:
        with open("data/users.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows([["id"], [user_id]])
        src.main_logger.info(f"Пользователь {user_id} добавлен в БД")

    else:
        if check_added(int(user_id)):
            with open("data/users.csv", "a", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(user_id)
            src.main_logger.info(f"Пользователь {user_id} добавлен в БД")


def check_added(id_: int):
    with open("data/users.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        reader.__next__()

        for i in reader:
            if id_ == int(i[0]):
                return False

    return True


def counting_users():
    with open("data/users.csv", "r", encoding="utf-8") as file:
        len_csv = len(list(csv.reader(file, delimiter=",")))

    return len_csv if len_csv == 0 else len_csv - 1


def clear_db():
    with open("data/users.csv", "w", encoding="utf-8") as file:
        file.write("")
