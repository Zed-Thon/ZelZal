"""
ZThon - ZelZal
"""

import html
import os
import base64

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest

from zthon import zedub
from zthon.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from . import spamwatch

plugin_category = "العروض"
LOGS = logging.getLogger(__name__)
ZED_TEXT = Config.CUSTOM_ALIVE_TEXT or "╮•⎚ مـعلومات الـشخص مـن بـوت زدثـون"
ZEDM = Config.CUSTOM_ALIVE_EMOJI or " •❃ "



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
    replied_user_profile_photos_count = "لاتوجد صوره بروفايل"
    dc_id = "Can't get dc id"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
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
    username = "@{}".format(username) if username else ("لايوجد معرف")
    user_bio = "لاتوجد نبذه" if not user_bio else user_bio
    rotbat = "「من مطـورين السورس 𓄂𓆃」" if user_id == 925972505 or user_id == 1895219306 or user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267 else (".「  العضـو 𓅫  」.") 
    rotbat = ".「 مـالك الحساب 𓀫 」." if user_id == (await event.client.get_me()).id and user_id != 925972505 and user_id != 1895219306 and user_id != 1346542270 and user_id != 1885375980 and user_id != 1721284724 and user_id != 1244786780 and user_id != 1951523146 and user_id != 1243462298 and user_id != 1037828349 and user_id != 1985711199 and user_id != 2028523456 and user_id != 2045039090 and user_id != 1961707816 and user_id != 1764272868 and user_id != 2067387667 and user_id != 294317157 and user_id != 2066568220 and user_id != 1403932655 and user_id != 1389046667 and user_id != 444672531 and user_id != 2055451976 and user_id != 294317157 and user_id != 2134101721 and user_id != 1719023510 and user_id != 1985225531 and user_id != 2107283646 and user_id != 2146086267 else rotbat
    caption = f"<b> {ZED_TEXT} </b>\n"
    caption += f"<b> ٴ•━─━─━─━─━─━─━─━─━• </b>\n"
    caption += f"<b> {ZEDM}| الاسـم    ⇦ </b> {full_name}\n"
    caption += f"<b> {ZEDM}| المعـرف  ⇦ </b> {username}\n"
    caption += f"<b> {ZEDM}| الايـدي   ⇦ </b> <code>{user_id}</code>\n"
    caption += f"<b> {ZEDM}| الرتبـــه  ⇦ {rotbat} </b>\n"
    caption += f"<b> {ZEDM}| الصـور   ⇦ </b> {replied_user_profile_photos_count}\n"
    caption += f"<b> {ZEDM}|الحسـاب ⇦ </b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    caption += f"\n<b> {ZEDM}| الـمجموعات المشتـركة ⇦ </b> {common_chat} \n"
    caption += f"<b> {ZEDM}| البايـو    ⇦ </b> {user_bio} \n"
    caption += f"<b> ٴ•━─━─━─━─━─━─━─━─━• </b>\n"
    caption += f"<b> 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 𓆪 </b> - @ZedThon "
    return photo, caption


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
    except AttributeError:
        return await edit_or_reply(zed, "**- لـم استطـع العثــور ع الشخــص**")
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
    except AttributeError:
        return await edit_or_reply(zed, "**- لـم استطـع العثــور ع الشخــص**")
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
    pattern="رابطه(?:\s|$)([\s\S]*)",
    command=("رابطه", plugin_category),
    info={
        "header": "لـ جـلب اسـم الشخـص بشكـل ماركـدون ⦇.رابطه بالـرد او + معـرف/ايـدي الشخص⦈ ",
        "الاسـتخـدام": "{tr}رابطه <username/userid/reply>",
    },
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"[{tag}](tg://user?id={user.id})")


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
                event, "**- لايـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
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
                return await edit_delete(event, "**- لايـوجـد هنـاك صـور لهـذا الشخـص ؟! **")
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
                event, "**- لايـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()

