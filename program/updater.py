import os
import wget
import speedtest
import re
import sys
import asyncio
import subprocess
from asyncio import sleep
from program.utils.formatters import bytes
from driver.filters import command, other_filters
from config import BOT_USERNAME as bname
from driver.veez import bot as app
from git import Repo
from pyrogram.types import Message
from driver.filters import command
from pyrogram import Client, filters
from os import system, execle, environ
from driver.decorators import sudo_users_only
from git.exc import InvalidGitRepositoryError
from config import UPSTREAM_REPO, BOT_USERNAME

    
@Client.on_message(command(["speed", f"speedtest@{bname}", f"السرعه"]) & ~filters.edited)
async def statsguwid(_, message: Message):
    m = await message.reply_text("جاࢪي اختباࢪ السࢪعه💞.")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("جاࢪي تشغيل اختباࢪ سࢪعة التنزيل💞🤤..")
        test.download()
        m = await m.edit("تشغيل اختباࢪ سࢪعة التحميل...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return await m.edit(e)
    m = await m.edit("مشاࢪكة نتائج اختباࢪ السࢪعة....")
    path = wget.download(result["share"])

    output = f"""💡 **SpeedTest Results**
    
<u>**Client:**</u>
**ISP:** {result['client']['isp']}
**Country:** {result['client']['country']}
  
<u>**Server:**</u>
**Name:** {result['server']['name']}
**Country:** {result['server']['country']}, {result['server']['cc']}
**Sponsor:** {result['server']['sponsor']}
**Latency:** {result['server']['latency']}
⚡️ **Ping:** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()

def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@Client.on_message(command(["update", f"update@KTOMUISCBOT", f"تحديث"]) & ~filters.edited)
@sudo_users_only
async def update_repo(_, message: Message):
    chat_id = message.chat.id
    msg = await message.reply("💞🤤 جار تحديث البوت...")
    update_avail = updater()
    if update_avail:
        await msg.edit("✅ تـم تحـديث البوت\n\n• تم اعادة تشـغيل البـوت وعـاد مࢪة اخرى الى العـمل خـلال دقيـقة. واحـدة.")
        system("git pull -f && pip3 install -r requirements.txt")
        execle(sys.executable, sys.executable, "main.py", environ)
        return
    await msg.edit("✓ إعادة تشغيل البوت\n\n• الآن يمكنك استخدام هذا البوت مرة أخرى.", disable_web_page_preview=True)

@Client.on_message(command(["رست", f"restart@{BOT_USERNAME}", f"ريستارت"]) & ~filters.edited)
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`جاࢪ ترسيت البوت💞🎧...`")
    args = [sys.executable, "main.py"]
    await msg.edit("✓ إعادة تشغيل البوت\n\n• الآن يمكنك استخدام هذا البوت مرة أخرى.")
    execle(sys.executable, *args, environ)
    return
