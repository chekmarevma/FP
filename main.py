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
    dp.include_router(handlers_endurance.router)
    dp.include_router(handlers_agility.router)
    dp.include_router(handlers_wrong.router)
    dp.startup.register(set_main_menu)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


# Поиск по роликам
# import asyncio
# from aiogram.types import FSInputFile
# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# import json
#
# TOKEN = '5779458896:AAFHz2_THHad2Xya8gZGS1Vf-HOFO_e0ZJc'
#
#
# async def main():
#     global bot
#     bot = Bot(TOKEN)
#     dp = Dispatcher()
#     dp.message.register(start_def, Command(commands=['start']))
#     dp.message.register(find_actress)
#     await dp.start_polling(bot)
#
#
# async def start_def(message):
#     with open('log.txt', 'a', encoding='utf-8') as file:
#         file.write(
#             f'{message.date} {message.chat.id} {message.chat.username} {message.chat.first_name} {message.chat.last_name} {message.text}\n')
#     await message.answer('Старт')
#
#
# async def find_actress(message):
#     d = {1: '1⃣', 2: '2⃣', 3: '3️⃣', 4: '4⃣', 5: '5⃣', 6: '6⃣', 7: '7⃣', 8: '8⃣', 9: '9⃣'}
#     with open('log.txt', 'a', encoding='utf-8') as file:
#         file.write(
#             f'{message.date} {message.chat.id} {message.chat.username} {message.chat.first_name} {message.chat.last_name} {message.text}\n')
#     with open(r'data_porn_files.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     with open(r'data_actress.json', 'r', encoding='utf-8') as file:
#         data_actress = json.load(file)
#     name = message.text
#     try:
#
#         for disk in data[0][name]:
#
#             # await message.answer(text=f'💾 Диск - {disk}')
#             await message.answer(text=d[int(disk)])
#             for path in data[0][name][disk]:
#                 list_of_films = []
#                 await message.answer(f'-----> {path}')
#                 for film in data[0][name][disk][path]:
#                     list_of_films.append(f'• {film}\n')
#                 await message.answer(f'{"".join(list_of_films)}')
#
#         try:
#             photo = FSInputFile(f'/home/finder/foto/{name}.jpg')
#             await bot.send_photo(chat_id=message.chat.id, photo=photo,
#                                  caption=f'{name}, {data_actress[0][name]["country"]}, {data_actress[0][name]["age"]} y.o.',
#                                  has_spoiler=True)
#         except:
#             photo = FSInputFile(f'/home/finder/foto/NoPhoto.jpg')
#             await bot.send_photo(chat_id=message.chat.id, photo=photo,
#                                  caption=f'{name}, {data_actress[0][name]["country"]}, {data_actress[0][name]["age"]} y.o.')
#
#     except:
#         await message.answer('No name')
#
#
# if __name__ == '__main__':
#     asyncio.run(main())






