from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

هلا حبي {me2},
• اختر الجلسه التي تريد انشاء عليها •

مقدم من  : [𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗔𝗟𝗜𝗣𝗛](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="• بدء جلسة •", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("• السورس •", url="https://t.me/aaaalqp"),
                    InlineKeyboardButton("• المطور •", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
