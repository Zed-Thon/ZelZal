import os
from asyncio.exceptions import CancelledError
from time import sleep

from zthon import zedub

from ..core.logger import logging
from ..core.managers import edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP, mention

LOGS = logging.getLogger(__name__)
plugin_category = "الادوات"


@zedub.zed_cmd(
    pattern="اعاده تشغيل$",
    command=("اعاده تشغيل", plugin_category),
    info={
        "header": "Restarts the bot !!",
        "الاستـخـدام": "{tr}اعاده تشغيل",
    },
    disable_errors=True,
)
async def _(event):
    "Restarts the bot !!"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#إعــادة_التشغيــل\n\n" "**⪼ بـوت زدثـــون في وضـع اعـادة التشغيـل انتظـر**\n\n" "**⪼ اذ لـم يستجـب البـوت بعـد خمـس دقائـق .. قـم بالذهـاب الـى حسـاب هيـروكو واعـادة التشغيـل اليـدوي**")
    sandy = await edit_or_reply(
        event,
        f"**⌔∮ اهـلا عـزيـزي** - {mention}\n\n"
        f"**⌔∮ يتـم الان اعـادة تشغيـل بـوت زدثــون قـد يستغـرق الامـر 1-2 دقيقـه ▬▭ ...**",
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS.error(e)
    try:
        await zedub.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS.error(e)


@zedub.zed_cmd(
    pattern="ايقاف البوت$",
    command=("ايقاف البوت", plugin_category),
    info={
        "header": "Shutdowns the bot !!",
        "description": "To turn off the dyno of heroku. you cant turn on by bot you need to got to heroku and turn on or use @hk_heroku_bot",
        "الاستـخـدام": "{tr}shutdown",
    },
)
async def _(event):
    "Shutdowns the bot"
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#ايقــاف البــوت\n\n" "**- بـوت زدثــون فـي وضــع الايقــاف**")
    await edit_or_reply(event, "**⌔∮جــارِ إيقـاف تشغيـل بـوت زدثــون الآن 📟 ... شغِّـلنـي يـدويًـا لاحقًــا**")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        os._exit(143)


@zedub.zed_cmd(
    pattern="نوم( [0-9]+)?$",
    command=("نوم", plugin_category),
    info={
        "header": "Userbot will stop working for the mentioned time.",
        "الاستـخـدام": "{tr}sleep <seconds>",
        "مثــال": "{tr}sleep 60",
    },
)
async def _(event):
    "To sleep the userbot"
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "Syntax: `.sleep time`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"You put the bot to sleep for {counter} seconds"
        )

    event = await edit_or_reply(event, f"`ok, let me sleep for {counter} seconds`")
    sleep(counter)
    await event.edit("`OK, I'm awake now.`")


@zedub.zed_cmd(
    pattern="notify (on|off)$",
    command=("notify", plugin_category),
    info={
        "header": "To update the your chat after restart or reload .",
        "description": "Will send the ping cmd as reply to the previous last msg of (restart/reload/update cmds).",
        "الاستـخـدام": [
            "{tr}notify <on/off>",
        ],
    },
)
async def set_pmlog(event):
    "To update the your chat after restart or reload ."
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        if gvarstatus("restartupdate") is None:
            return await edit_delete(event, "__Notify already disabled__")
        delgvar("restartupdate")
        return await edit_or_reply(event, "__Notify is disable successfully.__")
    if gvarstatus("restartupdate") is None:
        addgvar("restartupdate", "turn-oned")
        return await edit_or_reply(event, "__Notify is enable successfully.__")
    await edit_delete(event, "__Notify already enabled.__")
