import os
import shutil
from asyncio import sleep

from zthon import zedub
from zthon.core.logger import logging
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)


@zedub.zed_cmd(
    pattern="ذاتيه",
    command=("ذاتيه", plugin_category),
    info={
        "header": "لـ حفـظ الصـوره/الميديـا الذاتيـه",
        "description": "Suppose if you use .sdm 10 hi then message will be immediately send new message as hi and then after 10 sec this message will auto delete.",
        "الاسـتخـدام": "{tr}ذاتيه",
        "مثــال": "{tr}ذاتيه بالـرد ع صوره او ميديا ذاتيـه",
    },
)
async def oho(event):
  if not event.is_reply:
    return await event.edit('**- ❝ ⌊بالـرد علـى صورة ذاتيـة التدميـر 𓆰...**')
  zzzzl1l = await event.get_reply_message()
  pic = await zzzzl1l.download_media()
  await bot.send_file(BOTLOG_CHATID, pic, caption=f"""
**- ❝ ⌊تـم حفـظ الصـورة ذاتيـة التدمير بنجـاح ☑️ 🥳𓆰...**

  """)
  await event.delete()


@zedub.zed_cmd(
    pattern="ذاتي (\d*) ([\s\S]*)",
    command=("sdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time.",
        "description": "Suppose if you use .sdm 10 hi then message will be immediately send new message as hi and then after 10 sec this message will auto delete.",
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
    pattern="ذاتية (\d*) ([\s\S]*)",
    command=("selfdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time. and in message will show the time.",
        "description": "Suppose if you use .sdm 10 hi then message will be immediately will send new message as hi and then after 10 sec this message will auto delete.",
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
