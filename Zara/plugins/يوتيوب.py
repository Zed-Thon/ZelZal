import asyncio
import glob
import io
import os
import re
import pathlib
from time import time
import requests

try:
    from pyquery import PyQuery as pq
except ModuleNotFoundError:
    os.system("pip3 install pyquery")
    from pyquery import PyQuery as pq


from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import types
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.utils import get_attributes
from urlextract import URLExtract
from wget import download
from yt_dlp import YoutubeDL
from yt_dlp.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from ..Config import Config
from ..core import pool
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import progress, reply_id
from ..helpers.functions import delete_conv
from ..helpers.functions.utube import _mp3Dl, get_yt_video_id, get_ytthumb, ytsearch
from ..helpers.utils import _format
from . import BOTLOG, BOTLOG_CHATID, zedub

BASE_YT_URL = "https://www.youtube.com/watch?v="
extractor = URLExtract()
LOGS = logging.getLogger(__name__)

plugin_category = "البحث"


video_opts = {
    "format": "best",
    "addmetadata": True,
    "key": "FFmpegMetadata",
    "writethumbnail": True,
    "prefer_ffmpeg": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "postprocessors": [
        {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"},
        {"key": "FFmpegMetadata"},
    ],
    "outtmpl": "cat_ytv.mp4",
    "logtostderr": False,
    "quiet": True,
}


async def ytdl_down(event, opts, url):
    ytdl_data = None
    try:
        await event.edit("**╮ ❐ يتـم جلـب البيانـات انتظـر قليلاً ...𓅫╰▬▭ **")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{DE}`")
    except ContentTooShortError:
        await event.edit("**- عذرا هذا المحتوى قصير جدا لتنزيله ⚠️**")
    except GeoRestrictedError:
        await event.edit(
            "**- الفيديو غير متاح من موقعك الجغرافي بسبب القيود الجغرافية التي يفرضها موقع الويب ❕**"
        )
    except MaxDownloadsReached:
        await event.edit("**- تم الوصول إلى الحد الأقصى لعدد التنزيلات ❕**")
    except PostProcessingError:
        await event.edit("**كان هناك خطأ أثناء المعالجة**")
    except UnavailableVideoError:
        await event.edit("**⌔∮عـذراً .. الوسائط غير متوفـره بالتنسيق المطلـوب**")
    except XAttrMetadataError as XAME:
        await event.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        await event.edit("**حدث خطأ أثناء استخراج المعلومات يرجى وضعها بشكل صحيح ⚠️**")
    except Exception as e:
        await event.edit(f"**- خطـأ : **\n__{e}__")
    return ytdl_data


async def fix_attributes(
    path, info_dict: dict, supports_streaming: bool = False, round_message: bool = False
) -> list:
    """Avoid multiple instances of an attribute."""
    new_attributes = []
    video = False
    audio = False

    uploader = info_dict.get("uploader", "Unknown artist")
    duration = int(info_dict.get("duration", 0))
    suffix = path.suffix[1:]
    if supports_streaming and suffix != "mp4":
        supports_streaming = True

    attributes, mime_type = get_attributes(path)
    if suffix == "mp3":
        title = str(info_dict.get("title", info_dict.get("id", "Unknown title")))
        audio = types.DocumentAttributeAudio(
            duration=duration, voice=None, title=title, performer=uploader
        )
    elif suffix == "mp4":
        width = int(info_dict.get("width", 0))
        height = int(info_dict.get("height", 0))
        for attr in attributes:
            if isinstance(attr, types.DocumentAttributeVideo):
                duration = duration or attr.duration
                width = width or attr.w
                height = height or attr.h
                break
        video = types.DocumentAttributeVideo(
            duration=duration,
            w=width,
            h=height,
            round_message=round_message,
            supports_streaming=supports_streaming,
        )

    if audio and isinstance(audio, types.DocumentAttributeAudio):
        new_attributes.append(audio)
    if video and isinstance(video, types.DocumentAttributeVideo):
        new_attributes.append(video)

    new_attributes.extend(
        attr
        for attr in attributes
        if (
            isinstance(attr, types.DocumentAttributeAudio)
            and not audio
            or not isinstance(attr, types.DocumentAttributeAudio)
            and not video
            or not isinstance(attr, types.DocumentAttributeAudio)
            and not isinstance(attr, types.DocumentAttributeVideo)
        )
    )
    return new_attributes, mime_type


@zedub.zed_cmd(
    pattern="تحميل صوت(?:\s|$)([\s\S]*)",
    command=("تحميل صوت", plugin_category),
    info={
        "header": "تحميـل الاغـاني مـن يوتيوب .. فيسبوك .. انستا .. الـخ عـبر الرابـط",
        "مثــال": ["{tr}تحميل صوت بالــرد ع رابــط", "{tr}تحميل صوت + رابــط"],
    },
)
async def download_audio(event):
    """To download audio from YouTube and many other sites."""
    msg = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not msg and rmsg:
        msg = rmsg.text
    urls = extractor.find_urls(msg)
    if not urls:
        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل انتظر قليلا ▬▭ ...**")
    reply_to_id = await reply_id(event)
    for url in urls:
        try:
            vid_data = YoutubeDL({"no-playlist": True}).extract_info(
                url, download=False
            )
        except ExtractorError:
            vid_data = {"title": url, "uploader": "Catuserbot", "formats": []}
        startTime = time()
        retcode = await _mp3Dl(url=url, starttime=startTime, uid="320")
        if retcode != 0:
            return await event.edit(str(retcode))
        _fpath = ""
        thumb_pic = None
        for _path in glob.glob(os.path.join(Config.TEMP_DIR, str(startTime), "*")):
            if _path.lower().endswith((".jpg", ".png", ".webp")):
                thumb_pic = _path
            else:
                _fpath = _path
        if not _fpath:
            return await edit_delete(zedevent, "__Unable to upload file__")
        await zedevent.edit(
            f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\
            \n**{vid_data['title']}***"
        )
        attributes, mime_type = get_attributes(str(_fpath))
        ul = io.open(pathlib.Path(_fpath), "rb")
        if thumb_pic is None:
            thumb_pic = str(
                await pool.run_in_thread(download)(
                    await get_ytthumb(get_yt_video_id(url))
                )
            )
        uploaded = await event.client.fast_upload_file(
            file=ul,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    zedevent,
                    startTime,
                    "trying to upload",
                    file_name=os.path.basename(pathlib.Path(_fpath)),
                )
            ),
        )
        ul.close()
        media = types.InputMediaUploadedDocument(
            file=uploaded,
            mime_type=mime_type,
            attributes=attributes,
            force_file=False,
            thumb=await event.client.upload_file(thumb_pic) if thumb_pic else None,
        )
        await event.client.send_file(
            event.chat_id,
            file=media,
            caption=f"<b>File Name : </b><code>{vid_data.get('title', os.path.basename(pathlib.Path(_fpath)))}</code>",
            supports_streaming=True,
            reply_to=reply_to_id,
            parse_mode="html",
        )
        for _path in [_fpath, thumb_pic]:
            os.remove(_path)
    await zedevent.delete()


@zedub.zed_cmd(
    pattern="تحميل فيديو(?:\s|$)([\s\S]*)",
    command=("تحميل فيديو", plugin_category),
    info={
        "header": "تحميـل مقـاطـع الفيـديــو مـن يوتيوب .. فيسبوك .. انستا .. الـخ عـبر الرابـط",
        "مثــال": [
            "{tr}تحميل فيديو بالــرد ع رابــط",
            "{tr}تحميل فيديو + رابــط",
        ],
    },
)
async def download_video(event):
    """To download video from YouTube and many other sites."""
    msg = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not msg and rmsg:
        msg = rmsg.text
    urls = extractor.find_urls(msg)
    if not urls:
        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل انتظر قليلا ▬▭ ...**")
    reply_to_id = await reply_id(event)
    for url in urls:
        ytdl_data = await ytdl_down(zedevent, video_opts, url)
        if ytdl_down is None:
            return
        try:
            f = pathlib.Path("cat_ytv.mp4")
            print(f)
            catthumb = pathlib.Path("cat_ytv.jpg")
            if not os.path.exists(catthumb):
                catthumb = pathlib.Path("cat_ytv.webp")
            if not os.path.exists(catthumb):
                catthumb = None
            await zedevent.edit(
                f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\
                \n**{ytdl_data['title']}**"
            )
            ul = io.open(f, "rb")
            c_time = time()
            attributes, mime_type = await fix_attributes(
                f, ytdl_data, supports_streaming=True
            )
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, zedevent, c_time, "Upload :", file_name=ytdl_data["title"]
                    )
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type=mime_type,
                attributes=attributes,
            )
            await event.client.send_file(
                event.chat_id,
                file=media,
                reply_to=reply_to_id,
                caption=f'**⎉╎المقطــع :** `{ytdl_data["title"]}`',
                thumb=catthumb,
            )
            os.remove(f)
            if catthumb:
                os.remove(catthumb)
        except TypeError:
            await asyncio.sleep(2)
    await event.delete()


@zedub.zed_cmd(
    pattern="فيس(?:\s|$)([\s\S]*)",
    command=("فيسبوك", plugin_category),
    info={
        "header": "تحميـل مقـاطـع الفيـديــو مـن فيـس بــوك عـبر الرابـط",
        "مثــال": [
            "{tr}فيس بالــرد ع رابــط",
            "{tr}فيس + رابــط",
        ],
    },
)
async def download_video(event):
    """To download video from YouTube and many other sites."""
    msg = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not msg and rmsg:
        msg = rmsg.text
    urls = extractor.find_urls(msg)
    if not urls:
        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل مـن فيـس بـوك انتظر قليلا ▬▭ ...**")
    reply_to_id = await reply_id(event)
    for url in urls:
        ytdl_data = await ytdl_down(zedevent, video_opts, url)
        if ytdl_down is None:
            return
        try:
            f = pathlib.Path("cat_ytv.mp4")
            print(f)
            catthumb = pathlib.Path("cat_ytv.jpg")
            if not os.path.exists(catthumb):
                catthumb = pathlib.Path("cat_ytv.webp")
            if not os.path.exists(catthumb):
                catthumb = None
            await zedevent.edit(
                f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\
                \n**{ytdl_data['title']}**"
            )
            ul = io.open(f, "rb")
            c_time = time()
            attributes, mime_type = await fix_attributes(
                f, ytdl_data, supports_streaming=True
            )
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, zedevent, c_time, "Upload :", file_name=ytdl_data["title"]
                    )
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type=mime_type,
                attributes=attributes,
            )
            await event.client.send_file(
                event.chat_id,
                file=media,
                reply_to=reply_to_id,
                caption=f'**⎉╎المقطــع :** `{ytdl_data["title"]}`',
                thumb=catthumb,
            )
            os.remove(f)
            if catthumb:
                os.remove(catthumb)
        except TypeError:
            await asyncio.sleep(2)
    await event.delete()


@zedub.zed_cmd(
    pattern="سناب(?:\s|$)([\s\S]*)",
    command=("سناب شات", plugin_category),
    info={
        "header": "تحميـل مقـاطـع الفيـديــو مـن سنـاب_شـات عـبر الرابـط",
        "مثــال": [
            "{tr}سناب بالــرد ع رابــط",
            "{tr}سناب + رابــط",
        ],
    },
)
async def download_video(event):
    """To download video from YouTube and many other sites."""
    msg = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not msg and rmsg:
        msg = rmsg.text
    urls = extractor.find_urls(msg)
    if not urls:
        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل انتظر قليلا ▬▭ ...**")
    reply_to_id = await reply_id(event)
    for url in urls:
        ytdl_data = await ytdl_down(zedevent, video_opts, url)
        if ytdl_down is None:
            return
        try:
            f = pathlib.Path("cat_ytv.mp4")
            print(f)
            catthumb = pathlib.Path("cat_ytv.jpg")
            if not os.path.exists(catthumb):
                catthumb = pathlib.Path("cat_ytv.webp")
            if not os.path.exists(catthumb):
                catthumb = None
            await zedevent.edit(
                f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\
                \n**{ytdl_data['title']}**"
            )
            ul = io.open(f, "rb")
            c_time = time()
            attributes, mime_type = await fix_attributes(
                f, ytdl_data, supports_streaming=True
            )
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, zedevent, c_time, "Upload :", file_name=ytdl_data["title"]
                    )
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type=mime_type,
                attributes=attributes,
            )
            await event.client.send_file(
                event.chat_id,
                file=media,
                reply_to=reply_to_id,
                caption=f'**⎉╎المقطــع :** `{ytdl_data["title"]}`',
                thumb=catthumb,
            )
            os.remove(f)
            if catthumb:
                os.remove(catthumb)
        except TypeError:
            await asyncio.sleep(2)
    await event.delete()


@zedub.zed_cmd(
    pattern="تيك(?:\s|$)([\s\S]*)",
    command=("تيك", plugin_category),
    info={
        "header": "تحميـل مقـاطـع الفيـديــو مـن تيـك تـوك عـبر الرابـط",
        "مثــال": [
            "{tr}تيك بالــرد ع رابــط",
            "{tr}تيك + رابــط",
        ],
    },
)
async def download_video(event):
    """To download video from YouTube and many other sites."""
    msg = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not msg and rmsg:
        msg = rmsg.text
    urls = extractor.find_urls(msg)
    if not urls:
        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل انتظر قليلا ▬▭ ...**")
    reply_to_id = await reply_id(event)
    for url in urls:
        ytdl_data = await ytdl_down(zedevent, video_opts, url)
        if ytdl_down is None:
            return
        try:
            f = pathlib.Path("cat_ytv.mp4")
            print(f)
            catthumb = pathlib.Path("cat_ytv.jpg")
            if not os.path.exists(catthumb):
                catthumb = pathlib.Path("cat_ytv.webp")
            if not os.path.exists(catthumb):
                catthumb = None
            await zedevent.edit(
                f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\
                \n**{ytdl_data['title']}**"
            )
            ul = io.open(f, "rb")
            c_time = time()
            attributes, mime_type = await fix_attributes(
                f, ytdl_data, supports_streaming=True
            )
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, zedevent, c_time, "Upload :", file_name=ytdl_data["title"]
                    )
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type=mime_type,
                attributes=attributes,
            )
            await event.client.send_file(
                event.chat_id,
                file=media,
                reply_to=reply_to_id,
                caption=f'**⎉╎المقطــع :** `{ytdl_data["title"]}`',
                thumb=catthumb,
            )
            os.remove(f)
            if catthumb:
                os.remove(catthumb)
        except TypeError:
            await asyncio.sleep(2)
    await event.delete()


@zedub.zed_cmd(
    pattern="لايكي(?:\s|$)([\s\S]*)",
    command=("لايكي", plugin_category),
    info={
        "header": "تحميـل مقـاطـع الفيـديــو مـن لايكـي عـبر الرابـط",
        "مثــال": [
            "{tr}لايكي بالــرد ع رابــط",
            "{tr}لايكي + رابــط",
        ],
    },
)
async def download_video(event):
    """To download video from YouTube and many other sites."""
    msg = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not msg and rmsg:
        msg = rmsg.text
    urls = extractor.find_urls(msg)
    if not urls:
        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل انتظر قليلا ▬▭ ...**")
    reply_to_id = await reply_id(event)
    for url in urls:
        ytdl_data = await ytdl_down(zedevent, video_opts, url)
        if ytdl_down is None:
            return
        try:
            f = pathlib.Path("cat_ytv.mp4")
            print(f)
            catthumb = pathlib.Path("cat_ytv.jpg")
            if not os.path.exists(catthumb):
                catthumb = pathlib.Path("cat_ytv.webp")
            if not os.path.exists(catthumb):
                catthumb = None
            await zedevent.edit(
                f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\
                \n**{ytdl_data['title']}**"
            )
            ul = io.open(f, "rb")
            c_time = time()
            attributes, mime_type = await fix_attributes(
                f, ytdl_data, supports_streaming=True
            )
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, zedevent, c_time, "Upload :", file_name=ytdl_data["title"]
                    )
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type=mime_type,
                attributes=attributes,
            )
            await event.client.send_file(
                event.chat_id,
                file=media,
                reply_to=reply_to_id,
                caption=f'**⎉╎المقطــع :** `{ytdl_data["title"]}`',
                thumb=catthumb,
            )
            os.remove(f)
            if catthumb:
                os.remove(catthumb)
        except TypeError:
            await asyncio.sleep(2)
    await event.delete()


@zedub.zed_cmd(
    pattern="ساوند(?:\s|$)([\s\S]*)",
    command=("ساوند", plugin_category),
    info={
        "header": "تحميـل الاغـاني مـن سـاونـد كـلاود الـخ عـبر الرابـط",
        "مثــال": ["{tr}ساوند بالــرد ع رابــط", "{tr}ساوند + رابــط"],
    },
)
async def download_audio(event):
    """To download audio from YouTube and many other sites."""
    msg = event.pattern_match.group(1)
    rmsg = await event.get_reply_message()
    if not msg and rmsg:
        msg = rmsg.text
    urls = extractor.find_urls(msg)
    if not urls:
        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل انتظر قليلا ▬▭ ...**")
    reply_to_id = await reply_id(event)
    for url in urls:
        try:
            vid_data = YoutubeDL({"no-playlist": True}).extract_info(
                url, download=False
            )
        except ExtractorError:
            vid_data = {"title": url, "uploader": "Catuserbot", "formats": []}
        startTime = time()
        retcode = await _mp3Dl(url=url, starttime=startTime, uid="320")
        if retcode != 0:
            return await event.edit(str(retcode))
        _fpath = ""
        thumb_pic = None
        for _path in glob.glob(os.path.join(Config.TEMP_DIR, str(startTime), "*")):
            if _path.lower().endswith((".jpg", ".png", ".webp")):
                thumb_pic = _path
            else:
                _fpath = _path
        if not _fpath:
            return await edit_delete(zedevent, "__Unable to upload file__")
        await zedevent.edit(
            f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\
            \n**{vid_data['title']}***"
        )
        attributes, mime_type = get_attributes(str(_fpath))
        ul = io.open(pathlib.Path(_fpath), "rb")
        if thumb_pic is None:
            thumb_pic = str(
                await pool.run_in_thread(download)(
                    await get_ytthumb(get_yt_video_id(url))
                )
            )
        uploaded = await event.client.fast_upload_file(
            file=ul,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    zedevent,
                    startTime,
                    "trying to upload",
                    file_name=os.path.basename(pathlib.Path(_fpath)),
                )
            ),
        )
        ul.close()
        media = types.InputMediaUploadedDocument(
            file=uploaded,
            mime_type=mime_type,
            attributes=attributes,
            force_file=False,
            thumb=await event.client.upload_file(thumb_pic) if thumb_pic else None,
        )
        await event.client.send_file(
            event.chat_id,
            file=media,
            caption=f"<b>File Name : </b><code>{vid_data.get('title', os.path.basename(pathlib.Path(_fpath)))}</code>",
            supports_streaming=True,
            reply_to=reply_to_id,
            parse_mode="html",
        )
        for _path in [_fpath, thumb_pic]:
            os.remove(_path)
    await zedevent.delete()


@zedub.zed_cmd(
    pattern="انستا(?: |$)([\s\S]*)",
    command=("انستا", plugin_category),
    info={
        "header": "لـ تحميـل الصـور والفيـديـو مـن الانستـا",
        "مثــال": [
            "{tr}انستا + رابــط",
        ],
    },
)
async def insta_dl(event):
    "For downloading instagram media"
    link = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not link and reply:
        link = reply.text
    if not link:
        return await edit_delete(event, "**- احتـاج الـر رابــط للتحميــل**", 10)
    if "instagram.com" not in link:
        return await edit_delete(
            event, "**- احتـاج الـر رابــط للتحميــل**", 10
        )
    # v1 = "@instasave_bot"
    # v1 = "@IgGramBot"
    v1 = "Fullsavebot"
    v2 = "@videomaniacbot"
    media_list = []
    zedevent = await edit_or_reply(event, "**⎉╎جـارِ التحميل انتظر قليلا ▬▭ ...**")
    async with event.client.conversation(v1) as conv:
        try:
            v1_flag = await conv.send_message("/start")
        except YouBlockedUserError:
            await zedub(unblock("Fullsavebot"))
            v1_flag = await conv.send_message("/start")
        checker = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        if "Choose the language you like" in checker.message:
            await checker.click(1)
            await conv.send_message(link)
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await conv.send_message(link)
        await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        try:
            media = await conv.get_response(timeout=10)
            await event.client.send_read_acknowledge(conv.chat_id)
            if media.media:
                while True:
                    media_list.append(media)
                    try:
                        media = await conv.get_response(timeout=2)
                        await event.client.send_read_acknowledge(conv.chat_id)
                    except asyncio.TimeoutError:
                        break
                details = media_list[0].message.splitlines()
                await zedevent.delete()
                await event.client.send_file(
                    event.chat_id,
                    media_list,
                    caption=f"**{details[0]}**",
                )
                return await delete_conv(event, v1, v1_flag)
        except asyncio.TimeoutError:
            await delete_conv(event, v1, v1_flag)
        await edit_or_reply(zedevent, "**Switching v2...**")
        async with event.client.conversation(v2) as conv:
            try:
                v2_flag = await conv.send_message("/start")
            except YouBlockedUserError:
                await zedub(unblock("videomaniacbot"))
                v2_flag = await conv.send_message("/start")
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await asyncio.sleep(1)
            await conv.send_message(link)
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            media = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            if media.media:
                await zedevent.delete()
                await event.client.send_file(event.chat_id, media)
            else:
                await edit_delete(
                    zedevent,
                    f"**#ERROR\nv1 :** __Not valid URL__\n\n**v2 :**__ {media.text}__",
                    40,
                )
            await delete_conv(event, v2, v2_flag)


@zedub.zed_cmd(
    pattern="بنترست?(?:\s|$)([\s\S]*)",
    command=("بنترست", plugin_category),
    info={
        "header": "تحميـل مقـاطـع الفيـديـو والصــور مـن بنتـرسـت عـبر الرابـط",
        "مثــال": ["{tr}بنترست + رابــط"],
    },
)
async def _(event):
    M = event.pattern_match.group(1)
    links = re.findall(r"\bhttps?://.*\.\S+", M)
    await event.delete()
    if not links:
        N = await event.respond("**ارسل الامـر + الرابـط ... 🧸🎈**")
        await asyncio.sleep(2)
        await N.delete()
    else:
        pass
    A = await event.respond("**╮•⎚ جـارِ التحميل مـن بنتـرسـت ... 🧸🎈**")
    ZZZZL1L = get_download_url(M)
    await event.client.send_file(event.chat.id, ZZZZL1L)
    await A.delete()


@zedub.zed_cmd(
    pattern="يوتيوب(?: |$)(\d*)? ?([\s\S]*)",
    command=("يوتيوب", plugin_category),
    info={
        "header": "لـ البحـث عـن روابــط بالكلمــه المحــدده علـى يـوتيــوب",
        "مثــال": [
            "{tr}يوتيوب + كلمـه",
            "{tr}يوتيوب + عدد + كلمـه",
        ],
    },
)
async def yt_search(event):
    "Youtube search command"
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await edit_delete(
            event, "**╮ بالـرد ﮼؏ كلمـٓھہ للبحث أو ضعها مـع الأمـر ... 𓅫╰**"
        )
    video_q = await edit_or_reply(event, "**╮ جـارِ البحث ▬▭... ╰**")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        if lim <= 0:
            lim = int(10)
    else:
        lim = int(10)
    try:
        full_response = await ytsearch(query, limit=lim)
    except Exception as e:
        return await edit_delete(video_q, str(e), time=10, parse_mode=_format.parse_pre)
    reply_text = f"**⎉╎اليك عزيزي قائمة بروابط الكلمة اللتي بحثت عنها:**\n`{query}`\n\n**⎉╎النتائج:**\n{full_response}"
    await edit_or_reply(video_q, reply_text)
