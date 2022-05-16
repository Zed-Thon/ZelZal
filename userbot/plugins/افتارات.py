#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣


import asyncio
from collections import deque
import os
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.core.logger import logging
from userbot import zedub
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, deEmojify, mention
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
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل حـالات واتـس ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1569771593)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @amaterody_bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
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
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل السـتوري ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1915672327)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @Chhhbbot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)



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
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1354728480)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZelTrbot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
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
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1000915223)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @Maroooosh_bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)



@zedub.zed_cmd(pattern="رر$")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 130 - 1 مثـال .رر بالـرد ع رقـم ...𓅫╰**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 130 - 1 مثـال .رر بالـرد ع رقـم ...𓅫╰**")
        return
    chat = "@QQY_98BOT"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحميل ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2088144968)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @QQY_98BOT .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
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
            event, "**╮ . اكثـر من 200 رقيـه شرعيـه .. صـدقه جـاريـه 𓅫╰**"
        )
    chat = "@ZlZZl77bot"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرقيـه الشـرعيه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1956894280)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZlZZl77bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)




@zedub.zed_cmd(pattern="ر$")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 130 - 1 مثـال .ر بالـرد ع رقـم ...𓅫╰**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 130 - 1 مثـال .ر بالـرد ع رقـم ...𓅫╰**")
        return
    chat = "@SSSS_sssiBOT"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحميل ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2076530727)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @SSSS_sssiBOT .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)



@zedub.zed_cmd(pattern="ت$")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 29 - 1 مثـال .ت بالـرد ع رقـم ...𓅫╰**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 29 - 1 مثـال .ت بالـرد ع رقـم ...𓅫╰**")
        return
    chat = "@Zedthonbot"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحميل ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1863051724)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @Zedthonbot .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)



@zedub.zed_cmd(pattern="ح$")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 57 - 1 مثـال .ح بالـرد ع رقـم ...𓅫╰**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**╮ .قـم بالـرد علـى الـرقمـٓہ من 57 - 1 مثـال .ح بالـرد ع رقـم ...𓅫╰**")
        return
    chat = "@ZlZZl777BOT"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحميل ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2099294312)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZlZZl777BOT .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)

