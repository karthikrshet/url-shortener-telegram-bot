import asyncio
import contextlib
import logging
import os
import re
import sys

from config import ADMINS, OWNER_ID, SOURCE_CODE, UPDATE_CHANNEL
from database import update_user_info
from database.users import get_user
from helpers import Helpers, temp
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from translation import (
    ABOUT_REPLY_MARKUP,
    ABOUT_TEXT,
    ADMINS_MESSAGE,
    BACK_REPLY_MARKUP,
    BATCH_MESSAGE,
    CHANNELS_LIST_MESSAGE,
    CUSTOM_ALIAS_MESSAGE,
    HELP_MESSAGE,
    HELP_REPLY_MARKUP,
    METHOD_MESSAGE,
    METHOD_REPLY_MARKUP,
    START_MESSAGE,
    START_MESSAGE_REPLY_MARKUP,
)
from utils import get_me_button

logger = logging.getLogger(__name__)


@Client.on_callback_query(filters.regex("sub_refresh"))
async def refresh_cb(c, m):
    owner = c.owner
    if UPDATE_CHANNEL:
        try:
            user = await c.get_chat_member(UPDATE_CHANNEL, m.from_user.id)
            if user.status == "kicked":
                with contextlib.suppress(Exception):
                    await m.message.edit("**Hey You Are Banned**")
                return
        except UserNotParticipant:
            await m.answer(
                "You Have Not Yet Joined Our Channel. First Join And Then Press Refresh Button",
                show_alert=True,
            )

            return
        except Exception as e:
            print(e)
            await m.message.edit(
                f"Something Wrong. Please Try Again Later Or Contact {owner.mention(style='md')}"
            )

            return
    await m.message.delete()


@Client.on_callback_query(filters.regex(r"^ban"))
async def ban_cb_handler(c: Client, m: CallbackQuery):
    try:
        user_id = m.data.split("#")[1]
        user = await get_user(int(user_id))

        if user:
            if not user["banned"]:
                temp.BANNED_USERS.append(int(user_id))
                await update_user_info(user_id, {"banned": True})
                try:
                    owner = await c.get_users(int(OWNER_ID))
                    await c.send_message(
                        user_id,
                        f"You Are Now Banned From The Bot By Admin. Contact {owner.mention(style='md')} Regarding This",
                    )
                except Exception as e:
                    logging.error(e)
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Unban", callback_data=f"unban#{user_id}"
                            ),
                            InlineKeyboardButton("Close", callback_data="delete"),
                        ]
                    ]
                )
                await m.edit_message_reply_markup(reply_markup)
                await m.answer(
                    f"User [{user_id}] Has Been Banned From The Bot", show_alert=True
                )
            else:
                await m.answer("User Is Already Banned", show_alert=True)
        else:
            await m.answer("User Doesn't Exist", show_alert=True)
    except Exception as e:
        logging.exception(e, exc_info=True)


@Client.on_callback_query(filters.regex("^unban"))
async def unban_cb_handler(c, m: CallbackQuery):
    user_id = m.data.split("#")[1]
    user = await get_user(int(user_id))
    if user:
        if user["banned"]:
            temp.BANNED_USERS.remove(int(user_id))
            await update_user_info(user_id, {"banned": False})
            with contextlib.suppress(Exception):
                await c.send_message(
                    user_id,
                    "You Are Now Free To Use The Bot. You Have Been Unbanned By The Admin",
                )
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Ban", callback_data=f"ban#{user_id}"),
                        InlineKeyboardButton("Close", callback_data="delete"),
                    ]
                ]
            )
            await m.edit_message_reply_markup(reply_markup)
            await m.answer("User Is Unbanned", show_alert=True)
        else:
            await m.answer("User Is Not Banned Yet", show_alert=True)
    else:
        await m.answer("User Doesn't Exist", show_alert=True)


@Client.on_callback_query(filters.regex("^setgs"))
async def user_setting_cb(c, query: CallbackQuery):
    _, setting, toggle, user_id = query.data.split("#")
    myvalues = {setting: toggle == "True"}
    await update_user_info(user_id, myvalues)
    user = await get_user(user_id)
    buttons = await get_me_button(user)
    reply_markup = InlineKeyboardMarkup(buttons)
    try:
        await query.message.edit_reply_markup(reply_markup)
        setting = re.sub("is|_", " ", setting).title()
        toggle = "Enabled" if toggle == "True" else "Disabled"
        await query.answer(f"{setting} {toggle} Successfully", show_alert=True)
    except Exception as e:
        logging.error("Error Occurred While Updating User Information", exc_info=True)


@Client.on_callback_query()
async def on_callback_query(bot: Client, query: CallbackQuery):
    user_id = query.from_user.id
    h = Helpers()
    user = await get_user(user_id)
    if query.data == "delete":
        await query.message.delete()
    elif query.data == "help_command":
        await query.message.edit(
            HELP_MESSAGE.format(
                firstname=temp.FIRST_NAME,
                username=temp.BOT_USERNAME,
                repo=SOURCE_CODE,
                owner="@harmya",
            ),
            reply_markup=HELP_REPLY_MARKUP,
            disable_web_page_preview=True,
        )

    elif query.data == "about_command":
        bot = await bot.get_me()
        await query.message.edit(
            ABOUT_TEXT.format(bot.mention(style="md")),
            reply_markup=ABOUT_REPLY_MARKUP,
            disable_web_page_preview=True,
        )

    elif query.data == "start_command":
        new_user = await get_user(query.from_user.id)
        tit = START_MESSAGE.format(
            query.from_user.mention, new_user["method"], new_user["base_site"]
        )

        await query.message.edit(
            tit, reply_markup=START_MESSAGE_REPLY_MARKUP, disable_web_page_preview=True
        )

    elif query.data.startswith("change_method"):
        method_name = query.data.split("#")[1]
        user = temp.BOT_USERNAME
        await update_user_info(user_id, {"method": method_name})
        REPLY_MARKUP = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Back", callback_data="method_command")]]
        )

        await query.message.edit(
            "Method Changed Successfully To `{method}`".format(
                method=method_name, username=user
            ),
            reply_markup=REPLY_MARKUP,
        )

    elif query.data == "method_command":
        s = METHOD_MESSAGE.format(method=user["method"], shortener=user["base_site"])
        return await query.message.edit(s, reply_markup=METHOD_REPLY_MARKUP)
    elif query.data == "cbatch_command":
        if user_id not in ADMINS:
            return await query.message.edit(
                "Works only for admins", reply_markup=BACK_REPLY_MARKUP
            )

        await query.message.edit(BATCH_MESSAGE, reply_markup=BACK_REPLY_MARKUP)
    elif query.data == "alias_conf":
        await query.message.edit(
            CUSTOM_ALIAS_MESSAGE,
            reply_markup=BACK_REPLY_MARKUP,
            disable_web_page_preview=True,
        )

    elif query.data == "admins_list":
        if user_id not in ADMINS:
            return await query.message.edit(
                "Works Only For Admins", reply_markup=BACK_REPLY_MARKUP
            )

        await query.message.edit(
            ADMINS_MESSAGE.format(admin_list=await h.get_admins),
            reply_markup=BACK_REPLY_MARKUP,
        )

    elif query.data == "channels_list":
        if user_id not in ADMINS:
            return await query.message.edit(
                "Works Only For Admins", reply_markup=BACK_REPLY_MARKUP
            )

        await query.message.edit(
            CHANNELS_LIST_MESSAGE.format(channels=await h.get_channels),
            reply_markup=BACK_REPLY_MARKUP,
        )

    elif query.data == "restart":
        await query.message.edit("**Restarting.....**")
        await asyncio.sleep(5)
        os.execl(sys.executable, sys.executable, *sys.argv)
    await query.answer()
