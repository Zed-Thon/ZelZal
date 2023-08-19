import contextlib

from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    InputChatPhotoEmpty,
    MessageMediaPhoto,
)
from telethon.utils import get_display_name

from zthon import zedub

from ..core.data import _sudousers_list
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper.mute_sql import is_muted, mute, unmute
from ..sql_helper.globals import gvarstatus
from . import BOTLOG, BOTLOG_CHATID

# =================== STRINGS ============
PP_TOO_SMOL = "**⪼ الصورة صغيرة جدا**"
PP_ERROR = "**⪼ فشل اثناء معالجة الصورة**"
NO_ADMIN = "**⪼ أحتـاج الى صلاحيـات المشـرف هنـا!! 𓆰**"
NO_PERM = "**⪼ ليست لدي صلاحيـات كافيـه في هـذه المجمـوعـة**"
CHAT_PP_CHANGED = "**⪼ تم تغييـر صـورة المجمـوعـة .. بنجـاح ✓**"
INVALID_MEDIA = "**⪼ ابعاد الصورة غير صالحة**"

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

LOGS = logging.getLogger(__name__)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
zel_dev = (5176749470, 5426390871)

plugin_category = "الادمن"


ADMZ = gvarstatus("Z_ADMIN") or "رفع مشرف"
UNADMZ = gvarstatus("Z_UNADMIN") or "تنزيل مشرف"
BANN = gvarstatus("Z_BAN") or "حظر"
UNBANN = gvarstatus("Z_UNBAN") or "الغاء حظر"
MUTE = gvarstatus("Z_MUTE") or "كتم"
UNMUTE = gvarstatus("Z_UNMUTE") or "الغاء كتم"
KICK = gvarstatus("Z_KICK") or "طرد"
# ================================================


@zedub.zed_cmd(
    pattern="الصورة (وضع|حذف)$",
    command=("الصورة", plugin_category),
    info={
        "header": "لـ وضـع صــوره لـ المجمـوعـه",
        "الوصــف": "بالــرد ع صــوره",
        "امـر مضـاف": {
            "وضع": "- لتغييـر صـورة المجمـوعـة",
            "حذف": "- لحـذف صـورة المجمـوعـة",
        },
        "الاسـتخـدام": [
            "{tr}الصورة وضع بالــرد ع صــوره",
            "{tr}الصورة حذف بالــرد ع صــوره",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def set_group_photo(event):  # sourcery no-metrics
    "لـ وضـع صــوره لـ المجمـوعـه"
    flag = (event.pattern_match.group(1)).strip()
    if flag == "وضع":
        replymsg = await event.get_reply_message()
        photo = None
        if replymsg and replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await event.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split("/"):
                photo = await event.client.download_file(replymsg.media.document)
            else:
                return await edit_delete(event, INVALID_MEDIA)
        if photo:
            try:
                await event.client(
                    EditPhotoRequest(
                        event.chat_id, await event.client.upload_file(photo)
                    )
                )
                await edit_delete(event, CHAT_PP_CHANGED)
            except PhotoCropSizeSmallError:
                return await edit_delete(event, PP_TOO_SMOL)
            except ImageProcessFailedError:
                return await edit_delete(event, PP_ERROR)
            except Exception as e:
                return await edit_delete(event, f"**- خطــأ : **`{str(e)}`")
            process = "تم تغييرهـا"
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
        except Exception as e:
            return await edit_delete(event, f"**- خطــأ : **`{e}`")
        process = "تم حذفهـا"
        await edit_delete(event, "**- صورة الدردشـه {process} . . بنجـاح ✓**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#صـورة_المجمـوعـة\n"
            f"صورة المجموعه {process} بنجاح ✓ "
            f"الدردشة: {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
        )


@zedub.zed_cmd(pattern=f"{ADMZ}(?:\s|$)([\s\S]*)")
async def promote(event):
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(event, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=False,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admin"
    if not user:
        return
    zzevent = await edit_or_reply(event, "**╮ ❐  جـارِ  ࢪفعـه مشـرف  . . .❏╰**")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await zzevent.edit(NO_PERM)
    await zzevent.edit(f"**⎉╎المستخـدم** [{user.first_name}](tg://user?id={user.id}) \n**⎉╎تم رفعـه مشـرفـاً .. بنجـاح✓**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#رفــع_مشــرف\
            \n**⎉╎الشخـص :** [{user.first_name}](tg://user?id={user.id})\
            \n**⎉╎المجمــوعــه :** {get_display_name(await event.get_chat())} (`{event.chat_id}`)",
        )



@zedub.zed_cmd(pattern="رفع مالك(?:\s|$)([\s\S]*)")
async def promote(event):
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(event, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admin"
    if not user:
        return
    zzevent = await edit_or_reply(event, "**╮ ❐  جـاري ࢪفعه مشـرف بكـل الصـلاحيـات  ❏╰**")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await zzevent.edit(NO_PERM)
    await zzevent.edit(f"**⎉╎المستخـدم** [{user.first_name}](tg://user?id={user.id}) \n**⎉╎تم رفعـه مشـرفـاً بكل الصلاحيـات ✓**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#رفــع_مشــرف\
            \n**⎉╎الشخـص :** [{user.first_name}](tg://user?id={user.id})\
            \n**⎉╎المجمــوعــه :** {get_display_name(await event.get_chat())} (`{event.chat_id}`)",
        )


@zedub.zed_cmd(pattern="اخفاء(?:\s|$)([\s\S]*)")
async def promote(event):
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(event, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
        anonymous=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admin"
    if not user:
        return
    zzevent = await edit_or_reply(event, "**╮ ❐  ا . . .  ❏╰**")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await zzevent.edit(NO_PERM)
    await zzevent.edit("**- ❝ ⌊   تم  . . .𓆰**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#رفــع_مشــرف\
            \n**⎉╎الشخـص :** [{user.first_name}](tg://user?id={user.id})\
            \n**⎉╎المجمــوعــه :** {get_display_name(await event.get_chat())} (`{event.chat_id}`)",
        )


@zedub.zed_cmd(pattern=f"{UNADMZ}(?:\s|$)([\s\S]*)")
async def demote(event):
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(event, NO_ADMIN)
        return
    user, _ = await get_user_from_event(event)
    if not user:
        return
    zzevent = await edit_or_reply(event, "↮")
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    rank = "مشرف"
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        return await zzevent.edit(NO_PERM)
    await zzevent.edit("**⎉╎المستخـدم** [{user.first_name}](tg://user?id={user.id}) \n**⎉╎تم تنـزيلـه مشـرف .. بنجـاح✓**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#تنـزيــل_مشــرف\
            \n**⎉╎الشخـص : ** [{user.first_name}](tg://user?id={user.id})\
            \n**⎉╎المجمــوعــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
        )


@zedub.zed_cmd(pattern=f"{BANN}(?:\s|$)([\s\S]*)")
async def _ban_person(event):
    user, reason = await get_user_from_event(event)
    if reason and reason == "عام":
        return await edit_delete(event, "**⪼ لـ الحظـر العـام ارسـل** `.ح عام`")
    if not user:
        return
    if user.id == event.client.uid:
        return await edit_delete(event, "**⪼ عـذراً ..لا استطيـع حظـࢪ نفسـي 𓆰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_delete(event, "**╮ ❐ دي لا يمڪنني حظـر مطـور السـورس  ❏╰**")
    if user.id in zel_dev:
        return await edit_delete(event, "**╮ ❐ دي لا يمڪنني حظـر احـد مسـاعدين السـورس  ❏╰**")
    zedevent = await edit_or_reply(event, "**╮ ❐... جـاࢪِ الحـظـࢪ ...❏╰**")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await zedevent.edit(NO_PERM)
    reply = await event.get_reply_message()
    if reason:
        await zedevent.edit(
            f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**⎉╎تم حظـࢪه بنجـاح ☑️**\n\n**⎉╎السـبب :** `{reason}`"
        )
    else:
        await zedevent.edit(
            f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**⎉╎تم حظــࢪه بنجـاح ☑️**\n\n"
        )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الحظــࢪ\
                \n**⎉╎المحظـور :** [{user.first_name}](tg://user?id={user.id})\
                \n**⎉╎الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)\
                \n**⎉╎السـبب :** {reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الحظــࢪ\
                \n**⎉╎المحظـور :** [{user.first_name}](tg://user?id={user.id})\
                \n**⎉╎الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )
        try:
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()
        except BadRequestError:
            return await zedevent.edit(
                "`I dont have message nuking rights! But still he is banned!`"
            )


@zedub.zed_cmd(pattern=f"{UNBANN}(?:\s|$)([\s\S]*)")
async def nothanos(event):
    user, _ = await get_user_from_event(event)
    if not user:
        return
    zedevent = await edit_or_reply(event, "**╮ ❐.. جـاري الغاء حـظࢪه ..❏╰**")
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await zedevent.edit(
            f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**⎉╎تم الغـاء حظــࢪه .. بنجــاح✓**"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الحظــࢪ\n"
                f"**⎉╎المستخـدم :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**⎉╎الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )
    except UserIdInvalidError:
        await zedevent.edit("`Uh oh my unban logic broke!`")
    except Exception as e:
        await zedevent.edit(f"**- خطــأ :**\n`{e}`")


@zedub.zed_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


@zedub.zed_cmd(pattern=f"{MUTE}(?:\s|$)([\s\S]*)")
async def startmute(event):
    KTM_IMG = gvarstatus("KTM_PIC") or "https://telegra.ph/file/fbfcda1b054056c9264bf.mp4"
    if event.is_private:
        input_str = event.pattern_match.group(1)
        if input_str == "عام":
            return await event.edit("**⪼ لـ الكتـم العـام ارسـل** `.ك عام`")
        replied_user = await event.client.get_entity(event.chat_id)
        if is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "**- ❝ ⌊هـذا المسـتخـدم مڪتـوم . . سـابقـاً 𓆰**"
            )
        if event.chat_id == zedub.uid:
            return await edit_delete(event, "**- لا تستطــع كتـم نفسـك**")
        if event.chat_id in zel_dev:
            return await edit_delete(event, "**╮ ❐ دي لا يمڪنني كتـم احـد مساعديـن السـورس  ❏╰**")
        if event.chat_id == 925972505 or event.chat_id == 1895219306 or event.chat_id == 2095357462:
            return await edit_delete(event, "**╮ ❐ دي . . لا يمڪنني كتـم مطـور السـورس  ❏╰**")
        try:
            mute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**- خطـأ **\n`{e}`")
        else:
            await event.edit("**⪼ تم ڪتـم الـمستخـدم  . . بنجـاح 🔕𓆰**")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتــم_الخــاص\n"
                f"**⎉╎الشخـص  :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_or_reply(
                event, "**⪼ أنـا لسـت مشـرف هنـا ؟!! 𓆰.**"
            )
        user, reason = await get_user_from_event(event)
        if reason and reason == "عام":
            return await edit_or_reply(event, "**⪼ لـ الكتـم العـام ارسـل** `.ك عام`")
        if not user:
            return
        if user.id == zedub.uid:
            return await edit_or_reply(event, "**- عــذراً .. لا استطيــع كتــم نفســي**")
        if user.id in zel_dev:
            return await edit_or_reply(event, "**╮ ❐ دي لا يمڪنني كتـم احـد مساعديـن السـورس  ❏╰**")
        if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
            return await edit_or_reply(event, "**╮ ❐ دي . . لا يمڪنني كتـم مطـور السـورس  ❏╰**")
        if is_muted(user.id, event.chat_id):
            return await edit_or_reply(
                event, "**عــذراً .. هـذا الشخـص مكتــوم سـابقــاً هنـا**"
            )
        result = await event.client.get_permissions(event.chat_id, user.id)
        try:
            if result.participant.banned_rights.send_messages:
                return await edit_or_reply(
                    event,
                    "**عــذراً .. هـذا الشخـص مكتــوم سـابقــاً هنـا**",
                )
        except AttributeError:
            pass
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        try:
            mute(user.id, event.chat_id)
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await edit_or_reply(
                        event,
                        "**- عــذراً .. ليـس لديـك صـلاحيـة حـذف الرسـائل هنـا**",
                    )
            elif "creator" not in vars(chat):
                return await edit_or_reply(
                    event, "**- عــذراً .. ليـس لديـك صـلاحيـة حـذف الرسـائل هنـا**"
                )
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        if reason:
            await event.client.send_file(
                event.chat_id,
                KTM_IMG,
                caption=f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**⎉╎تم كتمـه بنجـاح ☑️**\n\n**⎉╎السـبب :** {reason}",
            )
            await event.delete()
        else:
            await event.client.send_file(
                event.chat_id,
                KTM_IMG,
                caption=f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**⎉╎تم كتمـه بنجـاح ☑️**\n\n",
            )
            await event.delete()
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الكــتم\n"
                f"**⎉╎المكتـوم :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**⎉╎الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@zedub.zed_cmd(pattern=f"{UNMUTE}(?:\s|$)([\s\S]*)")
async def endmute(event):
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
        input_str = event.pattern_match.group(1)
        if input_str == "عام":
            return await event.edit("**⪼ لـ الغـاء الكتـم العـام ارسـل** `.الغاء ك عام`")
        if not is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "**عــذراً .. هـذا الشخـص غيــر مكتــوم هنـا**"
            )
        try:
            unmute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**- خطــأ **\n`{e}`")
        else:
            await event.edit(
                "**⎉╎تم الغــاء كتــم الشخـص هنـا .. بنجــاح ✓**"
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**⎉╎الشخـص :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        user, _ = await get_user_from_event(event)
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client.get_permissions(event.chat_id, user.id)
                if result.participant.banned_rights.send_messages:
                    await event.client(
                        EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                    )
        except AttributeError:
            return await edit_or_reply(
                event,
                "**⎉╎الشخـص غيـر مكـتـوم**",
            )
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        await edit_or_reply(
            event,
            f"**⎉╎المستخـدم :** {_format.mentionuser(user.first_name ,user.id)} \n**⎉╎تم الغـاء كتمـه بنجـاح ☑️**",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**⎉╎الشخـص :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**⎉╎الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


@zedub.zed_cmd(pattern=f"{KICK}(?:\s|$)([\s\S]*)")
async def kick(event):
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_delete(event, "**╮ ❐ دي لا يمڪنني طـرد احـد مساعديـن السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_delete(event, "**╮ ❐ دي . . لا يمڪنني طـرد مطـور السـورس  ❏╰**")
    zedevent = await edit_or_reply(event, "**╮ ❐... جـاࢪِ الطــࢪد ...❏╰**")
    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except Exception as e:
        return await zedevent.edit(f"{NO_PERM}\n{e}")
    if reason:
        await zedevent.edit(
            f"**⎉╎تم طــࢪد**. [{user.first_name}](tg://user?id={user.id})  **بنجــاح ✓**\n\n**⎉╎السـبب :** {reason}"
        )
    else:
        await zedevent.edit(f"**⎉╎تم طــࢪد**. [{user.first_name}](tg://user?id={user.id})  **بنجــاح ✓**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#الـطــࢪد\n"
            f"**⎉╎الشخـص**: [{user.first_name}](tg://user?id={user.id})\n"
            f"**⎉╎الدردشــه** : {get_display_name(await event.get_chat())}(`{event.chat_id}`)\n",
        )


@zedub.zed_cmd(
    pattern="تثبيت( بالاشعار|$)",
    command=("تثبيت", plugin_category),
    info={
        "header": "لـ تثبيـت الرسـائـل فـي الكــروب",
        "امـر مضـاف": {"لود": "To notify everyone without this.it will pin silently"},
        "الاسـتخـدام": [
            "{tr}تثبيت <بالــرد>",
            "{tr}تثبيت لود <بالــرد>",
        ],
    },
)
async def pin(event):
    "لـ تثبيـت الرسـائـل فـي الكــروب"
    to_pin = event.reply_to_msg_id
    if not to_pin:
        return await edit_delete(event, "**- بالــرد ع رسـالـه لـ تثبيتـهـا...**", 5)
    options = event.pattern_match.group(1)
    is_silent = bool(options)
    try:
        await event.client.pin_message(event.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{e}`", 5)
    await edit_delete(event, "**⎉╎تم تثبيـت الرسـالـه .. بنجــاح ✓**", 3)
    sudo_users = _sudousers_list()
    if event.sender_id in sudo_users:
        with contextlib.suppress(BadRequestError):
            await event.delete()
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#تثبيــت_رســالـه\
                \n**⎉╎تم تثبيــت رســالـه فـي المجمـوعـة**\
                \n**⎉╎الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)\
                \n**⎉╎الإشعـار :** {is_silent}",
        )


@zedub.zed_cmd(
    pattern="الغاء تثبيت( الكل|$)",
    command=("الغاء تثبيت", plugin_category),
    info={
        "header": "لـ الغــاء تثبيـت الرسـائـل فـي الكــروب",
        "امـر مضـاف": {"الكل": "لـ الغــاء تثبيـت كــل الرسـائـل فـي الكــروب"},
        "الاسـتخـدام": [
            "{tr}الغاء تثبيت <بالــرد>",
            "{tr}الغاء تثبيت الكل",
        ],
    },
)
async def unpin(event):
    "لـ الغــاء تثبيـت الرسـائـل فـي الكــروب"
    to_unpin = event.reply_to_msg_id
    options = (event.pattern_match.group(1)).strip()
    if not to_unpin and options != "الكل":
        return await edit_delete(
            event,
            "**- بالــرد ع رســالـه لـ الغــاء تثبيتـهــا او اسـتخـدم امـر .الغاء تثبيت الكل**",
            5,
        )
    try:
        if to_unpin and not options:
            await event.client.unpin_message(event.chat_id, to_unpin)
        elif options == "الكل":
            await event.client.unpin_message(event.chat_id)
        else:
            return await edit_delete(
                event, "**- بالــرد ع رســالـه لـ الغــاء تثبيتـهــا او اسـتخـدم امـر .الغاء تثبيت الكل**", 5
            )
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{e}`", 5)
    await edit_delete(event, "**⎉╎تم الغـاء تثبيـت الرسـالـه/الرسـائـل .. بنجــاح ✓**", 3)
    sudo_users = _sudousers_list()
    if event.sender_id in sudo_users:
        with contextlib.suppress(BadRequestError):
            await event.delete()
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الغــاء_تثبيــت_رســالـه\
                \n**⎉╎تم الغــاء تثبيــت رســالـه فـي الدردشــه**\
                \n**⎉╎الدردشــه** : {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
        )


@zedub.zed_cmd(
    pattern="الاحداث( م)?(?: |$)(\d*)?",
    command=("الاحداث", plugin_category),
    info={
        "header": "لـ جـلب آخـر الرسـائـل المحـذوفـه مـن الاحـداث بـ العـدد",
        "امـر مضـاف": {
            "م": "{tr}الاحداث م لجـلب رسـائل الميديـا المحذوفـة من الاحـداث"
        },
        "الاسـتخـدام": [
            "{tr}الاحداث <عدد>",
            "{tr}الاحداث م <عـدد>",
        ],
        "مثــال": [
            "{tr}الاحداث 7",
            "{tr}الاحداث م 7 لـ جـلب آخـر 7 رسـائل ميديـا من الاحـداث",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _iundlt(event):  # sourcery no-metrics
    "لـ جـلب آخـر الرسـائـل المحـذوفـه مـن الاحـداث بـ العـدد"
    zedevent = await edit_or_reply(event, "**- جـاري البحث عـن آخـر الاحداث انتظــر ...🔍**")
    flag = event.pattern_match.group(1)
    if event.pattern_match.group(2) != "":
        lim = int(event.pattern_match.group(2))
        lim = min(lim, 15)
        if lim <= 0:
            lim = 1
    else:
        lim = 5
    adminlog = await event.client.get_admin_log(
        event.chat_id, limit=lim, edit=False, delete=True
    )
    deleted_msg = f"**- اليـك آخـر {lim} رسـائـل محذوفــه لـ هـذا الكــروب 🗑 :**"
    if not flag:
        for msg in adminlog:
            ruser = await event.client.get_entity(msg.old.from_id)
            _media_type = await media_type(msg.old)
            if _media_type is None:
                deleted_msg += f"\n**🖇┊الرسـاله :** {msg.old.message} \n\n**🛂┊المرسـل** {_format.mentionuser(ruser.first_name ,ruser.id)}"
            else:
                deleted_msg += f"\n**🖇┊الميديـا :** {_media_type} \n\n**🛂┊المرسـل** {_format.mentionuser(ruser.first_name ,ruser.id)}"
        await edit_or_reply(zedevent, deleted_msg)
    else:
        main_msg = await edit_or_reply(zedevent, deleted_msg)
        for msg in adminlog:
            ruser = await event.client.get_entity(msg.old.from_id)
            _media_type = await media_type(msg.old)
            if _media_type is None:
                await main_msg.reply(
                    f"\n**🖇┊الرسـاله :** {msg.old.message} \n\n**🛂┊المرسـل** {_format.mentionuser(ruser.first_name ,ruser.id)}"
                )
            else:
                await main_msg.reply(
                    f"\n**🖇┊الرسـاله :** {msg.old.message} \n\n**🛂┊المرسـل** {_format.mentionuser(ruser.first_name ,ruser.id)}",
                    file=msg.old.media,
                )
