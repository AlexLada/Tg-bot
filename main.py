import logging
from aiogram import Bot, Dispatcher, executor, types
# from psycopg4 import OperationalError
import asyncio
from prisma import Prisma
API_TOKEN = '5428224458:AAFi9LMU1zKz_8fEj6s6ZKjV8jh1US3Dggs'
CHANNEL_ID = '-1001867203843'



logging.basicConfig(level= logging.INFO )
logger = logging.getLogger(__name__)
logger. setLevel(logging. DEBUG)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns_text = ('Да!', 'Нет!')
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    await message.reply('Привет!\nЯ бот пересылки в канал!\n@ 2022 ')
    await message.answer('Введите текст рассылки')





@dp.message_handler(commands=['sendall'])
async def mailing_text(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id == 1016681799:
        text = message.text[9:]
        markup_inline = types.InlineKeyboardMarkup()
        userList = [] #список айдишников в тг
        stringList = ['Python', 'Swift', 'Go', 'C++', 'C#', 'TypeScript', 'JavaScript', 'Java']
        for i in range(len(stringList)):
            if stringList[i].lower() in text.lower():
                item = types.InlineKeyboardMarkup(text=stringList[i], callback_data='participate')
                markup_inline.add(item)
                result = await prisma.test.find_many(
                    where={
                        'user_role': {
                            'has' : stringList[i]
                        },
                    },
                )
                if result:
                    result.map(lambda x: x.tg_channel)
                    userList.join(userList, result)
        await bot.send_message(CHANNEL_ID, text, reply_markup=markup_inline)
        await bot.send_message(message.from_user.id, "Успешная рассылка")
        for a in userList:
            await bot.send_message(a, text, reply_markup=markup_inline)


    db = Prisma()
    await db.connect()
    test = await db.test.create_many(
        data=[
            {'Name': 'Tegan', 'ID_DC': '47476868975', 'user_role': ['i']},
            {'Name': 'Ann', 'ID_DC': '47346574468', 'user_role': ['i']},
            {'Name': 'Bot', 'ID_DC': '47468976906', 'user_role': ['i']},
        ],
        skip_duplicates=True,
    )
    await db.disconnect()


if __name__ == '__main__':
    asyncio.run(executor.start_polling(dp))

     # asyncio.run(executor.start_polling(dp)) вместо executor.start_polling(dp)









