import os
import shutil
from asyncio import sleep
from telethon import events

from zthon import zedub
from zthon.core.logger import logging
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.echo_sql import addecho, get_all_echos, get_echos, is_echo, remove_all_echos, remove_echo, remove_echos

from zthon.core.logger import logging
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)
zedself = True

POSC = gvarstatus("Z_POSC") or "(مم|ذاتية|ذاتيه|جلب الوقتيه)"

ZelzalSelf_cmd = (
    "𓆩 [ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حفـظ الذاتيـه 🧧](t.me/pp_g3) 𓆪\n\n"
    "**⪼** `.تفعيل الذاتيه`\n"
    "**لـ تفعيـل الحفظ التلقائي للذاتيـه**\n"
    "**سوف يقوم حسابك بحفظ الذاتيه تلقائياً في حافظة حسابك عندما يرسل لك اي شخص ميديـا ذاتيـه**\n\n\n"
    "**⪼** `.تعطيل الذاتيه`\n"
    "**لـ تعطيـل الحفظ التلقائي للذاتيـه**\n\n\n"
    "**⪼** `.ذاتيه`\n"
    "**بالـرد ؏ــلى صـوره ذاتيـه لحفظهـا في حال كان امر الحفظ التلقائي معطـل**\n\n"
    "\n 𓆩 [𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉](t.me/pp_g3) 𓆪"
)


@zedub.zed_cmd(pattern="الذاتيه")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalSelf_cmd)

@zedub.zed_cmd(pattern=f"{POSC}(?: |$)(.*)")
async def oho(event):
    if not event.is_reply:
        return await event.edit("**- ❝ ⌊بالـرد علـى صورة ذاتيـة التدميـر 𓆰...**")
    zzzzl1l = await event.get_reply_message()
    pic = await zzzzl1l.download_media()
    await zedub.send_file("me", pic, caption=f"**- ❝ ⌊تـم حفـظ الصـورة ذاتيـة التدمير بنجـاح ☑️ 🥳𓆰...**")
    await event.delete()

@zedub.zed_cmd(pattern="(تفعيل الذاتيه|تفعيل الذاتية)")
async def start_datea(event):
    global zedself
    if zedself:
        return await edit_or_reply(event, "**- حفظ الذاتيـة التلقـائي .. مفعـله مسبقـاً ☑️**")
    zedself = True
    await edit_or_reply(event, "**- تم تفعيـل حفظ الذاتيـة التلقائـي .. بنجـاح ☑️**")

@zedub.zed_cmd(pattern="(تعطيل الذاتيه|تعطيل الذاتية)")
async def stop_datea(event):
    global zedself
    if zedself:
        zedself = False
        return await edit_or_reply(event, "**- تم تعطيـل حفظ الذاتيـة التلقائـي .. بنجـاح ☑️**")
    await edit_or_reply(event, "**- حفظ الذاتيـة التلقـائي .. معطلـه مسبقـاً ☑️**")

#code for @R0R77
@zedub.on(events.NewMessage(func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread))
async def sddm(event):
    global zedself
    zelzal = event.sender_id
    malath = zedub.uid
    if zelzal == malath:
        return
    if zedself:
        sender = await event.get_sender()
        chat = await event.get_chat()
        pic = await event.download_media()
        await zedub.send_file("me", pic, caption=f"[ᯓ 𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴 - حفـظ الذاتيـه 🧧](t.me/S_EG_P) .\n\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**⌔╎مࢪحبـاً عـزيـزي المـالك 🫂\n⌔╎ تـم حفـظ الذاتيـة تلقائيـاً .. بنجـاح ☑️** ❝\n**⌔╎المـرسـل** {_format.mentionuser(sender.first_name , sender.id)} .")

@zedub.zed_cmd(
    pattern="تست (\d*) ([\s\S]*)",
    command=("sdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time.",
        "الاسـتخـدام": "{tr}sdm [number] [text]",
        "مثــال": "{tr}sdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()

@zedub.zed_cmd(
    pattern="محترقه (\d*) ([\s\S]*)",
    command=("selfdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time. and in message will show the time.",
        "الاسـتخـدام": "{tr}selfdm [number] [text]",
        "مثــال": "{tr}selfdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    text = message + f"\n\n`This message shall be self-destructed in {ttl} seconds`"

    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()
