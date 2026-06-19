import random
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

# Config aur DB se naye imports (Sahi path ke sath)
from config import START_IMG_URL, OWNER_ID, SUPPORT_CHAT, UPDATE_CHANNEL, LOG_GROUP_ID
from StringGenBot.db.users import add_served_user

# Custom Filters
def filter_cmd(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter_cmd("start"))
async def start(bot: Client, msg: Message):
    # --- DATABASE & LOGGING LOGIC ---
    user_id = msg.from_user.id
    
    # DB me user add karega, naya hua toh log bhejega
    is_new_user = await add_served_user(user_id)
    
    if is_new_user:
        log_text = (
            f"🆕 **Naya User Aaya!**\n\n"
            f"👤 **Naam:** {msg.from_user.mention}\n"
            f"🆔 **ID:** `{user_id}`\n"
            f"🤖 **Bot:** String Gen Bot"
        )
        try:
            await bot.send_message(LOG_GROUP_ID, log_text)
        except Exception as e:
            print(f"Log bhejne me error: {e}")
    # --------------------------------

    # --- LOADING ANIMATION ---
    loading_msg = await msg.reply_text("<b>ᴌᴏᴀᴅɪɴɢ....</b>")
    await asyncio.sleep(0.3)
    
    await loading_msg.edit_text("<b>ꜱᴛᴀʀᴛɪɴɢ..ʙᴀʙʏ.❤️❤️</b>")
    await asyncio.sleep(0.3)
    
    await loading_msg.edit_text("<b>ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ❤️😌🫣🫣</b>")
    await asyncio.sleep(0.5)
    
    await loading_msg.edit_text("<b>ʙᴇᴛᴀ ʙᴏᴛs🫣🫣.</b>")
    await asyncio.sleep(0.5)
    
    await loading_msg.delete()
    # -------------------------

    # --- TYPING ACTION & STICKER ---
    await bot.send_chat_action(msg.chat.id, ChatAction.TYPING)
    await msg.reply_sticker("CAACAgUAAxkBAAFJgZ1qBGwx9Z9vW5BhG3dw0l1A5j4CyQACXRYAAuc-wVWs4--9DGlDKzsE")
    # -------------------------------

    me2 = (await bot.get_me()).mention

    START_TXT = f"""**» ʜᴇʏ  {msg.from_user.mention}  ✤,

» ɪ ᴀᴍ {me2},

» ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

» ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

» ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ !**

🤞 𝐏ᴏᴡєʀєᴅ 𝐁ʏ ➛ BETA BOT HUB.🙂❤️"""

    START_BTN = [
        [InlineKeyboardButton("⌨️ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ", callback_data="generate")],
        [
            InlineKeyboardButton("💌 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
            InlineKeyboardButton("💻 ᴏᴡɴᴇʀ", user_id=OWNER_ID),
        ],
        [InlineKeyboardButton("📘 ɢᴜɪᴅᴇ", callback_data="guide")]
    ]

    # ✅ Random image select karne ka logic
    if isinstance(START_IMG_URL, list):
        start_img = random.choice(START_IMG_URL)
    else:
        start_img = START_IMG_URL

    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=start_img,
        caption=START_TXT,
        reply_markup=InlineKeyboardMarkup(START_BTN),
    )


GUIDE_TXT = """**✦ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs

➻ ᴛʏᴘᴇ /gen ᴏʀ ᴛᴀᴘ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ғᴏʀ ɢᴇɴ sᴇssɪᴏɴ.

➻ ᴛʏᴘᴇ /ping ᴄʜᴇᴄᴋ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ

➻ ᴛʏᴘᴇ /stats ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ sᴛᴀᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ)

➻ ᴛʏᴘᴇ /broadcast ᴛᴏ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs + ᴄʜᴀᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ)

⦿ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ғᴏʀ ᴍᴏʀᴇ ᴜᴘᴅᴀᴛᴇs.**

🤞 𝐏ᴏᴡєʀєᴅ 𝐁ʏ ➛ BETA BOT HUB.🙂❤️"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "guide":
        await query.message.edit_text(
            text=GUIDE_TXT,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("💌 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton("🪧 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE_CHANNEL}"),
                ],
                [InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="start_menu")]
            ])
        )

    elif data == "start_menu":
        me2 = (await client.get_me()).mention

        START_TXT = f"""**» ʜᴇʏ  {query.from_user.mention}  ✤,

» ɪ ᴀᴍ {me2},

» ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

» ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

» ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ !**

🤞 𝐏ᴏᴡєʀєᴅ 𝐁ʏ ➛ BETA BOT HUB.🙂❤️"""

        START_BTN = [
            [InlineKeyboardButton("⌨️ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ", callback_data="generate")],
            [
                InlineKeyboardButton("💌 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                InlineKeyboardButton("💻 ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            ],
            [InlineKeyboardButton("📘 ɢᴜɪᴅᴇ", callback_data="guide")]
        ]

        try:
            await query.message.edit_caption(
                caption=START_TXT,
                reply_markup=InlineKeyboardMarkup(START_BTN)
            )
        except:
            await query.message.edit_text(
                text=START_TXT,
                reply_markup=InlineKeyboardMarkup(START_BTN)
            )
