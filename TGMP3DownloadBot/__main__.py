# TG_MP3_Download_Bot

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TGMP3DownloadBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from TGMP3DownloadBot import MP3DownloadBot as app
from TGMP3DownloadBot import LOGGER

pm_start_text = """
 🎧 Telegram Musik Downloader Bot 🎧

Hallo Gaess [{}](tg://user?id={}) 👋 Saya Adalah Bot Telegram Yang Dibuat Untuk Mengunduh Musik  🎧

Kirimkan saja kepada saya ✍️   judul musik 👍   yang anda inginkan 👌
📜 Contoh: `/song Indonesia Pusaka `

~ @MusikdlroBot🤖 
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
                             text=" 👦 Own Bot ",
                             url="https://t.me/ebnudoang"),
                         InlineKeyboardButton(
                             text=" 📍 Instagram ",
                             url="https://www.instagram.com/ebnu_am/")
                    ],
                    [
                        InlineKeyboardButton(
                             text=" Stiker Telegram ",
                             url="https://telegra.ph/Stiker-Telegram-10-28"),
                         InlineKeyboardButton(
                             text=" Stiker WhatsApp ",
                             url="https://telegra.ph/Stiker-WhatsApp-10-28")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" Bot Lainya ",
                             url="https://telegra.ph/Stiker-WhatsApp-10-28") 
                    
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
