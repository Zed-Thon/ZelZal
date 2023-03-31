# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.

""" الوصـف : اوامـر حمـاية المجمـوعـات بالمسـح والطـرد والتقييـد
حقـوق : @ZedThon
@zzzzl1l - كتـابـة الملـف :  زلــزال الهيبــه"""


import contextlib
import base64
import asyncio
import io
import re
from asyncio import sleep
from datetime import datetime
from math import sqrt


from telethon.events import InlineQuery, callbackquery
from telethon import Button
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest


from telethon import events, functions, types
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.types import (
    ChatAdminRights,
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
    ChannelParticipantsKicked,
    ChatBannedRights,
    MessageActionChannelMigrateFrom,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)
from telethon.errors import (
    ChatAdminRequiredError,
    UserAdminInvalidError,
)
from zthon import zedub
from ..utils import is_admin
from ..sql_helper.locks_sql import get_locks, is_locked, update_lock
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id, _format
from ..sql_helper.fsub_sql import *

from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event
# All Rights Reserved for "Zed-Thon - ZelZal" "زلـزال الهيبـه"
ANTI_DDDD_ZEDTHON_MODE = ChatBannedRights(
    until_date=None, view_messages=None, send_media=True, send_stickers=True, send_gifs=True
)
from ..Config import Config


plugin_category = "الادمن"


async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        if sed.is_admin:
            is_mod = True
        else:
            is_mod = False
    except:
        is_mod = False
    return is_mod



@zedub.zed_cmd(
    pattern="الاعدادات$",
    command=("الاعدادات", plugin_category),
    info={
        "header": "لـ عـرض اعـدادات حمـاية المجمـوعـة الخـاصـه ببـوت زدثــون",
        "الاسـتخـدام": "{tr}الاعدادات",
    },
    groups_only=True,
)
async def _(event):
    if event.fwd_from:
        return
   # All Rights Reserved for "Zed-Thon - ZelZal" "زلـزال الهيبـه"
    res = ""
    current_zed_locks = get_locks(event.chat_id)
    if not current_zed_locks:
        res = "**⎉╎حـالة الحمـايه لـ هـذه المجمـوعـة :**"
    else:
        res = "**- فيمـا يلـي إعـدادات حمـاية المجمـوعـة :** \n"
        ubots = "❌" if current_zed_locks.bots else "✅"
        uegame = "❌" if current_zed_locks.egame else "✅"
        urtl = "❌" if current_zed_locks.rtl else "✅"
        uforward = "❌" if current_zed_locks.forward else "✅"
        ubutton = "❌" if current_zed_locks.button else "✅"
        uurl = "❌" if current_zed_locks.url else "✅"
        ugame = "❌" if current_zed_locks.game else "✅"
        ulocation = "❌" if current_zed_locks.location else "✅"
        ucontact = "❌" if current_zed_locks.contact else "✅"
        ubutton = "❌" if current_zed_locks.button else "✅"
        uinline = "❌" if current_zed_locks.inline else "✅"
        res += f"**⎉╎ البوتات :** {ubots}\n"
        res += f"**⎉╎ الدخول :** {ulocation}\n"
        res += f"**⎉╎ دخول الايران :** {uegame}\n"
        res += f"**⎉╎ الاضافه :** {ucontact}\n"
        res += f"**⎉╎ التوجيه :** {uforward}\n"
        res += f"**⎉╎ الميديا :** {ugame}\n"
        res += f"**⎉╎ المعرفات :** {ubutton}\n"
        res += f"**⎉╎ الفارسيه :** {uegame}\n"
        res += f"**⎉╎ الفشار :** {urtl}\n"
        res += f"**⎉╎ الروابط :** {uurl}\n"
        res += f"**⎉╎ الانلاين :** {uinline}\n"
    current_chat = await event.get_chat()
    with contextlib.suppress(AttributeError):
        chat_per = current_chat.default_banned_rights
    await edit_or_reply(event, res)

@zedub.zed_cmd(incoming=True, forword=None)
async def check_incoming_messages(event):
    if not event.is_group:
        return
    if event.is_group:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    zed_dev = (5289124437, 627658332, 5190136458, 1050898456, 1355571767)
    zelzal = event.sender_id
    malath = zedub.uid
    hhh = event.message.text
    zed_id = event.chat_id
    user = await event.get_sender()
    if is_locked(zed_id, "rtl") and ("خرا" in hhh or "كسها" in hhh or "كسمك" in hhh or "كسختك" in hhh or "عيري" in hhh or "كسخالتك" in hhh or "خرا بالله" in hhh or "عير بالله" in hhh or "كسخواتكم" in hhh or "اختك" in hhh or "بڪسسخخت" in hhh or "كحاب" in hhh or "مناويج" in hhh or "كحبه" in hhh or " كواد " in hhh or "كواده" in hhh or "تبياته" in hhh or "تبياتة" in hhh or "فرخ" in hhh or "كحبة" in hhh or "فروخ" in hhh or "طيز" in hhh or "آإيري" in hhh or "اختج" in hhh or "سالب" in hhh or "موجب" in hhh or "فحل" in hhh or "كسي" in hhh or "كسك" in hhh or "كسج" in hhh or "مكوم" in hhh or "نيج" in hhh or "نتنايج" in hhh or "مقاطع" in hhh or "ديوث" in hhh or "دياث" in hhh or "اديث" in hhh or "محارم" in hhh or "سكس" in hhh or "مصي" in hhh or "اعرب" in hhh or "أعرب" in hhh or "قحب" in hhh or "قحاب" in hhh or "عراب" in hhh or "مكود" in hhh or "عربك" in hhh or "مخنث" in hhh or "مخنوث" in hhh or "فتال" in hhh or "زاني" in hhh or "زنا" in hhh or "لقيط" in hhh or "بنات شوارع" in hhh or "بنت شوارع" in hhh or "نيك" in hhh or "منيوك" in hhh or "منيوج" in hhh or "نايك" in hhh or "قواد" in hhh or "زبي" in hhh or "ايري" in hhh or "ممحو" in hhh or "بنت شارع" in hhh or " است " in hhh or "اسات" in hhh or "زوب" in hhh or "عيير" in hhh or "املس" in hhh or "مربرب" in hhh or " خول " in hhh or "عرص" in hhh or "قواد" in hhh or "اهلاتك" in hhh or "جلخ" in hhh or "شرمو" in hhh or "فرك" in hhh or "رهط" in hhh):
        if zelzal == malath or await is_admin(event, zelzal) or zelzal in zed_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{user.first_name}](tg://user?id={user.id})  \n⌔╎**يُمنـع الفشـار والسب هنـا ⚠️•**", link_preview=False)
	        except Exception as e:
	            await event.reply(
	                "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(str(e))
	            )
	            update_lock(zed_id, "rtl", False)
    if is_locked(zed_id, "game") and event.message.media:
        if zelzal == malath or await is_admin(event, zelzal) or zelzal in zed_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{user.first_name}](tg://user?id={user.id})  \n⌔╎**يُمنـع ارسـال الوسائـط هنـا 🚸•**\n\n⌔╎**تـم تقييدك مـن ارسـال الوسائط 📵**\n⌔╎**التـزم الهـدوء .. تستطـيع ارسـال الرسـائل فقـط..**", link_preview=False)
	            await event.client(
	                EditBannedRequest(
	                    event.chat_id, event.sender_id, ANTI_DDDD_ZEDTHON_MODE
	                )
	            )
	        except Exception as e:
	            await event.reply(
	                "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(str(e))
	            )
	            update_lock(zed_id, "game", False)
    if is_locked(zed_id, "forward") and event.fwd_from:
        if zelzal == malath or await is_admin(event, zelzal) or zelzal in zed_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{user.first_name}](tg://user?id={user.id})  \n⌔╎**يُمنـع التوجيـه هنـا ⚠️•**", link_preview=False)
	        except Exception as e:
	            await event.reply(
	                "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(str(e))
	            )
	            update_lock(zed_id, "forward", False)
    if is_locked(zed_id, "button") and "@" in hhh:
        if zelzal == malath or await is_admin(event, zelzal) or zelzal in zed_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{user.first_name}](tg://user?id={user.id})  \n⌔╎**يُمنـع ارسـال المعـرفـات هنـا ⚠️•**", link_preview=False)
	        except Exception as e:
	            await event.reply(
	                "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(str(e))
	            )
	            update_lock(zed_id, "button", False)
    if is_locked(zed_id, "egame") and ("فارسى" in hhh or "خوببی" in hhh or "میخوام" in hhh or "کی" in hhh or "پی" in hhh or "گ" in hhh or "خسته" in hhh or "صكص" in hhh or "راحتی" in hhh or "بیام" in hhh or "بپوشم" in hhh or "گرمه" in hhh or "چ" in hhh or "چه" in hhh or "ڬ" in hhh or "ٺ" in hhh or "چ" in hhh or "ڿ" in hhh or "ڇ" in hhh or "ڀ" in hhh or "ڎ" in hhh or "ݫ" in hhh or "ژ" in hhh or "ڟ" in hhh or "۴" in hhh or "زدن" in hhh or "دخترا" in hhh or "كسى" in hhh or "مک" in hhh or "خالى" in hhh or "ݜ" in hhh or "ڸ" in hhh or "پ" in hhh or "بند" in hhh or "عزيزم" in hhh or "برادر" in hhh or "باشى" in hhh or "ميخوام" in hhh or "خوبى" in hhh or "ميدم" in hhh or "كى اومدى" in hhh or "خوابيدين" in hhh):
        if zelzal == malath or await is_admin(event, zelzal) or zelzal in zed_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{user.first_name}](tg://user?id={user.id})  \n⌔╎**يُمنـع التحـدث بالفارسيـه هنـا ⚠️•**", link_preview=False)
	        except Exception as e:
	            await event.reply(
	                "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(str(e))
	            )
	            update_lock(zed_id, "egame", False)
    if is_locked(zed_id, "url") and "http" in hhh:
        if zelzal == malath or await is_admin(event, zelzal) or zelzal in zed_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{user.first_name}](tg://user?id={user.id})  \n⌔╎**يُمنـع ارسـال الروابـط هنـا ⚠️•**", link_preview=False)
	        except Exception as e:
	            await event.reply(
	                "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(str(e))
	            )
	            update_lock(zed_id, "url", False)
    if is_locked(zed_id, "inline") and event.message.via_bot:
        if zelzal == malath or await is_admin(event, zelzal) or zelzal in zed_dev:
            return
        else:
	        try:
	            await event.delete()
	            await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{user.first_name}](tg://user?id={user.id})  \n⌔╎**يُمنـع استخـدام الانلايـن في هذه المجموعـة ⚠️•**", link_preview=False)
	        except Exception as e:
	            await event.reply(
	                "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(str(e))
	            )
	            update_lock(zed_id, "inline", False)



# Copyright (C) 2022 Zed-Thon
@zedub.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # All Rights Reserved for "Zed-Thon - ZelZal" "زلـزال الهيبـه"
    zed_dev = (5289124437, 627658332, 5190136458, 1050898456, 1355571767)
    malath = zedub.uid
    if not is_locked(event.chat_id, "contact"):
        return
    if event.user_added:
        zedy = await event.client.get_entity(event.user_id)
        zelzal_by = event.action_message.sender_id
        zed = await event.client.get_permissions(event.chat_id, zelzal_by)
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        added_users = event.action_message.action.users
        for user_id in added_users:
            user_obj = await event.client.get_entity(user_id)
            if event.user_added:
                is_ban_able = True
                if zelzal_by == malath or zed.is_admin or zelzal_by in zed_dev:
                    return
                else:
	                try:
	                    await event.client(
	                        functions.channels.EditBannedRequest(
	                            event.chat_id, user_obj, rights
	                        )
	                    )
	                    await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{zedy.first_name}](tg://user?id={zedy.id})  \n⌔╎**يُمنـع اضـافة الاعضـاء لـ هـذه المجموعـة ⚠️•**\n\n⌔╎**تـم حظـࢪ العضـو المضـاف .. بنجـاح ☑️**", link_preview=False)
	                except Exception as e:
	                    await event.reply(
	                        "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(
	                            str(e)
	                        )
	                    )
	                    update_lock(event.chat_id, "contact", False)
	                    break
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.client.send_message(BOTLOG_CHATID,
                "**⎉╎سيـدي المـالك**\n\n**⎉╎قـام هـذا** [الشخـص](tg://user?id={})  \n**⎉╎باضافـة اشخـاص للمجمـوعـة**\n**⎉╎تم تحذيـر الشخـص وطـرد الاعضـاء المضافيـن .. بنجـاح ✓𓆰**".format(
                    zelzal_by
                )
            )



# Copyright (C) 2022 Zed-Thon - كــود قفــل دخــول الايــران
@zedub.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # All Rights Reserved for "Zed-Thon - zthon" "زلـزال الهيبـه"
    zed_dev = (5289124437, 627658332, 5190136458, 1050898456, 1355571767)
    if not is_locked(event.chat_id, "egame"):
        return
    if event.user_joined: 
        a_user = await event.get_user()
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        zedy = await event.client.get_entity(event.user_id)
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        if event.user_joined and ("ژ" in first or "چ" in first or "۴" in first or "مهسا" in first or "sara" in first or "گ" in first or "نازنین" in first or "آسمان" in first or "ڄ" in first or "پ" in first or "Sanaz" in first or "𝓈𝒶𝓇𝒶" in first or "سارة" in first or "GIRL" in first or " Lady " in first or "فتاة" in first or "👅" in first or "سمانه" in first or "بهار" in first or "maryam" in first or "👙" in first or "هانیه" in first or "هستی" in first or "💋" in first or "ندا" in first or "Mina" in first or "خانم" in first or "ایناز" in first or "مبینا" in first or "امینی" in first or "سرنا" in first or "اندیشه" in first or "لنتكلم" in first or "دریا" in first or "زاده" in first or "نااز" in first or "ناز" in first or "بیتا" in first or "سكس" in first or "💄" in first or "اعرب" in first or "أعرب" in first or "قحب" in first or "قحاب" in first or "عراب" in first or "مكود" in first or "عربك" in first or "مخنث" in first or "مخنوث" in first or "فتال" in first or "زاني" in first or "زنا" in first or "لقيط" in first or "بنات شوارع" in first or "بنت شوارع" in first or "نيك" in first or "منيوك" in first or "منيوج" in first or "نايك" in first or "قواد" in first or "زبي" in first or "ايري" in first or "ممحو" in first or "بنت شارع" in first or " است " in first or "اسات" in first or "زوب" in first or "عيير" in first or "املس" in first or "مربرب" in first or " خول " in first or "عرص" in first or "قواد" in first or "اهلاتك" in first or "جلخ" in first or "شرمو" in first or "فرك" in first or "رهط" in first):
            is_ban_able = True
            if zedy.id in zed_dev:
                return
            else:
	            try:
	                await event.client(
	                        functions.channels.EditBannedRequest(
	                            event.chat_id, zedy.id, rights
	                        )
	                    )
	                await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً**  [{zedy.first_name}](tg://user?id={zedy.id})  \n⌔╎**يُمنـع انضمـام الايـࢪان هنـا 🚷•**\n\n⌔╎**تـم حظـࢪه .. بنجـاح ☑️**", link_preview=False)
	            except Exception as e:
	                await event.reply(
	                    "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(
	                        str(e)
	                    )
	                )
	                update_lock(event.chat_id, "egame", False)
	                return
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.client.send_message(BOTLOG_CHATID,
                "**⎉╎** [عـزيـزي](tg://user?id={}) **يمنـع دخـول الايـران لهـذه المجمـوعـة 𓆰•**".format(
                    zedy.id
                )
            )


# Copyright (C) 2022 Zed-Thon
@zedub.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # All Rights Reserved for "Zed-Thon - zthon" "زلـزال الهيبـه"
    zed_dev = (5289124437, 627658332, 5190136458, 1050898456, 1355571767)
    if not is_locked(event.chat_id, "location"):
        return
    if event.user_joined: 
        zedy = await event.client.get_entity(event.user_id)
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        if event.user_joined:
            is_ban_able = True
            if zedy.id in zed_dev:
                return
            else:
	            try:
	                await event.client(
	                        functions.channels.EditBannedRequest(
	                            event.chat_id, zedy.id, rights
	                        )
	                    )
	                await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/pp_g3)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{zedy.first_name}](tg://user?id={zedy.id})  \n⌔╎**يُمنـع الانضمـام لـ هـذه المجموعـة 🚷•**\n⌔╎**تـم حظـࢪه .. بنجـاح ☑️**", link_preview=False)
	            except Exception as e:
	                await event.reply(
	                    "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(
	                        str(e)
	                    )
	                )
	                update_lock(event.chat_id, "location", False)
	                return
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.client.send_message(BOTLOG_CHATID,
                "**⎉╎سيـدي المـالك**\n\n**⎉╎قـام هـذا** [الشخـص](tg://user?id={})  \n**⎉╎بالانضمـام للمجمـوعـة**\n**⎉╎تم تحذيـر الشخـص وطـرده .. بنجـاح ✓𓆰**".format(
                    zedy.id
                )
            )


# Copyright (C) 2022 Zed-Thon
@zedub.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # All Rights Reserved for "Zed-Thon - ZelZal" "زلـزال الهيبـه"
    zed_dev = (5289124437, 627658332, 5190136458, 1050898456, 1355571767)
    malath = zedub.uid
    if not is_locked(event.chat_id, "bots"):
        return
    # bots are limited Telegram accounts,
    # and cannot join by themselves
    if event.user_added:
        zedy = await event.client.get_entity(event.user_id)
        zelzal_by = event.action_message.sender_id
        zed = await event.client.get_permissions(event.chat_id, zelzal_by)
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        added_users = event.action_message.action.users
        for user_id in added_users:
            user_obj = await event.client.get_entity(user_id)
            if user_obj.bot:
                is_ban_able = True
                if zelzal_by == malath or zelzal_by in zed_dev:
                    return
                else:
	                try:
	                    await event.client(
	                        functions.channels.EditBannedRequest(
	                            event.chat_id, user_obj, rights
	                        )
	                    )
	                    await event.reply(f"[ᯓ 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉 - حمـاية المجموعـة ](t.me/source_av)\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n\n⌔╎**عـذࢪاً** [{zedy.first_name}](tg://user?id={zedy.id})  \n⌔╎**يُمنـع اضـافة البـوتـات لـ هـذه المجمـوعـة 🚫•**", link_preview=False)
	                except Exception as e:
	                    await event.reply(
	                        "**⎉╎عـذࢪاً  عـزيـزي .. لا املك صـلاحيات المشـرف هنـا 𓆰** \n`{}`".format(
	                            str(e)
	                        )
	                    )
	                    update_lock(event.chat_id, "bots", False)
	                    break
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.client.send_message(BOTLOG_CHATID,
                "**⎉╎سيـدي المـالك**\n\n**⎉╎قـام هـذا** [الشخـص](tg://user?id={})  \n**⎉╎باضـافة بـوت للمجمـوعـة**\n**⎉╎تم تحذيـر الشخـص وطـرد البـوت .. بنجـاح ✓𓆰**".format(
                    zelzal_by
                )
            )


# Copyright (C) 2022 Zed-Thon
@zedub.zed_cmd(pattern=f"البوتات ?(.*)")
async def zelzal(zed):
    con = zed.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**⎉╎مجمـوعتك/قناتـك في أمـان ✅.. لاتوجـد بوتـات في هذه المجمـوعـة ༗**"
    if con != "طرد":
        event = await edit_or_reply(zed, "**⎉╎جـاري البحـث عن بوتات في هـذه المجمـوعـة ...🝰**")
        async for user in zed.client.iter_participants(zed.chat_id):
            if user.bot:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"🛂**┊كشـف البـوتات -** 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉\
                           \n\n**⎉╎تم العثور على** **{del_u}**  **بـوت**\
                           \n**⎉╎لطـرد البوتات استخدم الامـر التالي ⩥** `.البوتات طرد`"
        await event.edit(del_status)
        return
    # All Rights Reserved for "Zed-Thon - ZelZal" "زلـزال الهيبـه"
    chat = await zed.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(zed, "**⎉╎عـذࢪاً .. احتـاج الى صلاحيـات المشـرف هنـا**", 5)
        return
    event = await edit_or_reply(zed, "**⎉╎جـارِ طـرد البوتـات من هنـا ...⅏**")
    del_u = 0
    del_a = 0
    async for user in zed.client.iter_participants(zed.chat_id):
        if user.bot:
            try:
                await zed.client.kick_participant(zed.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "**⎉╎اووبس .. ليس لدي صلاحيـات حظـر هنـا**", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"**⎉╎تم طـرد  {del_u}  بـوت .. بنجـاح🚮**"
    if del_a > 0:
        del_status = f"❇️**┊طـرد البـوتات -** 𝘾𝙍父𝙏𝞝𝙇𝞝𝙃𝙊𝙉\
                           \n\n**⎉╎تم طـرد  {del_u}  بـوت بنجـاح ✓** 🚮 \
                           \n**⎉╎لـم يتـم طـرد  {del_a}  بـوت لانـها اشـراف ..⅏** \
                           \n\n**⎉╎الان لـ الحفـاظ علـى كروبك/قناتك من التصفيـر ارسـل ⩥** `.قفل البوتات`"
    await edit_delete(event, del_status, 50)
    if BOTLOG:
        await zed.client.send_message(
            BOTLOG_CHATID,
            f"#طـرد_البوتـات\
            \n ⎉╎{del_status}\
            \n ⎉╎الدردشه: {zed.chat.title}(`{zed.chat_id}`)",
        )
