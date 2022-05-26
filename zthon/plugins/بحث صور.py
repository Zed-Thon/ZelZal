# image search for ZThon
import os
import shutil

from telethon.errors.rpcerrorlist import MediaEmptyError

from zthon import zedub

from ..core.managers import edit_or_reply
from ..helpers.google_image_download import googleimagesdownload
from ..helpers.utils import reply_id

plugin_category = "البحث"


@zedub.zed_cmd(
    pattern="صور(?: |$)(\d*)? ?([\s\S]*)",
    command=("صور", plugin_category),
    info={
        "header": "لـ بحـث الصـور مـن جـوجــل",
        "الاسـتخـدام": ["{tr}صور <1-10> <query>", "{tr}صور <query>"],
        "مثــال": [
            "{tr}صور 10 قطط",
            "{tr}صور قطط",
            "{tr}صور 7 قطط",
        ],
    },
)
async def img_sampler(event):
    "لـ بحـث الصـور مـن جـوجــل"
    reply_to_id = await reply_id(event)
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await edit_or_reply(
            event, "**╮ الرد ﮼؏ الرسالـٓھہ للبحث او ضعها مع الامر𓅫╰**"
        )
    cat = await edit_or_reply(event, "**╮ ❐ جـاري البحث عن 3 صـور افتراضياً...او استخدم .صور + عدد + اسم  𓅫╰**")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        if lim > 10:
            lim = int(10)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(3)
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query.replace(",", " "),
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    try:
        paths = response.download(arguments)
    except Exception as e:
        return await cat.edit(f"**- خطــأ**: \n`{e}`")
    lst = paths[0][query.replace(",", " ")]
    try:
        await event.client.send_file(event.chat_id, lst, reply_to=reply_to_id)
    except MediaEmptyError:
        for i in lst:
            try:
                await event.client.send_file(event.chat_id, i, reply_to=reply_to_id)
            except MediaEmptyError:
                pass
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await cat.delete()
