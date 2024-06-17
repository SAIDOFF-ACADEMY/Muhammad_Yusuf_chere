import asyncio
from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot(token='7245229622:AAHYLNNq418S6z1b_ayPOHG4OfwTg5VtX-A')
dp = Dispatcher()


@dp.message(CommandStart)
async def get_welcome(message: Message):
    await message.answer(f"Salom {message.from_user.first_name}! Botimizga hush kelib siz")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')