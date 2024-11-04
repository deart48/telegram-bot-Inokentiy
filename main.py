import asyncio
import logging
import sys
import webbrowser
from os import getenv
import app.keybords as kbs
from aiogram import F, Bot, Dispatcher, html, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = '7600938593:AAGaHWhbAJ0yNxWUdFYZgWshJTO1UCMjoxM'

# All handlers should be attached to the Router (or Dispatcher)
router = Router()
dp = Dispatcher()


@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")
    await message.answer(f"Меня зовут Иннокентий. Я ваш помощник.")
    await message.answer("Выберите опцию:", reply_markup= kbs.kb)


@dp.message(F.text == 'Замены')
async def substitutions(message: Message) -> None:
    await message.answer("Открываю ссылку", reply_markup= kbs.ref)
    await message.answer("Выберите опцию:", reply_markup= kbs.kb)
    webbrowser.open("https://disk.yandex.ru/d/gCqmY1cM4AIhNA")

@dp.message(F.text == 'Расписание')
async def schedule(message: Message) -> None:
    await message.answer("Открываю ссылку", reply_markup= kbs.ref2)
    await message.answer("Выберите опцию:", reply_markup= kbs.kb)
    webbrowser.open("https://disk.yandex.ru/d/mVe-IcIoqaVbhg")

@dp.message(F.text == 'Мероприятия')
async def events(message: Message) -> None:
    await message.reply("Находится в разработке.")
    await message.answer("Выберите опцию:", reply_markup= kbs.kb)

@dp.message(F.text == 'Заявка на питание, Посещаемость')
async def Food_Application_Attendance(message: Message) -> None:
    await message.reply("Находится в разработке.")
    await message.answer("Выберите опцию:", reply_markup= kbs.kb)



# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())