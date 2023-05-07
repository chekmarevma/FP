from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu = [BotCommand(command='/start', description='Старт бота'),
                 BotCommand(command='/help', description='Справка'),
                 BotCommand(command='/history', description='История обновлений')]
    await bot.set_my_commands(main_menu)