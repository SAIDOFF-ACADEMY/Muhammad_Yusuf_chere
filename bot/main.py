import asyncio

from decouple import config
from aiogram.filters import CommandStart
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot.models import Customer


bot = Bot(token=config('KEY'))
dp = Dispatcher()


class Register(StatesGroup):
    name = State()
    number = State()


@dp.message(CommandStart())
async def welcome(message: Message, state: FSMContext):
    user = Customer.objects.get(tg_id=message.from_user.id)
    if not user:
        await message.answer(f"Hello")
        await message.answer('Ismingizni kiriting')
        await state.set_state(Register.name)
    else:
        await message.answer(f"Hello")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())