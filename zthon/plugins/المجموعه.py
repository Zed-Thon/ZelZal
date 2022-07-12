#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®

from datetime import datetime
from math import sqrt
import asyncio
import time
import io
import os
import shutil
import zipfile
import base64
import csv
import random

from emoji import emojize

from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from datetime import datetime
from asyncio import sleep
from asyncio.exceptions import TimeoutError
from telethon import functions, types
from telethon import events
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest, GetFullChannelRequest, GetParticipantsRequest, EditAdminRequest, EditPhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest, ExportChatInviteRequest
from telethon.errors import ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, BadRequestError, ChatAdminRequiredError, FloodWaitError, MessageNotModifiedError, UserAdminInvalidError
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAdminInvalidError, UserIdInvalidError, UserAlreadyParticipantError, UserNotMutualContactError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError
from telethon.tl.types import ChatAdminRights, InputChatPhotoEmpty, MessageMediaPhoto, InputPeerUser
from telethon.tl.types import ChannelParticipantsKicked, ChannelParticipantAdmin, ChatBannedRights, ChannelParticipantCreator, ChannelParticipantsAdmins, ChannelParticipantsBots, MessageActionChannelMigrateFrom, UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently
from telethon.utils import get_display_name, get_input_location, get_extension
from os import remove
from math import sqrt
from prettytable import PrettyTable
from emoji import emojize
from pathlib import Path

from zthon import zedub

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import reply_id
from ..helpers.utils import _format, get_user_from_event, reply_id
from ..helpers import media_type
from ..helpers.google_image_download import googleimagesdownload
from ..helpers.tools import media_type
from ..sql_helper.locks_sql import get_locks, is_locked, update_lock
from ..utils import is_admin
from . import progress
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from ..sql_helper import no_log_pms_sql
from ..sql_helper.globals import addgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)
plugin_category = "الادمن"

BANNED_RIGHTS = ChatBannedRights(until_date=None, view_messages=True, send_messages=True, send_media=True, send_stickers=True, send_gifs=True, send_games=True, send_inline=True, embed_links=True)
ZELZAL_RIGHTS = ChatBannedRights(until_date=None, view_messages=True, send_messages=True, send_media=True, send_stickers=True, send_gifs=True, send_games=True, send_inline=True, embed_links=True)
UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)
plugin_category = "الادمن"

TYPES = [
    "Photo",
    "Audio",
    "Video",
    "Document",
    "Sticker",
    "Gif",
    "Voice",
    "Round Video",
]
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call

def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

def zipdir(dirName):
    filePaths = []
    for root, directories, files in os.walk(dirName):
        for filename in files:
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)
    return filePaths

class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0
LOG_CHATS_ = LOG_CHATS()

PP_TOO_SMOL = "**❈╎الصورة صغيرة جدًا  📸** ."
PP_ERROR = "**❈╎فشل أثناء معالجة الصورة  📵** ."
NO_ADMIN = "**❈╎أنا لست مشرف هنا ** ."
NO_PERM = "**❈╎ليس لدي أذونات كافية  🚮** ."
CHAT_PP_CHANGED = "**❈╎تغيّرت صورة الدردشة  🌅** ."
INVALID_MEDIA = "**⌔ ╎ ملحق غير صالح  📳** ."
IMOGE_ZEDTHON = "❈╎"



async def ban_user(chat_id, i, rights):
    try:
        await jmthon(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)


@zedub.zed_cmd(pattern=r"تفليش$")
async def _(event):
    result = await event.client.get_permissions(event.chat_id, event.client.uid)
    if not result:
        return await edit_or_reply(
            event, "**- عـذراً . . ليس لديك الصلاحيات الكافية لـ استخدام هذا الامـر هنـا**"
        )
    jmthonevent = await edit_or_reply(event, "جارِ")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await jmthonevent.edit(f"**- تـم بنجـاح ☑️ . . تفليش  {success}  مـن  {total} عضـو 🚮**")


@zedub.zed_cmd(pattern="اضافه ([\s\S]*)", groups_only=True)
async def get_users(event):
    legen_ = event.text[10:]
    zedthon_chat = legen_.lower
    restricted = ["@ZedThon_support", "@ZThon_support"]
    ZTHON = await edit_or_reply(event, f"**❈╎جـارِ اضافـه الاعضـاء مـن  ** {legen_}   **⅏ . . .**")
    if zedthon_chat in restricted:
        return await ZTHON.edit(
            event, "**- دي . . لا يمكنك تخميط الاعضـاء من كـروب السـورس**"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await ZTHON.edit("**❈╎ جـارِ إتمـام العمليـة إنتظـر ⅏ . . .**")
    else:
        await ZTHON.edit("**❈╎ جـارِ إتمـام العمليـة إنتظـر ⅏ . . .**")
    if event.is_private:
        return await ZTHON.edit("- لا يمكنك اضافه الاعضاء هنا")
    s = 0
    f = 0
    error = "None"
    await ZTHON.edit(
        "**❈╎ حالة الاضـافـه:**\n\n**❈╎ تتم جمع معلومات المستخدمين 🔄 ...⏣**"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await ZTHON.edit(
                    f"**حالة الاضـافـه انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await zedub(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await ZTHON.edit(
                f"**❈╎جـارِ الإضافـة . . .**\n\n**❈╎اضيف** `{s}` \n**❈╎خطـأ بـ اضافـة** `{f}` \n\n**❈╎آخـر خطـأ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await ZTHON.edit(
        f"**❈╎اڪتملت الإضافـة . . ✅** \n\n**❈╎تم بنجـاح اضافـة** `{s}` \n**❈╎خطـأ بـ اضافـة** `{f}`"
    )


@zedub.zed_cmd(pattern="تجميع الاعضاء$")
async def scrapmem(event):
    chat = event.chat_id
    xx = await edit_or_reply(event, "**❈╎جـارِ إتمـام العمليـة إنتظـر ⅏ . . .**")
    members = await event.client.get_participants(chat, aggressive=True)
    with open("members.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(["user_id", "hash"])
        for member in members:
            writer.writerow([member.id, member.access_hash])
    await xx.edit("**⪼ تم تجميع الاعضاء بنجاح 𓆰،**")


@zedub.zed_cmd(pattern="اضف الاعضاء$")
async def admem(event):
    xx = await edit_or_reply(event, "**⪼ اضافه 0 من الاعضاء  ؟..**")
    chat = await event.get_chat()
    users = []
    with open("members.csv", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {"id": int(row[0]), "hash": int(row[1])}
            users.append(user)
    n = 0
    for user in users:
        n += 1
        if n % 30 == 0:
            await xx.edit(
                f"**⪼ لقد قمت بأضافه 30 عضو لا يمكنك الاضافه اكثر الان انتظر :** `{900/60}` **دقيقة**"
            )
            await asyncio.sleep(900)
        try:
            userin = InputPeerUser(user["id"], user["hash"])
            await event.client(InviteToChannelRequest(chat, [userin]))
            await asyncio.sleep(random.randrange(5, 7))
            await xx.edit(f"**❈╎تم إكمـال العمليـه جـارِ اضافـة** `{n}` **مـن الاعضـاء . .**")
        except TypeError:
            n -= 1
            continue
        except UserAlreadyParticipantError:
            n -= 1
            continue
        except UserPrivacyRestrictedError:
            n -= 1
            continue
        except UserNotMutualContactError:
            n -= 1
            continue


@zedub.zed_cmd(
    pattern="المشرفين(?:\s|$)([\s\S]*)",
    command=("المشرفين", plugin_category),
    info={
        "header": "To get list of admins.",
        "description": "Will show you the list of admins and if you use this in group then will tag them.",
        "usage": [
            "{tr}admins <username/userid>",
            "{tr}admins <in group where you need>",
        ],
        "examples": "{tr}المشرفين + معرف او رابط المجموعه",
    },
)
async def _(event):
    "To get list of admins."
    mentions = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑮𝑹𝑶𝑼𝑷 𝑫𝑨𝑻𝑨 𓆪\n** ⪼ المشرفـون في ۿذه المجموعه :** \n"
    reply_message = await reply_id(event)
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if input_str:
        mentions = f"𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑮𝑹𝑶𝑼𝑷 𝑫𝑨𝑻𝑨 𓆪\n** ⪼ المشرفـون في {input_str} :** \n"
        try:
            chat = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, str(e))
    else:
        chat = to_write_chat
        if not event.is_group:
            return await edit_or_reply(event, "هل أنت متأكد من أن هذه مجموعة؟")
    try:
        async for x in event.client.iter_participants(
            chat, filter=ChannelParticipantsAdmins
        ):
            if not x.deleted and isinstance(x.participant, ChannelParticipantCreator):
                mentions += "\n⪼ المالك [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
        mentions += "\n"
        async for x in event.client.iter_participants(
            chat, filter=ChannelParticipantsAdmins
        ):
            if x.deleted:
                mentions += "\n `{}`".format(x.id)
            elif isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n ⪼ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id
                )
    except Exception as e:
        mentions += f" {str(e)}" + "\n"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_message)
    await event.delete()


@zedub.zed_cmd(
    pattern="الاعضاء(?:\s|$)([\s\S]*)",
    command=("الاعضاء", plugin_category),
    info={
        "header": "To get list of users.",
        "description": "Will show you the list of users.",
        "note": "There was limitation in this you cant get more 10k users",
        "usage": [
            "{tr}users <username/userid>",
            "{tr}users <in group where you need>",
        ],
    },
)
async def get_users(show):
    "To get list of Users."
    mentions = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑮𝑹𝑶𝑼𝑷 𝑫𝑨𝑻𝑨 𓆪\n**❈╎الأعضـاء فـي هـذه المجموعـة 𓎤:**\n\n"
    await reply_id(show)
    if input_str := show.pattern_match.group(1):
        mentions = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑮𝑹𝑶𝑼𝑷 𝑫𝑨𝑻𝑨 𓆪\n**❈╎الأعضاء في {} من المجموعات 𓎤:**\n".format(input_str)
        try:
            chat = await show.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(show, f"`{e}`", 10)
    elif not show.is_group:
        return await edit_or_reply(show, "**❈╎هـذه ليسـت مجموعـة ✕**")
    zedevent = await edit_or_reply(show, "**❈╎جـاري سحـب قائمـة معرّفـات الأعضـاء 🝛**")
    try:
        if show.pattern_match.group(1):
            async for user in show.client.iter_participants(chat.id):
                if user.deleted:
                    mentions += f"\n**❈╎الحسـابات المحذوفـة ⌦** `{user.id}`"
                else:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) "
                    )
        else:
            async for user in show.client.iter_participants(show.chat_id):
                if user.deleted:
                    mentions += f"\n**❈╎الحسـابات المحذوفـة ⌦** `{user.id}`"
                else:
                    mentions += (
                        f"\n[{user.first_name}](tg://user?id={user.id}) "
                    )
    except Exception as e:
        mentions += f" {str(e)}" + "\n"
    await edit_or_reply(zedevent, mentions)


@zedub.zed_cmd(
    pattern="المعلومات(?:\s|$)([\s\S]*)",
    command=("المعلومات", plugin_category),
    info={
        "header": "To get Group details.",
        "description": "Shows you the total information of the required chat.",
        "usage": [
            "{tr}chatinfo <username/userid>",
            "{tr}chatinfo <in group where you need>",
        ],
        "examples": "{tr}معلومات + معرف او رابط المجموعه",
    },
)
async def info(event):
    "To get group information"
    zedevent = await edit_or_reply(event, "**❈╎يتـمّ جلـب معلومـات الدردشـة، إنتظـر ⅏**")
    chat = await get_chatinfo(event, zedevent)
    if chat is None:
        return
    caption = await fetch_info(chat, event)
    try:
        await zedevent.edit(caption, parse_mode="html")
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, f"**❈╎هنـاك خطـأ في معلومـات الدردشـة ✕ : **\n`{str(e)}`"
            )

        await zedevent.edit("**❈╎حـدث خـطأ مـا، يرجـى التحقق من الأمـر ⎌**")


async def get_chatinfo(event, zedevent):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await zedevent.edit("**❈╎لـم يتـمّ العثـور على القنـاة/المجموعـة ✕**")
            return None
        except ChannelPrivateError:
            await zedevent.edit(
                "**❈╎هـذه مجموعـة أو قنـاة خاصـة أو لقد تمّ حظـري منه ⛞**"
            )
            return None
        except ChannelPublicGroupNaError:
            await zedevent.edit("**❈╎القنـاة أو المجموعـة الخارقـة غيـر موجـودة ✕**")
            return None
        except (TypeError, ValueError) as err:
            LOGS.info(err)
            await edit_delete(zedevent, "**❈╎لم يتم العثور على المجموعة او القناة**")
            return None
    return chat_info


async def fetch_info(chat, event):  # sourcery no-metrics
    # chat.chats is a list so we use get_entity() to avoid IndexError
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = (
        chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    )
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(
            GetHistoryRequest(
                peer=chat_obj_info.id,
                offset_id=0,
                offset_date=datetime(2010, 1, 1),
                add_offset=-1,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0,
            )
        )
    except Exception as e:
        msg_info = None
        LOGS.error(f"Exception: {e}")
    # No chance for IndexError as it checks for msg_info.messages first
    first_msg_valid = bool(
        msg_info and msg_info.messages and msg_info.messages[0].id == 1
    )

    # Same for msg_info.users
    creator_valid = bool(first_msg_valid and msg_info.users)
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = (
        msg_info.users[0].first_name
        if creator_valid and msg_info.users[0].first_name is not None
        else "Deleted Account"
    )
    creator_username = (
        msg_info.users[0].username
        if creator_valid and msg_info.users[0].username is not None
        else None
    )
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = (
        msg_info.messages[0].action.title
        if first_msg_valid
        and isinstance(msg_info.messages[0].action, MessageActionChannelMigrateFrom)
        and msg_info.messages[0].action.title != chat_title
        else None
    )
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception:
        dc_id = "Unknown"

    # this is some spaghetti I need to change
    description = chat.full_chat.about
    members = (
        chat.full_chat.participants_count
        if hasattr(chat.full_chat, "participants_count")
        else chat_obj_info.participants_count
    )
    admins = (
        chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    )
    banned_users = (
        chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    )
    restrcited_users = (
        chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    )
    members_online = (
        chat.full_chat.online_count if hasattr(chat.full_chat, "online_count") else 0
    )
    group_stickers = (
        chat.full_chat.stickerset.title
        if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset
        else None
    )
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = (
        chat.full_chat.read_inbox_max_id
        if hasattr(chat.full_chat, "read_inbox_max_id")
        else None
    )
    messages_sent_alt = (
        chat.full_chat.read_outbox_max_id
        if hasattr(chat.full_chat, "read_outbox_max_id")
        else None
    )
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = (
        "<b>نعم</b>"
        if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup
        else "لا"
    )
    slowmode = (
        "<b>مـفعل</b>"
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled
        else "غير مفـعل"
    )
    slowmode_time = (
        chat.full_chat.slowmode_seconds
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled
        else None
    )
    restricted = (
        "<b>لا</b>"
        if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted
        else "نعم"
    )
    verified = (
        "<b>مـوثق</b>"
        if hasattr(chat_obj_info, "verified") and chat_obj_info.verified
        else "غيـر موثق"
    )
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None
    # end of spaghetti block

    if admins is None:
        # use this alternative way if chat.full_chat.admins_count is None,
        # works even without being an admin
        try:
            participants_admins = await event.client(
                GetParticipantsRequest(
                    channel=chat.full_chat.id,
                    filter=ChannelParticipantsAdmins(),
                    offset=0,
                    limit=0,
                    hash=0,
                )
            )
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            LOGS.error(f"Exception:{e}")
    if bots_list:
        for _ in bots_list:
            bots += 1

    caption = "<b>❈╎معلومـات الدردشـة  🝢 :</b>\n\n"
    caption += f"<b>❈╎الآيـدي  :</b> <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"<b>❈╎إسـم المجموعـة :</b> {chat_title}\n"
    if former_title is not None:  # Meant is the very first title
        caption += f"<b>❈╎الإسم السابـق :</b>  {former_title}\n"
    if username is not None:
        caption += f"<b>❈╎نـوع المجموعـة ⌂:</b>  مجموعـة عامّـة  \n"
        caption += f"<b>❈╎الرابـط :</b>  \n {username}\n"
    else:
        caption += f"<b>❈╎نـوع المجموعـة ⌂:</b>  مجموعـة عامّـة  \n"
    if creator_username is not None:
        caption += f"<b>❈╎المالـك :</b>   {creator_username}\n"
    elif creator_valid:
        caption += ('<b>❈╎المالـك :</b>  <a href="tg://user?id={creator_id}">{creator_firstname}</a>\n')
    if created is not None:
        caption += f"<b>❈╎تاريـخ الإنشـاء :</b>  \n <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"<b>❈╎الإنتـاج :</b>    <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"<b>❈╎آيـدي قاعـدة البيانـات:</b>  {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1 + sqrt(1 + 7 * exp_count / 14)) / 2)
        caption += f"<b>❈╎الأعضـاء:</b>  <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"<b>❈╎الرسائـل التي يمڪن مشاهدتها:</b>  <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"<b>❈╎الرسائـل المرسلـة :</b> <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"<b>❈╎الرسـائل المرسلة: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"<b>❈╎الأعضـاء:</b>  <code>{members}</code>\n"
    if admins is not None:
        caption += f"<b>❈╎المشرفيـن:</b>  <code>{admins}</code>\n"
    if bots_list:
        caption += f"<b>❈╎البـوتات:</b>  <code>{bots}</code>\n"
    if members_online:
        caption += f"<b>❈╎المتصليـن حـالياً:</b>  <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"<b>❈╎الأعضـاء المقيّديـن:</b>  <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"<b>❈╎الأعضـاء المحظوريـن:</b>  <code>{banned_users}</code>"
    if group_stickers is not None:
        caption += f'{chat_type} <b>❈╎الملصقـات:</b>  <a href="t.me/addstickers/{chat.full_chat.stickerset.short_name}">{group_stickers}</a>'
    caption += "\n"
    if not broadcast:
        caption += f"<b>❈╎الوضـع البطيئ:</b>  {slowmode}"
        if (
            hasattr(chat_obj_info, "slowmode_enabled")
            and chat_obj_info.slowmode_enabled):
            caption += f", <code>{slowmode_time}s</code>\n"
        else:
            caption += "\n"
        caption += f"<b>❈╎الـمجموعـة الخارقـة :</b>  {supergroup}\n"
    if hasattr(chat_obj_info, "restricted"):
        caption += f"<b>❈╎المقيّـد:</b>  {restricted}"
        if chat_obj_info.restricted:
            caption += f">:</b>  {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> <b>❈╎السـبب :</b>  {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> <b>❈╎النّـص :</b>  {chat_obj_info.restriction_reason[0].text}\n\n"
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
        caption += "<b>❈╎السارقيـن:</b>  <b>Yes</b>\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"<b>❈╎الحسابـات الموثقـة  :</b>  {verified}\n"
    if description:
        caption += f"<b>❈╎الوصـف :</b>  \n<code>{description}</code>\n"
    return caption



@zedub.zed_cmd(pattern="معرفات 100(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 100):
        mentions += f"\n**-** @{x.username} "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="معرفات 200(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 200):
        mentions += f"\n**-** @{x.username} "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="معرفات 300(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 300):
        mentions += f"\n**-** @{x.username} "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 500(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 500):
        mentions += f"- @{x.username} "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 1k(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 1000):
        mentions += f"- @{x.username} "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 300(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 300):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 200(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 200):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 150(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 150):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 100(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 100):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 50(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 50):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@zedub.zed_cmd(pattern="تاك 10(?: |$)(.*)")
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 10):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) \n"
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()



@zedub.zed_cmd(pattern="رفع الحظر ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        LOGS.info("TODO: Not yet Implemented")
    else:
        if event.is_private:
            return False
        et = await edit_or_reply(event, "**↫ البحث في قوائم المشاركين ⇲**")
        p = 0
        async for i in event.client.iter_participants(
            event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
        ):
            rights = ChatBannedRights(until_date=0, view_messages=False)
            try:
                await event.client(
                    functions.channels.EditBannedRequest(event.chat_id, i, rights)
                )
            except Exception as ex:
                await et.edit(str(ex))
            else:
                p += 1
        await et.edit("⪼ {} **↫** {} **رفع الحظر عنهم**".format(event.chat_id, p))


@zedub.zed_cmd(pattern=r"غادر(.*)")
async def kickme(leave):
    await leave.edit("**❈╎جـاري مـغادرة المجـموعة مـع السـلامة  🚶‍♂️  ..**")
    await leave.client.kick_participant(leave.chat_id, "me")

@zedub.zed_cmd(pattern=r"مسح المحظورين(.*)")
async def _(event):
    zedevent = await edit_or_reply(event, "**❈╎ إلغاء حظر جميع الحسابات المحظورة في هذه المجموعة 🆘**")
    succ = 0
    total = 0
    flag = False
    chat = await event.get_chat()
    async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
        total += 1
        rights = ChatBannedRights(until_date=0, view_messages=False)
        try:
            await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
        except FloodWaitError as e:
            LOGS.warn(f"**❈╎هناك ضغط كبير بالاستخدام يرجى الانتضار .. ‼️ بسبب  : {e.seconds} **")
            await zedevent.edit(f"**❈╎{readable_time(e.seconds)} مطلـوب المـعاودة مـرة اخـرى للـمسح 🔁 **")
            await sleep(e.seconds + 5)
        except Exception as ex:
            await zedevent.edit(str(ex))
        else:
            succ += 1
            if flag:
                await sleep(2)
            else:
                await sleep(1)
            try:
                if succ % 10 == 0:
                    await zedevent.edit(f"**❈╎جـاري مسـح المحـظورين ⭕️  : \n {succ} الحسـابات الـتي غيـر محظـورة لحـد الان.**")
            except MessageNotModifiedError:
                pass
    await zedevent.edit(f"**❈╎تـم مسـح المحـظورين مـن أصـل 🆘 :**{succ}/{total} \n اسـم المجـموعـة 📄 : {chat.title}")

@zedub.zed_cmd(pattern=r"المحذوفين ?([\s\S]*)")
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**❈╎لا توجـد حـسابات محذوفـة في هـذه المجموعـة !**"
    if con != "تنظيف":
        event = await edit_or_reply(show, "**❈╎جـاري البحـث عـن الحسابـات المحذوفـة ⌯**")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"**❈╎تم ايجـاد  {del_u}  من  الحسابـات المحذوفـه في هـذه المجموعـه**\n**❈╎لحذفهـم إستخـدم الأمـر  ⩥ :**  `.المحذوفين تنظيف`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "❈╎أنـا لسـت مشـرفـاً هنـا !", 5)
        return
    event = await edit_or_reply(show, "**❈╎جـاري حـذف الحسـابات المحذوفـة ⌯**")
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "**❈╎ ليس لدي صلاحيات الحظر هنا**", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"**❈╎تـم حـذف  {del_u}  الحسـابات المحذوفـة ✓**"
    if del_a > 0:
        del_status = f"**❈╎تـم حـذف {del_u} الحسـابات المحذوفـة، ولڪـن لـم يتـم حذف الحسـابات المحذوفـة للمشرفيـن !**"
    await edit_delete(event, del_status, 5)
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"**❈╎تنظيف :**\
            \n❈╎{del_status}\
            \n*❈╎المحادثـة ⌂** {show.chat.title}(`{show.chat_id}`)",
        )

@zedub.zed_cmd(pattern="الرابط ?(.*)")
async def zed(event):
    zedevent = await edit_or_reply(event, "**⇜ جـاري جلـب رابـط المجموعـه ⇜**")
    chat = await event.get_chat()
    try:
        ZL = await event.client(
            ExportChatInviteRequest(event.chat_id),
        )
    except ChatAdminRequiredError:
        return await edit_delete(zedevent, "**❈╎عـذراً عـزيـزي .. انت لسـت مشرفـاً هنـا 🙇🏻**", 5)
    await zedevent.edit(f"**❈╎رابـط الـمجموعـه ⎋:**\n\n⎌ [{chat.title}]({ZL.link}) ⎌")   
    
@zedub.zed_cmd(pattern="رسائلي ?(.*)")
async def zed(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(
            f"**❈╎لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**"
        )
    thon = event.pattern_match.group(1)
    if thon:
        a = await bot.get_messages(event.chat_id, 0, from_user=thon)
        return await event.edit(
            f"**❈╎المستخـدم** {thon} **لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**"
        )
    else:
        thon = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=thon)
    await event.edit(
        f"**❈╎لديـك هنـا ⇽**  `{a.total}`  **رسـالـه 📩**"
    )   

@zedub.zed_cmd(pattern="رسائله ?(.*)")
async def zed(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(
            f"**❈╎لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**"
        )
    thon = event.pattern_match.group(1)
    if thon:
        a = await bot.get_messages(event.chat_id, 0, from_user=thon)
        return await event.edit(
            f"**❈╎المستخـدم** {thon} **لديـه هنـا ⇽**  `{a.total}`  **رسـالـه 📩**"
        )
    else:
        thon = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=thon)
    await event.edit(
        f"**❈╎لديـك هنـا ⇽**  `{a.total}`  **رسـالـه 📩**"
    )   
