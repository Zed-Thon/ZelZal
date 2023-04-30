import re
import os
try:
    import enum
except ModuleNotFoundError:
    os.system("pip3 install enum")
    import enum
from enum import Enum

from requests.exceptions import MissingSchema
from requests.models import PreparedRequest
from ..utils import runcmd
from yt_dlp import YoutubeDL


class Stream(Enum):
    audio = 1
    video = 2


yt_regex_str = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

yt_regex = re.compile(yt_regex_str)


def check_url(url):
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except MissingSchema:
        return False


async def get_yt_stream_link(url, audio_only=False):
    if audio_only:
        return (
            await runcmd(f"yt-dlp --no-warnings --geo-bypass -f bestaudio -g {url}")
        )[0]
    return (await runcmd(f"yt-dlp --no-warnings --geo-bypass -f best -g {url}"))[0]


async def video_dl(url, title):
    path = f"temp/{title.replace(' ', '_')}.mp4"
    video_opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": False,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"},
            {"key": "FFmpegMetadata"},
        ],
        "outtmpl": path,
        "logtostderr": False,
        "quiet": True,
    }

    with YoutubeDL(video_opts) as ytdl:
        ytdl.extract_info(url)
    return path
