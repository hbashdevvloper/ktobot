from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, AMR_NAME, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("‹ اخفاء القائمه ›", callback_data="cls")]]
)


@Client.on_message(command(["تحديث", f"reload@bnm1_bot"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "**تم تحديث الملفات !**\n **تم تحديث قائمة الادمنيه والمطورين !**"
    )


@Client.on_message(command(["تخطي", f"skip@bnm1_bot", "vskip"]) & other_filters)
@authorized_users_only
async def skipp(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="‹ لوحة التحكم ›", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="‹ اغلاق ›", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**هيه مافي شي شغال !**")
        elif op == 1:
            await m.reply("**✶ ابشر تم التخطي**")
        elif op == 2:
            await m.reply("🗑️**تم مسح قوائم الانتظار**\n**• غادر الحساب المساعد من المحادثه الصوتية**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"**✶ تم التخطي**\n\n- **العنوان -›** [{op[0]}]({op[1]})\n- **بواسطة -›** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **تم حذف الاغنيه من قائمة الانتظار:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)
            
            
@Client.on_message(filters.command("ريلا الي بعده", [".", ""]) & ~filters.edited)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="‹ لوحة التحكم ›", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="‹ اغلاق ›", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**هيه مافي شي شغال !**")
        elif op == 1:
            await m.reply("**✶ ابشر تم التخطي**")
        elif op == 2:
            await m.reply("🗑️**تم مسح قوائم الانتظار**\n**• غادر الحساب المساعد من المحادثه الصوتية**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"**✶ تم التخطي**\n\n- **العنوان -›** [{op[0]}]({op[1]})\n- **بواسطة -›** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **تم حذف الاغنيه من قائمة الانتظار:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)



@Client.on_message(filters.command("ريلا طفيها", [".", ""]) & ~filters.edited)
@authorized_users_only
async def stopp(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✶ ابشر طفيت الي شغال**")
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply("**يا حلو مافي شي شغال !**")

@Client.on_message(
    command(["اوكف", f"stop@bnm1_bot", "كافي", f"end@bnm1_bot", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✶ ابشر وقفت كل الي شغال**")
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply("**يا حلو مافي شي شغال !**")


@Client.on_message(
    command(["مؤقت", f"pause@bnm1_bot", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "**تم ايقاف التشغيل بشكل مؤقت**\n\n• **لاكمال التشغيل قم بأرسال ↓**\n» /resume"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("**هيه مافي شي شغال !!**")


@Client.on_message(
    command(["استئناف", f"resume@bnm1_bot", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "**تم استئناف التشغيل**\n\n• ** لأيقاف التشغيل مؤقتا ارسل ↓ **\n» /pause"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply(" **هيه مافي شي شغال !!**")


@Client.on_message(
    command(["كتم", f"mute@bnm1_bot", "vmute"]) & other_filters
)
@authorized_users_only
async def mutee(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "**تم كتم الحساب المساعد**\n\n• **لالغاء الكتم ارسل ↓ **\n» /unmute"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply(" **هيه مافي شي شغال !!**")
        
@Client.on_message(filters.command("ريلا اص", [".", ""]) & ~filters.edited)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "**تم كتم الحساب المساعد**\n\n• **لالغاء الكتم ارسل ↓ **\n» /unmute"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply(" **هيه مافي شي شغال !!**")


@Client.on_message(
    command(["الغاء كتم", f"unmute@bnm1_bot", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "**تم الغاء الكتم.**\n\n• **لكتمه ارسل ↓ **\n» /mute."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطا:**\n\n`{e}`")
    else:
        await m.reply(" **هيه مافي شي شغال !!**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يا حلو بس الادمنيه والي عندهم صلاحية المكالمه يقدرون يتحكمون !!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ تم ايقاف التشغيل بشكل مؤقت", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("مافي شي شغال عشان تتحكم فيه !", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يا حلو بس الادمنيه والي عندهم صلاحية المكالمه يقدرون يتحكمون !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ تم استئاف التشغيل", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("مافي شي شغال عشان تتحكم فيه ", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يا حلو بس الادمنيه والي عندهم صلاحية المكالمه يقدرون يتحكمون !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text(" **انتهاء التشغيل**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer(" هيه مافي شي شغال", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يا حلو بس الادمنيه والي عندهم صلاحية المكالمه يقدرون يتحكمون !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 تم كتم الحساب المساعد", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("هيه مافي شي شغال", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يا حلو بس الادمنيه والي عندهم صلاحية المكالمه يقدرون يتحكمون !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 تم الغاء الكتم عن الحساب المساعد", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("هيه مافي شي شغال !", show_alert=True)


@Client.on_message(
    command(["مستوى", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"**ضبط مستوى الصوت** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply(" **هيه مافي شي شغال !**")
