# Zed-Thon - ZelZal
# Copyright (C) 2023 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.


import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import zedub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="بريد$")
async def zelzal_gpt(event):
    chat = "@TeMail_Robot" # code by t.me/zzzzl1l
    zed = await edit_or_reply(event, "**⎉╎جـار إنشـاء ايميـل وهمـي 📧...**")
    async with borg.conversation(chat) as conv: # code by t.me/zzzzl1l
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📧 Generate Email")
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "📧 Your temporary email" in zedthon.text:
                aa = malath.replace("📧 Your temporary email address:", "**⎉╎تم انشـاء Email وهمـي .. بنجـاح ☑️\n⎉╎لجلب رسائـل الوارد ارسـل (.الوارد)\n⎉╎الايميـل الوهمـي الخـاص بك هـو 📧 :**") 
                await zed.delete()
                await borg.send_message(event.chat_id, aa)
        except YouBlockedUserError:
            await zedub(unblock("TeMail_Robot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📧 Generate Email")
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "📧 Your temporary email" in zedthon.text:
                aa = malath.replace("📧 Your temporary email address:", "**⎉╎تم انشـاء Email وهمـي .. بنجـاح ☑️\n⎉╎لجلب رسائـل الوارد ارسـل (.الوارد)\n⎉╎الايميـل الوهمـي الخـاص بك هـو 📧 :**") 
                await zed.delete()
                await borg.send_message(event.chat_id, aa)



# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="الوارد$")
async def zelzal_gpt(event):
    chat = "@TeMail_Robot" # code by t.me/zzzzl1l
    zed = await edit_or_reply(event, "**⎉╎جـار جلب رسائـل البريـد 📬...**")
    async with borg.conversation(chat) as conv: # code by t.me/zzzzl1l
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📫 Check OTP")
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "❌ No OTP" in zedthon.text:
                aa = malath.replace("❌ No OTP were received...", "**⎉╎لا يوجـد رسـالة واردة لبريـدك الوهمـي بعـد 📭❌**") 
                await zed.delete()
                return await borg.send_message(event.chat_id, aa)
            if "📬 Inbox" in zedthon.text:
                await zed.delete()
                return await borg.send_message(event.chat_id, f"**{malath}**\n\n───────────────────\n𝗭𝗧𝗵𝗼𝗻 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tᶻᵉˡᶻᵃˡ • البـريد الـوارد")
            await zed.delete()
            await borg.send_message(event.chat_id, f"**{malath}**\n\n───────────────────\n𝗭𝗧𝗵𝗼𝗻 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tᶻᵉˡᶻᵃˡ • البـريد الـوارد")
        except YouBlockedUserError:
            await zedub(unblock("TeMail_Robot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📫 Check OTP")
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "❌ No OTP" in zedthon.text:
                aa = malath.replace("❌ No OTP were received...", "**⎉╎لا يوجـد رسـالة واردة لبريـدك الوهمـي بعـد 📭❌**") 
                await zed.delete()
                return await borg.send_message(event.chat_id, aa)
            if "📬 Inbox" in zedthon.text:
                await zed.delete()
                return await borg.send_message(event.chat_id, f"**{malath}**\n\n───────────────────\n𝗭𝗧𝗵𝗼𝗻 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tᶻᵉˡᶻᵃˡ • البـريد الـوارد")
            await zed.delete()
            await borg.send_message(event.chat_id, f"**{malath}**\n\n───────────────────\n𝗭𝗧𝗵𝗼𝗻 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tᶻᵉˡᶻᵃˡ • البـريد الـوارد")

