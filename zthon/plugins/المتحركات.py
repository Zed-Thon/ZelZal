# Created by @Jisan7509

import random

import requests

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _zedutils, reply_id
from . import zedub

plugin_category = "البحث"


@zedub.zed_cmd(
    pattern="متحركه(?:\s|$)([\s\S]*)",
    command=("متحركه", plugin_category),
    info={
        "header": "Sends random gifs",
        "usage": "Search and send your desire gif randomly and in bulk",
        "examples": [
            "{tr}gifs cat",
            "{tr}gifs cat ; <1-20>",
        ],
    },
)
async def some(event):
    """Sends random gifs of your query"""
    inpt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not inpt:
        await edit_delete(event, "`Give an input to search...`")
    count = 1
    if ";" in inpt:
        inpt, count = inpt.split(";")
    if int(count) < 0 and int(count) > 20:
        await edit_delete(event, "`Give value in range 1-20`")
    zedevent = await edit_or_reply(event, "`Sending gif....`")
    res = requests.get("https://giphy.com/")
    res = res.text.split("GIPHY_FE_WEB_API_KEY =")[1].split("\n")[0]
    api_key = res[2:-1]
    r = requests.get(
        f"https://api.giphy.com/v1/gifs/search?q={inpt}&api_key={api_key}&limit=50"
    ).json()
    list_id = [r["data"][i]["id"] for i in range(len(r["data"]))]
    rlist = random.sample(list_id, int(count))
    for items in rlist:
        nood = await event.client.send_file(
            event.chat_id,
            f"https://media.giphy.com/media/{items}/giphy.gif",
            reply_to=reply_to_id,
        )
        await _zedutils.unsavegif(event, nood)
    await zedevent.delete()
