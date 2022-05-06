from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    AMR_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""▪️ **أهـلا بك عزيزي ✋🏼**\n
▫️ **انا بوت تشغيل الموسيقى في المكالمات الصوتية 🔉**

▪️ **يمكن اضافتي الى مجموعتك واستخدام الاوامر للتشغيل ❕*
▫️ **اضغط على الاوامر في الاسفل 🔻\n▪️للستفسار ارسل رسالة هنا : @e1r_10.**
**—  —  —  —  —  —  —  —  —  —**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اضفني الى مجموعتك ›",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("‹ تفعيل البوت ›", callback_data="cbhowtouse"),
               
                    InlineKeyboardButton("‹ اوامر البوت ›", callback_data="cbcmds"),
                    InlineKeyboardButton("‹ مطور البوت ›", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "‹ قناة السورس ›", url=f"https://t.me/UX4SL"
                    ),
                    InlineKeyboardButton(
                        "‹ شروحات البوت ›", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                       "‹ شراء بوت ›", url=f"https://t.me/QVVV7"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""~ **هذا هي طريقة تفعيل البوت 🔻**

1.) **اولا, اضفني الى مجموعتك.**
2.) **بعد ذالك, قم بترقيتي كمسؤول.**
3.) **بعد ذالك اكتب, .تحديث لتحديث البيانات.**
3.) **اضف @{ASSISTANT_NAME} في مجموعتك او اكتب .انضم **
4.) **بعد اكمال كل شي قم بفتح محادثة صوتية واستمتع.**
5.) **بعض الاحيان, ستواجه مشاكل في التشغيل ماعليك فقط سوى كتابة الامر .تحديث**

▪️ ** اذ لم ينضم حساب المساعد اكتب .اطلع , وبعد ذالك اكتب .انضم**

▫️ ** اي مشكلة تواجها لاتتردد في التحدث مع المطور: @QVVV7**

**—  —  —  —  —  —  —  —  —  —**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""• **مرحبًا بكم في قائمة المساعدة 👋🏽 ،**

**في هذه القائمة ، يمكنك فتح العديد من قوائم**
**الأوامر المتاحة ، وفي كل قائمة أوامر يوجد**
**أيضًا شرح موجز لكل أمر**
**—  —  —  —  —  —  —  —  —  —**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("~ اوامر المشرفين ", callback_data="kka"),
                
                    InlineKeyboardButton("~ اوامر الاعضاء ", callback_data="kkl")
                ],[
                    InlineKeyboardButton("‹ رجوع ›", callback_data="cbstart")
                ],
            ]
        ),
    )
    
    
    
@Client.on_callback_query(filters.regex("ck"))
async def ck(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
» **اضغط على الازرار أدناه لقراءة ومعرفة الأوامر الخاصة بالبوت**
» - لتفعيل الكت ارسل /Kstart
» - لتعطيل الكت ارسل /Kstop
✶ Dev - @{OWNER_NAME}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("~ اوامر المشرفين ", callback_data="cbadmin"),
                
                    InlineKeyboardButton("~ اوامر الاعضاء ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("‹ اخفاء القائمة ›", callback_data="cls")
                ],
            ]
        ),
    )





@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):

    ###############################################################################################
    if not query.from_user.id == query.message.reply_to_message.from_user.id:
            return await query.answer("يا ملقوف الاوامر مو لك وخر !", show_alert=True)
    ###############################################################################################

    await query.edit_message_text(
        f"""**✶ اوامر الاعضاء ↓
 - - - [ اوامر التشغيل ] 
➥•  /play + ( اسم الاغنيه او بالرد )
➥• /vplay + ( اسم الفيديو - بالرد )
➥• /playlist - لعرض قائمة الانتظار
- - - [ اوامر البث المباشر ]
➥•  /stream + ( رابط البث ) ~ صوت
 ➥• /vstream + ( رابط البث ) ~ فيديو
- - - [ اوامر التحميل ]
➥• /song + ( اسم الصوت - الاغنيه )
➥• /vsong + ( اسم الفيديو )
➥• /search + ( اسم الاغنيه او المقطع ) ~ يعطيك روابط له 
- - - [ اوامر المجموعة ]
➥• /ping - لعرض سرعة البوت
➥• /uptime - لعرض حالة البوت
➥• /alive - لعرض قاعدة البيانات
✶ 𝗠𝗮𝘀𝘁𝗲𝗿 - @{OWNER_NAME}**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="ck")]]
        ),
    )

    
@Client.on_callback_query(filters.regex("kkl"))
async def kkl(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**✶ اوامر الاعضاء ↓
 - - - [ اوامر التشغيل ] 
➥•  /play + ( اسم الاغنيه او بالرد )
➥• /vplay + ( اسم الفيديو - بالرد )
➥• /playlist - لعرض قائمة الانتظار
- - - [ اوامر البث المباشر ]
➥•  /stream + ( رابط البث ) ~ صوت
 ➥• /vstream + ( رابط البث ) ~ فيديو
- - - [ اوامر التحميل ]
➥• /song + ( اسم الصوت - الاغنيه )
➥• /vsong + ( اسم الفيديو )
➥• /search + ( اسم الاغنيه او المقطع ) ~ يعطيك روابط له 
- - - [ اوامر المجموعة ]
➥• /ping - لعرض سرعة البوت
➥• /uptime - لعرض حالة البوت
➥• /alive - لعرض قاعدة البيانات
✶ 𝗠𝗮𝘀𝘁𝗲𝗿 - @{OWNER_NAME}**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    ###############################################################################################
    if not query.from_user.id == query.message.reply_to_message.from_user.id:
            return await query.answer("يا ملقوف الاوامر مو لك وخر !", show_alert=True)
    ###############################################################################################

    await query.edit_message_text(
        f"""**✶ اوامر المشرفين ↓
- - - [ اوامر التحكم بالمكالمة ]
➥ /skip - للتخطي 
➥ /end - لايقاف التشغيل
➥ /pause - لايقاف مؤقت
➥ /resume - لاكمال التشغيل
➥ /mute - لكتم الصوت 
➥ /unmute - لرفع الكتم
➥ /vmute - لكتم الفيديو 
➥ /vunmute - لالغاء كتم الفيديو
- - - [اوامر البوت + الحساب المساعد ]
➥ /reload - لتحديث البوت 
➥ {AMR_NAME} ادخلي - لدعوة الحساب المساعد للمجموعة
➥ {AMR_NAME} اطلعي - لطرد الحساب المساعد من المجموعة
✶ 𝗠𝗮𝘀𝘁𝗲𝗿 - @{OWNER_NAME}**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="ck")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("kka"))
async def kka(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**✶ اوامر المشرفين ↓
- - - [ اوامر التحكم بالمكالمة ]
➥ /skip - للتخطي 
➥ /stop - لايقاف التشغيل
➥ /pause - لايقاف مؤقت
➥ /resume - لاكمال التشغيل
➥ /mute - لكتم الصوت 
➥ /unmute - لرفع الكتم
➥ /vmute - لكتم الفيديو 
➥ /vunmute - لالغاء كتم الفيديو
- - - [اوامر البوت + الحساب المساعد ]
➥ /reload - لتحديث البوت 
   {AMR_NAME} ادخلي  - لدعوة الحساب المساعد للمجموعة
➥ {AMR_NAME} اطلعي  - لطرد الحساب المساعد من المجموعة
✶ 𝗠𝗮𝘀𝘁𝗲𝗿 - @{OWNER_NAME}**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    ###############################################################################################
    if not query.from_user.id == query.message.reply_to_message.from_user.id:
            return await query.answer("يا ملقوف الاوامر مو لك وخر !", show_alert=True)
    ###############################################################################################    
    await query.edit_message_text(
        f"""**اوامر المطوريين**
» /rmw - تنظيف جميع ملفات الخادم
» /rmd - تنظيف جميع ملفات التنزيلات
» /sysinfo - عرض معلومات الاخادم
» /update - تحديث البوت الى اخر اصدار
» /restart - اعادة تشغيل البوت
» /leaveall - طلب من الحساب المساعد المغادره من كل المجموعات
༄ مطور البوت - @{OWNER_NAME}
ملاحظه الاوامر هاذي للناس الي حطهم مطور البوت مطورين فقط !! -""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يا ملقوف الاوامر مو لك وخر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"اهلين عزيزي\n- هاذي لوحة التحكم الخاصه بالمكالمة",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("ايقاف", callback_data="cbstop"),
                      InlineKeyboardButton("ايقاف مؤقت", callback_data="cbpause"),
                      InlineKeyboardButton("استئناف", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("كتم الصوت", callback_data="cbmute"),
                      InlineKeyboardButton("الغاء الكتم", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("اغلاق القائمة", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("بدري ؟\nمعد فيه شي شغال عشان تتحكم", show_alert=True)

############################### القديمة
# @Client.on_callback_query(filters.regex("cls"))
# async def close(_, query: CallbackQuery):
#     a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
#     if not a.can_manage_voice_chats:
#         return await query.answer("يا حلو بس المشرفين يقدرون يتحكمون !", show_alert=True)
#     await query.message.delete()

#################################  الجديدة
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):

    ###############################################################################################
    if not query.from_user.id == query.message.reply_to_message.from_user.id:
            return await query.answer("يا ملقوف الاوامر مو لك وخر !", show_alert=True)
    ###############################################################################################    
    await query.message.delete()
