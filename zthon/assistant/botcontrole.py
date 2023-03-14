import asyncio
from datetime import datetime

from telethon.errors import BadRequestError, FloodWaitError, ForbiddenError

from zthon import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import reply_id, time_formatter
from ..helpers.utils import _format
from ..sql_helper.bot_blacklists import check_is_black_list, get_all_bl_users
from ..sql_helper.bot_starters import del_starter_from_db, get_all_starters
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from .botmanagers import (
    ban_user_from_bot,
    get_user_and_reason,
    progress_str,
    unban_user_from_bot,
)

LOGS = logging.getLogger(__name__)

plugin_category = "bot"
botusername = Config.TG_BOT_USERNAME
cmhd = Config.COMMAND_HAND_LER





@zedub.bot_cmd(
    pattern="^/broadcast$",
    from_users=Config.OWNER_ID,
)
async def bot_broadcast(event):
    replied = await event.get_reply_message()
    if not replied:
        return await event.reply("قم بالرد على الرسالة للأذاعه !")
    start_ = datetime.now()
    br_cast = await replied.reply("يتم الأذاعه للجميع ...")
    blocked_users = []
    count = 0
    bot_users_count = len(get_all_starters())
    if bot_users_count == 0:
        return await event.reply("لا يوجد اي شخص يستخدم بوتك")
    users = get_all_starters()
    if users is None:
        return await event.reply("**هـنالك خـطأ اثناء فحص قائـمة المستخدمين**")
    for user in users:
        try:
            await event.client.send_message(
                int(user.user_id), "🔊 تم استلام اذاعه جديدة."
            )
            await event.client.send_message(int(user.user_id), replied)
            await asyncio.sleep(0.8)
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
        except (BadRequestError, ValueError, ForbiddenError):
            del_starter_from_db(int(user.user_id))
        except Exception as e:
            LOGS.error(str(e))
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID, f"**خطأ في الأذاعة **\n`{str(e)}`"
                )
        else:
            count += 1
            if count % 5 == 0:
                try:
                    prog_ = (
                        "🔊 الأذاعه العامه ...\n\n"
                        + progress_str(
                            total=bot_users_count,
                            current=count + len(blocked_users),
                        )
                        + f"\n\n• ✔️ **بنـجاح* :  `{count}`\n"
                        + f"• ✖️ **خطأ** :  `{len(blocked_users)}`"
                    )
                    await br_cast.edit(prog_)
                except FloodWaitError as e:
                    await asyncio.sleep(e.seconds)
    end_ = datetime.now()
    b_info = f"🔊 تـم بنجاح الأذاعه الى ➜  <b>{count} من المستخدمين.</b>"
    if len(blocked_users) != 0:
        b_info += f"\n🚫  <b>{len(blocked_users)} من المستخدمين</b> قام بحظر بوتك اذا تم حذف الرسالة."
    b_info += (
        f"\n⏳  <code> العملية اخذت: {time_formatter((end_ - start_).seconds)}</code>."
    )
    await br_cast.edit(b_info, parse_mode="html")


@zedub.bot_cmd(
    pattern="users$",
    command=("users", plugin_category),
    info={
        "header": "للحصول على مستخدمين البوت",
        "description": "لعـرض قـائمة المـستخدمين الـذي قـاموا بتـشغيل بـوتك",
        "usage": "{tr}المستخدمين",
    },
)
async def ban_starters(event):
    "للحصول على مستخدمين البوت."
    ulist = get_all_starters()
    if len(ulist) == 0:
        return await edit_delete(event, "** ليم يستخدم اي احد بوتك**")
    msg = "**قائمه مستخدمين البوت :\n\n**"
    for user in ulist:
        msg += f"• 👤 {_format.mentionuser(user.first_name , user.user_id)}\n**الايدي:** `{user.user_id}`\n**المعرفات:** @{user.username}\n**التاريخ: **__{user.date}__\n\n"
    await edit_or_reply(event, msg)


@zedub.bot_cmd(
    pattern="^/block\s+([\s\S]*)",
    from_users=Config.OWNER_ID,
)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id, "لا يمكنني العثور على المستخدم", reply_to=reply_to
        )
    if not reason:
        return await event.client.send_message(
            event.chat_id, "لحظر شخص اكتب السبب اولا", reply_to=reply_to
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**خطأ:**\n`{str(e)}`")
    if user_id == Config.OWNER_ID:
        return await event.reply("لا أستطيع حظر مالك البوت")
    check = check_is_black_list(user.id)
    if check:
        return await event.client.send_message(
            event.chat_id,
            f"#بالفعل_محظور\
            \nهذا المستخدم موجود في قائمه المحظورين\
            \n**سبب الحظر:** `{check.reason}`\
            \n**التاريخ:** `{check.date}`.",
        )
    msg = await ban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)


@zedub.ar_cmd(
    pattern="^/unblock(?:\s|$)([\s\S]*)",
    from_users=Config.OWNER_ID,
)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id, "** لا استطيع ايجاد المستخـدم للحـظر**", reply_to=reply_to
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**خـطأ:**\n`{str(e)}`")
    check = check_is_black_list(user.id)
    if not check:
        return await event.client.send_message(
            event.chat_id,
            f"#الغاء البلوك من الشخصي \
            \n👤 {_format.mentionuser(user.first_name , user.id)} تم الغاء حظره من البوت بنجاح.",
        )
    msg = await unban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)


@zedub.bot_cmd(
    pattern="المحظورين$",
    command=("المحظورين", plugin_category),
    info={
        "header": "لـعـرض قـائمـة الـمستخـدمين الـمحظوريـن فـي بـوتك.",
        "الـشـرح": "لعـرض قـائمـة الـمستخـدمين الـمحظوريـن فـي بـوتك",
        "الاستـخـدام": "{tr}المحظورين",
    },
)
async def ban_starters(event):
    "لـعـرض قـائمـة الـمستخـدمين الـمحظوريـن فـي بـوتك"
    ulist = get_all_bl_users()
    if len(ulist) == 0:
        return await edit_delete(event, "** لا يوجـد شخص محـظور في البـوت الـى الان**")
    msg = "**المسـتخدميـن المحـظورين في بـوتك هـم :\n\n**"
    for user in ulist:
        msg += f"• 👤 {_format.mentionuser(user.first_name , user.chat_id)}\n**الايدي:** `{user.chat_id}`\n**المعرف:** @{user.username}\n**التاريخ: **{user.date}\n**السبب:** {user.reason}\n\n"
    await edit_or_reply(event, msg)


@zedub.bot_cmd(
    pattern="وضع_التكرار (تشغيل|تعطيل)$",
    command=("وضع_تكرار", plugin_category),
    info={
        "header": "لتشغيل او تعطيل التكرار في بوتك",
        "الشـرح": "اذا قـام المسـتخدم بـتكرار او تعـديـل 10 رسـائل سيـقوم الـبوت بحـظره",
        "الاسـتخـدام": [
            "{tr}وضع_تكرار تشغيل",
            "{tr}وضع_تكرار تعطيل",
        ],
    },
)
async def ban_antiflood(event):
    "لتشغيل او تعطيل التكرار في بوتك."
    input_str = event.pattern_match.group(1)
    if input_str == "تشغيل":
        if gvarstatus("bot_antif") is not None:
            return await edit_delete(event, "`Bot Antiflood was already enabled.`")
        addgvar("bot_antif", True)
        await edit_delete(event, "`Bot Antiflood Enabled.`")
    elif input_str == "تعطيل":
        if gvarstatus("bot_antif") is None:
            return await edit_delete(event, "`Bot Antiflood was already disabled.`")
        delgvar("bot_antif")
        await edit_delete(event, "`Bot Antiflood Disabled.`")
