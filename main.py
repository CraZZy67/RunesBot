from asyncio import run

import src


src.dp.include_routers(src.start_router, src.education_router, src.transcript_router, src.about_router,
                       src.router_for_db, src.username_router)


async def main():
    await src.dp.start_polling(src.bot)

if __name__ == "__main__":
    src.main_logger.info("Бот запущен!")
    run(main())
