# Zed-Thon
# Copyright (C) 2022 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.
import json
import math
import os
import random
import re
import time
from pathlib import Path
from uuid import uuid4

from telethon import Button, types
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery
from youtubesearchpython import VideosSearch

from zthon import zedub

from ..Config import Config
from ..helpers.functions import rand_key
from ..helpers.functions.utube import (
    download_button,
    get_yt_video_id,
    get_ytthumb,
    result_formatter,
    ytsearch_data,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.logger import logging
from . import get_user_from_event

LOGS = logging.getLogger(__name__)

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
MEDIA_PATH_REGEX = re.compile(r"(:?\<\bmedia:(:?(?:.*?)+)\>)")
tr = Config.COMMAND_HAND_LER

def get_thumb(name):
    url = f"https://github.com/TgCatUB/CatUserbot-Resources/blob/master/Resources/Inline/{name}?raw=true"
    return types.InputWebDocument(url=url, size=0, mime_type="image/png", attributes=[])


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="همسه(?: |$)(.*)")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        okk = (await event.get_reply_message()).sender_id
        addgvar("hmsa_id", okk)
    response = await event.client.inline_query(TG_BOT, "")
    await response[1].click(event.chat_id)
    await event.delete()


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
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
    uzerid = gvarstatus("hmsa_id")
    ussr = int(uzerid) if uzerid.isdigit() else uzerid
    try:
        zzz = await event.client.get_entity(ussr)
    except ValueError:
        return
    zelzal = f"[{zzz.first_name}](tg://user?id={zzz.id})"
    if query_user_id == Config.OWNER_ID or query_user_id == zzz.id or query_user_id in Config.SUDO_USERS:
        hmm = re.compile("troll (.*) (.*)")
        match = re.findall(hmm, query)
        inf = re.compile("secret (.*) (.*)")
        match2 = re.findall(inf, query)
        hid = re.compile("hide (.*)")
        match3 = re.findall(hid, query)
        if match or match2 or match3:
            user_list = []
            if match3:
                zilzal = "Chat"
                query = query[5:]
                info_type = ["hide", "لا يستطيـع", "ظهـاࢪ الࢪسـاله 📃 "]
                zed_type = ["رسـالة", "لا يستطيـع", "ظهـاࢪ الࢪسـاله 📃 "]
            else:
                zilzal = ""
                if match:
                    query = query[6:]
                    info_type = ["troll", "ماعـدا", "فتـح الࢪسـاله 🧾"]
                    zed_type = ["رسـالة", "ماعـدا", "فتـح الࢪسـاله 🧾"]
                elif match2:
                    query = query[7:]
                    info_type = ["secret", "يستطيـع", "فتـح الهمسـه 🗳"]
                    zed_type = ["همسـة", "يستطيـع", "فتـح الهمسـه 🗳"]
                if "|" in query:
                    iris, query = query.replace(" |", "|").replace("| ", "|").split("|")
                    users = iris.split(" ")
                else:
                    user, query = query.split(" ", 1)
                    users = [user]
                for user in users:
                    usr = int(user) if user.isdigit() else user
                    try:
                        u = await event.client.get_entity(usr)
                    except ValueError:
                        return
                    if u.username:
                        zilzal += f"@{u.username}"
                    else:
                        zilzal += f"[{u.first_name}](tg://user?id={u.id})"
                    user_list.append(u.id)
                    zilzal += " "
                zilzal = zilzal[:-1]
            old_msg = os.path.join("./zthon", f"{info_type[0]}.txt")
            try:
                jsondata = json.load(open(old_msg))
            except Exception:
                jsondata = False
            timestamp = int(time.time() * 2)
            new_msg = {
                str(timestamp): {"text": query}
                if match3
                else {"userid": user_list, "text": query}
            }
            buttons = [[Button.inline(info_type[2], data=f"{info_type[0]}_{timestamp}")],[Button.switch_inline("اضغـط للـرد", query=f"secret {Config.OWNER_ID} \nهلو", same_peer=True)]]
            result = builder.article(
                title=f"{info_type[0].title()} سـࢪيـه الـى {zilzal}.",
                description="ارسـال رساله مخفيه في مجمـوعـة."
                if match3
                else f"هـو فقـط مـن {info_type[1]} ࢪؤيتهـا.",
                thumb=get_thumb(f"{info_type[0]}.png"),
                text="✖✖✖"
                if match3
                else f"[ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 - همسـة سـࢪيـه 📠](t.me/ZedThon)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n**⌔╎الهمسـة لـ** {zilzal} \n**⌔╎هو فقط من يستطيع ࢪؤيتهـا**",
                buttons=buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(new_msg)
                json.dump(jsondata, open(old_msg, "w"))
            else:
                json.dump(new_msg, open(old_msg, "w"))
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
                    title="Not Found",
                    text=f"No Results found for `{str_y[1]}`",
                    description="INVALID",
                )
            try:
                await event.answer([result] if result else None)
            except QueryIdInvalidError:
                await event.answer(
                    [
                        builder.article(
                            title="Not Found",
                            text=f"No Results found for `{str_y[1]}`",
                            description="INVALID",
                        )
                    ]
                )
        elif string == "":
            results = []
            results.append(
                builder.article(
                    title="رسـاله مخفيـه",
                    description="ارسـال رساله مخفيه في مجمـوعـة.\nادخـل : hide + نـص",
                    text="__Send hidden message for spoilers/quote prevention.__",
                    thumb=get_thumb("hide.png"),
                    buttons=[
                        Button.switch_inline(
                            "اضغـط هنـا", query="hide هلو", same_peer=True
                        )
                    ],
                ),
            )
            results.append(
                builder.article(
                    title="همسـه سريـه",
                    description="ارسـال همسـه سريـه لـ (شخـص/اشخـاص).\nادخـل : secret + يوزر + نـص",
                    text=f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 **- همسـة سـࢪيـه**\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n**⌔╎اضغـط 🚹**\n**⌔╎لـ اࢪسـال همسـه سـࢪيـه الى** {zelzal} 💌\n**⌔╎او اضغـط 🛗**\n**⌔╎لـ اࢪسـال همسـه جماعية الى الشخص وأشخـاص آخرون 📨**",
                    thumb=get_thumb("secret.png"),
                    buttons=[
                        (
                            Button.switch_inline(
                                "🛗", query=f"secret {uzerid} @يوزر2 | \nهل", same_peer=True
                            ),
                            Button.switch_inline(
                                "🚹",
                                query=f"secret {uzerid} \nهلو",
                                same_peer=True,
                            ),
                        )
                    ],
                ),
            )
            results.append(
                builder.article(
                    title="رسـاله سريـه",
                    description="ارسـال همسـه سريـه لـ الكـل ماعدا شخص محدد.\nادخـل : troll + يوزر الشخص + نـص",
                    text="__Send **troll message** which everyone can see except the reciever.\n\nFor multiple users give space to username & use **|** to seperate text.__",
                    thumb=get_thumb("troll.png"),
                    buttons=[
                        (
                            Button.switch_inline(
                                "🚹", query="troll @username \nهلو", same_peer=True
                            ),
                            Button.switch_inline(
                                "🛗",
                                query="troll @username @username2 | \nهلو",
                                same_peer=True,
                            ),
                        )
                    ],
                ),
            )
            results.append(
                builder.article(
                    title="يوتيـوب انـلايـن",
                    description="تحميـل الفيديـو والمقاطع الصوتيـه من يوتيـوب\nادخـل : ytdl + نـص",
                    text="__Download videos or audios from YouTube with different options of resolutions/quality.__",
                    thumb=get_thumb("youtube.png"),
                    buttons=[
                        Button.switch_inline(
                            "اضغـط هنـا", query="ytdl حسين الجسمي احبك", same_peer=True
                        )
                    ],
                ),
            )
            await event.answer(results)
        elif string == "pmpermit":
            buttons = [
                Button.inline(text="عـرض الخيـارات", data="show_pmpermit_options"),
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
            "𝗗𝗲𝗽𝗹𝗼𝘆 𝘆𝗼𝘂𝗿 𝗼𝘄𝗻 𝗭𝗧𝗵𝗼𝗻.", "md"
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
