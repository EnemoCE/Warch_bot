import asyncio
from aiogram import Bot, Dispatcher
#executor
#from aiogram.utils.executor import start_webhook

from config_reader import config
from handlers import basic, registration
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Base
from db.ops import get_session_maker, build_engine

# webhook settings
WEBHOOK_HOST = f'https://{config.heroku_app_name}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{config.bot_token.get_secret_value()}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = config.webapp_host
WEBAPP_PORT = config.webapp_port


async def on_shutdown(engine):
    #await bot.delete_webhook()
    await engine.dispose()


async def main():
    engine = await build_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    session_maker = await get_session_maker(engine)
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    #dp.startup.register(on_shutdown(engine))
    dp.include_routers(basic.router, registration.router)
    await dp.start_polling(bot, session_maker=session_maker)

if __name__ == '__main__':
    asyncio.run(main())

"""
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
"""



"""
async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
    
"""