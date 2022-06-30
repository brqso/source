import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from Codexun.utils.filters import command

from Codexun import BOT_NAME, BOT_USERNAME
from Codexun.config import BOT_USERNAME 
from Codexun.config import BOT_NAME
from Codexun.config import START_IMG

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**مرحباً {message.from_user.mention()}** 👋
انا بوت استطيع تشغيل الأغاني في مجموعتك قم بإضافتي إلى مجموعتك وقم برفعي مشرفا وقم بإعطائي جميع الصلاحيات وقم بكتابة /reload 
 شكرا لك على إضافة البوت إلى مجموعتك 📍""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 | الاوامر", callback_data="cbcmnds"),
                    InlineKeyboardButton(
                        "🖥️ | السورس", callback_data="cbabout")
                ],
                [
                    InlineKeyboardButton(
                        "🧨 ¦ دلـيل الاسـتخـدام", callback_data="cbguide")
                ],
                [
                    InlineKeyboardButton(
                        "✅ | اضفني إلى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )