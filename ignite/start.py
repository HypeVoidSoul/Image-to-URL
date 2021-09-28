"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""
from pyrogram import StopPropagation
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from pyrogram import Client, filters


joinButton = InlineKeyboardMarkup([
    [InlineKeyboardButton(
        "🚀『 𝐆𝐫𝐨𝐮𝐩 』",
        url="https://t.me/Krakns")],
    [InlineKeyboardButton(
        "🍤『 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 』",
        url="https://t.me/KrakinzLab")],
])


@Client.on_message(filters.command("start"))
async def start(_, ryui: Message):
    user_and_chats = ryui.from_user.first_name
    await ryui.reply_photo(
        "https://telegra.ph/file/e26f9a6f0082b4171b6ef.jpg",
        reply_markup=joinButton,
        caption=f"""╰☆☆••| 𝗜𝗺𝗮𝗴𝗲 𝟮 𝗨𝗥𝗟 |••☆☆╮
            𝐇𝐨𝐰𝐝𝐲 **__`{user_and_chats}`__**,
           
🏷 ɪᴍᴀɢᴇ ᴛᴏ ᴜʀʟ ʙᴏᴛ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴛʜᴇꜱᴇ ʙᴇʟᴏᴡ ꜰɪʟᴇ ᴛʏᴘᴇꜱ ᴛᴏ [ᴛᴇʟᴇɢʀᴀᴘʜ](https://pypi.org/project/telegraph/) ᴜʀʟ.
🏷 ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴇɪᴛʜᴇʀ ɪɴ ᴄᴏᴍᴘʀᴇꜱꜱᴇᴅ ᴏʀ ᴜɴᴄᴏᴍᴘʀᴇꜱꜱᴇᴅ ꜰᴏʀᴍᴀᴛ
- `JPG`
- `JPEG`
- `PNG`
- `GIF` __(send as a document)__
- `Mp4` __(send as a document)__
- `Mp3` __(send as a document)__
🏷 ᴋᴇᴇᴘ ꜱᴇɴᴅɪɴɢ ʏᴏᴜʀ ʀᴇQᴜɪʀᴇᴅ ᴛʏᴘᴇ ꜰɪʟᴇꜱ ᴏɴᴇ ʙʏ ᴏɴᴇ.
🏷 ꜰɪʟᴇꜱ ᴍᴏʀᴇ ᴛʜᴇɴ 5ᴍʙ ɪꜱ ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ ᴛᴇʟᴇɢʀᴀᴘʜ.


🖥 Dҽʋ Mҽɳƚισɳ: @Krakinz | @KrakinzBot
╰☆☆••| 𝗜𝗺𝗮𝗴𝗲 𝟮 𝗨𝗥𝗟 |••☆☆╮""")
    raise StopPropagation
