from aiogram.types import FSInputFile

import os
from datetime import datetime, timedelta


class TranscriptReader:
    @classmethod
    def read_pages_tr(cls, number: str):
        page_images = os.listdir(f"image/transcript/page_{number}")
        page_texts = os.listdir(f"text/transcript/page_{number}")
        page_texts.sort()
        page_images.sort()

        images = list()
        texts = list()

        for i in page_images:
            images.append(FSInputFile(path=f"image/transcript/page_{number}/{i}"))

        for i in page_texts:
            with open(f"text/transcript/page_{number}/{i}", "r", encoding="utf-8") as f:
                texts.append("".join(f.readlines()))

        return [texts, images]


class AboutReader:
    @classmethod
    def read_about_runes(cls):
        files = os.listdir("text/about")
        files.sort()

        texts = list()

        for i in files[1:]:
            if i == "variation_runes.txt":
                continue

            with open(f"text/about/{i}", "r", encoding="utf-8") as f:
                texts.append("".join(f.readlines()))
        return texts

    @classmethod
    def read_variation(cls):
        with open("text/about/variation_runes.txt", "r", encoding="utf-8") as f:
            text = "".join(f.readlines())

        image = FSInputFile(path=f"image/about/variation_runes.jpg")
        return [text, image]

    @staticmethod
    def create_dict():
        files = os.listdir(f"text/about/day_rune")
        files.sort()

        files += files
        files.append(files[0])

        day_runes = dict()

        for i in range(1, 32):
            day_runes[str(i)] = files[i - 1]
        return day_runes

    @staticmethod
    def get_difference():
        now = datetime.now()
        midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())

        time_until_midnight = midnight - now

        hours, remainder = divmod(time_until_midnight.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f" {hours} часа {minutes} минуты."

    @classmethod
    def read_day_runes(cls):
        day = datetime.now().isoformat()[8:10].replace("0", "")
        file = AboutReader.create_dict()[day]

        with open(f"text/about/day_rune/{file}", "r", encoding="utf-8") as f:
            text = "".join(f.readlines())

        image = FSInputFile(path=f"image/about/day_rune.jpg")
        text = text + AboutReader.get_difference()
        return [text, image]