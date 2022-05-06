# Copyright (C) 2021 By VeezMusicProject

import sys
import os
import time
import traceback
import asyncio
import shutil
import psutil
from pyrogram import Client, filters
from pyrogram.types import Message
from driver.filters import command, other_filters
from driver.decorators import sudo_users_only, errors
from driver.decorators import sudo_users_only, humanbytes
downloads = os.path.realpath("program/downloads")
raw = os.path.realpath(".")


#stats


@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **تم تنظيف ملفات التنزيل**")
    else:
        await message.reply_text("❌ **مافي شي يحتاج التنظيف**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            if file.endswith('.raw'):
                os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **تم تنظيف جميع الملفات**")
    else:
        await message.reply_text("❌ **مافي شي يحتاج تنظيف**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.raw *.jpg")
        await message.reply_text("✅ **تم التنظيف**")
    else:
        await message.reply_text("✅ **تم التنظيف**")
        
        
