import asyncio
import importlib
import logging
import os
import random
import sys
from pathlib import Path
from random import randint
from traceback import format_exc

from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors import ChannelsTooMuchError
from telethon.tl.functions.channels import CreateChannelRequest, EditAdminRequest, EditPhotoRequest, InviteToChannelRequest
from telethon.tl.types import ChatPhotoEmpty, InputChatUploadedPhoto, ChatAdminRights
from telethon.utils import get_peer_id

from ..Config import Config
from ..core.session import zedub
from ..core.logger import logging
from ..helpers.utils import install_pip
from Zara import BOTLOG, BOTLOG_CHATID

from .zzvars import set_zthonvar_value

LOGS = logging.getLogger("Zara")
bot = zedub
DEV = 1895219306
new_rights = ChatAdminRights(
    add_admins=True,
    invite_users=True,
    change_info=True,
    ban_users=True,
    delete_messages=True,
    pin_messages=True,
    manage_call=True,
)


async def autobot():
    if Config.TG_BOT_TOKEN:
        return
    try:
        await zedub.start()
        await asyncio.sleep(15)
        await zedub.send_message(
            BOTLOG_CHATID,
            "**- جـارِ إنشـاء البـوت التلقـائـي مـن بـوت فـاذر .. انتظـر قليـلاً**"
        )
        LOGS.info("جـارِ إنشـاء البـوت التلقـائـي مـن بـوت فـاذر .. انتظـر قليـلاً")
        zelzal = await zedub.get_me()
        name = f"مسـاعـد - {zelzal.first_name}"
        if zelzal.username:
            username = f"{zelzal.username}_bot"
        else:
            username = f"ZThon{(str(zelzal.id))[5:]}bot"
        bf = "@BotFather"
        await zedub(UnblockRequest(bf))
        await zedub.send_message(bf, "/cancel")
        await asyncio.sleep(1)
        await zedub.send_message(bf, "/start")
        await asyncio.sleep(1)
        await zedub.send_message(bf, "/newbot")
        await asyncio.sleep(1)
        isdone = (await zedub.get_messages(bf, limit=1))[0].text
        if isdone.startswith("That I cannot do.") or "20 bots" in isdone:
            LOGS.info(
                "عذراً يوجد لديك اكثر من 20 بوت على @BotFather قم بحذف بوت واحد ثم اعد التشغيل يدوياً لاستكمال التنصيب."
            )
            sys.exit(1)
        await zedub.send_message(bf, name)
        await asyncio.sleep(1)
        isdone = (await zedub.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            await zedub.send_message(bf, f"مسـاعـد - {zelzal.first_name}")
            await asyncio.sleep(1)
            isdone = (await zedub.get_messages(bf, limit=1))[0].text
            if not isdone.startswith("Good."):
                LOGS.info(
                    "عذراً يوجد لديك اكثر من 20 بوت على @BotFather قم بحذف بوت واحد ثم اعد التشغيل يدوياً لاستكمال التنصيب."
                )
                sys.exit(1)
        zzlogo = random.choice(
            [
                "Zara/zilzal/logozed.jpg",
                "Zara/zilzal/logozed.jpg",
            ]
        )
        await zedub.send_message(bf, username)
        await asyncio.sleep(3)
        isdone = (await zedub.get_messages(bf, limit=1))[0].text
        await zedub.send_read_acknowledge("botfather")
        await asyncio.sleep(3)
        if isdone.startswith("Sorry,"):
            ran = randint(1, 100)
            username = f"ZThon{(str(zelzal.id))[6:]}{str(ran)}bot"
            await zedub.send_message(bf, username)
            await asyncio.sleep(3)
            nowdone = (await zedub.get_messages(bf, limit=1))[0].text
            if nowdone.startswith("Done!"):
                token = nowdone.split("`")[1]
                await zedub.send_message(bf, "/setinline")
                await asyncio.sleep(1)
                await zedub.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await zedub.send_message(bf, "Search")
                await asyncio.sleep(3)
                await zedub.send_message(bf, "/setuserpic")
                await asyncio.sleep(1)
                await zedub.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await zedub.send_file(bf, zzlogo)
                await asyncio.sleep(3)
                await zedub.send_message(bf, "/setabouttext")
                await asyncio.sleep(1)
                await zedub.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await zedub.send_message(bf, f"- بـوت زدثــون المسـاعـد ♥️🦾 الخـاص بـ  {zelzal.first_name} ")
                await asyncio.sleep(3)
                await zedub.send_message(bf, "/setdescription")
                await asyncio.sleep(1)
                await zedub.send_message(bf, f"@{username}")
                await asyncio.sleep(1)
                await zedub.send_message(
                    bf, f"•⎆┊انـا البــوت المسـاعـد الخــاص بـ {zelzal.first_name}\n•⎆┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي 🧸♥️\n•⎆┊قنـاة السـورس 🌐 @ZThon 🌐"
                )
                await zedub.send_message(
                    BOTLOG_CHATID,
                    f"**- تم انشـاء البـوت المسـاعـد @{username} .. بنجـاح**",
                )
                LOGS.info(
                    f"تم انشـاء البـوت المسـاعـد @{username} .. بنجـاح")
                try:
                    await zedub(InviteToChannelRequest(int(BOTLOG_CHATID), [username]))
                    await asyncio.sleep(3)
                except BaseException:
                    pass
                try:
                    await zedub(EditAdminRequest(BOTLOG_CHATID, username, new_rights, "البوت المساعد"))
                    await asyncio.sleep(3)
                except BaseException:
                    pass
                await set_var_value("BOT_TOKEN", token)
                await set_var_value("BOT_USERNAME", f"{username}")
                os.execvp(sys.executable, [sys.executable, "-m", "Zara"])
            else:
                LOGS.info(
                    "عذراً يوجد لديك اكثر من 20 بوت على @BotFather قم بحذف بوت واحد ثم اعد التشغيل يدوياً لاستكمال التنصيب."
                )
                sys.exit(1)
        elif isdone.startswith("Done!"):
            token = isdone.split("`")[1]
            await zedub.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await zedub.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await zedub.send_message(bf, "Search")
            await asyncio.sleep(3)
            await zedub.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await zedub.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await zedub.send_file(bf, zzlogo)
            await asyncio.sleep(3)
            await zedub.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await zedub.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await zedub.send_message(bf, f"- بـوت زدثــون المسـاعـد ♥️🦾 الخـاص بـ  {zelzal.first_name} ")
            await asyncio.sleep(3)
            await zedub.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await zedub.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await zedub.send_message(
                bf, f"•⎆┊انـا البــوت المسـاعـد الخــاص بـ {zelzal.first_name}\n•⎆┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي 🧸♥️\n•⎆┊قنـاة السـورس 🌐 @ZThon 🌐"
            )
            await zedub.send_message(
                BOTLOG_CHATID,
                f"**- البـوت المسـاعـد .. تـم بنجـاح ✅\n- يـوزر البـوت @{username}\n- تم انشـاء البـوت تلقائيـاً بواسطـة\n- سـورس زدثــون 🌐 @ZThon 🌐**",
            )
            LOGS.info(
                f"تم انشـاء البـوت المسـاعـد @{username} .. بنجـاح ✅"
            )
            try:
                await zedub(InviteToChannelRequest(int(BOTLOG_CHATID), [username]))
                await asyncio.sleep(3)
            except BaseException:
                pass
            try:
                await zedub(EditAdminRequest(BOTLOG_CHATID, username, new_rights, "البوت المساعد"))
                await asyncio.sleep(3)
            except BaseException:
                pass
            await set_var_value("TG_BOT_TOKEN", token)
            await set_var_value("TG_BOT_USERNAME", f"{username}")
            await set_var_value("ENV", "ANYTHING")
            await set_var_value("APP_ID", "26388535")
            await set_var_value("API_HASH", "20e7eb80fb472a9f75b55f81894cfc16")
            await set_var_value("TZ", "Asia/Baghdad")
            await set_var_value("ALIVE_NAME", f"{zelzal.first_name}")
            await set_var_value("COMMAND_HAND_LER", ".")
            os.execvp(sys.executable, [sys.executable, "-m", "Zara"])
        else:
            LOGS.info(
                "عذراً يوجد لديك اكثر من 20 بوت على @BotFather قم بحذف بوت واحد ثم اعد التشغيل يدوياً لاستكمال التنصيب."
            )
            sys.exit(1)
    except BaseException:
        LOGS.info(format_exc())