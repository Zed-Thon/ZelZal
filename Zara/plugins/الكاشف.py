#𝙕𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙏𝙝𝙤𝙣
#الملف مرفـوع ع استضـافتـي مهمـا خمطت راح تطلـع حقـــوقــي بســورســـك
#هههههههههههههههههه

import requests
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from Zara import zedub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

ZelzalPH_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗭𝗧𝗵𝗼𝗻 📲 - كـاشـف الارقـام العربيــة](t.me/ZThon) 𓆪\n\n"
    "**⪼ الامــر ↵**\n\n"
    "⪼ `.اكشف` + الـرقـم مـع مفتـاح الـدولة\n\n"
    "**⪼ الوصـف :**\n"
    "**- لجـلب قائمـه بـ أسمـاء صاحب رقـم هـاتف معيـن**\n\n"
)


@zedub.zed_cmd(pattern="اكشف(?: |$)([\s\S]*)")
async def _(event): #Code by T.me/zzzzl1l
    number = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not number and reply:
        number = reply.text
    if not number:
        return await edit_delete(event, "**- الرقم خطأ او لم تقم بادخال كود الدولة +**", 10)
    if "+" not in number:
        return await edit_delete(
            event, "**- الرقم خطأ او لم تقم بادخال كود الدولة +**", 10
        )
    zelzal = "@ZZIIIbot" #Code by T.me/zzzzl1l
    zed = await edit_or_reply(event, "**⎉╎جـارِ الكشـف عن الرقـم 📲**\n**⎉╎انتظـر قليـلاً ... ▬▭**")
    async with borg.conversation(zelzal) as conv: # code by t.me/zzzzl1l
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(number)
            zthon = await conv.get_response()
            malath = zthon.text
            await borg.send_message(event.chat_id, zthon)
            await zed.delete()
        except YouBlockedUserError:
            await zedub(unblock("ZZIIIbot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(number)
            zthon = await conv.get_response()
            malath = zthon.text
            await borg.send_message(event.chat_id, zthon)
            await zed.delete()



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="الكاشف")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalPH_cmd)