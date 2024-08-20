from asyncio import run

from src.create_bot import bot, dp


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен!")
    run(main())
