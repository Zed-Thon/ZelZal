import asyncio
import base64
import io
import urllib.parse
import os
from pathlib import Path
import asyncio
from asyncio import sleep

from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError, ChatSendMediaForbiddenError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, name_dl, song_dl, video_dl, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import _zedutils, reply_id
from . import zedub

plugin_category = "البحث"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                                                             𝙕𝙏𝙝𝙤𝙣
# =========================================================== #
SONG_SEARCH_STRING = "<b>╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰</b>"
SONG_NOT_FOUND = "<b>⎉╎لـم استطـع ايجـاد المطلـوب .. جرب البحث باستخـدام الامـر (.اغنيه)</b>"
SONG_SENDING_STRING = "<b>╮ جـارِ تحميـل الاغنيـٓه... 🎧♥️╰</b>"
# =========================================================== #
#                                                             𝙕𝙏𝙝𝙤𝙣
# =========================================================== #

@zedub.zed_cmd(
    pattern="بحث(320)?(?:\s|$)([\s\S]*)",
    command=("بحث", plugin_category),
    info={
        "header": "لـ تحميـل الاغـانـي مـن يـوتيـوب",
        "امـر مضـاف": {
            "320": "لـ البحـث عـن الاغـانـي وتحميـلهـا بـدقـه عـاليـه 320k",
        },
        "الاسـتخـدام": "{tr}بحث + اسـم الاغنيـه",
        "مثــال": "{tr}بحث حسين الجسمي احبك",
    },
)
async def _(event):
    "لـ تحميـل الاغـانـي مـن يـوتيـوب"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "**⎉╎قم باضافـة الاغنيـه للامـر .. بحث + اسـم الاغنيـه**")
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    zedevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await zedevent.edit(
            f"⌔∮ عذرا لم استطع ايجاد مقاطع ذات صلة بـ `{query}`"
        )
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    try:
        stderr = (await _zedutils.runcmd(song_cmd))[1]
        await sleep(3)
        zedname, stderr = (await _zedutils.runcmd(name_cmd))[:2]
        if stderr:
            return await zedevent.edit(f"**خطأ :** `{stderr}`")
        await sleep(3)
        zedname = os.path.splitext(zedname)[0]
        await sleep(2)
        song_file = Path(f"{zedname}.mp3")
        zedname = urllib.parse.unquote(zedname)
    except:
        pass
    if not os.path.exists(song_file):
        return await zedevent.edit(
            f"**⎉╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    await zedevent.edit("**- جـارِ التحميـل انتظـر ▬▭...**")
    zedthumb = Path(f"{zedname}.jpg")
    if not os.path.exists(zedthumb):
        zedthumb = Path(f"{zedname}.webp")
    elif not os.path.exists(zedthumb):
        zedthumb = None
    title = zedname.replace("./temp/", "").replace("_", "|")
    try:
        await event.client.send_file(
            event.chat_id,
            song_file,
            force_document=False,
            caption=f"**⎉╎البحث :** `{title}`",
            thumb=zedthumb,
            supports_streaming=True,
            reply_to=reply_to_id,
        )
        await zedevent.delete()
        for files in (zedthumb, song_file):
            if files and os.path.exists(files):
                os.remove(files)
    except ChatSendMediaForbiddenError as err:
        await zedevent.edit("**- الوسائط مغلقـه هنـا ؟؟**")
        LOGS.error(str(err))


@zedub.zed_cmd(
    pattern="فيديو(?:\s|$)([\s\S]*)",
    command=("فيديو", plugin_category),
    info={
        "header": "لـ تحميـل مقـاطـع الفيـديـو مـن يـوتيـوب",
        "الاسـتخـدام": "{tr}فيديو + اسـم المقطـع",
        "مثــال": "{tr}فيديو حالات واتس",
    },
)
async def _(event):
    "لـ تحميـل مقـاطـع الفيـديـو مـن يـوتيـوب"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "**⎉╎قم باضافـة الاغنيـه للامـر .. فيديو + اسـم الفيديـو**")
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    zedevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الفيديـو... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await zedevent.edit(
            f"**⎉╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    try:
        stderr = (await _zedutils.runcmd(video_cmd))[1]
        # if stderr:
        # return await zedevent.edit(f"**Error :** `{stderr}`")
        zedname, stderr = (await _zedutils.runcmd(name_cmd))[:2]
        if stderr:
            return await zedevent.edit(f"**خطأ :** `{stderr}`")
        zedname = os.path.splitext(zedname)[0]
        vsong_file = Path(f"{zedname}.mp4")
    except:
        pass
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{zedname}.mkv")
    elif not os.path.exists(vsong_file):
        return await zedevent.edit(
            f"**⎉╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    await zedevent.edit("**- جـارِ التحميـل انتظـر ▬▭...**")
    zedthumb = Path(f"{zedname}.jpg")
    if not os.path.exists(zedthumb):
        zedthumb = Path(f"{zedname}.webp")
    elif not os.path.exists(zedthumb):
        zedthumb = None
    title = zedname.replace("./temp/", "").replace("_", "|")
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"**⎉╎البحث :** `{title}`",
        thumb=zedthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await zedevent.delete()
    for files in (zedthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)
