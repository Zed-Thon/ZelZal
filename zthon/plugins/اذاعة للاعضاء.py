# Zed-Thon
# Copyright (C) 2023 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.

import contextlib
import asyncio
from asyncio import sleep

from telethon.errors import UserAdminInvalidError
from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest

from zthon import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
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
# =========================================================== #
#                                      زلـــزال الهيبـــه - T.me/zzzzl1l                                  #
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

