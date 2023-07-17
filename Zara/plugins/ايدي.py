# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

"""
ZThon - ZelZal
- كتـابـة الاضـافـات
زلــزال الـهيبــه - @zzzzl1l
- حقـوق زدثـــون @ZedThon
- تخمـط صيـر مطـور كفــوو واذكــر المصــدر لو اطشـك لـ النـاس
"""
import contextlib
import html
import os
import base64

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest

from Zara import zedub
from Zara.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from ..sql_helper.globals import gvarstatus
from . import spamwatch

plugin_category = "العروض"
LOGS = logging.getLogger(__name__)
#Code by T.me/zzzzl1l
zed_dev = (5176749470, 1895219306, 925972505, 5280339206, 5426390871)
zel_dev = (5176749470, 5426390871)
zelzal = (925972505, 1895219306, 5280339206)


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


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "لا يـوجـد بروفـايـل"
    dc_id = "Can't get dc id"
    with contextlib.suppress(AttributeError):
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    zilzal = (await event.client.get_entity(user_id)).premium
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("لا يـوجـد")
    user_bio = "لا يـوجـد" if not user_bio else user_bio
# Copyright (C) 2021 Zed-Thon . All Rights Reserved
# الـرتب الوهميـه & فارات الكليشـه & البريميـوم & عـدد الرسـائل & التفاعـل = كتـابـة الكـود - زلــزال الـهيبــه @zzzzl1l / خاصـه بسـورس - زدثــون @ZThon فقـط
    zmsg = await bot.get_messages(event.chat_id, 0, from_user=username) #Code by T.me/zzzzl1l
    zzz = zmsg.total
    if zzz < 100: #Code by T.me/zzzzl1l
        zelzzz = "غير متفاعل  🗿"
    elif zzz > 200 and zzz < 500:
        zelzzz = "ضعيف  🗿"
    elif zzz > 500 and zzz < 700:
        zelzzz = "شد حيلك  🏇"
    elif zzz > 700 and zzz < 1000:
        zelzzz = "ماشي الحال  🏄🏻‍♂"
    elif zzz > 1000 and zzz < 2000:
        zelzzz = "ملك التفاعل  🎖"
    elif zzz > 2000 and zzz < 3000:
        zelzzz = "امبراطور التفاعل  🥇"
    elif zzz > 3000 and zzz < 4000:
        zelzzz = "غنبله  💣"
    else:
        zelzzz = "نار وشرر  🏆"
################# Dev ZilZal #################
    if user_id in zelzal: #Code by T.me/zzzzl1l
        rotbat = "⌁ مطـور السـورس 𓄂𓆃 ⌁" 
    elif user_id in zel_dev:
        rotbat = "⌁ مطـور مسـاعـد 𐏕⌁" 
    elif user_id == (await event.client.get_me()).id and user_id not in zed_dev:
        rotbat = "⌁ مـالك الحساب 𓀫 ⌁" 
    else:
        rotbat = "⌁ العضـو 𓅫 ⌁"
################# Dev ZilZal #################
    ZED_TEXT = gvarstatus("CUSTOM_ALIVE_TEXT") or "•⎚• مـعلومـات المسـتخـدم مـن بـوت زدثــون"  #Code by T.me/zzzzl1l
    ZEDM = gvarstatus("CUSTOM_ALIVE_EMOJI") or "✦ " #Code by T.me/zzzzl1l
    ZEDF = gvarstatus("CUSTOM_ALIVE_FONT") or "⋆─┄─┄─┄─ ᶻᵗʰᵒᶰ ─┄─┄─┄─⋆" #Code by T.me/zzzzl1l
    caption = f"<b> {ZED_TEXT} </b>\n"
    caption += f"ٴ<b>{ZEDF}</b>\n"
    caption += f"<b>{ZEDM}الاسـم    ⇠ </b> "
    caption += f'<a href="tg://user?id={user_id}">{full_name}</a>'
    caption += f"\n<b>{ZEDM}المعـرف  ⇠  {username}</b>"
    caption += f"\n<b>{ZEDM}الايـدي   ⇠ </b> <code>{user_id}</code>\n"
    caption += f"<b>{ZEDM}الرتبـــه   ⇠ {rotbat} </b>\n" #Code by T.me/zzzzl1l
    if zilzal == True or user_id in zelzal: #Code by T.me/zzzzl1l
        caption += f"<b>{ZEDM}الحسـاب ⇠  بـريميـوم 🌟</b>\n"
    caption += f"<b>{ZEDM}الصـور    ⇠</b>  {replied_user_profile_photos_count}\n"
    caption += f"<b>{ZEDM}الرسائل   ⇠</b>  {zzz}  💌\n" #Code by T.me/zzzzl1l
    caption += f"<b>{ZEDM}التفاعل   ⇠</b>  {zelzzz}\n" #Code by T.me/zzzzl1l
    if user_id != (await event.client.get_me()).id: #Code by T.me/zzzzl1l
        caption += f"<b>{ZEDM}الـمجموعات المشتـركة ⇠  {common_chat}</b>\n"
    caption += f"<b>{ZEDM}البايـو     ⇠  {user_bio}</b>\n"
    caption += f"ٴ<b>{ZEDF}</b>"
    return photo, caption
# Copyright (C) 2021 Zed-Thon . All Rights Reserved


@zedub.zed_cmd(
    pattern="ايدي(?: |$)(.*)",
    command=("ايدي", plugin_category),
    info={
        "header": "لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ايدي بالـرد او {tr}ايدي + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    zed = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(zed, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await zed.delete()
    except TypeError:
        await zed.edit(caption, parse_mode="html")


@zedub.zed_cmd(
    pattern="ا(?: |$)(.*)",
    command=("ا", plugin_category),
    info={
        "header": "امـر مختصـر لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ا بالـرد او {tr}ا + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    zed = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(zed, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await zed.delete()
    except TypeError:
        await zed.edit(caption, parse_mode="html")


@zedub.zed_cmd(
    pattern="صورته(?:\s|$)([\s\S]*)",
    command=("صورته", plugin_category),
    info={
        "header": "لـ جـلب بـروفـايـلات الشخـص",
        "الاستـخـدام": [
            "{tr}صورته + عدد",
            "{tr}صورته الكل",
            "{tr}صورته",
        ],
    },
)
async def potocmd(event):
    "To get user or group profile pic"
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user and user.sender:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "الكل":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "**- رقـم خـاطـئ . . .**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "**- رقـم خـاطـئ . . .**")
            return
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()

