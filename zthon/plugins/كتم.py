import base64
import asyncio
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "admin"

#=================== الكـــــــــــــــتم  ===================  #

@zedub.on(admin_cmd(pattern=f"كتم(?:\s|$)([\s\S]*)"))
async def mutezedub(event):
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
        if is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "**- هـذا المسـتخـدم مڪتـوم . . سـابقـاً **"
            )
        if event.chat_id == zedub.uid:
            return await edit_delete(event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**")
        if event.chat_id == 5190136458:
            return await edit_delete(event, "**  . . لا يمڪنني كتـم مبرمج السـورس  ╰**")
        if event.chat_id == 627658332:
            return await edit_delete(event, "**  . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        try:
            mute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**- خطـأ **\n`{e}`")
        else:
            await event.edit("** تم ڪتـم الـمستخـدم  . . بنجـاح 🔕✓**")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتــم_الخــاص\n"
                f"**- الشخـص  :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_or_reply(
                event, "** أنـا لسـت مشـرف هنـا ؟!! .**"
            )
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == zedub.uid:
            return await edit_or_reply(event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**")
        if user.id == 5190136458:
            return await edit_or_reply(event, "**  . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if user.id == 627658332:
            return await edit_or_reply(event, "**  . . لا يمڪنني كتـم مطـور السـورس  ╰**")
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
            await edit_or_reply(
                event,
                f"**- المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**- تـم كتمـه بنجـاح ✓**\n\n**- السـبب :** {reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"**- المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**- تـم كتمـه بنجـاح ✓**\n\n",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الكــتم\n"
                f"**الشخـص :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**الدردشـه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )

#=================== الغـــــــــــــاء الكـــــــــــــــتم  ===================  #

@zedub.on(admin_cmd(pattern=f"الغاء كتم(?:\s|$)([\s\S]*)"))
async def unmutezedub(event):
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
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
                "**- تـم الغــاء كتــم الشخـص هنـا .. بنجــاح ✓**"
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**- الشخـص :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
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
                "**- الشخـص غيـر مكـتـوم**",
            )
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        await edit_or_reply(
            event,
            f"**- المستخـدم :** {_format.mentionuser(user.first_name ,user.id)} \n**- تـم الغـاء كتمـه بنجـاح ✓**",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**- الشخـص :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**- الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )


# ===================================== # 

@zedub.zed_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "كتم_مؤقت"):
        await event.delete()

#=====================================  #
