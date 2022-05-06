import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "A L O N E")
ALIVE_NAME = getenv("ALIVE_NAME", "A L O N E")
AMR_NAME = getenv("AMR_NAME", "A L O N E")
BOT_USERNAME = getenv("BOT_USERNAME", "S_T_1BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝗠𝗜𝗥𝗔 ♫")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "S_T_Dl")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "e1r_1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/0c2b093b524a1ebc0c417.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mafia132/uu")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/0c2b093b524a1ebc0c417.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/0c2b093b524a1ebc0c417.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/0c2b093b524a1ebc0c417.jpg")
