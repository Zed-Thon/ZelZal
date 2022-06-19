from telethon import *

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

SPRD = gvarstatus("Z_POSC") or "(نشر_تلقائي|نشر|تلقائي)"
OFSPRD = gvarstatus("Z_OFPOSC") or "(ايقاف_النشر|الغاء_التلقائي|ستوب)"

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


@zedub.zed_cmd(pattern=f"{SPRD} ?(.*)")
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        zed = str(trz_).replace("-100", "")
    else:
        zed = trz_
    if not zed.isdigit():
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بوضـع ايـدي القنـاة اولاً**")
    if is_post(zed , event.chat_id):
        return await edit_or_reply(event, "**✾╎تم تفعيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    add_post(zed, event.chat_id)
    await edit_or_reply(event, f"**✾╎جـاري بدء النشـر التلقـائي من القنـاة ** `{trz_}`")


@zedub.zed_cmd(pattern=f"{OFSPRD} ?(.*)")
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        zed = str(trz_).replace("-100", "")
    else:
        zed = trz_
    if not zed.isdigit():
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بوضـع ايـدي القنـاة اولاً**")
    if not is_post(zed, event.chat_id):
        return await edit_or_reply(event, "**✾╎تم تعطيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    remove_post(zed, event.chat_id)
    await edit_or_reply(event, f"**✾╎تم ايقـاف النشـر التلقـائي من** `{trz_}`")


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

