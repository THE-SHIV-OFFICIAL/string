import logging
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# --- LOGGER SETUP ---
logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)
# --------------------

API_ID = int(getenv("API_ID", "27383453"))
API_HASH = getenv("API_HASH", "4c246fb0c649477cc2e79b6a178ddfaa")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "8418584090"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
MUST_JOIN = getenv("MUST_JOIN", "betabot_hub")

# ✅ Log Group ID Added
LOG_GROUP_ID = getenv("LOG_GROUP_ID", "istubabyhothaibabyyyyyyyyyyyyyyy")

# ✅ Added your new images to the list
START_IMG_URL = [
    getenv("START_IMG", "https://files.catbox.moe/gyeoqw.jpg"),
    "https://files.catbox.moe/i75dzc.jpg",
    "https://files.catbox.moe/h7whcn.jpg"
]

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "betabot_support")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "betabot_hub")
