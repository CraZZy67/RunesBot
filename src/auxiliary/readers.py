from aiogram.types import FSInputFile


class Reader:

    @classmethod
    def read_combination_txt(cls) -> list:
        combination_space_texts = list()

        for i in range(1, 5):
            with open(f"text/combination_{i}.txt", "r", encoding="utf-8") as f:
                combination_space_texts.append("".join(f.readlines()))

        with open("text/prepare.txt", "r", encoding="utf-8") as f:
            combination_space_texts.append("".join(f.readlines()))

        with open("text/choice.txt", "r", encoding="utf-8") as f:
            combination_space_texts.append("".join(f.readlines()))
        return combination_space_texts

    @classmethod
    def read_combination_image(cls) -> list:
        combination_space_image = list()

        for i in range(1, 5):
            combination_space_image.append(FSInputFile(path=f"image/combination_{i}.jpg"))
        return combination_space_image
