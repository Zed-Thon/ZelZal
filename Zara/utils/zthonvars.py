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
    if Config.API_HASH is not None:
        return
    try:
        await zedub.start()
        await asyncio.sleep(15)
        zelzal = await zedub.get_me()
        await set_var_value("ENV", "ANYTHING")
        await set_var_value("APP_ID", "26388535")
        await set_var_value("API_HASH", "20e7eb80fb472a9f75b55f81894cfc16")
        await set_var_value("TZ", "Asia/Baghdad")
        await set_var_value("ALIVE_NAME", f"{zelzal.first_name}")
        await set_var_value("COMMAND_HAND_LER", ".")
        os.execvp(sys.executable, [sys.executable, "-m", "Zara"])
    except BaseException:
        LOGS.info(format_exc())