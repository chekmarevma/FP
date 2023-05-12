import asyncio
from environs import Env
from aiogram import Bot, Dispatcher
from keyboards.menu import set_main_menu
from handlers import handlers, handlers_speed, handlers_strong, handlers_wrong, handlers_endurance, handlers_agility, handlers_VPN
from aiogram.fsm.storage.memory import MemoryStorage

async def main():
    env = Env()
    env.read_env()
    token = env('BOT_TOKEN')

    # Создаем объекты бота и диспетчера
    storage: MemoryStorage = MemoryStorage()
    bot: Bot = Bot(token=token)
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_router(handlers.router)
    dp.include_router(handlers_speed.router)
    dp.include_router(handlers_strong.router)
    dp.include_router(handlers_agility.router)
    dp.include_router(handlers_endurance.router)
    dp.include_router(handlers_wrong.router)
    dp.startup.register(set_main_menu)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())







