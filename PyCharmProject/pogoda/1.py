import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types, html
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
bot = Bot(token="7430663568:AAEEy8U1ucBWy9Qzthzc-XdWpeo6vYOEBak")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

#echo
@dp.message_handler()
async def echo(messege: types.Message):
    await messege.answer(messege.text)

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())