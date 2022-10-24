# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

""" الوصـف : تحـديث اوامـر النشـر التلقـائـي للقنـوات ™
الاوامـر صـارت تدعـم المعـرفـات والروابـط الى جانب ايديـات القنـوات
حقـوق : @ZedThon
@zzzzl1l - كتـابـة الملـف :  زلــزال الهيبــه"""


from telethon import *
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetParticipantRequest, GetFullChannelRequest
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest

from zthon import zedub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.autopost_sql import add_post, get_all_post, is_post, remove_post
from zthon.core.logger import logging
from ..sql_helper.globals import gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from . import *

plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

SPRS = gvarstatus("Z_SPRS") or "(نشر_تلقائي|نشر|تلقائي)"
OFSPRS = gvarstatus("Z_OFSPRS") or "(ايقاف_النشر|ايقاف النشر|ستوب)"

ZelzalNSH_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗭𝗧𝗵𝗼𝗻 - اوامـر النشـر التلقـائي](t.me/ZEDthon) 𓆪\n\n"
    "**- اضغـط ع الامـر للنسـخ** \n\n\n"
    "**⪼** `.تلقائي` \n"
    "**- الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد النشـر التلقـائي منهـا** \n"
    "**- استخـدم الامـر بقنـاتـك \n\n\n"
    "**⪼** `.ايقاف النشر` \n"
    "**- الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد ايقـاف النشـر التلقـائي منهـا** \n"
    "**- استخـدم الامـر بقنـاتـك \n\n\n"
    "**- ملاحظـه :**\n"
    "**- الاوامـر صـارت تدعـم المعـرفات والروابـط الى جـانب الايـدي 🏂🎗**\n"
    "**🛃 سيتـم اضـافة المزيـد من اوامــر النشـر التلقـائي بالتحديثـات الجـايه**\n"
)


async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern=f"{SPRS} ?(.*)")
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    zch = event.pattern_match.group(1)
    if not zch:
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بـ إضـافة معـرف/ايـدي القنـاة الى الامـر اولاً**")
    if zch.startswith("@"):
        zelzal = zch
    elif zch.startswith("https://t.me/"):
        zelzal = zch.replace("https://t.me/", "@")
    elif str(zch).startswith("-100"):
        zelzal = str(zch).replace("-100", "")
    else:
        try:
            zelzal = int(zch)
        except BaseException:
            return await edit_or_reply(event, "**✾╎عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    try:
        zilzal = (await event.client.get_entity(zelzal)).id
    except BaseException:
        return await event.reply("**✾╎عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    if is_post(str(zilzal) , event.chat_id):
        return await edit_or_reply(event, "**✾╎النشـر التلقـائي من القنـاة ** `{zch}` **مفعـل مسبقـاً ✓**")
    add_post(str(zilzal), event.chat_id)
    await edit_or_reply(event, f"**✾╎تم تفعيـل النشـر التلقـائي من القنـاة ** `{zch}` **بنجـاح ✓**")



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern=f"{OFSPRS} ?(.*)")
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    zch = event.pattern_match.group(1)
    if not zch:
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بـ إضـافة معـرف/ايـدي القنـاة الى الامـر اولاً**")
    if zch.startswith("@"):
        zelzal = zch
    elif zch.startswith("https://t.me/"):
        zelzal = zch.replace("https://t.me/", "@")
    elif str(zch).startswith("-100"):
        zelzal = str(zch).replace("-100", "")
    else:
        try:
            zelzal = int(zch)
        except BaseException:
            return await edit_or_reply(event, "**✾╎عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    try:
        zilzal = (await event.client.get_entity(zelzal)).id
    except BaseException:
        return await event.reply("**✾╎عـذراً .. معـرف/ايـدي القنـاة غيـر صـالح**\n**✾╎الرجـاء التـأكـد مـن المعـرف/الايـدي**")
    if not is_post(str(zilzal), event.chat_id):
        return await edit_or_reply(event, "**✾╎تم تعطيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    remove_post(str(zilzal), event.chat_id)
    await edit_or_reply(event, f"**✾╎تم ايقـاف النشـر التلقـائي من** `{zch}`")


@zedub.zed_cmd(incoming=True, forword=None)
async def _(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await zedub.send_message(int(chat), event.message)



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="النشر")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalNSH_cmd)

