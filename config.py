from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "15080950"))
API_HASH = getenv("API_HASH", "75eb42c44a91b4c859096f8d0a6659b6")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","𝙰𝚁𝙽𝙰𝚅 𝚂𝙸𝙽𝙶𝙷 ᴍᴜsɪᴄ ʙᴏᴛ")
BOT_USERNAME = getenv("BOT_USERNAME", "nehamusicop_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "OP_ARNAV_SINGH")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "link_copied")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/4d5a367e195c2fa13b164.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2a206d482ec7a0c347ce3.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5233362054").split()))
