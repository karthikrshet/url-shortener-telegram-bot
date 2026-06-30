from config import UPDATE_CHANNEL
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from plugins.filters import private_use


user_commands = [
    "mdisk_api",
    "api",
    "header",
    "footer",
    "username",
    "banner_image",
    "base_site",
    "settings",
]

@Client.on_message(filters.private | filters.all )
async def forcesub_handler(c: Client, m: Message):
    owner = c.owner
    if UPDATE_CHANNEL:
        invite_link = c.invite_link
        try:
            user = await c.get_chat_member(UPDATE_CHANNEL, m.from_user.id)
            if user.status == "kicked":
                await m.reply_text("**Hey You Are Banned 😜**", quote=True)
                return
        except UserNotParticipant:
            buttons = [
                [
                    InlineKeyboardButton(
                        text="Updates Channel", url=invite_link.invite_link
                    )
                ]
            ]
            buttons.append(
                [InlineKeyboardButton("🔄 Refresh", callback_data="sub_refresh")]
            )

            await m.reply_text(
                f"Hey {m.from_user.mention(style='md')} You Need Join My Updates Channel In Order To Use Me\n\n"
                "Press The Following Button To Join Now ",
                reply_markup=InlineKeyboardMarkup(buttons),
                quote=True,
            )
            await m.continue_propagation()
        except Exception as e:
            print(e)
            await m.reply_text(
                f"Something Wrong. Please Try Again Later Or Contact {owner.mention(style='md')}",
                quote=True,
            )
        return
    await m.continue_propagation()
