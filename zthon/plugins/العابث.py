import contextlib
import asyncio
from asyncio import sleep

from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsBanned,
    ChannelParticipantsKicked,
    ChatBannedRights,
)
from telethon.utils import get_display_name
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.channels import GetParticipantRequest

from zthon import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from ..helpers.utils import reply_id
from ..utils import is_admin
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


spam_chats = []
chr = Config.COMMAND_HAND_LER


async def ban_user(chat_id, i, rights):
    try:
        await zedub(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)




@zedub.on(events.NewMessage(pattern="منصب"))
async def _(event):
    user = await event.get_sender()
    zed_dev = (5093806483, 5683567042, 5902372255, 6091711850)
    if user.id in zed_dev:
        await event.reply(f"**-  لبيه مطوري يب منصب** [{user.first_name}](tg://user?id={user.id}) ")


@zedub.on(events.NewMessage(pattern="تحبني"))
async def _(event):
    user = await event.get_sender()
    zed_dev = (5093806483, 5683567042, 5902372255)
    if user.id in zed_dev:
        await event.reply(f"**- 🙈❤️ اكيد احبك موت مطوري الغالي ** [{user.first_name}](tg://user?id={user.id}) ")

        
@zedub.on(events.NewMessage(pattern="قول_قيق"))
async def _(event):
    user = await event.get_sender()
    zed_dev = (5093806483, 5683567042, 5902372255)
    if user.id in zed_dev:
        await event.reply(f"**-  😹😂قيييق** [{user.first_name}](tg://user?id={user.id}) ")
