import sys
import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID, HEROKU_APP
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("Zelzal")

print(userbot.__copyright__)
print(f"المرخصة بموجب شروط  {userbot.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("⌭ بـدء تنزيـل زدثــون ⌭")
    zedub.loop.run_until_complete(setup_bot())
    LOGS.info("⌭ بـدء تشغيـل البـوت ⌭")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()
class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()

async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("تـم التنصـيب .. بنجـاح ✓")
    print(
        f"<b> •⎆┊زدثــون™يـوزربـوت.. 🧸♥️ </b> \n<b>•⎆┊تحيـاتي .. زلـزال الهيبـه</b>\n<b>•⎆┊قنـاة السـورس ↶. </b>\n🌐┊@ZedThon "
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return
zedub.loop.run_until_complete(startup_process())
def start_bot():
  try:
    zedub.loop.run_until_complete(zedub(functions.channels.JoinChannelRequest("ZedThon")))
    zedub.loop.run_until_complete(zedub(functions.channels.JoinChannelRequest("Zed_Thon")))
    zedub.loop.run_until_complete(zedub(functions.channels.JoinChannelRequest("zzzlvv")))
    zedub.loop.run_until_complete(zedub(functions.channels.JoinChannelRequest("zzzvrr")))
    zedub.loop.run_until_complete(zedub(functions.channels.JoinChannelRequest("W_l_N")))
    zedub.loop.run_until_complete(zedub(functions.channels.JoinChannelRequest("Z_ZZZ8")))
  except Exception as e:
    print(e)
    return False
Checker = start_bot()
if Checker == False:
    print(
"عذراً لديك حظر مؤقت .. حاول التنصيب بعد 24 ساعـة"
)
    zedub.disconnect()
    sys.exit()
if len(sys.argv) in {1, 3, 4}:
    zedub.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        zedub.run_until_disconnected()
    except ConnectionError:
        pass
