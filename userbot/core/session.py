import os
import sys

try:
    pass
except ModuleNotFoundError:
    os.system("pip3 install py-tgcalls")

from pySmartDL import SmartDL
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import ZedUserBotClient

__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "zelzal"

try:
    zedub = ZedUserBotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(zedub)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()

if Config.STRING_2:
    session2 = StringSession(str(STRING_2))
    ZED2 = ZedUserBotClient(
        session=session2,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py2 = PyTgCalls(ZED2)
else:
    call_py2 = None
    ZED2 = None

zedub.tgbot = tgbot = ZedUserBotClient(
    session="ZedTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)
