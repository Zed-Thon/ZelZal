# animation code for zed edit by @zlzzl77

import asyncio
from collections import deque
import os
import random
from urllib.parse import quote_plus
from collections import deque
from zthon.core.logger import logging
from zthon import zedub
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, deEmojify, mention


plugin_category = "الترفيه"


@zedub.zed_cmd(pattern="افكر$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, ".🧐")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern=r"متت$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, ".🤣")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern=r"ضايج$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🙂.")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern="ساعه$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🕙.")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern=r"مح$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "😗.")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern="قلب$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🧡.")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern="جيم$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "جيم")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern=f"الارض$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🌏.")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern="قمر$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🌗.")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@zedub.zed_cmd(pattern=f"اقمار$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🌗.")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("⇆")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@zedub.zed_cmd(pattern=f"قمور$")
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "قمور..")
    animation_interval = 0.1
    animation_ttl = range(96)
    await event.edit("tmoon..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


Fun2_cmd = (
"**╮•❐ اوامـر تسليـه متحـركه ممطـروقـه 2 ⦂ **\n\n"
"  •  `.افكر`\n"
"  •  `.متت`\n"
"  •  `.ضايج`\n"
"  •  `.ساعه`\n"
"  •  `.مح`\n"
"  •  `.قلب`\n"
"  •  `.جيم`\n"
"  •  `.الارض`\n"
"  •  `.قمر`\n"
"  •  `.اقمار`\n"
"  •  `.قمور`\n\n"
  
"**للنســخ : ** __اضغط ع الامـر لنسخـه__"
)

# Copyright (C) 2022 Zedthon . All Rights Reserved
@zedub.zed_cmd(pattern="تسليه2")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, Fun2_cmd)
