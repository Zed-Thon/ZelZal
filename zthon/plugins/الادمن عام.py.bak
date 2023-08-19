import asyncio
import contextlib
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "الادمن"

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

zel_dev = (5176749470, 5426390871)


@zedub.zed_cmd(
    pattern="ح عام(?:\s|$)([\s\S]*)",
    command=("gban", plugin_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "الـوصـف": "Will ban the person in every group where you are admin only.",
        "الاستخـدام": "{tr}gban <username/reply/userid> <reason (optional)>",
    },
)
async def zedgban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    zede = await edit_or_reply(event, "**╮ ❐... جـاࢪِ حـظـࢪ الشخـص عـام**")
    start = datetime.now()
    user, reason = await get_user_from_event(event, zede)
    if not user:
        return
    if user.id == zedub.uid:
        return await edit_delete(zede, "**⎉╎عـذراً ..لا استطيـع حظـࢪ نفسـي **")
    if user.id in zel_dev:
        return await edit_delete(zede, "**⎉╎عـذراً ..لا استطيـع حظـࢪ احـد المطـورين عـام **")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_delete(zede, "**⎉╎عـذراً ..لا استطيـع حظـࢪ مطـور السـورس عـام **")


    if gban_sql.is_gbanned(user.id):
        await zede.edit(
            f"**⎉╎المسـتخـدم ↠** [{user.first_name}](tg://user?id={user.id}) \n**⎉╎مـوجــود بالفعــل فـي ↠ قائمـة المحظــورين عــام**"
        )
    else:
        gban_sql.zedgban(user.id, reason)
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(zede, "**⎉╎عــذراً .. يجـب ان تكــون مشـرفـاً فـي مجموعـة واحـده ع الأقــل **")
    await zede.edit(
        f"**⎉╎جـاري بـدء حظـر ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎مـن ↠ {len(san)} كــروب**"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⎉╎عــذراً .. لـيس لـديــك صـلاحيـات فـي ↠**\n**⎉╎كــروب :** {get_display_name(achat)}(`{achat.id}`)",
            )
    end = datetime.now()
    zedtaken = (end - start).seconds
    if reason:
        await zede.edit(
            f"**⎉╎المستخـدم :** [{user.first_name}](tg://user?id={user.id})\n\n**⎉╎تم حـظـࢪه عـام مـن {count} كــࢪوب خـلال {zedtaken} ثـانيـه**\n**⎉╎السـبب :** {reason}"
        )
    else:
        await zede.edit(
            f"**╮ ❐... الشخـص :** [{user.first_name}](tg://user?id={user.id})\n\n**╮ ❐... تـم حـظـࢪه عـام مـن {count} كــࢪوب خـلال {zedtaken} ثـانيـه**"
        )
    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- الســبب :** `{reason}`\
                \n**- تـم حظـره مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {zedtaken} **ثــانيـه**",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- تـم حظـره مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {zedtaken} **ثــانيـه**",
            )
        with contextlib.suppress(BadRequestError):
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()


@zedub.zed_cmd(
    pattern="الغاء ح عام(?:\s|$)([\s\S]*)",
    command=("الغاء ح عام", plugin_category),
    info={
        "header": "To unban the person from every group where you are admin.",
        "الـوصـف": "will unban and also remove from your gbanned list.",
        "الاستخـدام": "{tr}ungban <username/reply/userid>",
    },
)
async def zedgban(event):
    "To unban the person from every group where you are admin."
    zede = await edit_or_reply(event, "**╮ ❐  جـاري الغــاء الحظـر العــام ❏╰**")
    start = datetime.now()
    user, reason = await get_user_from_event(event, zede)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        return await edit_delete(
            zede,
            f"**⎉╎المسـتخـدم ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎ليـس مـوجــود فـي ↠ قائمـة المحظــورين عــام**",
        )
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(zede, "**⎉╎عــذراً .. يجـب ان تكــون مشـرفـاً فـي مجموعـة واحـده ع الأقــل **")
    await zede.edit(
        f"**⎉╎جـاري الغــاء حظـر ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎مـن ↠ {len(san)} كــروب**"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⎉╎عــذراً .. لـيس لـديــك صـلاحيـات فـي ↠**\n**⎉╎كــروب :** {get_display_name(achat)}(`{achat.id}`)",
            )
    end = datetime.now()
    zedtaken = (end - start).seconds
    if reason:
        await zede.edit(
            f"**⎉╎المستخـدم :** [{user.first_name}](tg://user?id={user.id})\n\n**⎉╎تم الغــاء حـظـࢪه عـام مـن {count} كــࢪوب خـلال {zedtaken} ثـانيـه**\n**⎉╎السـبب :** {reason}"
        )
    else:
        await zede.edit(
            f"**⎉╎المستخـدم :** [{user.first_name}](tg://user?id={user.id})\n\n**⎉╎تم الغــاء حـظـࢪه عـام مـن {count} كــࢪوب خـلال {zedtaken} ثـانيـه**"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الغـــاء_الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- الســبب :** `{reason}`\
                \n**- تـم الغــاء حظـره مـن  {count} كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {zedtaken} **ثــانيـه**",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الغـــاء_الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- تـم الغــاء حظـره مـن  {count} كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {zedtaken} **ثــانيـه**",
            )


@zedub.zed_cmd(
    pattern="العام$",
    command=("العام", plugin_category),
    info={
        "header": "Shows you the list of all gbanned users by you.",
        "الاستخـدام": "{tr}listgban",
    },
)
async def gablist(event):
    "Shows you the list of all gbanned users by you."
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "- قائمـة المحظـورين عــام :\n\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"**⎉╎المستخـدم :**  [{a_user.chat_id}](tg://user?id={a_user.chat_id}) \n**⎉╎سـبب الحظـر : {a_user.reason} ** \n\n"
            else:
                GBANNED_LIST += (
                    f"**⎉╎المستخـدم :**  [{a_user.chat_id}](tg://user?id={a_user.chat_id}) \n**⎉╎سـبب الحظـر : لا يـوجـد ** \n\n"
                )
    else:
        GBANNED_LIST = "**- لايــوجـد محظــورين عــام بعــد**"
    await edit_or_reply(event, GBANNED_LIST)


@zedub.zed_cmd(
    pattern="ك عام(?:\s|$)([\s\S]*)",
    command=("ك عام", plugin_category),
    info={
        "header": "To mute a person in all groups where you are admin.",
        "الـوصـف": "It doesnt change user permissions but will delete all messages sent by him in the groups where you are admin including in private messages.",
        "الاستخـدام": "{tr}gmute username/reply> <reason (optional)>",
    },
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    if event.is_private:
        await event.edit("**- لا يمكنك استخـدام اوامـر العـام هنـا ؟!**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == zedub.uid:
            return await edit_or_reply(event, "**- عــذࢪاً .. لايمكــنك كتــم نفســك ؟!**")
        if user.id in zel_dev:
            return await edit_or_reply(event, "**- عــذࢪاً .. لايمكــنك كتــم احـد المطـورين عــام ؟!**")
        if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
            return await edit_or_reply(event, "**- عــذࢪاً .. لايمكــنك كتــم مطـور السـورس عــام ؟!**")
        userid = user.id
    try:
        user = await event.client.get_entity(userid)
    except Exception:
        return await edit_or_reply(event, "**- عــذࢪاً .. لايمكــنني العثــوࢪ علـى المسـتخــدم ؟!**")
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"**⎉╎المستخـدم**  {_format.mentionuser(user.first_name ,user.id)} \n**⎉╎مڪتوم سابقـاً**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**- خطـأ :**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}\n\n**⎉╎تم كتمــه عـام بنجــاح ✓**\n**⎉╎السـبب :** {reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}\n\n**⎉╎تم كتمــه عـام بنجــاح ✓**",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الكتــم_العـــام\n"
                f"**- الشخـص :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**- الســبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الكتــم_العـــام\n"
                f"**- الشخـص :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


@zedub.zed_cmd(
    pattern="الغاء ك عام(?:\s|$)([\s\S]*)",
    command=("الغاء ك عام", plugin_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "الـوصـف": "This will work only if you mute that person by your gmute command.",
        "الاستخـدام": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("**- لا يمكنك استخـدام اوامـر العـام هنـا ؟!**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == zedub.uid:
            return await edit_or_reply(event, "**- عــذࢪاً .. انت غيـر مكتـوم يامطــي ؟!**")
        userid = user.id
    try:
        user = await event.client.get_entity(userid)
    except Exception:
        return await edit_or_reply(event, "**- عــذࢪاً .. لايمكــنني العثــوࢪ علـى المسـتخــدم ؟!**")
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}\n\n**⎉╎غيـر مكتـوم عــام ✓**"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**- خطـأ :**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}\n\n**⎉╎تم الغـاء كتمــه مـن العــام بنجــاح ✓**\n**⎉╎السـبب :** {reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}\n\n**⎉╎تم الغـاء كتمــه مـن العــام بنجــاح ✓**",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغـــاء_الكتــم_العـــام\n"
                f"**- الشخـص :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**- الســبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغـــاء_الكتــم_العـــام\n"
                f"**- الشخـص :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


@zedub.zed_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


@zedub.zed_cmd(
    pattern="ط عام(?:\s|$)([\s\S]*)",
    command=("ط عام", plugin_category),
    info={
        "header": "kicks the person in all groups where you are admin.",
        "الاستخـدام": "{tr}gkick <username/reply/userid> <reason (optional)>",
    },
)
async def catgkick(event):  # sourcery no-metrics
    "kicks the person in all groups where you are admin"
    zede = await edit_or_reply(event, "**╮ ❐ ... جــاࢪِ طــرد الشخــص عــام ... ❏╰**")
    start = datetime.now()
    user, reason = await get_user_from_event(event, zede)
    if not user:
        return
    if user.id == zedub.uid:
        return await edit_delete(zede, "**╮ ❐ ... عــذراً لا استطــيع طــرد نفســي ... ❏╰**")
    if user.id in zel_dev:
        return await edit_delete(zede, "**╮ ❐ ... عــذࢪاً .. لا استطــيع طــرد المطـورين ... ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_delete(zede, "**╮ ❐ ... عــذࢪاً .. لا استطــيع طــرد مطـور السـورس ... ❏╰**")
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(zede, "**⎉╎عــذراً .. يجـب ان تكــون مشـرفـاً فـي مجموعـة واحـده ع الأقــل **")
    await zede.edit(
        f"**⎉╎بـدء طـرد ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎فـي ↠ {len(san)} كــروب**"
    )
    for i in range(sandy):
        try:
            await event.client.kick_participant(san[i], user.id)
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⎉╎عــذراً .. لـيس لـديــك صـلاحيـات فـي ↠**\n**⎉╎كــروب :** {get_display_name(achat)}(`{achat.id}`)",
            )
    end = datetime.now()
    zedtaken = (end - start).seconds
    if reason:
        await zede.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {zedtaken} seconds`!!\n**- الســبب :** `{reason}`"
        )
    else:
        await zede.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {zedtaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الطــࢪد_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- الســبب :** `{reason}`\
                \n**- تـم طــرده مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {zedtaken} **ثــانيـه**",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الطــࢪد_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- تـم طــرده مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {zedtaken} **ثــانيـه**",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)
