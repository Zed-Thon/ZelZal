# Zed-Thon
# Copyright (C) 2023 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

import asyncio
import requests
import logging
from asyncio import sleep

from telethon.tl import functions, types
from telethon.errors import UserAdminInvalidError
from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest

from zthon import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import gvarstatus
from ..helpers import readable_time
from ..helpers.utils import reply_id
from ..utils import is_admin
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

spam_chats = []

# =========================================================== #
#                           الملـــف كتـــابـــة مـــن الصفـــر - T.me/ZedThon                           #
# =========================================================== #
Warn = "تخمـط بـدون ذكـر المصـدر - ابلعــك نعــال وراح اهينــك"
ZEDTHON_BEST_SOURCE = "[ᯓ 𝗭𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة خـاص 🚹](t.me/ZedThon) .\n\n**- جـارِ الاذاعـه خـاص لـ أعضـاء الكـروب 🛗\n- الرجـاء الانتظـار .. لحظـات ⏳**"
ZEDTHON_PRO_SOURCE = "[ᯓ 𝗭𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة زاجـل 🕊](t.me/ZedThon) .\n\n**- جـارِ الاذاعـه لـ قائمـة زاجـل 📜\n- الرجـاء الانتظـار .. لحظـات ⏳**"
ZELZAL_PRO_DEV = "[ᯓ 𝗭𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة زاجـل 🕊](t.me/ZedThon) .\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**⎉╎قائمـة الاذاعـه فارغـه ؟! ❌**\n**⎉╎قم باضافة يوزرات عبـر الامر**\n`.اضف زاجل` **بالـرد ع عدة يوزرات تفصل بينهم مسافات**"
# =========================================================== #
#                                      زلـــزال الهيبـــه - T.me/zzzzl1l                                  #
# =========================================================== #
#                                      تـاريـخ كتابـة الملـف - 7 ابريل/2023                                  #
# =========================================================== #


@zedub.zed_cmd(pattern=f"للكل(?: |$)(.*)", groups_only=True)
async def malath(event):
    zedthon = event.pattern_match.group(1)
    if zedthon:
        await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        zilzal = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    chat_id = event.chat_id
    is_admin = False
    try:
        await zedub(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        pass
    spam_chats.append(chat_id)
    zelzal = await event.edit(ZEDTHON_BEST_SOURCE, link_preview=False)
    total = 0
    success = 0
    async for usr in event.client.iter_participants(event.chat_id):
        total += 1
        if not chat_id in spam_chats:
            break
        username = usr.username
        magtxt = f"@{username}"
        if str(username) == "None":
            idofuser = usr.id
            magtxt = f"{idofuser}"
        if zilzal.text:
            try:
                await borg.send_message(magtxt, zilzal, link_preview=False)
                success += 1
            except BaseException:
                return
        else:
            try:
                await borg.send_file(
                    magtxt,
                    zilzal,
                    caption=zilzal.caption,
                    link_preview=False,
                )
                success += 1
            except BaseException:
                return
    ZELZAL_BEST_DEV = f"[ᯓ 𝗭𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة خـاص 🚹](t.me/ZedThon) .\n\n**⎉╎تمت الاذاعـه لـ اعضـاء الكـروب .. بنجـاح  ✅**\n**⎉╎عـدد {success} عضـو**"
    await zelzal.edit(ZELZAL_BEST_DEV, link_preview=False)
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@zedub.zed_cmd(pattern="ايقاف للكل", groups_only=True)
async def unmalath(event):
    if not event.chat_id in spam_chats:
        return await event.edit("**- لاتوجـد عمليـة اذاعـه للاعضـاء هنـا لـ إيقافـها ؟!**")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.edit("**⎉╎تم إيقـاف عمليـة الاذاعـه للاعضـاء هنـا .. بنجـاح✓**")



#                                       تـاريـخ كتابـة الكـود - 19 ابريل/2023                                  #
#                                        الملف كتابتي من الصفر ومتعوب عليه                                  #
#                                           تخمط بدون ذكر المصدر = اهينك                                     #
@zedub.zed_cmd(pattern="زاجل(?: |$)(.*)")
async def malath(event):
    zedthon = event.pattern_match.group(1)
    if zedthon:
        await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zilzal = await event.get_reply_message()
    if gvarstatus("ZAGL_Zed") is None:
        return await event.edit(ZELZAL_PRO_DEV, link_preview=False)
    zelzal = gvarstatus("ZAGL_Zed")
    users = zelzal.split(" ")
    zzz = await event.edit(ZEDTHON_PRO_SOURCE, link_preview=False)
    total = 0
    success = 0
    user_entity = None
    for user in users:
        total += 1
        if zilzal.text:
            try:
                user_entity = await zedub.get_entity(user)
                if user_entity.bot or user_entity.deleted:
                    continue
                await zedub.send_message(user_entity.id, zilzal, link_preview=False)
                success += 1
            except UserAdminInvalidError:
                pass
            except Exception as e:
                zzz.edit(f"خطأ في إرسال الرسالة إلى {user_entity.id}: {str(e)}")
        elif zilzal.media:
            try:
                user_entity = await zedub.get_entity(user)
                if user_entity.bot or user_entity.deleted:
                    continue
                await zedub.send_file(user_entity.id, zilzal.media, caption=zilzal.text)
                success += 1
            except UserAdminInvalidError:
                pass
            except Exception as e:
                zzz.edit(f"خطأ في إرسال الرسالة إلى {user_entity.id}: {str(e)}")
    ZELZAL_BEST_DEV = f"[ᯓ 𝗭𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اذاعـة زاجـل 🕊](t.me/ZedThon) .\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**⎉╎تمت الاذاعـه .. بنجـاح  ✅**\n**⎉╎عـدد {success} أشخـاص**"
    await zzz.edit(ZELZAL_BEST_DEV, link_preview=False)

