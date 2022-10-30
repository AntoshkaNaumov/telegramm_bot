from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot('5563695248:AAEwZXuTpksgNsdEVQ3WH3tFgChFzsJO9wE')
dp = Dispatcher(bot, storage=storage)