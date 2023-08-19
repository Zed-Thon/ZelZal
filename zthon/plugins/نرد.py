""" ©ZED™ - @ZlZZl77 """

import asyncio
import random
import pyfiglet
from telethon.tl.types import InputMediaDice
from time import sleep
from datetime import datetime
from telethon import Button, events ,types, version
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from zthon import StartTime, zedub, zedversion
from ..Config import Config
from ..core import check_owner, pool
from ..core.logger import logging
from collections import deque
from random import choice
from . import ALIVE_NAME
from ..helpers import fonts as emojify
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id, get_user_from_event, _format
from . import deEmojify
# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"
FOOT_E_MOJI = "⚽️"
SLOT_E_MOJI = "🎰"
# EMOJI CONSTANTS


@zedub.zed_cmd(pattern="اكس او$")
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@zedub.zed_cmd(pattern=f"({DART_E_MOJI}|سهم)( ([1-6])|$)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "سهم":
        emoticon = "🎯"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@zedub.zed_cmd(pattern=f"({DICE_E_MOJI}|نرد)( ([1-6])|$)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "نرد":
        emoticon = "🎲"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@zedub.zed_cmd(pattern=f"({BALL_E_MOJI}|سله)( ([1-5])|$)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "سله":
        emoticon = "🏀"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@zedub.zed_cmd(pattern=f"({FOOT_E_MOJI}|.كرة)( ([1-5])|$)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == ".كرة":
        emoticon = "⚽️"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@zedub.zed_cmd(pattern=f"({SLOT_E_MOJI}|حظ)( ([1-64])|$)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "حظ":
        emoticon = "🎰"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))



@zedub.zed_cmd(pattern=f"احكام(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, f"**⪼ عـذراً .. اللعبـه فـي وضـع الصيـانـه سيتـم تحديثهـا لاحقـاً ...⏣**")


@zedub.zed_cmd(pattern=f"عقاب(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, f"**⪼ عـذراً .. اللعبـه فـي وضـع الصيـانـه سيتـم تحديثهـا لاحقـاً ...⏣**")



