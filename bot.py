from aiogram import Dispatcher, Bot, executor, types
from config import TOKEN
import main
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
const = main.Constructor()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text="Я бот созданный для того чтобы переводить переданный текст. Бот можно использовать в "
                              "групповых чатах. Чтобы узнать список всех доступных комманд - введите команду /help")


@dp.message_handler(commands=["help"])
async def show_commands(message: types.Message):
    commands = "<b>/to_ru</b> - <i>перевод на русский</i>\n" \
               "<b>/to_en</b> - <i>перевод на английский</i>\n" \
               "<b>/to_fr</b> - <i>перевод на французский</i>\n" \
               "<b>/to_kz</b> - <i>перевод на казахский</i>"
    await message.reply(text=commands, parse_mode="html")


@dp.message_handler(commands=["to_ru"])
async def to_ru(msg: types.Message):
    text_to_trans = msg.reply_to_message.text
    res = "🇷🇺: " + const.text_translator(message=text_to_trans, to_lang="ru").text
    await msg.reply(text=res)


@dp.message_handler(commands=["to_en"])
async def to_ru(msg: types.Message):
    text_to_trans = msg.reply_to_message.text
    res = "🇺🇸: " + const.text_translator(message=text_to_trans, to_lang="en").text
    await msg.reply(text=res)


@dp.message_handler(commands=["to_kz"])
async def to_ru(msg: types.Message):
    text_to_trans = msg.reply_to_message.text
    res = "🇰🇿: " + const.text_translator(message=text_to_trans, to_lang="kk").text
    await msg.reply(text=res)


@dp.message_handler(commands=["to_fr"])
async def to_ru(msg: types.Message):
    text_to_trans = msg.reply_to_message.text
    res = "🇫🇷: " + const.text_translator(message=text_to_trans, to_lang="fr").text
    await msg.reply(text=res)


if __name__ == '__main__':
    executor.start_polling(dp)
