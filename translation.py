from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """**💠 I Will Short All Your Channels Link With MoneyCase. Make Me Admin In Your Channel Withh All Rights And Follow Steps.

➡️ Example : `/batch Moneycase`

⚠️ You Can Also Use Channel ID Instead Of Channel Username

⚙️ Hit `/settings` To Control Your Settings**
"""

START_MESSAGE = """**Hi There {} !

🔰 I Am A Powerful Link Shortener Robot With Fast Speed And A Lot Of Functions.

➡️ To Know More About Bot Hit /help Command
➡️ To Link Your Shortener API Hit /api Command

Current Method : {}
**"""

HELP_MESSAGE = """**💠 Hey Welcome To LinkShortify Bot, I Have Many eatures To Make Your Work Easier And Help You To Earn More 💰.

👉 Here Is The List Of My Features :

➡️ Moneycase Detailed Balance
➡️ HyperLink And Hidden Link Support
➡️ Button Conversion Support
➡️ Your Moneycase Account Infomation
➡️ Domain Inclusion And Exclusion Options
➡️ Header And Footer Text Support
➡️ Replace Username Function
➡️ Banner Image Support
➡️ Batch Conversion For Channels
➡️ Channel Support For Admins Only

🔰 For Support Contact Here @Playitlinksofficial**"""

ABOUT_TEXT = """
**My Details:**

🔰 I Am : Moneycase RoBot

🔰 Our Support  : [Whatsapp]() & [Telegram](https://t.me/moneycaseadmin)

🔰 Official Channel : @Moneycaseofficial

🔰 Payment Proof : [Click Here](https://moneycase.link)

❤️ Made With Love By Moneycase ❤️**
"""


METHOD_MESSAGE = """

➡️ `Mdisk + Shortener (MDLINK)` - Change All The Links Of The Post To Your MDisk Account First And Then Short To Moneycase Link.

➡️ `Shortener` - Short All The Links Of The Post To Moneycase Link Directly.
    
**👉 Current Method :** {method}
    
Click Below Button To Set/Change Method :"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

**🔴 Format : [link] | [alias]**

**➡️ Example :** https://google.com | demolink

**⚠️ Note :** This Feature Works Only In Private Mode Only.
"""


ADMINS_MESSAGE = """
List Of Admins Who Has Access To This Bot :
{admin_list}"""


CHANNELS_LIST_MESSAGE = """
Here Is A List Of The Channels :
{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Methods", callback_data="method_command"),
            InlineKeyboardButton("Batch", callback_data="cbatch_command"),
        ],
        [
            InlineKeyboardButton("Custom Alias", callback_data="alias_conf"),
            InlineKeyboardButton("Admins", callback_data="admins_list"),
        ],
        [
            InlineKeyboardButton("Channels", callback_data="channels_list"),
            InlineKeyboardButton("Home", callback_data="start_command"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [InlineKeyboardButton("Close", callback_data="delete")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Help", callback_data="help_command"),
            InlineKeyboardButton("About", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("Method", callback_data="method_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Mdisk + Shortener", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "Shortener", callback_data="change_method#shortener"
            ),
        ],
        [
            InlineKeyboardButton("Back", callback_data="help_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Back", callback_data="help_command")]]
)

USER_ABOUT_MESSAGE = """
**💠 Here Are Your Current Settings For This Bot :

➡️ Method :** {method}

**➡️ MoneyCase API :** {shortener_api}

**➡️ Mdisk API :** {mdisk_api}

**➡️ Username :** @{username}

**➡️ Header Text :** {header_text}

**➡️ Footer Text :** {footer_text}

**➡️ Banner Image:**  {banner_image}
"""


MDISK_API_MESSAGE = """💠 To Add Or Update Your Mdisk API,
            
**➡️ Example :** `/mdisk_api 6LZq851sXoPHugiKQq`
            
⚠️ Get Your Mdisk API From @VideoToolMoneyTreebot

**🔴 To Remove Mdisk API :** `/mdisk_api remove`

**👉 Current Mdisk API :** `{}`

⚙️ Hit `/settings` To Control Your Settings"""

SHORTENER_API_MESSAGE = """To Add Or Update Your Moneycase API,
            
**➡️ Example :** `/api 6LZq851sXofffPHugiKQq`

⚠️ Get Your MoneyCase API From [Here](https://Moneycase.link/member/tools/api)

**🔴 To Remove Moneycase API :** `/api remove`

**👉 Current Moneycase API :** `{shortener_api}`

⚙️ Hit `/settings` To Control Your Settings"""

HEADER_MESSAGE = """💠 To Set The Header Text For Every Message Caption Or Text.

➡️ Reply To Any Text With `/header` To Set It As Header

**🔴 To Remove The Header Text :** `/header remove`

**👉 Current Header Text :** {header_text}

⚙️ Hit `/settings` To Control Your Settings"""

FOOTER_MESSAGE = """💠 To Set The Footer Text For Every Message Caption Or Text.

➡️ Reply To Any Text With `/footer` To Set It As Footer

**🔴 To Remove The Footer Text :** `/footer remove`

**👉 Current Header Text :** {footer_text}

⚙️ Hit `/settings` To Control Your Settings"""

USERNAME_TEXT = """💠 To Replace Specific Username From Post.

**➡️ Example :** `/username Moneycase`

**🔴 To Remove The Username :** `/username remove`

**👉 Current Username :** {username}

⚙️ Hit `/settings` To Control Your Settings"""

BANNER_IMAGE = """💠 To Replace The Image From Post.

**➡️ Example :** /banner_image https://Moneycase.link/logo.png

⚠️ You Can Also Reply To Any Image With `/banner_image` To Set It As Banner Image.

**🔴 To Remove The Banner Image :** `/banner_image remove`

**👉 Current Banner Image :** {banner_image}

⚙️ Hit `/settings` To Control Your Settings"""

INCLUDE_DOMAIN_TEXT = """💠 Bot Will Short Only Included Domains Only With This Command

**➡️ Example :** /include_domain t.me telegram.me

**🔴 To Remove The Specific Included Domain :** `/include_domain remove t.me`

**🔴 To Remove All Included Domains :** `/include_domain remove_all`

**👉 Current Included Domains :** {}

⚙️ Hit `/settings` To Control Your Settings"""

EXCLUDE_DOMAIN_TEXT = """💠 Bot Will Not Short Excluded Domains With This Command

**➡️ Example :** /exclude_domain t.me telegram.me

**🔴 To Remove The Specific Excluded Domain :** `/exclude_domain remove t.me`

**🔴 To Remove All Excluded Domains :** `/exclude_domain remove_all`

**👉 Current Excluded Domains :** {}

⚙️ Hit `/settings` To Control Your Settings"""

BANNED_USER_TXT = """
Usage : `/ban [User ID]`
Usage : `/unban [User ID]`

List Of Banned Users :
{users}"""
