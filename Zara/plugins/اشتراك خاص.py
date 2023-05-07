# Zed-Thon
# Copyright (C) 2022 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/Zara/LICENSE/>.
#يبووووووووووووووووووو
#هههههههههههههههههههههههههههههههههههههه
import asyncio
import requests
import logging
import os
import re
import telethon
from telethon.events import CallbackQuery, InlineQuery
from telethon import Button, events, functions
from telethon.tl import functions, types
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import EditBannedRequest, GetFullChannelRequest, GetParticipantRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

from Zara import zedub
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete, edit_or_reply
from ..core.logger import logging
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

# =========================================================== #
#                                                  الملـــف كتـــابـــة  - T.me/ZThon                                    #
# =========================================================== #
Warn = "تخمـط بـدون ذكـر المصـدر - راح توثقهـا فضيحـه ع نفسـك"
# =========================================================== #
#                                                       زلـــزال الهيبـــه - T.me/zzzzl1l                                  #
# =========================================================== #
#                                              تـاريـخ كتابـة الملـف - 30 اكتوبر/2022                                  #
#                                                   الملف كان مدفوع وتم تنزيله مجاني                                   #
#                                                  الدليل https://t.me/ZThon/260                                 #
# =========================================================== #

zilzal = zedub.uid
zed_dev = (2095357462, 1895219306, 925972505)
LOGS = logging.getLogger(__name__)
zelzaal = False

async def check_him(channel, user):
    try:
        result = await bot(
            functions.channels.GetParticipantRequest(channel, user)
        )
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False


@zedub.zed_cmd(pattern="(ضع اشتراك الخاص|وضع اشتراك الخاص)(?:\s|$)([\s\S]*)")
async def _(event):
    if input_str := event.pattern_match.group(2):
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{e}`", 5)
        try:
            if p.first_name:
                await asyncio.sleep(1.5)
                delgvar("Custom_Pm_Channel")
                addgvar("Custom_Pm_Channel", f"-100{p.id}")
                return await edit_or_reply(
                    event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎يوزر القناة : ↶** `{input_str}`\n**⎉╎ايدي القناة : ↶** `{p.id}`\n\n**⎉╎ارسـل الان** `.تفعيل الاشتراك خاص`"
                )
        except Exception:
            try:
                if p.title:
                    await asyncio.sleep(1.5)
                    delgvar("Custom_Pm_Channel")
                    addgvar("Custom_Pm_Channel", f"-100{p.id}")
                    return await edit_or_reply(
                        event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎اسم القناة : ↶** `{p.title}`\n**⎉╎ايدي القناة : ↶** `{p.id}`\n\n**⎉╎ارسـل الان** `.تفعيل الاشتراك خاص`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "⪼ **أدخل معـرف القناة او قم باستخدام الامر داخل القناة**")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            await asyncio.sleep(1.5)
            delgvar("Custom_Pm_Channel")
            addgvar("Custom_Pm_Channel", event.chat_id)
            await edit_or_reply(
                event,
                f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.تفعيل الاشتراك خاص`",
            )

        else:
            await asyncio.sleep(1.5)
            delgvar("Custom_Pm_Channel")
            addgvar("Custom_Pm_Channel", event.chat_id)
            await edit_or_reply(
                event,
                f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.تفعيل الاشتراك خاص`",
            )

    else:
        await asyncio.sleep(1.5)
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", event.chat_id)
        await edit_or_reply(event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.تفعيل الاشتراك خاص`")


@zedub.zed_cmd(pattern="(تفعيل اشتراك الخاص|تفعيل الاشتراك خاص)")
async def start_datea(event):
    global zelzaal
    if zelzaal:
        return await edit_or_reply(event, "**⎉╎الاشتراك الاجبـاري لـ الخـاص .. مفعـل مسبقـاً ☑️**")
    zelzaal = True
    await edit_or_reply(event, "**⎉╎تم تفعيـل الاشتـراك الاجبـاري خـاص .. بنجـاح ☑️**")

@zedub.zed_cmd(pattern="(تعطيل اشتراك الخاص|تعطيل الاشتراك الخاص)")
async def stop_datea(event):
    global zelzaal
    if zelzaal:
        zelzaal = False
        return await edit_or_reply(event, "**⎉╎تم تعطيـل الاشتـراك الاجبـاري خـاص .. بنجـاح ☑️**")
    await edit_or_reply(event, "**⎉╎الاشتراك الاجبـاري لـ الخـاص .. معطـل مسبقـاً ☑️**")


@zedub.zed_cmd(incoming=True, func=lambda e: e.is_private, edited=False, forword=None)
async def f(event):
    chat_id = event.chat_id
    chat = await event.get_chat()
    user = await event.get_sender()
    zelzal = (await event.get_sender()).id
    if chat.bot:
        return
    if zelzal in zed_dev:
        return
    global zelzaal
    if zelzaal:
        try:
            ch = gvarstatus("Custom_Pm_Channel")
            try:
                ch = int(ch)
            except BaseException:
                return
            rip = await check_him(ch, event.sender_id)
            if rip is False:
                c = await zedub.get_entity(ch)
                chn = c.username
                if c.username == None:
                    ra = await zedub(ExportChatInviteRequest(ch))
                    chn = ra.link
                if chn.startswith("https://"):
                    await event.reply(f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 - **الاشتࢪاك الإجباࢪي**\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**مࢪحبـاً عـزيـزي 🫂** [{user.first_name}](tg://user?id={user.id}) \n⌔╎**لـ الغـاء كتمـك 🔊**\n⌔╎**يُࢪجـى الإشتـࢪاك بالقنـاة {chn} **", link_preview=False
                    )
                    return await event.delete()
                else:
                    await event.reply(f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 - **الاشتࢪاك الإجباࢪي**\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**مࢪحبـاً عـزيـزي 🫂** [{user.first_name}](tg://user?id={user.id}) \n⌔╎**لـ الغـاء كتمـك 🔊**\n⌔╎**يُࢪجـى الإشتـࢪاك بالقنـاة @{chn} **", link_preview=False
                    )
                    return await event.delete()
        except BaseException:
            return

