from aiogram.types import FSInputFile

import os


class Reader:

    @classmethod
    def read_combinations_txt(cls) -> list:
        combination_space_texts = list()

        for i in range(1, 5):
            with open(f"text/combination/combination_{i}.txt", "r", encoding="utf-8") as f:
                combination_space_texts.append("".join(f.readlines()))

        with open("text/prepare.txt", "r", encoding="utf-8") as f:
            combination_space_texts.append("".join(f.readlines()))

        with open("text/choice.txt", "r", encoding="utf-8") as f:
            combination_space_texts.append("".join(f.readlines()))
        return combination_space_texts

    @classmethod
    def read_combinations_image(cls) -> list:
        combination_space_image = list()

        for i in range(1, 5):
            combination_space_image.append(FSInputFile(path=f"image/combination_{i}.jpg"))
        return combination_space_image

    @classmethod
    def read_unique_combination_texts(cls, number: str) -> list:
        unique_space_texts = list()

        with open("text/free_layout.txt", "r", encoding="utf-8") as f:
            unique_space_texts.append("".join(f.readlines()))

        with open(f"text/combination/unique_text/unique_text_{number}.txt", "r", encoding="utf-8") as f:
            unique_space_texts.append("".join(f.readlines()))

        return unique_space_texts

    @classmethod
    def read_greeting(cls):
        with open("text/greeting.txt", "r", encoding="utf-8") as f:
            return "".join(f.readlines())

    @classmethod
    def read_congratulation(cls):
        with open("text/congratulation.txt", "r", encoding="utf-8") as f:
            return "".join(f.readlines())


class EducationReader:

    @classmethod
    def read_page_1(cls):
        content_page_1 = list()

        with open("text/education/page_1.txt", "r", encoding="utf-8") as f:
            content_page_1.append("".join(f.readlines()))

        content_page_1.append(FSInputFile(path="image/education/page_1.jpg"))
        return content_page_1

    @classmethod
    def read_page_2(cls):
        with open("text/education/page_2.txt", "r", encoding="utf-8") as f:
            return "".join(f.readlines())

    @classmethod
    def read_variation_content(cls):
        education_images = os.listdir("image/education")
        education_texts = os.listdir("text/education")
        education_texts.sort()
        education_images.sort()

        images = list()
        texts = list()

        for i in education_images:
            if i == "page_1.jpg":
                continue

            images.append(FSInputFile(path=f"image/education/{i}"))
        images.insert(4, None)

        for i in education_texts:
            if i == "page_1.txt" or i == "page_2.txt":
                continue

            with open(f"text/education/{i}", "r", encoding="utf-8") as f:
                texts.append("".join(f.readlines()))
        return [texts, images]
