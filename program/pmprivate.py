from os import getenv

from driver.veez import user as USER
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

PMSET = True
pchats = []
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2042690935").split()))
PMPERMIT = getenv("PMPERMIT", "ENABLE")


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            buttons = [[InlineKeyboardButton("‹ قناة السورس ›", url="https://t.me/S_T_Dl")]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await USER.send_message(chat_id=message.chat.id, text="✶ اهلا عزيزي\n⇜ انا حساب مساعد خاص لبوت تشغيل الاغاني [ @S_T_1BOT ] بس !\n⇜ لو سمحت لا تسولف هنا ولا تدخلني بقروبات خاصه انا مو حساب شخصي مجرد حساب مساعد فقط ..\n⇜ المطور يقدر يخش الحساب ويشوف كل شي فا لا ترسل صور او صوتيات ولا تسولف هنا ..\n\n- مطور البوت @e1r_10\n\n", reply_markup=reply_markup, )
            
            return


@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit turned off")
            return


@USER.on_message(filters.text & filters.private & filters.me)
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM due to outgoing messages")
        return
    message.continue_propagation()


@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM")
        return
    message.continue_propagation()


@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()
