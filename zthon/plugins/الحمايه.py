import random
import re
from datetime import datetime

from telethon import Button, functions
from telethon.events import CallbackQuery
from telethon.utils import get_display_name

from zthon import zedub
from zthon.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format, get_user_from_event, reply_id
from ..sql_helper import global_collectionjson as sql
from ..sql_helper import global_list as sqllist
from ..sql_helper import pmpermit_sql
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG_CHATID, mention

plugin_category = "البوت"
LOGS = logging.getLogger(__name__)
cmdhd = Config.COMMAND_HAND_LER


class PMPERMIT:
    def __init__(self):
        self.TEMPAPPROVED = []


PMPERMIT_ = PMPERMIT()


async def do_pm_permit_action(event, chat):  # sourcery no-metrics
    # sourcery skip: low-code-quality
    reply_to_id = await reply_id(event)
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    me = await event.client.get_me()
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    first = chat.first_name
    last = chat.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{chat.username}" if chat.username else mention
    userid = chat.id
    my_first = me.first_name
    my_last = me.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{me.username}" if me.username else my_mention
    if str(chat.id) not in PM_WARNS:
        PM_WARNS[str(chat.id)] = 0
    try:
        MAX_FLOOD_IN_PMS = Config.MAX_FLOOD_IN_PMS
    except (ValueError, TypeError):
        MAX_FLOOD_IN_PMS = 6
    totalwarns = MAX_FLOOD_IN_PMS + 1
    warns = PM_WARNS[str(chat.id)] + 1
    remwarns = totalwarns - warns
    if PM_WARNS[str(chat.id)] >= MAX_FLOOD_IN_PMS:
        try:
            if str(chat.id) in PMMESSAGE_CACHE:
                await event.client.delete_messages(
                    chat.id, PMMESSAGE_CACHE[str(chat.id)]
                )
                del PMMESSAGE_CACHE[str(chat.id)]
        except Exception as e:
            LOGS.info(str(e))
        custompmblock = gvarstatus("pmblock") or None
        if custompmblock is not None:
            USER_BOT_WARN_ZERO = custompmblock.format(
                mention=mention,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
                totalwarns=totalwarns,
                warns=warns,
                remwarns=remwarns,
            )
        else:
            USER_BOT_WARN_ZERO = f"**⤶ لقـد حذرتـڪ مـسـبـقـاً مـن الـتـڪـرار 📵** \n**⤶ تـم حـظـرڪ تلقـائيـاً .. الان لا يـمـڪـنـڪ ازعـاجـي🔕**\n\n**⤶ تحيـاتـي** {my_mention}  🫡**"
        msg = await event.reply(USER_BOT_WARN_ZERO)
        await event.client(functions.contacts.BlockRequest(chat.id))
        the_message = f"#حمـايـة_الخـاص\
                            \n** ⎉╎المستخـدم** [{get_display_name(chat)}](tg://user?id={chat.id}) .\
                            \n** ⎉╎تم حظـره .. تلقائيـاً**\
                            \n** ⎉╎عـدد رسـائله :** {PM_WARNS[str(chat.id)]}"
        del PM_WARNS[str(chat.id)]
        sql.del_collection("pmwarns")
        sql.del_collection("pmmessagecache")
        sql.add_collection("pmwarns", PM_WARNS, {})
        sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
        try:
            return await event.client.send_message(
                BOTLOG_CHATID,
                the_message,
            )
        except BaseException:
            return
    custompmpermit = gvarstatus("pmpermit_txt") or None
    if custompmpermit is not None:
        USER_BOT_NO_WARN = custompmpermit.format(
            mention=mention,
            first=first,
            last=last,
            fullname=fullname,
            username=username,
            userid=userid,
            my_first=my_first,
            my_last=my_last,
            my_fullname=my_fullname,
            my_username=my_username,
            my_mention=my_mention,
            totalwarns=totalwarns,
            warns=warns,
            remwarns=remwarns,
        )
    elif gvarstatus("pmmenu") is None:
        USER_BOT_NO_WARN = f"""ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 **- الـرد التلقـائي 〽️**
**•─────────────────•**

❞ **مرحبـاً**  {mention} ❝

**⤶ قد اكـون مشغـول او غيـر موجـود حـاليـاً ؟!**
**⤶ ❨ لديـك** {warns} **مـن** {totalwarns} **تحذيـرات ⚠️❩**
**⤶ لا تقـم بـ إزعاجـي والا سـوف يتم حظـرك تلقـائياً . . .**

**⤶ فقط قل سبب مجيئك وانتظـر الـرد ⏳**"""
    else:
        USER_BOT_NO_WARN = f"""ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗭𝗧𝗛𝗢𝗡 **- الـرد التلقـائي 〽️**
**•─────────────────•**

❞ **مرحبـاً**  {mention} ❝

**⤶ قد اكـون مشغـول او غيـر موجـود حـاليـاً ؟!**
**⤶ ❨ لديـك** {warns} **مـن** {totalwarns} **تحذيـرات ⚠️❩**
**⤶ لا تقـم بـ إزعاجـي والا سـوف يتم حظـرك تلقـائياً . . .**

**⤶ فقط قل سبب مجيئك وانتظـر الـرد ⏳**"""
    addgvar("pmpermit_text", USER_BOT_NO_WARN)
    PM_WARNS[str(chat.id)] += 1
    try:
        if gvarstatus("pmmenu") is None:
            results = await event.client.inline_query(
                Config.TG_BOT_USERNAME, "pmpermit"
            )
            msg = await results[0].click(chat.id, reply_to=reply_to_id, hide_via=True)
        else:
            PM_PIC = gvarstatus("pmpermit_pic")
            if PM_PIC:
                CAT = [x for x in PM_PIC.split()]
                PIC = list(CAT)
                CAT_IMG = random.choice(PIC)
            else:
                CAT_IMG = None
            if CAT_IMG is not None:
                msg = await event.client.send_file(
                    chat.id,
                    CAT_IMG,
                    caption=USER_BOT_NO_WARN,
                    reply_to=reply_to_id,
                    force_document=False,
                )
            else:
                msg = await event.client.send_message(
                    chat.id, USER_BOT_NO_WARN, reply_to=reply_to_id
                )
    except Exception as e:
        LOGS.error(e)
        msg = await event.reply(USER_BOT_NO_WARN)
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    PMMESSAGE_CACHE[str(chat.id)] = msg.id
    sql.del_collection("pmwarns")
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmwarns", PM_WARNS, {})
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})


async def do_pm_options_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "**⤶ اخـتـر احـد الخـيـارات بــدون تـڪـرار ، وهـذا هــو تـحـذيـرڪ الاخـيـر 🚸**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = "**⤶ لقـد حـذرتــڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل ...📵**\n**⤶ تـم حـظـرڪ تلقـائيـاً 🚷** \n**⤶ الـى ان يـاتـي مـالـڪ الـحـسـاب 😕**"

    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حمـايـة_الخـاص\
                            \n** ⎉╎المستخـدم** [{get_display_name(chat)}](tg://user?id={chat.id}) .\
                            \n** ⎉╎تم حظـره .. تلقائيـاً**\
                            \n** ⎉╎السبب:** لم يختر أي من الخيارات المتاحـة واستمـر بتكـرار الرسـائـل ☹️😹."
    sqllist.rm_from_list("pmoptions", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


async def do_pm_enquire_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "**⤶ الرجـاء الانـتـظـار حتـى يتـم قراءة رسـائلـڪ.💌\n⤶ مـالـڪ الـحـسـاب سَــوف يـرد عـلـيـڪ عـنـد تفــرغـه ..\n⤶ نرجـو عـدم تـڪـرار الـرسـائـل لـتـجـنـب الـحـظـر 🚷**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = "**⤶ لقـد حـذرتــڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل ...📵**\n**⤶ تـم حـظـرڪ تلقـائيـاً 🚷** \n**⤶ الـى ان يـاتـي مـالـڪ الـحـسـاب 😕**"

    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حمـايـة_الخـاص\
                \n** ⎉╎المستخـدم** [{get_display_name(chat)}](tg://user?id={chat.id}) .\
                \n** ⎉╎تم حظـره .. تلقائيـاً**\
                \n** ⎉╎السـبب:** لقد اختار خيار الاستفسار ولكنه لم ينتظر بعد أن تم إخباره واستمر بتكـرار الرسـائل 🥲😹."
    sqllist.rm_from_list("pmenquire", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


async def do_pm_request_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "**⤶ الرجـاء الانـتـظـار حتـى يتـم قراءة رسـائلـڪ.💌\n⤶ مـالـڪ الـحـسـاب سَــوف يـرد عـلـيـڪ عـنـد تفــرغـه ..\n⤶ نرجـو عـدم تـڪـرار الـرسـائـل لـتـجـنـب الـحـظـر 🚷**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = "**⤶ لقـد حـذرتــڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل ...📵**\n**⤶ تـم حـظـرڪ تلقـائيـاً 🚷** \n**⤶ الـى ان يـاتـي مـالـڪ الـحـسـاب 😕**"

    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حمـايـة_الخـاص\
                \n** ⎉╎المستخـدم** [{get_display_name(chat)}](tg://user?id={chat.id}) .\
                \n** ⎉╎تم حظـره .. تلقائيـاً**\
                \n** ⎉╎السـبب:** لقد اختار خيار الطلب ولكنه لم ينتظر وتم حظره تلقائيـاً 🥲😹."
    sqllist.rm_from_list("pmrequest", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


async def do_pm_chat_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "**⤶ الرجـاء الانـتـظـار حتـى يتـم قراءة رسـائلـڪ.💌\n⤶ مـالـڪ الـحـسـاب سَــوف يـرد عـلـيـڪ عـنـد تفــرغـه ..\n⤶ نرجـو عـدم تـڪـرار الـرسـائـل لـتـجـنـب الـحـظـر 🚷**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = "**⤶ لقـد حـذرتــڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل ...📵**\n**⤶ تـم حـظـرڪ تلقـائيـاً 🚷** \n**⤶ الـى ان يـاتـي مـالـڪ الـحـسـاب 😕**"

    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حمـايـة_الخـاص\
                \n** ⎉╎المستخـدم** [{get_display_name(chat)}](tg://user?id={chat.id}) .\
                \n** ⎉╎تم حظـره .. تلقائيـاً**\
                \n** ⎉╎السـبب:** لقد اختار خيار الدردشـه مع المالك ولكنه لم ينتظر وتم حظره تلقائيـاً 🥲😹."
    sqllist.rm_from_list("pmchat", chat.id)
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


async def do_pm_spam_action(event, chat):
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    USER_BOT_WARN_ZERO = "**⤶ لقـد حـذرتــڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل ...📵**\n**⤶ تـم حـظـرڪ تلقـائيـاً 🚷** \n**⤶ الـى ان يـاتـي مـالـڪ الـحـسـاب 😕**"

    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"#حمـايـة_الخـاص\
                            \n** ⎉╎المستخـدم** [{get_display_name(chat)}](tg://user?id={chat.id}) .\
                            \n** ⎉╎تم حظـره .. تلقائيـاً**\
                            \n** ⎉╎السـبب:** لقد اختار خيار ازعاج المالك واستمر بتكرار الرسائل وتم حظره تلقائيـاً 🥲😹."
    sqllist.rm_from_list("pmspam", chat.id)
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    try:
        return await event.client.send_message(
            BOTLOG_CHATID,
            the_message,
        )
    except BaseException:
        return


@zedub.zed_cmd(incoming=True, func=lambda e: e.is_private, edited=False, forword=None)
async def on_new_private_message(event):
    if gvarstatus("pmpermit") is None:
        return
    chat = await event.get_chat()
    zel_dev = (5176749470, 5426390871)
    if chat.bot or chat.verified:
        return
    if pmpermit_sql.is_approved(chat.id):
        return
    if event.chat_id in zel_dev:
        reason = "**انـه احـد المطـورين المساعديـن 🥳♥️**"
        try:
            PM_WARNS = sql.get_collection("pmwarns").json
        except AttributeError:
            PM_WARNS = {}
        if not pmpermit_sql.is_approved(chat.id):
            if str(chat.id) in PM_WARNS:
                del PM_WARNS[str(chat.id)]
            start_date = str(datetime.now().strftime("%B %d, %Y"))
            pmpermit_sql.approve(
                chat.id, get_display_name(chat), start_date, chat.username, reason
            )
        return await event.client.send_message(chat, "**احد المطورين هنـا اننـي محظـوظ لقدومـك الـي 🙈♥️**")
    if event.chat_id == 925972505 or event.chat_id == 1895219306 or event.chat_id == 2095357462 or event.chat_id == 5280339206:
        reason = "**انـه مطـور السـورس 🥳♥️**"
        try:
            PM_WARNS = sql.get_collection("pmwarns").json
        except AttributeError:
            PM_WARNS = {}
        if not pmpermit_sql.is_approved(chat.id):
            if str(chat.id) in PM_WARNS:
                del PM_WARNS[str(chat.id)]
            start_date = str(datetime.now().strftime("%B %d, %Y"))
            pmpermit_sql.approve(
                chat.id, get_display_name(chat), start_date, chat.username, reason
            )
        return await event.client.send_message(chat, "**اطـلق هـلاو مطـوري الغـالي اننـي محظـوظ لقدومـك الـي 🙈♥️**")
    if chat.id in PMPERMIT_.TEMPAPPROVED:
        return
    if str(chat.id) in sqllist.get_collection_list("pmspam"):
        return await do_pm_spam_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmchat"):
        return await do_pm_chat_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmrequest"):
        return await do_pm_request_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmenquire"):
        return await do_pm_enquire_action(event, chat)
    if str(chat.id) in sqllist.get_collection_list("pmoptions"):
        return await do_pm_options_action(event, chat)
    await do_pm_permit_action(event, chat)


@zedub.zed_cmd(outgoing=True, func=lambda e: e.is_private, edited=False, forword=None)
async def you_dm_other(event):
    if gvarstatus("pmpermit") is None:
        return
    chat = await event.get_chat()
    if chat.bot or chat.verified:
        return
    if str(chat.id) in sqllist.get_collection_list("pmspam"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmchat"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmrequest"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmenquire"):
        return
    if str(chat.id) in sqllist.get_collection_list("pmoptions"):
        return
    if event.text and event.text.startswith(
        (
            f"{cmdhd}بلوك",
            f"{cmdhd}رفض",
            f"{cmdhd}قبول",
            f"{cmdhd}da",
            f"{cmdhd}سماح",
            f"{cmdhd}tempapprove",
            f"{cmdhd}tempa",
            f"{cmdhd}tapprove",
            f"{cmdhd}ta",
        )
    ):
        return
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    start_date = str(datetime.now().strftime("%B %d, %Y"))
    if not pmpermit_sql.is_approved(chat.id) and str(chat.id) not in PM_WARNS:
        pmpermit_sql.approve(
            chat.id, get_display_name(chat), start_date, chat.username, "اووبس . . لـم يتـم رفضـه"
        )
        try:
            PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
        except AttributeError:
            PMMESSAGE_CACHE = {}
        if str(chat.id) in PMMESSAGE_CACHE:
            try:
                await event.client.delete_messages(
                    chat.id, PMMESSAGE_CACHE[str(chat.id)]
                )
            except Exception as e:
                LOGS.info(str(e))
            del PMMESSAGE_CACHE[str(chat.id)]
        sql.del_collection("pmmessagecache")
        sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"show_pmpermit_options")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == event.client.uid:
        text = "⤶ عـذراً سيـدي ، هـذه الـخـيـارات لـلـمـسـتـخـدم الـذي يـراسـلـك 🤷🏻‍♂"
        return await event.answer(text, cache_time=0, alert=True)
    text = f"**⤶ حسنا عـزيزي بإمكانك اختيار احد الخيارات في الاسفل للتواصل مع :** {mention}.\n\n**⤶ اختر خيار واحد فقط لنعرف سبب قدومك الـى هنـا 🧐"
    buttons = [
        (Button.inline(text="⤶ لـ إسـتـفـسـار مـعـيـن", data="to_enquire_something"),),
        (Button.inline(text="⤶ لـ طـلـب مـعـيـن", data="to_request_something"),),
        (Button.inline(text="⤶ لـ الـدردشــه فـقـط", data="to_chat_with_my_master"),),
        (Button.inline(text="⤶ لـ إزعـاجـي فـقـط", data="to_spam_my_master_inbox"),),
    ]
    sqllist.add_to_list("pmoptions", event.query.user_id)
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    if str(event.query.user_id) in PM_WARNS:
        del PM_WARNS[str(event.query.user_id)]
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
    await event.edit(text, buttons=buttons)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"to_enquire_something")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == event.client.uid:
        text = "⤶ عـذراً سيـدي ، هـذه الـخـيـارات لـلـمـسـتـخـدم الـذي يـراسـلـك 🤷🏻‍♂"
        return await event.answer(text, cache_time=0, alert=True)
    text = "**⤶ حـسـنـاً عـزيـزي ، تـم أرسـال طـلـبـڪ بـنـجـاح 📨 . لا تـقـم بـ إخـتـيـار خـيـار آخــر .**\n**⤶ سيـتـم الـرد عـلـيـڪ عـنـد تـفـرغ الـمـالـڪ .🧸🤍**"
    sqllist.add_to_list("pmenquire", event.query.user_id)
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    if str(event.query.user_id) in PM_WARNS:
        del PM_WARNS[str(event.query.user_id)]
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
    sqllist.rm_from_list("pmoptions", event.query.user_id)
    await event.edit(text)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"to_request_something")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == event.client.uid:
        text = "⤶ عـذراً سيـدي ، هـذه الـخـيـارات لـلـمـسـتـخـدم الـذي يـراسـلـك 🤷🏻‍♂"
        return await event.answer(text, cache_time=0, alert=True)
    text = "**⤶ حـسـنـاً عـزيـزي .. قـمـت بـإبـلاغ مـالـڪ الـحـسـاب بـطلبـڪ**\n**⤶ عـنـدمـا يـڪـون مـالـڪ الـحـسـاب مـتـاحـاً سـوف يـقـوم بـالـرد عـلـيـڪ .. الرجـاء الإنـتـظـار ⏳**\n**⤶ لا تـڪـرر الـرسـائـل حـاليـاً لـ تـجـنـب الـحـظـر 🚷**"
    sqllist.add_to_list("pmrequest", event.query.user_id)
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    if str(event.query.user_id) in PM_WARNS:
        del PM_WARNS[str(event.query.user_id)]
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
    sqllist.rm_from_list("pmoptions", event.query.user_id)
    await event.edit(text)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"to_chat_with_my_master")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == event.client.uid:
        text = "⤶ عـذراً سيـدي ، هـذه الـخـيـارات لـلـمـسـتـخـدم الـذي يـراسـلـك 🤷🏻‍♂"
        return await event.answer(text, cache_time=0, alert=True)
    text = "**⤶ بـالـطـبـع عـزيـزي يـمـكـنـك الـتـحـدث مـع مـالـك الـحـسـاب لـكـن لـيـس الان 🤷🏻‍♂\n\n⤶ نـسـتـطـيـع الـتـكـلـم فـي وقـت آخـر حـالـيـاً أنـا مـشـغـول قـلـيـلاً  - عـنـد تـفـرغـي سـأكـلـمـك بالتـأكيــد .😇🤍**"
    sqllist.add_to_list("pmchat", event.query.user_id)
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    if str(event.query.user_id) in PM_WARNS:
        del PM_WARNS[str(event.query.user_id)]
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
    sqllist.rm_from_list("pmoptions", event.query.user_id)
    await event.edit(text)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"to_spam_my_master_inbox")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == event.client.uid:
        text = "⤶ عـذراً سيـدي ، هـذه الـخـيـارات لـلـمـسـتـخـدم الـذي يـراسـلـك 🤷🏻‍♂"
        return await event.answer(text, cache_time=0, alert=True)
    text = "`███████▄▄███████████▄\
         \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\
         \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\
         \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\
         \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\
         \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\
         \n▓▓▓▓▓▓███░░░░░░░░░░░░█\
         \n██████▀▀▀█░░░░██████▀ \
         \n░░░░░░░░░█░░░░█\
         \n░░░░░░░░░░█░░░█\
         \n░░░░░░░░░░░█░░█\
         \n░░░░░░░░░░░█░░█\
         \n░░░░░░░░░░░░▀▀`\
         \n**⤶ لسـت متفـرغـاً لـ تـراهـاتـك.\
         \n\n⤶ وهـذا هـو تحذيرك الأخيـر إذا قـمـت بإرسـال رسـالة أخـرى فـ سيتـم حـظـرك تلقـائـيًـا 🚷**"
    sqllist.add_to_list("pmspam", event.query.user_id)
    try:
        PM_WARNS = sql.get_collection("pmspam").json
    except AttributeError:
        PM_WARNS = {}
    if str(event.query.user_id) in PM_WARNS:
        del PM_WARNS[str(event.query.user_id)]
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
    sqllist.rm_from_list("pmoptions", event.query.user_id)
    await event.edit(text)


@zedub.zed_cmd(
    pattern="الحمايه (تفعيل|تعطيل)$",
    command=("الحمايه", plugin_category),
    info={
        "header": "لـ تفعيـل/تعطيـل حمـايـة الخـاص لـ حسـابـك",
        "الاسـتخـدام": "{tr}الحمايه تفعيل/تعطيل",
    },
)
async def pmpermit_on(event):
    "Turn on/off pmpermit."
    input_str = event.pattern_match.group(1)
    if input_str == "تفعيل":
        if gvarstatus("pmpermit") is None:
            addgvar("pmpermit", "true")
            await edit_delete(
                event, "**⎉╎تـم تفعيـل امـر حمايـه الخـاص .. بنجـاح 🔕☑️...**"
            )
        else:
            await edit_delete(event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُفعـل  🔐✅**")
    elif gvarstatus("pmpermit") is not None:
        delgvar("pmpermit")
        await edit_delete(
            event, "**⎉╎تـم تعطيـل أمـر حمايـة الخـاص .. بنجـاح 🔔☑️...**"
        )
    else:
        await edit_delete(event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُعطـل 🔓✅**")
    if input_str == "تعطيل":
        if gvarstatus("pmmenu") is None:
            addgvar("pmmenu", "false")
            await edit_delete(
                event,
                "**⎉╎تـم تعطيـل أمـر حمايـة الخـاص .. بنجـاح 🔔☑️...**",
            )
        else:
            await edit_delete(
                event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُعطـل 🔓✅**"
            )
    elif gvarstatus("pmmenu") is not None:
        delgvar("pmmenu")
        await edit_delete(
            event, "**⎉╎تـم تفعيـل امـر حمايـه الخـاص .. بنجـاح 🔕☑️...**"
        )
    else:
        await edit_delete(
            event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُفعـل  🔐✅**"
        )

@zedub.zed_cmd(
    pattern="الحماية (تفعيل|تعطيل)$",
    command=("الحماية", plugin_category),
    info={
        "header": "لـ تفعيـل/تعطيـل حمـايـة الخـاص لـ حسـابـك",
        "الاسـتخـدام": "{tr}الحماية تفعيل/تعطيل",
    },
)
async def pmpermit_on(event):
    "Turn on/off pmmenu."
    input_str = event.pattern_match.group(1)
    if input_str == "تفعيل":
        if gvarstatus("pmpermit") is None:
            addgvar("pmpermit", "true")
            await edit_delete(
                event, "**⎉╎تـم تفعيـل امـر حمايـه الخـاص .. بنجـاح 🔕☑️...**"
            )
        else:
            await edit_delete(event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُفعـل  🔐✅**")
    elif gvarstatus("pmpermit") is not None:
        delgvar("pmpermit")
        await edit_delete(
            event, "**⎉╎تـم تعطيـل أمـر حمايـة الخـاص .. بنجـاح 🔔☑️...**"
        )
    else:
        await edit_delete(event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُعطـل 🔓✅**")
    if input_str == "تعطيل":
        if gvarstatus("pmmenu") is None:
            addgvar("pmmenu", "false")
            await edit_delete(
                event,
                "**⎉╎تـم تعطيـل أمـر حمايـة الخـاص .. بنجـاح 🔔☑️...**",
            )
        else:
            await edit_delete(
                event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُعطـل 🔓✅**"
            )
    elif gvarstatus("pmmenu") is not None:
        delgvar("pmmenu")
        await edit_delete(
            event, "**⎉╎تـم تفعيـل امـر حمايـه الخـاص .. بنجـاح 🔕☑️...**"
        )
    else:
        await edit_delete(
            event, "** ⎉╎ امـر حمايـه الخـاص بالفعـل .. مُفعـل  🔐✅**"
        )


@zedub.zed_cmd(
    pattern="(قبول|سماح)(?:\s|$)([\s\S]*)",
    command=("سماح", plugin_category),
    info={
        "header": "لـ السمـاح لـ شخـص بمـراسلتـك خـاص اثنـاء تفعيـل الحمـايـه",
        "الاسـتخـدام": [
            "{tr}قبول/سماح + المعـرف/بالـرد + السـبب فـي الكـروب",
            "{tr}قبول/سماح + السـبب فـي الخـاص",
        ],
    },
)
async def approve_p_m(event):  # sourcery no-metrics
    "To approve user to pm"
    if gvarstatus("pmpermit") is None:
        return await edit_delete(
            event,
            f"** ⎉╎لـيشتغل هذا الأمـر ...**\n** ⎉╎ يـجب تفعيـل امـر الحـمايـه اولاً **\n** ⎉╎بإرسـال** `{cmdhd}الحمايه تفعيل`",
        )
    if event.is_private:
        user = await event.get_chat()
        reason = event.pattern_match.group(2)
    else:
        user, reason = await get_user_from_event(event, secondgroup=True)
        if not user:
            return
    if not reason:
        reason = "**⎉╎لـم يـذكـر 🤷🏻‍♂**"
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    if not pmpermit_sql.is_approved(user.id):
        if str(user.id) in PM_WARNS:
            del PM_WARNS[str(user.id)]
        start_date = str(datetime.now().strftime("%B %d, %Y"))
        pmpermit_sql.approve(
            user.id, get_display_name(user), start_date, user.username, reason
        )
        chat = user
        if str(chat.id) in sqllist.get_collection_list("pmspam"):
            sqllist.rm_from_list("pmspam", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmchat"):
            sqllist.rm_from_list("pmchat", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmrequest"):
            sqllist.rm_from_list("pmrequest", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmenquire"):
            sqllist.rm_from_list("pmenquire", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmoptions"):
            sqllist.rm_from_list("pmoptions", chat.id)
        await edit_delete(
            event,
            f"**⎉╎المستخـدم**  [{user.first_name}](tg://user?id={user.id})\n**⎉╎تـم السـمـاح لـه بـإرسـال الـرسـائـل 💬✓** \n **⎉╎ الـسـبـب ❔  :** {reason}",
        )
        try:
            PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
        except AttributeError:
            PMMESSAGE_CACHE = {}
        if str(user.id) in PMMESSAGE_CACHE:
            try:
                await event.client.delete_messages(
                    user.id, PMMESSAGE_CACHE[str(user.id)]
                )
            except Exception as e:
                LOGS.info(str(e))
            del PMMESSAGE_CACHE[str(user.id)]
        sql.del_collection("pmwarns")
        sql.del_collection("pmmessagecache")
        sql.add_collection("pmwarns", PM_WARNS, {})
        sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    else:
        await edit_delete(
            event,
            f"**⎉╎المستخـدم** [{user.first_name}](tg://user?id={user.id}) \n**⎉╎هـو بـالـفـعل فـي قـائـمـة الـسـمـاح ✅**",
        )


@zedub.zed_cmd(
    pattern="t(emp)?(a|approve)(?:\s|$)([\s\S]*)",
    command=("tapprove", plugin_category),
    info={
        "header": "To approve user to direct message you for temporarily.",
        "note": "Heroku restarts every 24 hours so with every restart it dissapproves every temp approved user",
        "الاسـتخـدام": [
            "{tr}ta/tapprove <username/reply reason> in group",
            "{tr}ta/tapprove <reason> in pm",
        ],
    },
)
async def tapprove_pm(event):  # sourcery no-metrics
    "Temporarily approve user to pm"
    if gvarstatus("pmpermit") is None:
        return await edit_delete(
            event,
            f"** ⎉╎لـيشتغل هذا الأمـر ...**\n** ⎉╎ يـجب تفعيـل امـر الحـمايـه اولاً **\n** ⎉╎بإرسـال** `{cmdhd}الحمايه تفعيل`",
        )
    if event.is_private:
        user = await event.get_chat()
        reason = event.pattern_match.group(3)
    else:
        user, reason = await get_user_from_event(event, thirdgroup=True)
        if not user:
            return
    if not reason:
        reason = "**⎉╎لـم يـذكـر 🤷🏻‍♂**"
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    if (user.id not in PMPERMIT_.TEMPAPPROVED) and (
        not pmpermit_sql.is_approved(user.id)
    ):
        if str(user.id) in PM_WARNS:
            del PM_WARNS[str(user.id)]
        PMPERMIT_.TEMPAPPROVED.append(user.id)
        chat = user
        if str(chat.id) in sqllist.get_collection_list("pmspam"):
            sqllist.rm_from_list("pmspam", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmchat"):
            sqllist.rm_from_list("pmchat", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmrequest"):
            sqllist.rm_from_list("pmrequest", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmenquire"):
            sqllist.rm_from_list("pmenquire", chat.id)
        if str(chat.id) in sqllist.get_collection_list("pmoptions"):
            sqllist.rm_from_list("pmoptions", chat.id)
        await edit_delete(
            event,
            f"**⎉╎المستخـدم**  [{user.first_name}](tg://user?id={user.id}) is __temporarily approved to pm__\n**Reason :** __{reason}__",
        )
        try:
            PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
        except AttributeError:
            PMMESSAGE_CACHE = {}
        if str(user.id) in PMMESSAGE_CACHE:
            try:
                await event.client.delete_messages(
                    user.id, PMMESSAGE_CACHE[str(user.id)]
                )
            except Exception as e:
                LOGS.info(str(e))
            del PMMESSAGE_CACHE[str(user.id)]
        sql.del_collection("pmwarns")
        sql.del_collection("pmmessagecache")
        sql.add_collection("pmwarns", PM_WARNS, {})
        sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    elif pmpermit_sql.is_approved(user.id):
        await edit_delete(
            event,
            f"**⎉╎المستخـدم**  [{user.first_name}](tg://user?id={user.id}) __is in approved list__",
        )
    else:
        await edit_delete(
            event,
            f"**⎉╎المستخـدم**  [{user.first_name}](tg://user?id={user.id}) __is already in temporary approved list__",
        )


@zedub.zed_cmd(
    pattern="(رف|رفض)(?:\s|$)([\s\S]*)",
    command=("رفض", plugin_category),
    info={
        "header": "لـ رفـض الاشخـاص مـن الخـاص اثنـاء تفعيـل الحمـايـه",
        "امـر مضـاف": {"الكل": "لـ رفـض الكـل"},
        "الاسـتخـدام": [
            "{tr}رف/رفض <المعـرف/بالـرد> فـي الكـروب",
            "{tr}رف/رفض فـي الخـاص",
            "{tr}رف/رفض الكل لـ رفـض الكـل",
        ],
    },
)
async def disapprove_p_m(event):
    "To disapprove user to direct message you."
    if gvarstatus("pmpermit") is None:
        return await edit_delete(
            event,
            f"** ⎉╎لـيشتغل هذا الأمـر ...**\n** ⎉╎ يـجب تفعيـل امـر الحـمايـه اولاً **\n** ⎉╎بإرسـال** `{cmdhd}الحمايه تفعيل`",
        )
    if event.is_private:
        user = await event.get_chat()
        reason = event.pattern_match.group(2)

    else:
        reason = event.pattern_match.group(2)
        if reason != "الكل":
            user, reason = await get_user_from_event(event, secondgroup=True)
            if not user:
                return
    if reason == "الكل":
        pmpermit_sql.disapprove_all()
        return await edit_delete(
            event, "**⎉╎حــسـنـا تــم رفـض الـجـمـيـع .. بنجـاح 💯**"
        )
    if not reason:
        reason = "**⎉╎ لـم يـذكـر 💭**"
    if pmpermit_sql.is_approved(user.id):
        pmpermit_sql.disapprove(user.id)
        await edit_or_reply(
            event,
            f"**⎉╎المستخـدم**  [{user.first_name}](tg://user?id={user.id})\n**⎉╎تـم رفـضـه مـن أرسـال الـرسـائـل ⚠️**\n**⎉╎ الـسـبـب ❔  :** {reason}",
        )
    elif user.id in PMPERMIT_.TEMPAPPROVED:
        PMPERMIT_.TEMPAPPROVED.remove(user.id)
        await edit_or_reply(
            event,
            f"**⎉╎المستخـدم**  [{user.first_name}](tg://user?id={user.id})\n**⎉╎تـم رفـضـه مـن أرسـال الـرسـائـل ⚠️**\n**⎉╎ الـسـبـب ❔  :** {reason}",
        )
    else:
        await edit_delete(
            event,
            f"**⎉╎المستخـدم**  [{user.first_name}](tg://user?id={user.id})\n **⎉╎لــم تـتـم الـمـوافـقـة عـلـيـه مـسـبـقـاً ❕ **",
        )


@zedub.zed_cmd(pattern="بلوك(?:\s|$)([\s\S]*)")
async def block_p_m(event):
    if event.is_private:
        user = await event.get_chat()
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
    if not reason:
        reason = "**⎉╎ لـم يـذكـر 💭**"
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(user.id) in PM_WARNS:
        del PM_WARNS[str(user.id)]
    if str(user.id) in PMMESSAGE_CACHE:
        try:
            await event.client.delete_messages(user.id, PMMESSAGE_CACHE[str(user.id)])
        except Exception as e:
            LOGS.info(str(e))
        del PMMESSAGE_CACHE[str(user.id)]
    if pmpermit_sql.is_approved(user.id):
        pmpermit_sql.disapprove(user.id)
    sql.del_collection("pmwarns")
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmwarns", PM_WARNS, {})
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    await event.client(functions.contacts.BlockRequest(user.id))
    await edit_or_reply(
        event,
        f"**- المسـتخـدم :**  [{user.first_name}](tg://user?id={user.id}) **تم حظـره بنجـاح .. لايمكنـه ازعـاجـك الان**\n\n**- السـبب :** {reason}",
    )


@zedub.zed_cmd(pattern="الغاء بلوك(?:\s|$)([\s\S]*)")
async def unblock_pm(event):
    if event.is_private:
        user = await event.get_chat()
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
    if not reason:
        reason = "**⎉╎ لـم يـذكـر 💭**"
    await event.client(functions.contacts.UnblockRequest(user.id))
    await edit_or_reply(
        event,
        f"**- المسـتخـدم :**  [{user.first_name}](tg://user?id={user.id}) **تم الغـاء حظـره بنجـاح .. يمكنـه التكلـم معـك الان**\n\n**- السـبب :** {reason}",
    )


@zedub.zed_cmd(pattern="المقبولين$")
async def approve_p_m(event):
    if gvarstatus("pmpermit") is None:
        return await edit_delete(
            event,
            f"** ⎉╎لـيشتغل هذا الأمـر ...**\n** ⎉╎ يـجب تفعيـل امـر الحـمايـه اولاً **\n** ⎉╎بإرسـال** `{cmdhd}الحمايه تفعيل`",
        )
    approved_users = pmpermit_sql.get_all_approved()
    APPROVED_PMs = "**- قائمـة المسمـوح لهـم ( المقبـوليـن ) :**\n\n"
    if len(approved_users) > 0:
        for user in approved_users:
            APPROVED_PMs += f"**• 👤 الاسـم :** {_format.mentionuser(user.first_name , user.user_id)}\n**- الايـدي :** `{user.user_id}`\n**- المعـرف :** @{user.username}\n**- التـاريخ : **__{user.date}__\n**- السـبب : **__{user.reason}__\n\n"
    else:
        APPROVED_PMs = "**- انت لـم توافـق على اي شخـص بعـد**"
    await edit_or_reply(
        event,
        APPROVED_PMs,
        file_name="قائمـة الحمايـة.txt",
        caption="**- ️قائمـة المسمـوح لهـم ( المقبوليـن )**\n\n**- سـورس زدثــون** 𝙕𝙏𝙝𝙤𝙣 ",
    )
