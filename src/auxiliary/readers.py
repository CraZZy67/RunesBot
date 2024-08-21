from aiogram.types import FSInputFile


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
