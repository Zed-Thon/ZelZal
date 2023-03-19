# Zed-Thon
# Copyright (C) 2022 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.
import asyncio
import requests
import logging

from telethon import events, Button, functions
from telethon.tl import functions, types
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import EditBannedRequest, GetFullChannelRequest, GetParticipantRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

from zthon import zedub
from zthon import BOTLOG_CHATID
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..core.logger import logging

LOGS = logging.getLogger(__name__)
plugin_category = "الادمن"
cmdhd = Config.COMMAND_HAND_LER


@zedub.zed_cmd(pattern="(ضع الاشتراك خاص|وضع الاشتراك خاص)(?:\s|$)([\s\S]*)")
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
                    event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎يوزر القناة : ↶** `{input_str}`\n**⎉╎ايدي القناة : ↶** `{p.id}`\n\n**⎉╎ارسـل الان** `.اشتراك خاص`"
                )
        except Exception:
            try:
                if p.title:
                    await asyncio.sleep(1.5)
                    delgvar("Custom_Pm_Channel")
                    addgvar("Custom_Pm_Channel", f"-100{p.id}")
                    return await edit_or_reply(
                        event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎اسم القناة : ↶** `{p.title}`\n**⎉╎ايدي القناة : ↶** `{p.id}`\n\n**⎉╎ارسـل الان** `.اشتراك خاص`"
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
                f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.اشتراك خاص`",
            )

        else:
            await asyncio.sleep(1.5)
            delgvar("Custom_Pm_Channel")
            addgvar("Custom_Pm_Channel", event.chat_id)
            await edit_or_reply(
                event,
                f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.اشتراك خاص`",
            )

    else:
        await asyncio.sleep(1.5)
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", event.chat_id)
        await edit_or_reply(event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للخاص .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.اشتراك خاص`")



@zedub.zed_cmd(pattern="(ضع الاشتراك كروب|وضع الاشتراك كروب)(?:\s|$)([\s\S]*)")
async def _(event):
    if input_str := event.pattern_match.group(2):
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{e}`", 5)
        try:
            if p.first_name:
                await asyncio.sleep(1.5)
                delgvar("Custom_G_Channel")
                addgvar("Custom_G_Channel", f"-100{p.id}")
                return await edit_or_reply(
                    event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للكروب .. بنجـاح ☑️**\n\n**⎉╎يوزر القناة : ↶** `{input_str}`\n**⎉╎ايدي القناة : ↶** `{p.id}`\n\n**⎉╎ارسـل الان** `.اشتراك كروب`"
                )
        except Exception:
            try:
                if p.title:
                    await asyncio.sleep(1.5)
                    delgvar("Custom_G_Channel")
                    addgvar("Custom_G_Channel", f"-100{p.id}")
                    return await edit_or_reply(
                        event, f"**⎉╎تم إضافة قناة الاشتراك الاجباري للكروب .. بنجـاح ☑️**\n\n**⎉╎اسم القناة : ↶** `{p.title}`\n**⎉╎ايدي القناة : ↶** `{p.id}`\n\n**⎉╎ارسـل الان** `.اشتراك كروب`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "⪼ **أدخل إما اسم مستخدم أو الرد على المستخدم**")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            await asyncio.sleep(1.5)
            delgvar("Custom_G_Channel")
            addgvar("Custom_G_Channel", event.chat_id)
            await edit_or_reply(
                event,
                f"**⎉╎تم إضافة قناة الاشتراك الاجباري للكروب .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.اشتراك كروب`",
            )

        else:
            await asyncio.sleep(1.5)
            delgvar("Custom_G_Channel")
            addgvar("Custom_G_Channel", event.chat_id)
            await edit_or_reply(
                event,
                f"**⎉╎تم إضافة قناة الاشتراك الاجباري للكروب .. بنجـاح ☑️**\n\n**⎉╎ايدي القناة : ↶** `{event.chat_id}`\n\n**⎉╎ارسـل الان** `.اشتراك كروب`",
            )


@zedub.zed_cmd(pattern="اشتراك")
async def supc(event):
    ty = event.text
    ty = ty.replace(".اشتراك", "")
    ty = ty.replace(" ", "")
    if len (ty) < 2:
        return await edit_delete(event, "**⎉╎اختـر نوع الاشتـراك الاجبـاري اولاً :**\n\n`.اشتراك كروب`\n\n`.اشتراك خاص`")
    if ty == "كروب" or ty == "جروب" or  ty == "قروب" or  ty == "مجموعة" or  ty == "مجموعه":
        if not event.is_group:
            return await edit_delete("**⎉╎عـذراً .. هذه ليست مجمـوعـة ؟!**")
        if event.is_group:
            if gvarstatus ("sub_group") == event.chat_id:
                return await edit_delete(event, "**⎉╎الاشتـراك الاجبـاري لـ هذه المجمـوعـة مفعـل مسبقـاً**")
            if gvarstatus("sub_group"):
                return await edit_or_reply(event, "**⎉╎الاشتـراك الاجبـاري مفعـل لـ مجمـوعة آخـرى**\n**⎉╎ارسل (.تعطيل كروب) لـ الغائـه وتفعيلـه هنـا**")
            addgvar("sub_group", event.chat_id)
            return await edit_or_reply(event, "**⎉╎تم تفعيل الاشتراك الاجباري لـ هذه المجموعة .. بنجـاح✓**")
    if ty == "خاص":
        if gvarstatus ("sub_private"):
            return await edit_delete(event, "**⎉╎الاشتـراك الاجبـاري لـ الخـاص مفعـل مسبقـاً**")
        if not gvarstatus ("sub_private"):
            addgvar ("sub_private", True)
            await edit_or_reply(event, "**⎉╎تم تفعيل الاشتراك الاجباري لـ الخـاص .. بنجـاح✓**")
    if ty not in ["خاص", "كروب", "جروب", "قروب", "مجموعة", "مجموعه"]:
        return await edit_delete(event, "**⎉╎اختـر نوع الاشتـراك الاجبـاري اولاً :**\n\n`.اشتراك كروب`\n\n`.اشتراك خاص`")

@zedub.zed_cmd(pattern="تعطيل")
async def supc (event):
    cc = event.text.replace(".تعطيل", "")
    cc = cc.replace(" ", "")
    if cc == "كروب" or cc == "جروب" or  cc == "قروب" or  cc == "مجموعة" or  cc == "مجموعه" or cc == "الكروب" or cc == "اشتراك الكروب":
        if not gvarstatus ("sub_group"):
            return await edit_delete("**⎉╎الاشتراك الاجباري للكـروب غير مفعـل من الاسـاس ؟!**")
        if gvarstatus ("sub_group"):
            delgvar ("sub_group")
            return await edit_delete(event, "**⎉╎تم الغاء الاشتراك الاجباري للكروب .. بنجـاح ✓**")
    if cc == "خاص" or cc == "الخاص" or cc == "اشتراك الخاص":
        if not gvarstatus ("sub_private"):
            return await edit_delete(event, "**⎉╎الاشتراك الاجباري للخـاص غير مفعـل من الاسـاس ؟!**")
        if gvarstatus ("sub_private"):
            delgvar ("sub_private")
            return await edit_delete(event, "**⎉╎تم إلغاء الاشتراك الاجباري للخاص .. بنجـاح✓**")
    if cc not in ["خاص", "كروب", "جروب", "قروب", "مجموعة", "مجموعه", "الخاص", "اشتراك الخاص", "الكروب", "اشتراك الكروب"]:
        return await edit_delete(event, "**⎉╎اختـر نوع الاشتـراك الاجبـاري اولاً لـ الالغـاء :**\n\n`.تعطيل كروب`\n\n`.تعطيل خاص`")


@zedub.zed_cmd(incoming=True, func=lambda e: e.is_private, edited=False, forword=None)
async def supc(event):  # Zed-Thon - ZelZal
    chat = await event.get_chat()
    zed_dev = (929790454, 1050898456, 5252385385, 5289124437, 627658332, 5190136458, 1355571767)
    zelzal = (await event.get_sender()).id
    if zelzal in zed_dev:
    	return
    if chat.bot:
    	return
    if gvarstatus ("sub_private"):
        try:
   
            idd = event.peer_id.user_id
            tok = Config.TG_BOT_TOKEN
            ch = gvarstatus ("Custom_Pm_Channel")
            try:
                ch = int(ch)
            except BaseException as r:
                return await zedub.tgbot.send_message(BOTLOG_CHATID, f"**- خطـأ \n{r}**")
            url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={ch}&user_id={idd}"
            req = requests.get(url)
            reqt = req.text
            if "chat not found" in reqt:
                mb = await zedub.tgbot.get_me()
                mb = mb.username
                await zedub.tgbot.send_message(BOTLOG_CHATID, f"**⎉╎البوت الخاص بك @{mb} ليس في قناة الاشتراك الاجباري ؟!**")
                return
            if "bot was kicked" in reqt:
                mb = await zedub.tgbot.get_me()
                mb = mb.username
                await zedub.tgbot.send_message(BOTLOG_CHATID, "**⎉╎البوت الخاص بك @{mb} مطرود من قناة الاشتراك الاجباري اعد اضافته؟!**")
                return
            if "not found" in reqt:
                try:
                    c = await zedub.get_entity(ch)
                    chn = c.username
                    if c.username == None:
                        ra = await zedub.tgbot(ExportChatInviteRequest(ch))
                        chn = ra.link
                    if chn.startswith("https://"):
                        await event.reply(f"**⎉╎يجب عليك الإشـتࢪاڪ بالقناة أولاً\n⎉╎قناة الاشتراك : {chn}**", buttons=[[Button.url("اضغط لـ الإشـتࢪاڪ 🗳", chn)]]
                        )
                        return await event.delete()
                    else:
                        await event.reply(f"**⎉╎للتحدث معي يجب عليك الاشتراك في القناة\n⎉╎قناة الاشتراك : @{chn} **", buttons=[[Button.url("اضغط لـ الإشـتࢪاڪ 🗳", f"https://t.me/{chn}")]]
                        )
                        return await event.delete()
                except BaseException as er:
                    await zedub.tgbot.send_message(BOTLOG_CHATID, f"- خطـأ \n{er}")
            if "left" in reqt:
                try:
                    c = await zedub.get_entity(ch)
                    chn = c.username
                    if c.username == None:
                        ra = await zedub.tgbot(ExportChatInviteRequest(ch))
                        chn = ra.link
                    if chn.startswith("https://"):
                        await event.reply(f"**⎉╎يجب عليك الإشـتࢪاڪ بالقناة أولاً\n⎉╎قناة الاشتراك : {chn}**", buttons=[[Button.url("اضغط لـ الإشـتࢪاڪ 🗳", chn)]]
                        )
                        return await event.message.delete()
                    else:
                        await event.reply(f"**⎉╎للتحدث معي يجب عليك الاشتراك في القناة\n⎉╎قناة الاشتراك : @{chn} **", buttons=[[Button.url("اضغط لـ الإشـتࢪاڪ 🗳", f"https://t.me/{chn}")]]
                        )
                        return await event.message.delete()
                except BaseException as er:
                    await zedub.tgbot.send_message(BOTLOG_CHATID, f"- خطـأ \n{er}")
            if "error_code" in reqt:
                await zedub.tgbot.send_message(BOTLOG_CHATID, f"**- خطـأ غير معروف قم باعادة توجيه الرسالة ل@iiqllll لحل المشكلة\n{reqt}**")
            
            return
        except BaseException as er:
            await zedub.tgbot.send_message(BOTLOG_CHATID, f"** - خطـأ\n{er}**")
