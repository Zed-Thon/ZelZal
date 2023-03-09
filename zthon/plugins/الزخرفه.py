#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙏𝙝𝙤𝙣

import asyncio
import os
import sys
import urllib.request
from datetime import timedelta

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from zthon import zedub

from ..core.managers import edit_or_reply



@zedub.zed_cmd(pattern="زخرفه ?(.*)")
async def zilzal(event):
    card = event.pattern_match.group(1)
    chat = "@ZZ_ARBot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**جـارِ الزخـرفـه العربيـة 💞🧸...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("ZZ_ARBot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


@zedub.zed_cmd(pattern="زغرفه ?(.*)")
async def zelzal(event):
    card = event.pattern_match.group(1)
    chat = "@Z_ENBot"
    reply_id_ = await reply_id(event)
    zed = await edit_or_reply(event, "**جـارِ الزغـرفـه للانكـلش 💞🧸...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zedub(unblock("Z_ENBot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()

