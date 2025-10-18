from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from config import ADMIN

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_caption(
            caption=text.START.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ⇆', url=f"https://telegram.me/join_request_accept_pro_bot?startgroup=true&admin=invite_users")],
                [InlineKeyboardButton('⇆ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ⇆', url=f"https://telegram.me/join_request_accept_pro_bot?startchannel=true&admin=invite_users")]
            ])
        )

    elif query.data == "help":
        await query.message.edit_caption(
            caption=text.HELP.format(query.from_user.mention)
        )

    elif query.data == "about":
        await query.message.edit_caption(
            caption=text.ABOUT
        )

    elif query.data == "close":
        await query.message.delete()
