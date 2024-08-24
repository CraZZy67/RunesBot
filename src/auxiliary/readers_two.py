from aiogram.types import FSInputFile

import os


class TranscriptReader:
    @classmethod
    def read_pages_tr(cls, number: str):
        page_images = os.listdir(f"image\\transcript\\page_{number}")
        page_texts = os.listdir(f"text\\transcript\\page_{number}")

        images = list()
        texts = list()

        for i in page_images:
            images.append(FSInputFile(path=f"image/transcript/page_{number}/{i}"))

        for i in page_texts:
            with open(f"text/transcript/page_{number}/{i}", "r", encoding="utf-8") as f:
                texts.append("".join(f.readlines()))

        return [texts, images]
