import logging
from create_bot import dp
from handlers import client
from aiogram import executor

logging.basicConfig(level=logging.INFO)

client.register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)