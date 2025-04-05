from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = "7374201034:AAHZ48nTvc1n4I02veri2ry-mkuFcnd2FFM"
DJANGO_APP_URL = "https://glasshalf.ru/teletest"

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Открыть Django приложение", url=DJANGO_APP_URL
                )
            ]
        ]
    )

    await message.answer(
        "Добро пожаловать! Нажмите кнопку ниже, чтобы открыть приложение:",
        reply_markup=keyboard,
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
