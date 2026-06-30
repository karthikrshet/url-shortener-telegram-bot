import os

from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Mandatory variables for the bot to start
# API ID from https://my.telegram.org/auth
API_ID = int(os.environ.get("API_ID","25479482"))
# API Hash from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH","6ab604ff91a73fb91cc6526818e28ab1")
BOT_TOKEN = os.environ.get("BOT_TOKEN","6276597033:AAHC10wSfs0-k3Kc1yJjplJ8HTt45x_iHwM")  # Bot token from @BotFather
ADMINS = (
    [int(i.strip()) for i in os.environ.get("ADMINS").split(",")]
    if os.environ.get("ADMINS")
    else []
)

DATABASE_NAME = os.environ.get("DATABASE_NAME", "linkshortify")
DATABASE_URL = os.environ.get(
    "DATABASE_URL", "mongodb+srv://devilbot:Rajbot@cluster0.ldrbggy.mongodb.net/?retryWrites=true&w=majority"
)  # mongodb uri from https://www.mongodb.com/
OWNER_ID = int(os.environ.get("OWNER_ID", "5736579519"))  # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
 
#  Optionnal variables
LOG_CHANNEL = int(
    os.environ.get("LOG_CHANNEL", "-1001840955187")
)  # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Moneycaseofficial")  # For Force Subscription
BROADCAST_AS_COPY = is_enabled(
    (os.environ.get("BROADCAST_AS_COPY", "True")), True
)  # true if forward should be avoided
IS_PRIVATE = is_enabled(
    os.environ.get("IS_PRIVATE", "False"), "False"
)  # true for private use and restricting users
SOURCE_CODE = os.environ.get(
    "SOURCE_CODE", "https://github.com/learnandearnwithkarthik/krsbots"
)  # for upstream repo
# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "https://i.postimg.cc/wTcN9Cbz/bot-description.png")
LINK_BYPASS = is_enabled(
    (os.environ.get("LINK_BYPASS", "False")), False
)  # if true, urls will be bypassed
# your shortener site domain
BASE_SITE = os.environ.get("BASE_SITE", "Moneycase.link")

# For Admin use
CHANNELS = is_enabled((os.environ.get("CHANNELS", "True")), True)
CHANNEL_ID = (
    [int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(",")]
    if os.environ.get("CHANNEL_ID")
    else []
)

DE_BYPASS = (
    [i.strip() for i in os.environ.get("DE_BYPASS").split(",")]
    if os.environ.get("DE_BYPASS")
    else []
)
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(
    (os.environ.get("FORWARD_MESSAGE", "True")), True
)  # true if forwardd message to converted by reposting the post


WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "240"))
PORT = int(os.environ.get("PORT", "8000"))
