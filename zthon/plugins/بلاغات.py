import asyncio
import base64
import contextlib

from telethon.errors.rpcerrorlist import ForbiddenError
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type, unsavegif
from ..helpers.utils import _zedutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "الخدمات"
UNSPAM = gvarstatus("Z_UNSPAM") or "ايقاف البلاغ"


async def spam_abuse(event, sandy, zed, sleeptimem, sleeptimet, DelaySpam=False):
    # sourcery no-metrics
    counter = int(zed[0])
    if len(zed) == 2:
        spam_message = str(zed[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message('@AbuseNotifications', spam_message)
            await asyncio.sleep(4)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message('@AbuseNotifications', spam_message)
            await asyncio.sleep(4)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**- البلاغـات 📌**\n"
                    + f"**- تم تنفيـذ تڪـرار البـلاغـات بنجاح في ** [Abuse Notifications](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **رسائل** \n"
                    + f"**- كليشـة البلاغـات :**\n `{spam_message}`",
                )
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**- التڪـرار الوقتـي ♽**\n"
                + f"**- تم تنفيـذ التڪـرار الوقتي  بنجاح في ** [Abuse Notifications](tg://user?id=4245000) **الدردشة مع** {sleeptimet} seconds and with {counter} **رسائل الـ   :** \n"
                + f"- `{spam_message}`",
            )


@zedub.zed_cmd(
    pattern="بلاغ ([\s\S]*)",
    command=("بلاغ", plugin_category),
    info={
        "header": "لـ تكـرار كلمـه معينـه لعـدد معيـن من المـرات",
        "ملاحظـه": "لـ ايقـاف التكـرار استخـدم الامـر  {tr}ايقاف التكرار",
        "الاستخـدام": ["{tr}كرر + العدد + الكلمـه", "{tr}كرر + العدد بالـرد ع رسـاله"],
        "مثــال": "{tr}كرر 10 هلو",
    },
)
async def spammer(event):
    "لـ تكـرار كلمـه معينـه لعـدد معيـن من المـرات"
    sandy = await event.get_reply_message()
    zed = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(zed[0])
    except Exception:
        return await edit_delete(
            event, "**- ارسـل الامـر بالشكـل التالي**\n\n`.بلاغ` **+ عدد التكرار + الرسالة او بالـرد ع رسالة**\n**- مثـال : .بلاغ 12 بالـرد ع كليشـة البـلاغ**"
        )
    if counter > 50:
        sleeptimet = 4
        sleeptimem = 1
    else:
        sleeptimet = 4
        sleeptimem = 0.3
    await event.delete()
    addgvar("spamwork", True)
    await spam_abuse(event, sandy, zed, sleeptimem, sleeptimet)




@zedub.zed_cmd(pattern=f"{UNSPAM} ?(.*)",)
async def spammer(event):
    if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
        delgvar("spamwork")
        return await edit_delete(event, "**- تم ايقـاف البلاغـات .. بنجـاح ✅**")
    return await edit_delete(event, "**- لايوجـد هنـاك بلاغـات لـ إيقافهـا ؟!**")



