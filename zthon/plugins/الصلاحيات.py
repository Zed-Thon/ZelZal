import base64

from telethon import events, functions, types
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import ChatBannedRights


from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper.locks_sql import get_locks, is_locked, update_lock
from ..utils import is_admin
from . import BOTLOG, get_user_from_event

plugin_category = "admin" 

# Copyright (C) 2021 joker TEAM
# FILES WRITTEN BY  @lMl10l

@zedub.zed_cmd(
    pattern="اقفل (.*)",
    command=("اقفل", plugin_category),
    info={
        "header": "To lock the given permission for entire group.",
        "description": "Db options will lock for admins also,",
        "api options": {
            "msg": "To lock messages",
            "media": "To lock media like videos/photo",
            "sticker": "To lock stickers",
            "gif": "To lock gif.",
            "preview": "To lock link previews.",
            "game": "To lock games",
            "inline": "To lock using inline bots",
            "poll": "To lock sending polls.",
            "invite": "To lock add users permission",
            "pin": "To lock pin permission for users",
            "info": "To lock changing group description",
            "all": "To lock above all options",
        },
        "db options": {
            "bots": "To lock adding bots by users",
            "commands": "To lock users using commands",
            "email": "To lock sending emails",
            "forward": "To lock forwording messages for group",
            "url": "To lock sending links to group",
        },
        "usage": "{tr}lock <permission>",
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):  # sourcery no-metrics
    "To lock the given permission for entire group."
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    if not event.is_group:
        return await edit_delete(event, "᯽︙ هذه ليست مجموعة لقفل بعض الصلاحيات")
    chat_per = (await event.get_chat()).default_banned_rights
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    if input_str in (("bots", "commands", "email", "forward", "url")):
        update_lock(peer_id, input_str, True)
        await edit_or_reply(event, "᯽︙ تـم قفل {} بنجـاح ✅".format(input_str))
    else:
        msg = chat_per.send_messages
        media = chat_per.send_media
        sticker = chat_per.send_stickers
        gif = chat_per.send_gifs
        gamee = chat_per.send_games
        ainline = chat_per.send_inline
        embed_link = chat_per.embed_links
        gpoll = chat_per.send_polls
        adduser = chat_per.invite_users
        cpin = chat_per.pin_messages
        changeinfo = chat_per.change_info
        if input_str == "الدردشه":
            if msg:
                return await edit_delete(
                    event, "᯽︙ المجموعه بالتأكيد مقفولة من الرسائل "
                )
            msg = True
            locktype = "الدردشه"
        elif input_str == "الوسائط":
            if media:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من الوسائط ⌁"
                )
            media = True
            locktype = "الوسائط"
        elif input_str == "الملصقات":
            if sticker:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من الملصقات ⌁"
                )
            sticker = True
            locktype = "الملصقات"
        elif input_str == "الروابط":
            if embed_link:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من الروابط ⌁"
                )
            embed_link = True
            locktype = "الروابط"
        elif input_str == "المتحركه":
            if gif:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من المتحركه ⌁"
                )
            gif = True
            locktype = "المتحركه"
        elif input_str == "الالعاب":
            if gamee:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من الالعاب ⌁"
                )
            gamee = True
            locktype = "الالعاب"
        elif input_str == "الانلاين":
            if ainline:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من الانلاين ⌁"
                )
            ainline = True
            locktype = "الانلاين"
        elif input_str == "التصويت":
            if gpoll:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من ارسال التصويت ⌁"
                )
            gpoll = True
            locktype = "التصويت"
        elif input_str == "الاضافة":
            if adduser:
                return await edit_delete(
                    event, "᯽︙ المجمـوعة بالتأكـيد مقفولة من اضافه الاعضاء ⌁"
                )
            adduser = True
            locktype = "الاضافة"
        elif input_str == "التثبيت":
            if cpin:
                return await edit_delete(
                    event,
                    "᯽︙ المجمـوعة بالتأكـيد مقفولة من تثبيت الرسائل ⌁",
                )
            cpin = True
            locktype = "التثبيت"
        elif input_str == "تغيير المعلومات":
            if changeinfo:
                return await edit_delete(
                    event,
                    "᯽︙ المجمـوعة بالتأكـيد مقفولة من تغيير معلومات الدردشه ⌁",
                )
            changeinfo = True
            locktype = "تغيير المعلومات"
        elif input_str == "الكل":
            msg = True
            media = True
            sticker = True
            gif = True
            gamee = True
            ainline = True
            embed_link = True
            gpoll = True
            adduser = True
            cpin = True
            changeinfo = True
            locktype = "الكل"
        else:
            if input_str:
                return await edit_delete(
                    event, f"᯽︙ هنالك خطأ في الامر : `{input_str}`", time=5
                )

            return await edit_or_reply(event, "᯽︙ لا استطيع قفل شيء")
        try:
            cat = Get(cat)
            await event.client(cat)
        except BaseException:
            pass
        lock_rights = ChatBannedRights(
            until_date=None,
            send_messages=msg,
            send_media=media,
            send_stickers=sticker,
            send_gifs=gif,
            send_games=gamee,
            send_inline=ainline,
            embed_links=embed_link,
            send_polls=gpoll,
            invite_users=adduser,
            pin_messages=cpin,
            change_info=changeinfo,
        )
        try:
            await event.client(
                EditChatDefaultBannedRightsRequest(
                    peer=peer_id, banned_rights=lock_rights
                )
            )
            await edit_or_reply(event, f"᯽︙ تـم قفـل  {locktype} بنجـاح ⌁ ")
        except BaseException as e:
            await edit_delete(
                event,
                f"`ليس لديك صلاحيات كافية ??`\n\n**خطأ:** `{str(e)}`",
                time=5,
            )


@zedub.zed_cmd(
    pattern="افتح (.*)",
    command=("افتح", plugin_category),
    info={
        "header": "To unlock the given permission for entire group.",
        "description": "Db options/api options will unlock only if they are locked.",
        "api options": {
            "msg": "To unlock messages",
            "media": "To unlock media like videos/photo",
            "sticker": "To unlock stickers",
            "gif": "To unlock gif.",
            "preview": "To unlock link previews.",
            "game": "To unlock games",
            "inline": "To unlock using inline bots",
            "poll": "To unlock sending polls.",
            "invite": "To unlock add users permission",
            "pin": "To unlock pin permission for users",
            "info": "To unlock changing group description",
            "all": "To unlock above all options",
        },
        "db options": {
            "bots": "To unlock adding bots by users",
            "commands": "To unlock users using commands",
            "email": "To unlock sending emails",
            "forward": "To unlock forwording messages for group",
            "url": "To unlock sending links to group",
        },
        "usage": "{tr}unlock <permission>",
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):  # sourcery no-metrics
    "To unlock the given permission for entire group."
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    if not event.is_group:
        return await edit_delete(event, "᯽︙ هذه ليست مجموعة قفل بعض الصلاحيات")
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    chat_per = (await event.get_chat()).default_banned_rights
    if input_str in (("bots", "commands", "email", "forward", "url")):
        update_lock(peer_id, input_str, False)
        await edit_or_reply(event, "᯽︙ تـم فتح {} بنجـاح ✅".format(input_str))
    else:
        msg = chat_per.send_messages
        media = chat_per.send_media
        sticker = chat_per.send_stickers
        gif = chat_per.send_gifs
        gamee = chat_per.send_games
        ainline = chat_per.send_inline
        gpoll = chat_per.send_polls
        embed_link = chat_per.embed_links
        adduser = chat_per.invite_users
        cpin = chat_per.pin_messages
        changeinfo = chat_per.change_info
        if input_str == "الدردشه":
            if not msg:
                return await edit_delete(
                    event, "᯽︙ الدردشه مفتوحه في هذه المجموعه ⌁"
                )
            msg = False
            locktype = "الدردشه"
        elif input_str == "الوسائط":
            if not media:
                return await edit_delete(
                    event, "᯽︙ ارسال الوسائط مسموح في هذه الدردشه"
                )
            media = False
            locktype = "الوسائط"
        elif input_str == "الملصقات":
            if not sticker:
                return await edit_delete(
                    event, "᯽︙ ارسال المصقات مسموح في هذه الدردشه ⌁"
                )
            sticker = False
            locktype = "الملصقات"
        elif input_str == "الروابط":
            if not embed_link:
                return await edit_delete(
                    event, "᯽︙ ارسال الروابط مسموح في هذه الدردشه ⌁"
                )
            embed_link = False
            locktype = "الروابط"
        elif input_str == "المتحركه":
            if not gif:
                return await edit_delete(
                    event, "᯽︙ ارسال المتحركه مسموح في هذه الدردشه ⌁"
                )
            gif = False
            locktype = "المتحركه"
        elif input_str == "الالعاب":
            if not gamee:
                return await edit_delete(
                    event, "᯽︙ ارسال الالعاب مسموح في هذه الدردشه ⌁"
                )
            gamee = False
            locktype = "الالعاب"
        elif input_str == "الانلاين":
            if not ainline:
                return await edit_delete(
                    event, "᯽︙ ارسال الانلاين مسموح في هذه الدردشه ⌁"
                )
            ainline = False
            locktype = "الانلاين"  # BY  @lMl10l  -  @UUNZZ
        elif input_str == "التصويت":  
            if not gpoll:
                return await edit_delete(
                    event, "᯽︙ ارسال التصويت مسموح في هذه الدردشه ⌁ "
                )
            gpoll = False
            locktype = "التصويت"
        elif input_str == "الاضافة":
            if not adduser:
                return await edit_delete(
                    event, "᯽︙ اضافة الاعضاء مسموح في هذه الدردشه ⌁"
                )
            adduser = False
            locktype = "الاضافة"
        elif input_str == "التثبيت":
            if not cpin:
                return await edit_delete(
                    event,
                    "᯽︙ تثبيت الرسائل مسموح في هذه الدردشه ⌁",
                )
            cpin = False
            locktype = "التثبيت"
        elif input_str == "تغيير المعلومات":
            if not changeinfo:
                return await edit_delete(
                    event,
                    "᯽︙ تغيير معلومات الدردشه مسموح في هذه الدردشه ⌁",
                )
            changeinfo = False
            locktype = "تغيير المعلومات"
        elif input_str == "الكل":
            msg = False
            media = False
            sticker = False
            gif = False
            gamee = False
            ainline = False
            gpoll = False
            embed_link = False
            adduser = False
            cpin = False
            changeinfo = False
            locktype = "الكل"
        else:
            if input_str:
                return await edit_delete(
                    event, f"᯽︙ خطأ في فتح الامر : `{input_str}`", time=5
                )

            return await edit_or_reply(event, "`لا يمكنني فتح اي شي !!`")
        try:
            cat = Get(cat)
            await event.client(cat)
        except BaseException:
            pass
        unlock_rights = ChatBannedRights(
            until_date=None,
            send_messages=msg,
            send_media=media,
            send_stickers=sticker,
            send_gifs=gif,
            send_games=gamee,
            send_inline=ainline,
            send_polls=gpoll,
            embed_links=embed_link,
            invite_users=adduser,
            pin_messages=cpin,
            change_info=changeinfo,
        )
        try:
            await event.client(
                EditChatDefaultBannedRightsRequest(
                    peer=peer_id, banned_rights=unlock_rights
                )
            )
            await edit_or_reply(event, f"᯽︙ تـم فتـح  {locktype} بنجاح ⌁ ")
        except BaseException as e:
            return await edit_delete(
                event,
                f"᯽︙ ليس لديك صلاحيات كافيه ??\n\n**خطأ:** `{str(e)}`",
                time=5,
            )

# BY  @lMl10l
@zedub.zed_cmd(
    pattern="الصلاحيات$",
    command=("الصلاحيات", plugin_category),
    info={
        "header": "To see the active locks in the current group",
        "usage": "{tr}locks",
    },
    groups_only=True,
)
async def _(event):  # sourcery no-metrics
    "To see the active locks in the current group"
    res = ""
    current_db_locks = get_locks(event.chat_id)
    if not current_db_locks:
        res = "لا توجد معلومات كافيه في هذه الدردشه"
    else:
        res = "᯽︙ ملـف الاوامر مقدم من سورس كرستين: \n"
        ubots = "✗" if current_db_locks.bots else "✔"
        ucommands = "✗" if current_db_locks.commands else "✔"
        uemail = "✗" if current_db_locks.email else "✔"
        uforward = "✗" if current_db_locks.forward else "✔"
        uurl = "✗" if current_db_locks.url else "✔"
        res += f" البـوتات ☣️: `{ubots}`\n"
        res += f" الاوامـر ⚒️ : `{ucommands}`\n"
        res += f" الايـميل 📬: {mail}`\n"
        res += f" التـحويل ➡️: `{uforward}`\n"
        res += f" الـرابط  🔗: `{uurl}`\n"
    current_chat = await event.get_chat()
    try:
        chat_per = current_chat.default_banned_rights
    except AttributeError as e:
        logger.info(str(e))
    else:
        umsg = "✗" if chat_per.send_messages else "✔"
        umedia = "✗" if chat_per.send_media else "✔"
        usticker = "✗" if chat_per.send_stickers else "✔"
        ugif = "✗" if chat_per.send_gifs else "✔"
        ugamee = "✗" if chat_per.send_games else "✔"
        uainline = "✗" if chat_per.send_inline else "✔"
        uembed_link = "✗" if chat_per.embed_links else "✔"
        ugpoll = "✗" if chat_per.send_polls else "✔"
        uadduser = "✗" if chat_per.invite_users else "✔"
        ucpin = "✗" if chat_per.pin_messages else "✔"
        uchangeinfo = "✗" if chat_per.change_info else "✔"
        res += "\n᯽︙ هذه الصلاحيات الموجوده في هذه الدردشه : \n\n"
        res += f" ᯽︙ ارسال الرسائل: `{umsg}`\n"
        res += f" ᯽︙ ارسال الوسائط: `{umedia}`\n"
        res += f" ᯽︙ ارسال الملصقات: `{usticker}`\n"
        res += f" ᯽︙ ارسال المتحركه: `{ugif}`\n"
        res += f" ᯽︙ ارسال الروابط: `{uembed_link}`\n"
        res += f" ᯽︙ ارسال الالعاب: `{ugamee}`\n"
        res += f" ᯽︙ ارسال الانلاين: `{uainline}`\n"
        res += f" ᯽︙ ارسال التصويت: `{ugpoll}`\n"
        res += f" ᯽︙ اضافه الاعضاء: `{uadduser}`\n"
        res += f" ᯽︙ تثبيت الرسائل: `{ucpin}`\n"
        res += f" ᯽︙ تغيير معلومات الدردشه: `{uchangeinfo}`\n"
    await edit_or_reply(event, res)
    await edit_or_reply(event, res)


@zedub.zed_cmd(
    pattern="قفل (.*)",
    command=("فتح", plugin_category),
    info={
        "header": "To lock the given permission for replied person only.",
        "api options": {
            "msg": "To lock messages",
            "media": "To lock media like videos/photo",
            "sticker": "To lock stickers",
            "gif": "To lock gif.",
            "preview": "To lock link previews.",
            "game": "To lock games",
            "inline": "To lock using inline bots",
            "poll": "To lock sending polls.",
            "invite": "To lock add users permission",
            "pin": "To lock pin permission for users",
            "info": "To lock changing group description",
            "all": "To lock all above permissions",
        },
        "usage": "{tr}plock <api option>",
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):  # sourcery no-metrics
    "To lock the given permission for replied person only."
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    chat_per = (await event.get_chat()).default_banned_rights
    result = await event.client(
        functions.channels.GetParticipantRequest(peer_id, reply.from_id)
    )
    admincheck = await is_admin(event.client, peer_id, reply.from_id)
    if admincheck:
        return await edit_delete(event, "`This user is admin you cant play with him`")
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "الدردشه":
        if msg:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من الرسائل .`"
            )
        if umsg:
            return await edit_delete(
                event, "`الدردشه مقفوله  لهذا الشخص.`"
            )
        umsg = True
        locktype = "الدردشه"
    elif input_str == "الوسائط":
        if media:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من الوسائط `"
            )
        if umedia:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من ارسال الوسائط`"
            )
        umedia = True
        locktype = "الوسائط"
    elif input_str == "الملصقات":
        if sticker:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من الملصقات `"
            )
        if usticker:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من ارسال الملصقات`"
            )
        usticker = True
        locktype = "الملصقات"
    elif input_str == "الروابط":
        if embed_link:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من الروابط `"
            )
        if uembed_link:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من ارسال الروابط`"
            )
        uembed_link = True
        locktype = "الروابط"
    elif input_str == "المتحركه":
        if gif:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من المتحركات `"
            )
        if ugif:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من ارسال المتحركه`"
            )
        ugif = True
        locktype = "المتحركه"
    elif input_str == "الالعاب":
        if gamee:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من الالعاب `"
            )
        if ugamee:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من ارسال الالعاب`"
            )
        ugamee = True
        locktype = "الالعاب"
    elif input_str == "الانلاين":
        if ainline:
            return await edit_delete(
                event, "᯽︙ المجموعه بالتأكيد مقفولة من الانلاين "
            )
        if uainline:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من ارسال الانلاين`"
            )
        uainline = True
        locktype = "الانلاين"
    elif input_str == "التصويت":
        if gpoll:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من التصويت `"
            )
        if ugpoll:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من ارسال تصويت`"
            )
        ugpoll = True
        locktype = "التصويت"
    elif input_str == "الاضافه":
        if adduser:
            return await edit_delete(
                event, "`᯽︙ المجموعه بالتأكيد مقفولة من الاضافه `"
            )
        if uadduser:
            return await edit_delete(
                event, "`᯽︙ العضو بالتأكيد مقيد من الاضافه`"
            )
        uadduser = True
        locktype = "الاضافه"
    elif input_str == "التثبيت":
        if cpin:
            return await edit_delete(
                event,
                "`᯽︙ المجموعه بالتأكيد مقفولة من تثبيت الرسايل `",
            )
        if ucpin:
            return await edit_delete(
                event,
                "`᯽︙ العضو بالتأكيد مقيد من تثبيت الرسايل`",
            )
        ucpin = True
        locktype = "التثبيت"
    elif input_str == "تغيير المعلومات":
        if changeinfo:
            return await edit_delete(
                event,
                "`᯽︙ المجموعه بالتأكيد مقفولة من تغيير المعلومات `",
            )
        if uchangeinfo:
            return await edit_delete(
                event,
                "`᯽︙ العضو بالتأكيد مقيد من تغيير المعلومات`",
            )
        uchangeinfo = True
        locktype = "تغيير المعلومات"
    elif input_str == "الكل":
        umsg = True
        umedia = True
        usticker = True
        ugif = True
        ugamee = True
        uainline = True
        uembed_link = True
        ugpoll = True
        uadduser = True
        ucpin = True
        uchangeinfo = True
        locktype = "الكل"
    else:
        if input_str:
            return await edit_delete(
                event, f"**Invalid lock type : `{input_str}`", time=5
            )

        return await edit_or_reply(event, "`I can't lock nothing !!`")
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await edit_or_reply(event, f"`قفل {locktype} لهذا المستخدم!`")
    except BaseException as e:
        await edit_delete(
            event,
            f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
            time=5,
        )


@zedub.zed_cmd(
    pattern="افتح (.*)",
    command=("افتح", plugin_category),
    info={
        "header": "To unlock the given permission for replied person only.",
        "note": "If entire group is locked with that permission then you cant unlock that permission only for him.",
        "api options": {
            "msg": "To unlock messages",
            "media": "To unlock media like videos/photo",
            "sticker": "To unlock stickers",
            "gif": "To unlock gif.",
            "preview": "To unlock link previews.",
            "game": "To unlock games",
            "inline": "To unlock using inline bots",
            "poll": "To unlock sending polls.",
            "invite": "To unlock add users permission",
            "pin": "To unlock pin permission for users",
            "info": "To unlock changing group description",
            "all": "To unlock all above permissions",
        },
        "usage": "{tr}punlock <api option>",
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):  # sourcery no-metrics
    "To unlock the given permission for replied person only."
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    chat_per = (await event.get_chat()).default_banned_rights
    result = await event.client(
        functions.channels.GetParticipantRequest(peer_id, reply.from_id)
    )
    admincheck = await is_admin(event.client, peer_id, reply.from_id)
    if admincheck:
        return await edit_delete(event, "`This user is admin you cant play with him`")
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "الدردشه":
        if msg:
            return await edit_delete(
                event, "`᯽︙ الدردشه مفتوحه في هذه المجموعه ⌁.`"
            )
        if not umsg:
            return await edit_delete(
                event, "`الدردشه مفتوحه  لهذا الشخص`"
            )
        umsg = False
        locktype = "الرسائل"
    elif input_str == "الوسائط":
        if media:
            return await edit_delete(event, "`᯽︙ الوسائط مفتوحه في هذه المجموعه `")
        if not umedia:
            return await edit_delete(
                event, "`الوسائط مفتوحه  لهذا الشخص`"
            )
        umedia = False
        locktype = "الوسائط"
    elif input_str == "الملصقات":
        if sticker:
            return await edit_delete(
                event, "`᯽︙ الملصقات مفتوحه في هذه المجموعه `"
            )
        if not usticker:
            return await edit_delete(
                event, "`الملصقات مفتوحه  لهذا الشخص`"
            )
        usticker = False
        locktype = "الملصقات"
    elif input_str == "الروابط":
        if embed_link:
            return await edit_delete(
                event, "`᯽︙ الروابط مفتوحه في هذه المجموعه `"
            )
        if not uembed_link:
            return await edit_delete(
                event, "`الروابط مفتوحه  لهذا الشخص`"
            )
        uembed_link = False
        locktype = "الروابط"
    elif input_str == "المتحركه":
        if gif:
            return await edit_delete(event, "`᯽︙ المتحركه مفتوحه في هذه المجموعه `")
        if not ugif:
            return await edit_delete(
                event, "`المتحركه مفتوحه  لهذا الشخص"
            )
        ugif = False
        locktype = "المتحركه"
    elif input_str == "الالعاب":
        if gamee:
            return await edit_delete(event, "`᯽︙ الالعاب مفتوحه في هذه المجموعه`")
        if not ugamee:
            return await edit_delete(
                event, "`الالعاب مفتوحه  لهذا الشخص`"
            )
        ugamee = False
        locktype = "الالعاب"
    elif input_str == "الانلاين":
        if ainline:
            return await edit_delete(
                event, "`᯽︙ الانلاين مفتوحه في هذه المجموعه `"
            )
        if not uainline:
            return await edit_delete(
                event, "`الانلاين مفتوح  لهذا الشخص`"
            )
        uainline = False
        locktype = "الانلاين"
    elif input_str == "التصويت":
        if gpoll:
            return await edit_delete(event, "`᯽︙ التصويت مفتوحه في هذه المجموعه ")
        if not ugpoll:
            return await edit_delete(
                event, "`التصويت مفتوح  لهذا الشخص`"
            )
        ugpoll = False
        locktype = "التصويت"
    elif input_str == "الاضافه":
        if adduser:
            return await edit_delete(
                event, "`᯽︙ الاضافه مفتوحه في هذه المجموعه `"
            )
        if not uadduser:
            return await edit_delete(
                event, "`الاضافه مفتوحه  لهذا الشخص`"
            )
        uadduser = False
        locktype = "الاضافة"
    elif input_str == "التثبيت":
        if cpin:
            return await edit_delete(
                event,
                "`᯽︙ التثبيت مفتوحه في هذه المجموعه `",
            )
        if not ucpin:
            return await edit_delete(
                event,
                "`التثبيت مفعل  لهذا الشخص`",
            )
        ucpin = False
        locktype = "التثبيت"
    elif input_str == "تغيير المعلومات":
        if changeinfo:
            return await edit_delete(
                event,
                "`᯽︙ تغيير معلومات مفتوحه في هذه المجموعه `",
            )
        if not uchangeinfo:
            return await edit_delete(
                event,
                "`᯽︙ تغيير معلومات مفتوحه  لهذا الشخص  `",
            )
        uchangeinfo = False
        locktype = "تغيير المعلومات"
    elif input_str == "الكل":
        if not msg:
            umsg = False
        if not media:
            umedia = False
        if not sticker:
            usticker = False
        if not gif:
            ugif = False
        if not gamee:
            ugamee = False
        if not ainline:
            uainline = False
        if not embed_link:
            uembed_link = False
        if not gpoll:
            ugpoll = False
        if not adduser:
            uadduser = False
        if not cpin:
            ucpin = False
        if not changeinfo:
            uchangeinfo = False
        locktype = "الكل"
    else:
        if input_str:
            return await edit_delete(
                event, f"**حدث خطا :** `{input_str}`", time=5
            )

        return await edit_or_reply(event, "`متقولي اعمل اي!!`")
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await edit_or_reply(event, f"`فتح {locktype} لهذا العضو !!`")
    except BaseException as e:
        await edit_delete(
            event,
            f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
            time=5,
        )


@zedub.zed_cmd(
    pattern="صلاحياته(?: |$)(.*)",
    command=("صلاحياته", plugin_category),
    info={
        "header": "To get permissions of replied user or mentioned user in that group.",
        "usage": "{tr}uperm <reply/username>",
    },
    groups_only=True,
)
async def _(event):  # sourcery no-metrics
    "To get permissions of user."
    peer_id = event.chat_id
    user, reason = await get_user_from_event(event)
    if not user:
        return
    admincheck = await is_admin(event.client, peer_id, user.id)
    result = await event.client(
        functions.channels.GetParticipantRequest(peer_id, user.id)
    )
    output = ""
    if admincheck:
        c_info = "✅" if result.participant.admin_rights.change_info else "❌"
        del_me = "✅" if result.participant.admin_rights.delete_messages else "❌"
        ban = "✅" if result.participant.admin_rights.ban_users else "❌"
        invite_u = "✅" if result.participant.admin_rights.invite_users else "❌"
        pin = "✅" if result.participant.admin_rights.pin_messages else "❌"
        add_a = "✅" if result.participant.admin_rights.add_admins else "❌"
        call = "✅" if result.participant.admin_rights.manage_call else "❌"
        output += f"**الصلاحيات العضو **{_format.mentionuser(user.first_name ,user.id)} **في {event.chat.title} المجموعه هي **\n"
        output += f"__تغيير المعلومات :__ {c_info}\n"
        output += f"__حذف الرسائل :__ {del_me}\n"
        output += f"__الحظر :__ {ban}\n"
        output += f"__الاضافه :__ {invite_u}\n"
        output += f"__التثبيت :__ {pin}\n"
        output += f"__اضافه مشرفين :__ {add_a}\n"
        output += f"__المكالمه :__ {call}\n"
    else:
        chat_per = (await event.get_chat()).default_banned_rights
        try:
            umsg = "❌" if result.participant.banned_rights.send_messages else "✅"
            umedia = "❌" if result.participant.banned_rights.send_media else "✅"
            usticker = "❌" if result.participant.banned_rights.send_stickers else "✅"
            ugif = "❌" if result.participant.banned_rights.send_gifs else "✅"
            ugamee = "❌" if result.participant.banned_rights.send_games else "✅"
            uainline = "❌" if result.participant.banned_rights.send_inline else "✅"
            uembed_link = "❌" if result.participant.banned_rights.embed_links else "✅"
            ugpoll = "❌" if result.participant.banned_rights.send_polls else "✅"
            uadduser = "❌" if result.participant.banned_rights.invite_users else "✅"
            ucpin = "❌" if result.participant.banned_rights.pin_messages else "✅"
            uchangeinfo = "❌" if result.participant.banned_rights.change_info else "✅"
        except AttributeError:
            umsg = "❌" if chat_per.send_messages else "✅"
            umedia = "❌" if chat_per.send_media else "✅"
            usticker = "❌" if chat_per.send_stickers else "✅"
            ugif = "❌" if chat_per.send_gifs else "✅"
            ugamee = "❌" if chat_per.send_games else "✅"
            uainline = "❌" if chat_per.send_inline else "✅"
            uembed_link = "❌" if chat_per.embed_links else "✅"
            ugpoll = "❌" if chat_per.send_polls else "✅"
            uadduser = "❌" if chat_per.invite_users else "✅"
            ucpin = "❌" if chat_per.pin_messages else "✅"
            uchangeinfo = "❌" if chat_per.change_info else "✅"
        output += f"{_format.mentionuser(user.first_name ,user.id)} **permissions in {event.chat.title} chat are **\n"
        output += f"__Send Messages :__ {umsg}\n"
        output += f"__Send Media :__ {umedia}\n"
        output += f"__Send Stickers :__ {usticker}\n"
        output += f"__Send Gifs :__ {ugif}\n"
        output += f"__Send Games :__ {ugamee}\n"
        output += f"__Send Inline bots :__ {uainline}\n"
        output += f"__Send Polls :__ {ugpoll}\n"
        output += f"__Embed links :__ {uembed_link}\n"
        output += f"__Add Users :__ {uadduser}\n"
        output += f"__Pin messages :__ {ucpin}\n"
        output += f"__Change Chat Info :__ {uchangeinfo}\n"
    await edit_or_reply(event, output)


@zedub.zed_cmd(incoming=True)
async def check_incoming_messages(event):  # sourcery no-metrics
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    peer_id = event.chat_id
    if is_locked(peer_id, "commands"):
        entities = event.message.entities
        is_command = False
        if entities:
            for entity in entities:
                if isinstance(entity, types.MessageEntityBotCommand):
                    is_command = True
        if is_command:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "I don't seem to have ADMIN permission here. \n`{}`".format(str(e))
                )
                update_lock(peer_id, "commands", False)
    if is_locked(peer_id, "forward") and event.fwd_from:
        try:
            await event.delete()
        except Exception as e:
            await event.reply(
                "I don't seem to have ADMIN permission here. \n`{}`".format(str(e))
            )
            update_lock(peer_id, "forward", False)
    if is_locked(peer_id, "email"):
        entities = event.message.entities
        is_email = False
        if entities:
            for entity in entities:
                if isinstance(entity, types.MessageEntityEmail):
                    is_email = True
        if is_email:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "I don't seem to have ADMIN permission here. \n`{}`".format(str(e))
                )
                update_lock(peer_id, "email", False)
    if is_locked(peer_id, "url"):
        entities = event.message.entities
        is_url = False
        if entities:
            for entity in entities:
                if isinstance(
                    entity, (types.MessageEntityTextUrl, types.MessageEntityUrl)
                ):
                    is_url = True
        if is_url:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "I don't seem to have ADMIN permission here. \n`{}`".format(str(e))
                )
                update_lock(peer_id, "url", False)


@zedub.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # check for "lock" "bots"
    if not is_locked(event.chat_id, "bots"):
        return
    # bots are limited Telegram accounts,
    # and cannot join by themselves
    if event.user_added:
        users_added_by = event.action_message.sender_id
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        added_users = event.action_message.action.users
        for user_id in added_users:
            user_obj = await event.client.get_entity(user_id)
            if user_obj.bot:
                is_ban_able = True
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(
                            event.chat_id, user_obj, rights
                        )
                    )
                except Exception as e:
                    await event.reply(
                        "I don't seem to have ADMIN permission here. \n`{}`".format(
                            str(e)
                        )
                    )
                    update_lock(event.chat_id, "bots", False)
                    break
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.reply(
                "!warn [user](tg://user?id={}) Please Do Not Add BOTs to this chat.".format(
                    users_added_by
                )
            )
#THIS FILE WRITTEN BY  @lMl10l
