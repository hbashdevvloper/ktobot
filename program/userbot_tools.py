import asyncio
from driver.veez import user
from pyrogram.types import Message
from pyrogram import Client, filters
from config import BOT_USERNAME, AMR_NAME, SUDO_USERS
from driver.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from driver.decorators import authorized_users_only, sudo_users_only


@Client.on_message(
    command(["ادخلي", f"join@{BOT_USERNAME}"]) & other_filters
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = await c.export_chat_invite_link(chat_id)
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
            await user.join_chat(invitelink)
            return await user.send_message(chat_id, "**ابشر دخلت**")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "انا موجوده يا عيني")

    
@Client.on_message(filters.command("لانا ادخلي", [".", ""]) & ~filters.edited)
@authorized_users_only
async def join_chatt(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = await c.export_chat_invite_link(chat_id)
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
            await user.join_chat(invitelink)
            return await user.send_message(chat_id, "**ابشر دخلت 💕**")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "انا موجوده يا عيني")


@Client.on_message(
    command(["اطلعي", f"userbotleave@{BOT_USERNAME}"]) & other_filters
)
@authorized_users_only
async def leave_chat(_, m: Message):
    chat_id = m.chat.id
    try:
        await user.leave_chat(chat_id)
        return await _.send_message(
            chat_id,
            "**ابشر طلعت**",
        )
    except UserNotParticipant:
        return await _.send_message(
            chat_id,
            "**ابشر طلعت**",
        )
    
@Client.on_message(filters.command("لانا اطلعي", [".", ""]) & ~filters.edited)
@authorized_users_only
async def leave_chat(_, m: Message):
    chat_id = m.chat.id
    try:
        await user.leave_chat(chat_id)
        return await _.send_message(
            chat_id,
            "**ابشر طلعت**",
        )
    except UserNotParticipant:
        return await _.send_message(
            chat_id,
            "**ابشر طلعت**",
        )


@Client.on_message(filters.left_chat_member)
async def ubot_leave(c: Client, m: Message):
#    ass_id = (await user.get_me()).id
    bot_id = (await c.get_me()).id
    chat_id = m.chat.id
    left_member = m.left_chat_member
    if left_member.id == bot_id:
        await user.leave_chat(chat_id)
#    elif left_member.id == ass_id:
#        await c.leave_chat(chat_id)
