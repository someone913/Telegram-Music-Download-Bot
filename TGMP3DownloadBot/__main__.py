# TG_MP3_Download_Bot

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TGMP3DownloadBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from TGMP3DownloadBot import MP3DownloadBot as app
from TGMP3DownloadBot import LOGGER

pm_start_text = """
 🎧 Telegram Song  Download Bot 🎧

Hey [{}](tg://user?id={}) 👋 I'm Telegram song  Download Bot 🎧

Just Send me ✍️   The MP3 Name 👍   You Want to Download 👌
📜 Example: `/song upamawak `

~ @fastsongdownloderslbzbot 🤖 
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                             text=" 👪 Bot Support Group ",
                             url="https://t.me/slbotzone"),
                         InlineKeyboardButton(
                             text=" 🔔 Bot Update Channel ",
                             url="https://t.me/sl_bot_zone")
                    ],
                    [
                        InlineKeyboardButton(
                             text=" 📦 Github Socure Code ",
                             url="https://github.com/youtubeslgeekshow/Telegram-Music-Download-Bot"),
                         InlineKeyboardButton(
                             text=" 💝 Subscribe Our Youtube  Channel ",
                             url="https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" ⚡️ Developer ",
                             url="https://t.me/supunma") 
                    
                    ]
            ]
        ),
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


app.start()
LOGGER.info("TG Song  Download Bot is online 👨‍💻 .")
idle()
