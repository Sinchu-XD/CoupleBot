import telegram.ext as tg
from aiohttp import ClientSession
from pyrogram import Client
from telethon import TelegramClient

from Config import API_ID, API_HASH, TOKEN


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("Abhi", API_ID, API_HASH)

Bot = Client("CoupleBot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN,in_memory=True)
dispatcher = updater.dispatcher
aiohttpsession = ClientSession()


print("[INFO]: Getting Bot Info...")
BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_USERNAME = dispatcher.bot.username
