#ZedThon

import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id, _format
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "الترفيه"


@zedub.zed_cmd(pattern="(حساب العمر|عمري) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = input_str = event.text[7:]
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not input_str:
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(input_str)
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ .حساب العمر + 17/8/2003 ... لمعرفه  عمرك ...𓅫╰**"
        )
    chat = "@musiyic_bot"
    zzzzl1l = await edit_or_reply(event, "**╮•⎚ جـارِ حسب عمرك ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6106343444)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            responses = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @musiyic_bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)
