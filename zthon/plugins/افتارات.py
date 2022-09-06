#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣


import asyncio
from collections import deque
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos

from zthon import zedub

from zthon.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@zedub.zed_cmd(pattern="حالات ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . اكثـر مـن 500 حـالات واتـس قصيـرة .. ارسـل .حالات واتس 𓅫╰**"
        )
    chat = "@amaterody_bot"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل حـالات واتـس ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1569771593)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @amaterody_bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ستوري ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . اكثـر مـن 1000 ستـوريات انمـي قصيـرة ممطـروقـه.. ارسـل .ستوري انمي 𓅫╰**"
        )
    chat = "@Chhhbbot"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل السـتوري ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1915672327)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @Chhhbbot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="رمادي ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**❈╎افتـارات ولـد رمـاديـه 🙋🏻‍♂🎆**\n**❈╎قـم باضافـة رقمـہ من 130 - 1 للامـر . . مثـال ( .رمادي 1 ) ...𓅫╰**"
        )
    chat = "@QQY_98BOT"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2088144968)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @QQY_98BOT .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="رقيه ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**❈╎مقاطـع رقيـه شرعيـة 🕋🌸**\n**❈╎قـم باضافـة رقمـہ من 200 - 1 للامـر . . مثـال ( .رقيه 1 ) ...𓅫╰**"
        )
    chat = "@ZlZZl77bot"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرقيـه الشـرعيه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1956894280)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZlZZl77bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="رماديه ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**❈╎افتـارات بنـات رمـاديـه 🙋🏻‍♀🎆**\n**❈╎قـم باضافـة رقمـہ من 130 - 1 للامـر . . مثـال ( .رماديه 1 ) ...𓅫╰**"
        )
    chat = "@SSSS_sssiBOT"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2076530727)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @SSSS_sssiBOT .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="بيست ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**❈╎افتـارات بيست تطقيـم بنـات 👯‍♀🎆**\n**❈╎قـم باضافـة رقمـہ من 29 - 1 للامـر . . مثـال ( .بيست 1 ) ...𓅫╰**"
        )
    chat = "@Zedthonbot"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الآفتـار ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1863051724)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @Zedthonbot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="حب ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**❈╎افتـارات تطقيـم حب ♥️🎆**\n**❈╎قـم باضافـة رقمـہ من 57 - 1 للامـر . . مثـال ( .حب 1 ) ...𓅫╰**"
        )
    chat = "@ZlZZl777BOT"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الآفتـار ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2099294312)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZlZZl777BOT .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="رياكشن$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@reagshn", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"** 🎬┊رياكشـن تحشيـش ➧🎃😹◟**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="ادت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل مقطـع ادت ...**")
    try:
        ZTHONR = [
            asupan
            async for asupan in event.client.iter_messages(
                "@snje1", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**🎬┊مقاطـع ايـدت منوعـه ➧ 🖤🎭◟**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="غنيلي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل المقطـع ...**")
    try:
        zedgan = [
            desah
            async for desah in event.client.iter_messages(
                "@TEAMSUL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختياࢪ الاغنيـه لك 💞🎶**ٴ▁ ▂ ▉ ▄ ▅ ▆ ▇ ▅ ▆ ▇ █ ▉ ▂ ▁\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        

@zedub.zed_cmd(pattern="شعر$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الشعـر ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@L1BBBL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختيـار مقطـع الشعـر هـذا لك**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="ميمز$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الميمـز ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@MemzWaTaN", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختيـار مقطـع الميمـز هـذا لك**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="ري اكشن$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@gafffg", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**🎆┊رياكشـن تحشيـش ➧🎃😹◟**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="معلومه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل صـورة ومعلومـة ...**")
    try:
        zedph = [
            zilzal
            async for zilzal in event.client.iter_messages(
                "@A_l3l", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**🎆┊صـورة ومعلومـة ➧ 🛤💡◟**\n\n[➧??𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="تويت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ كـت تـويت بالصـور ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@twit_selva", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**✦┊كـت تـويت بالصـور ➧⁉️🌉◟**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="خيرني$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ لـو خيـروك بالصـور ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@SourceSaidi", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✦┊لـو خيـروك  ➧⁉️🌉◟**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zedub.zed_cmd(pattern="ولد ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . اكثـر مـن 1000 افتـارات انمـي شبـاب ممطـروقـه.. ارسـل .ولد انمي 𓅫╰**"
        )
    chat = "@ZelTrbot"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1354728480)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZelTrbot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="بنت ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . اكثـر مـن 1000 افتـارات انمـي بنـات ممطـروقـه.. ارسـل ..بنت انمي 𓅫╰**"
        )
    chat = "@Maroooosh_bot"
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1000915223)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @Maroooosh_bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


