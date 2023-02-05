import json
import math
import os
import random
import re
import time
from uuid import uuid4

from telethon import Button, types
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery
from youtubesearchpython import VideosSearch

from zthon import zedub

from ..assistant.inlinefm import get_manager
from ..Config import Config
from ..helpers.functions import rand_key
from ..helpers.functions.utube import (
    download_button,
    get_yt_video_id,
    get_ytthumb,
    result_formatter,
    ytsearch_data,
)
from ..plugins import mention
from ..sql_helper.globals import gvarstatus
from . import CMD_INFO, GRP_INFO, PLG_INFO, check_owner
from .logger import logging

LOGS = logging.getLogger(__name__)

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
MEDIA_PATH_REGEX = re.compile(r"(:?\<\bmedia:(:?(?:.*?)+)\>)")
ZEDLOGO = "https://telegra.ph/file/f821d27af168206b472ad.mp4"
MALATH_PIC = "https://telegra.ph/file/f821d27af168206b472ad.mp4"
tr = Config.COMMAND_HAND_LER


def getkey(val):
    for key, value in GRP_INFO.items():
        for plugin in value:
            if val == plugin:
                return key
    return None


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


def main_menu():
    text = f"**🧑🏻‍💻┊مـرحباً عـزيـزي {mention}**\n**🛂┊في قائمـة اوامـر المسـاعـده \n**⋆─┄─┄─┄─ ᶻᵗʰᵒᶰ ─┄─┄─┄─⋆**\n[ᯓ 𝗭𝗧𝗵𝗼𝗻 🦾♥️](https://t.me/ZedThon)\n\n"
    buttons = [
        (Button.inline("ℹ️ معلومـات الملفـات", data="check"),),
        (
            Button.inline("ملفات الادمن 👮‍ ", data="admin_menu"),
            Button.inline("ملفات البوت 🤖", data="bot_menu"),
        ),
        (
            Button.inline("ملفات التسليـه 🎮", data="fun_menu"),
            Button.inline("ملفات الخـدمـات 🧩", data="misc_menu"),
        ),
        (
            Button.inline("الادوات 💡", data="tools_menu"),
            Button.inline("المـرفقـات 🖥", data="utils_menu"),
        ),
        (
            Button.inline("البـحـث والتحميـل 🪄", data="extra_menu"),
            Button.inline("🔒 اغـلاق اللوحـه", data="close"),
        ),
    ]

    return text, buttons


def command_in_category(cname):
    cmds = 0
    for i in GRP_INFO[cname]:
        for _ in PLG_INFO[i]:
            cmds += 1
    return cmds


def paginate_help(
    page_number,
    loaded_plugins,
    prefix,
    plugins=True,
    category_plugins=None,
    category_pgno=0,
):  # sourcery no-metrics
    try:
        number_of_rows = int(gvarstatus("NO_OF_ROWS_IN_HELP") or 5)
    except (ValueError, TypeError):
        number_of_rows = 5
    try:
        number_of_cols = int(gvarstatus("NO_OF_COLUMNS_IN_HELP") or 2)
    except (ValueError, TypeError):
        number_of_cols = 2
    HELP_EMOJI = gvarstatus("HELP_EMOJI") or " "
    helpable_plugins = [p for p in loaded_plugins if not p.startswith("_")]
    helpable_plugins = sorted(helpable_plugins)
    if len(HELP_EMOJI) == 2:
        if plugins:
            modules = [
                Button.inline(
                    f"{HELP_EMOJI[0]} {x} {HELP_EMOJI[1]}",
                    data=f"{x}_prev(1)_command_{prefix}_{page_number}",
                )
                for x in helpable_plugins
            ]
        else:
            modules = [
                Button.inline(
                    f"{HELP_EMOJI[0]} {x} {HELP_EMOJI[1]}",
                    data=f"{x}_cmdhelp_{prefix}_{page_number}_{category_plugins}_{category_pgno}",
                )
                for x in helpable_plugins
            ]
    elif plugins:
        modules = [
            Button.inline(
                f"{HELP_EMOJI} {x} {HELP_EMOJI}",
                data=f"{x}_prev(1)_command_{prefix}_{page_number}",
            )
            for x in helpable_plugins
        ]
    else:
        modules = [
            Button.inline(
                f"{HELP_EMOJI} {x} {HELP_EMOJI}",
                data=f"{x}_cmdhelp_{prefix}_{page_number}_{category_plugins}_{category_pgno}",
            )
            for x in helpable_plugins
        ]
    if number_of_cols == 1:
        pairs = list(zip(modules[::number_of_cols]))
    elif number_of_cols == 2:
        pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    else:
        pairs = list(
            zip(
                modules[::number_of_cols],
                modules[1::number_of_cols],
                modules[2::number_of_cols],
            )
        )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    elif len(modules) % number_of_cols == 2:
        pairs.append((modules[-2], modules[-1]))
    max_num_pages = math.ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if plugins:
        if len(pairs) > number_of_rows:

            pairs = pairs[
                modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
            ] + [
                (
                    Button.inline("⌫", data=f"{prefix}_prev({modulo_page})_plugin"),
                    Button.inline("⚙️ الرئيسيـه", data="mainmenu"),
                    Button.inline("⌦", data=f"{prefix}_next({modulo_page})_plugin"),
                )
            ]
        else:
            pairs = pairs + [(Button.inline("⚙️ الرئيسيـه", data="mainmenu"),)]
    elif len(pairs) > number_of_rows:
        if category_pgno < 0:
            category_pgno = len(pairs) + category_pgno
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline(
                    "⌫",
                    data=f"{prefix}_prev({modulo_page})_command_{category_plugins}_{category_pgno}",
                ),
                Button.inline(
                    "⬅️ رجـوع ",
                    data=f"back_plugin_{category_plugins}_{category_pgno}",
                ),
                Button.inline(
                    "⌦",
                    data=f"{prefix}_next({modulo_page})_command_{category_plugins}_{category_pgno}",
                ),
            )
        ]
    else:
        if category_pgno < 0:
            category_pgno = len(pairs) + category_pgno
        pairs = pairs + [
            (
                Button.inline(
                    "⬅️ رجـوع ",
                    data=f"back_plugin_{category_plugins}_{category_pgno}",
                ),
            )
        ]
    return pairs


@zedub.tgbot.on(InlineQuery)
async def inline_handler(event):  # sourcery no-metrics
    builder = event.builder
    result = None
    query = event.text
    string = query.lower()
    query.split(" ", 2)
    str_y = query.split(" ", 1)
    string.split()
    query_user_id = event.query.user_id
    if query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS:
        hmm = re.compile("troll (.*) (.*)")
        match = re.findall(hmm, query)
        inf = re.compile("secret (.*) (.*)")
        match2 = re.findall(inf, query)
        hid = re.compile("hide (.*)")
        match3 = re.findall(hid, query)
        if query.startswith("**ZThon"):
            buttons = [
                (
                    Button.inline("Stats", data="stats"),
                    Button.url("𝗭𝗧𝗵𝗼𝗻™ 𓅛", "https://t.me/ZedThon"),
                )
            ]
            ALIVE_PIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/f821d27af168206b472ad.mp4"
            IALIVE_PIC = gvarstatus("IALIVE_PIC") or "https://telegra.ph/file/f821d27af168206b472ad.mp4"
            if IALIVE_PIC:
                ZED = [x for x in IALIVE_PIC.split()]
                PIC = list(ZED)
                I_IMG = random.choice(PIC)
            if not IALIVE_PIC and ALIVE_PIC:
                ZED = [x for x in ALIVE_PIC.split()]
                PIC = list(ZED)
                I_IMG = random.choice(PIC)
            elif not IALIVE_PIC:
                I_IMG = None
            if I_IMG and I_IMG.endswith((".jpg", ".png", ".mp4")):
                result = builder.photo(
                    I_IMG,
                    text=query,
                    buttons=buttons,
                )
            elif I_IMG:
                result = builder.document(
                    I_IMG,
                    title="Alive ZThon",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Alive ZThon",
                    text=query,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
        elif query.startswith("Inline buttons"):
            markdown_note = query[14:]
            prev = 0
            note_data = ""
            buttons = []
            media = None
            zedmedia = MEDIA_PATH_REGEX.search(markdown_note)
            if zedmedia:
                media = zedmedia.group(2)
                markdown_note = markdown_note.replace(zedmedia.group(0), "")
            for match in BTN_URL_REGEX.finditer(markdown_note):
                n_escapes = 0
                to_check = match.start(1) - 1
                while to_check > 0 and markdown_note[to_check] == "\\":
                    n_escapes += 1
                    to_check -= 1
                if n_escapes % 2 == 0:
                    buttons.append(
                        (match.group(2), match.group(3), bool(match.group(4)))
                    )
                    note_data += markdown_note[prev : match.start(1)]
                    prev = match.end(1)
                elif n_escapes % 2 == 1:
                    note_data += markdown_note[prev:to_check]
                    prev = match.start(1) - 1
                else:
                    break
            else:
                note_data += markdown_note[prev:]
            message_text = note_data.strip()
            tl_ib_buttons = ibuild_keyboard(buttons)
            if media and media.endswith((".jpg", ".png", ".mp4")):
                result = builder.photo(
                    media,
                    text=message_text,
                    buttons=tl_ib_buttons,
                )
            elif media:
                result = builder.document(
                    media,
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                )
            else:
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)
        elif match:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            troll = os.path.join("./zthon", "troll.txt")
            try:
                jsondata = json.load(open(troll))
            except Exception:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        zilzal = f"[{u.first_name}](tg://user?id={u.id})"
                    else:
                        zilzal = f"@{u.username}"
                    u = int(u.id)
                except ValueError:
                    # ValueError: Could not find the input entity
                    zilzal = f"[user](tg://user?id={u})"
            except ValueError:
                # if u is username
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    zilzal = f"[{u.first_name}](tg://user?id={u.id})"
                else:
                    zilzal = f"@{u.username}"
                u = int(u.id)
            except Exception:
                return
            timestamp = int(time.time() * 2)
            newtroll = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [Button.inline("فتـح الࢪسـاله 🧾", data=f"troll_{timestamp}")]
            result = builder.article(
                title="رسـاله سـࢪيـه",
                text=f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 **- ࢪسـالة سـࢪيـه 🗳**\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n**⌔╎الࢪسـاله لـ** {zilzal} \n**⌔╎هو فقط من يستطيع فتحهـا**",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newtroll)
                json.dump(jsondata, open(troll, "w"))
            else:
                json.dump(newtroll, open(troll, "w"))
        elif match2:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./zthon", "secrets.txt")
            try:
                jsondata = json.load(open(secret))
            except Exception:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.first_name:
                        zilzal = f"[{u.first_name}](tg://user?id={u.id})"
                    else:
                        zilzal = f"@{u.username}"
                    u = int(u.id)
                except ValueError:
                    # ValueError: Could not find the input entity
                    zilzal = f"[user](tg://user?id={u})"
            except ValueError:
                # if u is username
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.first_name:
                    zilzal = f"[{u.first_name}](tg://user?id={u.id})"
                else:
                    zilzal = f"@{u.username}"
                u = int(u.id)
            except Exception:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [Button.inline("فتـح الهمسـه 🗳", data=f"secret_{timestamp}")]
            result = builder.article(
                title="** همسـه سـريـه**",
                text=f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 **- همسـة سـࢪيـه 📠**\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n**⌔╎الهمسـة لـ** {zilzal} \n**⌔╎هو فقط من يستطيع ࢪؤيتهـا**",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))
        elif match3:
            query = query[5:]
            builder = event.builder
            hide = os.path.join("./zthon", "hide.txt")
            try:
                jsondata = json.load(open(hide))
            except Exception:
                jsondata = False
            timestamp = int(time.time() * 2)
            newhide = {str(timestamp): {"text": query}}

            buttons = [Button.inline("إظهـاࢪ الࢪسـاله 📃", data=f"hide_{timestamp}")]
            result = builder.article(
                title="**⌔╎ࢪسـاله مشفـࢪه 📟**",
                text=f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 **- ࢪسـالة مشفـࢪه 📟**\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n**⌔╎اضغـط الـزࢪ لـ إظهـاࢪ الࢪسـاله**",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newhide)
                json.dump(jsondata, open(hide, "w"))
            else:
                json.dump(newhide, open(hide, "w"))
        elif string == "help":
            _result = main_menu()
            result = builder.article(
                title="© ZThon Help",
                description="Help menu for ZThon",
                text=_result[0],
                buttons=_result[1],
                link_preview=False,
            )
            await event.answer([result] if result else None)
        elif str_y[0].lower() == "ytdl" and len(str_y) == 2:
            link = get_yt_video_id(str_y[1].strip())
            found_ = True
            if link is None:
                search = VideosSearch(str_y[1].strip(), limit=15)
                resp = (search.result()).get("result")
                if len(resp) == 0:
                    found_ = False
                else:
                    outdata = await result_formatter(resp)
                    key_ = rand_key()
                    ytsearch_data.store_(key_, outdata)
                    buttons = [
                        Button.inline(
                            f"1 / {len(outdata)}",
                            data=f"ytdl_next_{key_}_1",
                        ),
                        Button.inline(
                            "القائمـة 📜",
                            data=f"ytdl_listall_{key_}_1",
                        ),
                        Button.inline(
                            "⬇️  تحميـل",
                            data=f'ytdl_download_{outdata[1]["video_id"]}_0',
                        ),
                    ]
                    caption = outdata[1]["message"]
                    photo = await get_ytthumb(outdata[1]["video_id"])
            else:
                caption, buttons = await download_button(link, body=True)
                photo = await get_ytthumb(link)
            if found_:
                markup = event.client.build_reply_markup(buttons)
                photo = types.InputWebDocument(
                    url=photo, size=0, mime_type="image/jpeg", attributes=[]
                )
                text, msg_entities = await event.client._parse_message_text(
                    caption, "html"
                )
                result = types.InputBotInlineResult(
                    id=str(uuid4()),
                    type="photo",
                    title=link,
                    description="⬇️ اضغـط للتحميـل",
                    thumb=photo,
                    content=photo,
                    send_message=types.InputBotInlineMessageMediaAuto(
                        reply_markup=markup, message=text, entities=msg_entities
                    ),
                )
            else:
                result = builder.article(
                    title="**- غيـر موجـود ✘**",
                    text=f"**- لا يوجـد نتائـج لــ **`{str_y[1]}` ✘",
                    description="غير صالحة",
                )
            try:
                await event.answer([result] if result else None)
            except QueryIdInvalidError:
                await event.answer(
                    [
                        builder.article(
                            title="**- غيـر موجـود ✘**",
                            text=f"**- لا يوجـد نتائـج لــ **`{str_y[1]}` ✘",
                            description="غير صالحة",
                        )
                    ]
                )
        elif string == "age_verification_alert":
            buttons = [
                Button.inline(text="Yes I'm 18+", data="age_verification_true"),
                Button.inline(text="No I'm Not", data="age_verification_false"),
            ]
            markup = event.client.build_reply_markup(buttons)
            photo = types.InputWebDocument(
                url="https://i.imgur.com/Zg58iXc.jpg",
                size=0,
                mime_type="image/jpeg",
                attributes=[],
            )
            text, msg_entities = await event.client._parse_message_text(
                "<b>ARE YOU OLD ENOUGH FOR THIS ?</b>", "html"
            )
            result = types.InputBotInlineResult(
                id=str(uuid4()),
                type="photo",
                title="Age verification",
                thumb=photo,
                content=photo,
                send_message=types.InputBotInlineMessageMediaAuto(
                    reply_markup=markup, message=text, entities=msg_entities
                ),
            )
            await event.answer([result] if result else None)
        elif string == "pmpermit":
            buttons = [
                Button.inline(text="عـرض الخيـارات ", data="show_pmpermit_options"),
            ]
            PM_PIC = gvarstatus("pmpermit_pic")
            if PM_PIC:
                CAT = [x for x in PM_PIC.split()]
                PIC = list(CAT)
                CAT_IMG = random.choice(PIC)
            else:
                CAT_IMG = None
            query = gvarstatus("pmpermit_text")
            if CAT_IMG and CAT_IMG.endswith((".jpg", ".jpeg", ".png")):
                result = builder.photo(
                    CAT_IMG,
                    # title="Alive zed",
                    text=query,
                    buttons=buttons,
                )
            elif CAT_IMG:
                result = builder.document(
                    CAT_IMG,
                    title="Alive cat",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Alive cat",
                    text=query,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
    else:
        buttons = [
            (
                Button.url("قنـاة السـورس", "https://t.me/ZedThon"),
                Button.url(
                    "مطـور السـورس",
                    "https://t.me/zzzzl1l",
                ),
            )
        ]
        markup = event.client.build_reply_markup(buttons)
        photo = types.InputWebDocument(
            url=ZEDLOGO, size=0, mime_type="image/jpeg", attributes=[]
        )
        text, msg_entities = await event.client._parse_message_text(
            "- لـ تنصيب سـورس زدثــون 𝗭𝗧𝗵𝗼𝗻", "md"
        )
        result = types.InputBotInlineResult(
            id=str(uuid4()),
            type="photo",
            title="𝗭𝗧𝗵𝗼𝗻 𓅛",
            description="روابـط التنصـيب",
            url="https://t.me/ZedThon/105",
            thumb=photo,
            content=photo,
            send_message=types.InputBotInlineMessageMediaAuto(
                reply_markup=markup, message=text, entities=msg_entities
            ),
        )
        await event.answer([result] if result else None)


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"close")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    buttons = [
        (Button.inline("فتح القائمة 🔓", data="mainmenu"),),
    ]
    await event.edit("غلق القائمة 🔒", buttons=buttons)


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"check")))
async def on_plugin_callback_query_handler(event):
    text = f"**⌔╎الملفـات 🗃 :** {len(PLG_INFO)}\n**⌔╎عـدد الاوامـر 📑 :** {len(CMD_INFO)}\
        \n\n**.مساعده + اسم الملف :** للحصول على معلومـات الملـف المسـاعد المحـدد\n**.مساعده + الامـر :** للحصول ع معلومـات لـ الامـر المحـدد.\n**.استفسار + الاوامر :** للبحث عـن أي أوامـر."
    await event.answer(text, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"(.*)_menu")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    category = str(event.pattern_match.group(1).decode("UTF-8"))
    buttons = paginate_help(0, GRP_INFO[category], category)
    text = f"**⌔╎القسـم 🗄: **{category}\
        \n**⌔╎مجمـوع الملفـات 🗃 :** {len(GRP_INFO[category])}\
        \n**⌔╎مجمـوع الاوامـر 🔍:** {command_in_category(category)}"
    await event.edit(text, buttons=buttons)


@zedub.tgbot.on(
    CallbackQuery(
        data=re.compile(b"back_([a-z]+)_([a-z_1-9]+)_([0-9]+)_?([a-z1-9]+)?_?([0-9]+)?")
    )
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    mtype = str(event.pattern_match.group(1).decode("UTF-8"))
    category = str(event.pattern_match.group(2).decode("UTF-8"))
    pgno = int(event.pattern_match.group(3).decode("UTF-8"))
    if mtype == "plugin":
        buttons = paginate_help(pgno, GRP_INFO[category], category)
        text = f"**⌔╎القسـم 🗄: **{category}\
            \n**⌔╎مجمـوع الملفـات 🗃 :** {len(GRP_INFO[category])}\
             \n**⌔╎مجمـوع الاوامـر 🔍:** {command_in_category(category)}"
    else:
        category_plugins = str(event.pattern_match.group(4).decode("UTF-8"))
        category_pgno = int(event.pattern_match.group(5).decode("UTF-8"))
        buttons = paginate_help(
            pgno,
            PLG_INFO[category],
            category,
            plugins=False,
            category_plugins=category_plugins,
            category_pgno=category_pgno,
        )
        text = f"**⌔╎الملـف 📁: **`{category}`\
                \n**⌔╎القسـم 🗄: ** {getkey(category)} \
                \n**⌔╎مجمـوع الاوامـر 🔍 :** {len(PLG_INFO[category])}"
    await event.edit(text, buttons=buttons)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"mainmenu")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    _result = main_menu()
    await event.edit(_result[0], buttons=_result[1])


@zedub.tgbot.on(
    CallbackQuery(data=re.compile(rb"(.*)_prev\((.+?)\)_([a-z]+)_?([a-z]+)?_?(.*)?"))
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    category = str(event.pattern_match.group(1).decode("UTF-8"))
    current_page_number = int(event.data_match.group(2).decode("UTF-8"))
    htype = str(event.pattern_match.group(3).decode("UTF-8"))
    if htype == "plugin":
        buttons = paginate_help(current_page_number - 1, GRP_INFO[category], category)
    else:
        category_plugins = str(event.pattern_match.group(4).decode("UTF-8"))
        category_pgno = int(event.pattern_match.group(5).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number - 1,
            PLG_INFO[category],
            category,
            plugins=False,
            category_plugins=category_plugins,
            category_pgno=category_pgno,
        )
        text = f"**⌔╎الملـف 📁: **`{category}`\
                \n**⌔╎القسـم 🗄: ** {getkey(category)} \
                \n**⌔╎مجمـوع الاوامـر 🔍 :** {len(PLG_INFO[category])}"
        try:
            return await event.edit(text, buttons=buttons)
        except Exception as e:
            LOGS.error(str(e))
    await event.edit(buttons=buttons)


@zedub.tgbot.on(
    CallbackQuery(data=re.compile(rb"(.*)_next\((.+?)\)_([a-z]+)_?([a-z]+)?_?(.*)?"))
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    category = str(event.pattern_match.group(1).decode("UTF-8"))
    current_page_number = int(event.data_match.group(2).decode("UTF-8"))
    htype = str(event.pattern_match.group(3).decode("UTF-8"))
    category_plugins = event.pattern_match.group(4)
    if category_plugins:
        category_plugins = str(category_plugins.decode("UTF-8"))
    category_pgno = event.pattern_match.group(5)
    if category_pgno:
        category_pgno = int(category_pgno.decode("UTF-8"))
    if htype == "plugin":
        buttons = paginate_help(current_page_number + 1, GRP_INFO[category], category)
    else:
        buttons = paginate_help(
            current_page_number + 1,
            PLG_INFO[category],
            category,
            plugins=False,
            category_plugins=category_plugins,
            category_pgno=category_pgno,
        )
    await event.edit(buttons=buttons)


@zedub.tgbot.on(
    CallbackQuery(
        data=re.compile(b"(.*)_cmdhelp_([a-z_1-9]+)_([0-9]+)_([a-z]+)_([0-9]+)")
    )
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    cmd = str(event.pattern_match.group(1).decode("UTF-8"))
    category = str(event.pattern_match.group(2).decode("UTF-8"))
    pgno = int(event.pattern_match.group(3).decode("UTF-8"))
    category_plugins = str(event.pattern_match.group(4).decode("UTF-8"))
    category_pgno = int(event.pattern_match.group(5).decode("UTF-8"))
    buttons = [
        (
            Button.inline(
                "⬅️ رجـوع ",
                data=f"back_command_{category}_{pgno}_{category_plugins}_{category_pgno}",
            ),
            Button.inline("القائمة الرئيسية ⚙️", data="mainmenu"),
        )
    ]
    text = f"**⌔╎الامـر 🔍:** `{cmd}`\n**⌔╎اسـم الملـف 📁:** `{category}`\n**⌔╎القسـم 🗄:** `{category_plugins}`\n\n**⌔╎المقدمـة 📍 :**\n{CMD_INFO[cmd][0]}"
    await event.edit(text, buttons=buttons)
