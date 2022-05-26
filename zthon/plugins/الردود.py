# ported from paperplaneExtended by avinashreddy3108 for media support
import re

from telethon.utils import get_display_name

from zthon import zedub

from ..core.managers import edit_or_reply
from ..sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "العروض"


@zedub.zed_cmd(incoming=True)
async def filter_incoming_handler(event):  # sourcery no-metrics
    if event.sender_id == event.client.uid:
        return
    name = event.raw_text
    filters = get_filters(event.chat_id)
    if not filters:
        return
    a_user = await event.get_sender()
    chat = await event.get_chat()
    me = await event.client.get_me()
    title = get_display_name(await event.get_chat()) or "هـذه الدردشــه"
    participants = await event.client.get_participants(chat)
    count = len(participants)
    mention = f"[{a_user.first_name}](tg://user?id={a_user.id})"
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    first = a_user.first_name
    last = a_user.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{a_user.username}" if a_user.username else mention
    userid = a_user.id
    my_first = me.first_name
    my_last = me.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{me.username}" if me.username else my_mention
    for trigger in filters:
        pattern = f"( |^|[^\\w]){re.escape(trigger.keyword)}( |$|[^\\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            file_media = None
            filter_msg = None
            if trigger.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id)
                )
                file_media = msg_o.media
                filter_msg = msg_o.message
                link_preview = True
            elif trigger.reply:
                filter_msg = trigger.reply
                link_preview = False
            await event.reply(
                filter_msg.format(
                    mention=mention,
                    title=title,
                    count=count,
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
                ),
                file=file_media,
                link_preview=link_preview,
            )


@zedub.zed_cmd(
    pattern="رد (.*)",
    command=("رد", plugin_category),
    info={
        "header": "To save filter for the given keyword.",
        "description": "If any user sends that filter then your bot will reply.",
        "option": {
            "{mention}": "To mention the user",
            "{title}": "To get chat name in message",
            "{count}": "To get group members",
            "{first}": "To use user first name",
            "{last}": "To use user last name",
            "{fullname}": "To use user full name",
            "{userid}": "To use userid",
            "{username}": "To use user username",
            "{my_first}": "To use my first name",
            "{my_fullname}": "To use my full name",
            "{my_last}": "To use my last name",
            "{my_mention}": "To mention myself",
            "{my_username}": "To use my username.",
        },
        "usage": "{tr}filter <keyword>",
    },
)
async def add_new_filter(event):
    "To save the filter"
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الــردود\
            \n ⪼ ايدي الدردشه: {event.chat_id}\
            \n ⪼ الرد: {keyword}\
            \n ⪼ يتم حفظ الرسالة التالية كبيانات رد على المستخدمين في الدردشه ، يرجى عدم حذفها !!",
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                event,
                "**❈╎يتطلب رد ميديـا تعيين كـروب السجـل اولاً ..**\n**❈╎لاضافـة كـروب السجـل**\n**❈╎اتبـع الشـرح ⇚** https://t.me/zzzvrr/13",
            )
            return
    elif msg and msg.text and not string:
        string = msg.text
    elif not string:
        return await edit_or_reply(event, "__What should i do ?__")
    success = "**- ❝ الـرد ↫** {} **تـم {} لـ الميديـا بـ نجـاح 🎆☑️𓆰**"
    if add_filter(str(event.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(event, success.format(keyword, "اضافتـه"))
    remove_filter(str(event.chat_id), keyword)
    if add_filter(str(event.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(event, success.format(keyword, "تحديثـه"))
    await edit_or_reply(event, f"خطأ أثناء تعيين عامل التصفية لـ {keyword}")


@zedub.zed_cmd(
    pattern="الردود$",
    command=("الردود", plugin_category),
    info={
        "header": "To list all filters in that chat.",
        "description": "Lists all active (of your userbot) filters in a chat.",
        "usage": "{tr}filters",
    },
)
async def on_snip_list(event):
    "To list all filters in that chat."
    OUT_STR = "There are no filters in this chat."
    filters = get_filters(event.chat_id)
    for filt in filters:
        if OUT_STR == "** ❈╎لاتوجـد ردود في هـذه الدردشـه ༗**":
            OUT_STR = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑭𝑰𝑳𝑻𝑬𝑹𝑺 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**  ⪼ قائمـه الـردود في هذه الدردشـه :  **\n"
        OUT_STR += "⪼ {}  𓆰.\n".format(filt.keyword)
    await edit_or_reply(
        event,
        OUT_STR,
        caption="**⧗╎الـردود المضـافـه في هـذه الدردشـه هـي :**ش",
        file_name="filters.text",
    )


@zedub.zed_cmd(
    pattern="حذف رد ([\s\S]*)",
    command=("حذف رد", plugin_category),
    info={
        "header": "To delete that filter . so if user send that keyword bot will not reply",
        "usage": "{tr}stop <keyword>",
    },
)
async def remove_a_filter(event):
    "Stops the specified keyword."
    filt = event.pattern_match.group(1)
    if not remove_filter(event.chat_id, filt):
        await event.edit("**- ❝ الـرد ↫** {} **غيـر موجـود ⁉️**".format(filt))
    else:
        await event.edit("**- ❝ الـرد ↫** {} **تم حذفه بنجاح ☑️**".format(filt))


@zedub.zed_cmd(
    pattern="حذف الردود$",
    command=("حذف الردود", plugin_category),
    info={
        "header": "To delete all filters in that group.",
        "usage": "{tr}rmfilters",
    },
)
async def on_all_snip_delete(event):
    "To delete all filters in that group."
    filters = get_filters(event.chat_id)
    if filters:
        remove_all_filters(event.chat_id)
        await edit_or_reply(event, "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑭𝑰𝑳𝑻𝑬𝑹𝑺 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ تم حذف جـميع الــردود المضـافـهہ بنجـاح☑️**")
    else:
        await edit_or_reply(event, "**❈╎عـذراً .. لا توجـد ردود في هـذه المجموعـه**")
