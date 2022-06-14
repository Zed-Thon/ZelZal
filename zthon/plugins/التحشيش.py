import os
import shutil
from asyncio import sleep
import random

from telethon import events

from zthon import zedub
from zthon.core.logger import logging
from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("**- بالـرد ع الشخـص او باضافـة معـرف / ايـدي الشخـص لـ الامـر**")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################

import random

from telethon import events


@zedub.zed_cmd(pattern="رابط الحذف")
async def _(zed):
    await edit_or_reply (zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝘿𝙀𝙇𝙀𝙏𝙀](t.me/ZedThon) 🗑♻️𓆪\n**𓍹━─━─━─━─𝙕𝞝𝘿─━─━─━─━𓍻**\n\n **✵│رابـط الحـذف ↬** https://telegram.org/deactivate \n\n\n **✵│بـوت الحـذف  ↬** @LC6BOT ")

########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################

@zedub.zed_cmd(pattern="رفع جلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n**✾╎تم رفعـه جلب 🐕‍🦺 في البـوت**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


@zedub.zed_cmd(pattern="رفع مرتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه مـࢪتك مـشي نخـلف 🤰🏻😹🤤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################

@zedub.zed_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه تـاج 👑🔥**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@zedub.zed_cmd(pattern="رفع بكلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه بڪلبك 🖤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


@zedub.zed_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم ** [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه بــ قلبـك .. نبـضك والوريـد 🖤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


@zedub.zed_cmd(pattern="رفع قلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم ** [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه بــ قلبـك .. نبـضك والوريـد 🖤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@zedub.zed_cmd(pattern="رفع جريذي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه جـࢪيذي ۿنـا 😹🐀** ",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@zedub.zed_cmd(pattern="رفع فرخ(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تم رفعه فرخ هنا 🖕😹**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@ZlZZl77)  ########################

mth = [
    "100% تحبك وتخاف عليك",
    "100% يحبج ويخاف عليج",
    "91% جـزء من قـلبه 💞",
    "81% تموت عليك ههاي ",
    "81% يموت عليج ههذا ",
    "40% واحد حيوان ومصلحه عوفه ",
    "50% شوف شعندك وياه ",
    "30% خاين نصحيا عوفيه ميفيدج ",
    "25% مصادق غيرج ويكلج احبج",
    "25% واحد كلب ابن كلب عوفه",
    "0% يكهرك ",
    "0% تكرهك ",
]

zid = [
    "100%",
    "99%",
    "98%",
    "97%",
    "96%",
    "95%",
    "90%",
    "89%",
    "88%",
    "87%",
    "86%",
    "85%",
    "80%",
    "79%",
    "78%",
    "77%",
    "76%",
    "75%",
    "70%",
    "69%",
    "68%",
    "67%",
    "66%",
    "65%",
    "60%",
    "59%",
    "58%",
    "57%",
    "56%",
    "55%",
    "50%",
    "48%",
    "47%",
    "46%",
    "45%",
    "40%",
    "39%",
    "38%",
    "37%",
    "36%",
    "35%",
    "30%",
    "29%",
    "28%",
    "27%",
    "25%",
    "20%",
    "19%",
    "18%",
    "17%",
    "16%",
    "15%",
    "10%",
    "9%",
    "8%",
    "7%",
    "6%",
    "5%",
    "4%",
    "3%",
    "2%",
    "1%",
    "0%",

]

@zedub.zed_cmd(pattern="(نسبه الحب|نسبة الحب)(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(mth)
    await edit_or_reply(mention, f"**✾╎نـسبـة حبكـم انـت و**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 😻♥️**")
@zedub.zed_cmd(pattern="(نسبه الانوثة|نسبة الانوثه|نسبه الانوثه|نسبة الانوثة)(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الانوثه لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤰**")
@zedub.zed_cmd(pattern="(نسبه الغباء|نسبة الغباء)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الغبـاء لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 😂💔**")
@zedub.zed_cmd(pattern="(نسبه الانحراف|نسبة الانحراف)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الانحـراف لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🥵🖤**")
@zedub.zed_cmd(pattern="(نسبه المثليه|نسبة المثليه)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة المثليـه لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤡 🏳️‍🌈.**")
@zedub.zed_cmd(pattern="(نسبه النجاح|نسبة النجاح)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة النجـاح لـ** [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤓.**") 
@zedub.zed_cmd(pattern="(نسبه الكراهية|نسبة الكراهيه|نسبه الكراهيه|نسبة الكراهية)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الكراهيـة لـ** [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤮.**")

@zedub.zed_cmd(pattern="رفع ورع(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه ورع القـروب .. بنجـاح😹🙇🏻.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مزه(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخـدم ه ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـها مـزة الكروب .. بنجـاح 🥳💃.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مطي(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مطي سبورتي 🐴.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حمار(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حمار جحا 😂🐴.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع خروف(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه خـروف 🐑.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع زباله(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه زباله معفنه 🗑.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع منشئ(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه منشئ الكروب 👷‍♂️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مدير(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مدير الكروب 🤵‍♂️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع كواد(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه كـواد .. بنجـاح 👀. ** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مرتبط(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـه مرتبـط .. بنجـاح 💍💞** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مرتبطه(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخـدم ه ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـهـا مرتبطـه .. بنجـاح 💍💞. .** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حبيبي(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حبيبـج .. بنجـاح 💍🤵‍♂👰🏻‍♀.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع خطيبتي(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user_id == 1346542270 or user_id == 1885375980 or user_id == 1721284724 or user_id == 1244786780 or user_id == 1951523146 or user_id == 1243462298 or user_id == 1037828349 or user_id == 1985711199 or user_id == 2028523456 or user_id == 2045039090 or user_id == 1961707816 or user_id == 1764272868 or user_id == 2067387667 or user_id == 294317157 or user_id == 2066568220 or user_id == 1403932655 or user_id == 1389046667 or user_id == 444672531 or user_id == 2055451976 or user_id == 294317157 or user_id == 2134101721 or user_id == 1719023510 or user_id == 1985225531 or user_id == 2107283646 or user_id == 2146086267:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد مطـورين السـورس  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخـدم ه ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـهـا خطيبتك .. بنجـاح 💍👰🏼‍♀️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع صاك(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه صاك 🤴 .** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@zedub.zed_cmd(pattern="رفع صاكه(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـها صاكه 👸🏼.** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حات(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه حـات الكـروب 🤴 .** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حاته(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـها حـاتـه الكـروب 👸🏼.** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")


