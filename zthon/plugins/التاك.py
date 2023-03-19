#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
import asyncio
import time
import io
import os
import shutil
import random
import logging
import glob

from datetime import datetime
from math import sqrt
from asyncio import sleep
from asyncio.exceptions import TimeoutError

from telethon import functions, types
from telethon.sync import errors
from telethon import events
from telethon.tl import functions

from telethon.tl.types import ChannelParticipantsAdmins

from zthon import zedub

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import reply_id
from ..helpers.utils import _format, get_user_from_event, reply_id 
from . import BOTLOG, BOTLOG_CHATID, mention, progress

LOGS = logging.getLogger(__name__)
plugin_category = "الادمن"


moment_worker = []
@zedub.zed_cmd(pattern="all?(.*)")
async def tagall(event):
  global moment_worker
  if event.is_private:
    return await edit_or_reply(event, "**- عـذراً ... هـذه ليـست مجمـوعـة ؟!**")
  if event.pattern_match.group(1):
    mode = "by_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "by_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await edit_or_reply(event, "**- عـذراً ... الرسـالة غيـر ظـاهـرة للأعضـاء الجـدد ؟!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await edit_or_reply(event, "**- اضـف نـص لـ الامـر . . .**\n\n**- مثـال :** `.all وينكـم`")
  else:
    return await edit_or_reply(event, "**- بالـرد عـلى رسـالـه . . او باضـافة نـص مـع الامـر**")
  if mode == "by_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in zedub.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"- [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await edit_or_reply(event, "**⎉╎تم إيقـاف التـاك .. بنجـاح ✓**")
        return
      if usrnum == 5:
        await zedub.send_message(event.chat_id, f"{usrtxt}\n\n- {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
  if mode == "by_reply":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in zedub.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"- [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await edit_or_reply(event, "**⎉╎تم إيقـاف التـاك .. بنجـاح ✓**")
        return
      if usrnum == 5:
        await zedub.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""



@zedub.zed_cmd(pattern="ايقاف التاك?(.*)")
async def stop_tagall(event):
  if not event.chat_id in moment_worker:
    return await edit_or_reply(event, '**- عـذراً .. لا يوجـد هنـاك تـاك لـ إيقـافـه ؟!**')
  else:
    try:
      moment_worker.remove(event.chat_id)
    except:
      pass
    return await edit_or_reply(event, '**⎉╎تم إيقـاف التـاك .. بنجـاح ✓**')


@zedub.zed_cmd(pattern="تاك?(.*)")
async def tagall(event):
  global moment_worker
  if event.is_private:
    return await edit_or_reply(event, "**- عـذراً ... هـذه ليـست مجمـوعـة ؟!**")
  if event.pattern_match.group(1):
    mode = "by_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "by_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await edit_or_reply(event, "**- عـذراً ... الرسـالة غيـر ظـاهـرة للأعضـاء الجـدد ؟!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await edit_or_reply(event, "**- اضـف نـص لـ الامـر . . .**\n\n**- مثـال :** `.all وينكـم`")
  else:
    return await edit_or_reply(event, "**- بالـرد عـلى رسـالـه . . او باضـافة نـص مـع الامـر**")
  if mode == "by_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in zedub.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"- [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await edit_or_reply(event, "**⎉╎تم إيقـاف التـاك .. بنجـاح ✓**")
        return
      if usrnum == 5:
        await zedub.send_message(event.chat_id, f"{usrtxt}\n\n- {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
  if mode == "by_reply":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in zedub.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"- [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await edit_or_reply(event, "**⎉╎تم إيقـاف التـاك .. بنجـاح ✓**")
        return
      if usrnum == 5:
        await zedub.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@zedub.zed_cmd(pattern="تبليغ$")
async def _(event):
    mentions = "- انتباه الى المشرفين تم تبليغكم \n@admin"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@zedub.zed_cmd(pattern="منشن ([\s\S]*)")
async def _(event):
    user, input_str = await get_user_from_event(event)
    if not user:
        return
    reply_to_id = await reply_id(event)
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"<a href='tg://user?id={user.id}'>{input_str}</a>",
        parse_mode="HTML",
        reply_to=reply_to_id,
    )

