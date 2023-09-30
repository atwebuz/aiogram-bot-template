from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("test", "test message"),
            types.BotCommand("anketa", "anketa"),
            types.BotCommand("task", "task"),
        ]
    )
