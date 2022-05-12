
from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = '5342144284:AAG8y5SfqSGPs74wprsUW4IR1WYA82ftF5Q'

storage = MemoryStorage()


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=storage)