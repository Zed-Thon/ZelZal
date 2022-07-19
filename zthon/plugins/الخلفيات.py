import os
import random

import requests
from bs4 import BeautifulSoup

from zthon import zedub

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

LOGS = logging.getLogger(os.path.basename(__name__))
plugin_category = "البحث"


async def wall_download(piclink, query):
    try:
        if not os.path.isdir("./temp"):
            os.mkdir("./temp")
        picpath = f"./temp/{query.title().replace(' ', '')}.jpg"
        if os.path.exists(picpath):
            i = 1
            while os.path.exists(picpath) and i < 11:
                picpath = f"./temp/{query.title().replace(' ', '')}-{i}.jpg"
                i += 1
        with open(picpath, "wb") as f:
            f.write(requests.get(piclink).content)
        return picpath
    except Exception as e:
        LOGS.info(str(e))
        return None


@zedub.zed_cmd(
    pattern="خلفيات(?:\s|$)([\s\S]*)",
    command=("خلفيات", plugin_category),
    info={
        "header": "Searches and uploads wallpaper",
        "الاسـتخـدام": ["{tr}wall <query>", "{tr}wall <query> ، <1-10>"],
        "مثــال": ["{tr}wall one piece", "{tr}wall one piece ، 2"],
    },
)
async def noods(event):  # sourcery no-metrics
    "Wallpaper searcher"
    query = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    limit = 1
    if not query:
        return await edit_delete(event, "**- اعطـني نـص للبحـث . . .**", 10)
    if "،" in query:
        query, limit = query.split("،")
    if int(limit) > 10:
        return await edit_delete(event, "**- اقصـى عـدد للبحـث هـو 10 . . .**", 10)
    zedevent = await edit_or_reply(event, "**- جـارِ البحـث عـن خلفيـات HD . . .**")
    r = requests.get(
        f"https://wall.alphacoders.com/search.php?search={query.replace(' ','+')}"
    )
    soup = BeautifulSoup(r.content, "lxml")
    walls = soup.find_all("img", class_="img-responsive")
    if not walls:
        return await edit_delete(
            zedevent, f"**Can't find anything with** `{query}`", 10
        )
    i = count = 0
    piclist = []
    piclinks = []
    captionlist = []
    await edit_or_reply(zedevent, "**- جــارِ . . .**⏳")
    url2 = "https://api.alphacoders.com/content/get-download-link"
    for x in walls:
        wall = random.choice(walls)["src"][8:-4]
        server = wall.split(".")[0]
        fileid = wall.split("-")[-1]
        data = {
            "content_id": fileid,
            "content_type": "wallpaper",
            "file_type": "jpg",
            "image_server": server,
        }
        res = requests.post(url2, data=data)
        a = res.json()["link"]
        if "We are sorry," not in requests.get(a).text and a not in piclinks:
            await edit_or_reply(zedevent, "**- جـارِ التحميـل . . .📥**")
            pic = await wall_download(a, query)
            if pic is None:
                return await edit_delete(
                    zedevent, "__Sorry i can't download wallpaper.__"
                )
            piclist.append(pic)
            piclinks.append(a)
            captionlist.append("")
            count += 1
            i = 0
        else:
            i += 1
        await edit_or_reply(
            zedevent, f"**- تم تحميـل 📥 :** {count}/{limit}\n\n**- خطـأ بتحميـل ❌ :** {i}/5"
        )
        if count == int(limit):
            break
        if i == 5:
            await edit_or_reply(zedevent, "`Max search error limit exceed..`")
    try:
        await edit_or_reply(zedevent, "**- جـارِ التنزيـل . . .**")
        captionlist[-1] = f"**➥ البحـث :-** `{query.title()}`"
        await event.client.send_file(
            event.chat_id,
            piclist,
            caption=captionlist,
            reply_to=reply_to_id,
            force_document=True,
        )
        await zedevent.delete()
    except Exception as e:
        LOGS.info(str(e))
    for i in piclist:
        os.remove(i)
