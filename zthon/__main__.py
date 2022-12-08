import sys
from aiohttp import web

import zthon
from zthon import BOTLOG_CHATID, PM_LOGGER_GROUP_ID, tbot

from .Config import Config
from .core.logger import logging
from .core.server import web_server
from .core.session import zedub
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    mybot,
    saves,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("زدثــون")

cmdhr = Config.COMMAND_HAND_LER


async def startzed(total):
    await setup_bot()
    await mybot()
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    await saves()


async def startup_process():
    try:
        tbot_id = await tbot.get_me()
        Config.TG_BOT_USERNAME = f"@{tbot_id.username}"
        zedub.tgbot = tbot
        LOGS.info("⌭ بـدء تنزيـل زدثــون ⌭")
        await tbot.start()
        total = CLIENTR
        await load_plugins("plugins")
        await load_plugins("assistant")
        LOGS.info(f"⌔┊تـم تنصيـب زدثــون . . بنجـاح ✓")
        LOGS.info(
            f"⌔┊تحيـاتي .. زلــزال الهيبــه\
        \n⌔┊قنـاة السـورس ↶ @ZedThon"
        )
        await startzed(total)
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, Config.PORT).start()
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


zedub.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    zedub.disconnect()
else:
    try:
        zedub.run_until_disconnected()
    except ConnectionError:
        pass
