import json

import logging
from aiogram import Bot, Dispatcher, executor

from config import TOKEN, valid_types

bot = Dispatcher(Bot(token=TOKEN))
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	)

@bot.message_handler(content_types=valid_types)
async def mainHandler(message):
	convert = json.dumps(dict(message), sort_keys=True, indent=2)
	await message.answer(f"``` {convert} ```", parse_mode="Markdown")


if __name__ == '__main__':
	executor.start_polling(bot, skip_updates=False)