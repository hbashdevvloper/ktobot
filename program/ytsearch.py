import logging
from config import BOT_USERNAME
from driver.filters import command, other_filters
from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(command(["روابط", f"search@NKQBoT"]))
async def ytsearch(_, message: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "‹ اغلاق القائمه ›", callback_data="cls",
                )
            ]
        ]
    )

    try:
        if len(message.command) < 2:
            await message.reply_text("**اكتب اسم البحث يا عيني**")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎 **جاري البحث**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"▹￤ **العنوان:** __{results[i]['title']}__\n"
            text += f"▹￤ **مدة:** `{results[i]['duration']}`\n"
            text += f"▹￤ **المشاهدات:** `{results[i]['views']}`\n"
            text += f"▹￤ **القناة:** {results[i]['channel']}\n"
            text += f"▹￤: https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
