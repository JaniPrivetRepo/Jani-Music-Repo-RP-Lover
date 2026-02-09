from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Jani_Music import app
from config import BOT_USERNAME
from Jani_Music.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ Wҽʅƈσɱҽ Tσ Jαɳι Rҽρσʂ ❃</u>
 
✼ 𝙍𝙚𝙥𝙤 𝙏𝙤 𝙉𝙝𝙞 𝙈𝙞𝙡𝙚𝙜𝙖 😁
 
❉  पत्थर की मूरत के आगे सिर मत झुका जब कुछ ना बचे तो शैतान से नाता बाना !!  

✼ || [ᴊᴀɴɪ 𔘓 ᴍᴜꜱɪᴄ™♪ 𝚁𔘓𝙿 ](https://t.me/Jani_Music_Robot?start=_tgr_I548BOJjYTg1)) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• Update •", url="https://t.me/Selfish_Jani_Lover"),
          InlineKeyboardButton("• Support •", url="https://t.me/+a3O_RK3xMbA1ZGZl"),
          ],
[
InlineKeyboardButton("• ϻᴧɪη ʙσᴛ •", url=f"https://t.me/Jani_Music_Robot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://litter.catbox.moe/k2zjdk.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
