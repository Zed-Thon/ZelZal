import io
import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument

from zthon import zedub

from ..core.managers import edit_or_reply
from ..helpers.functions import deEmojify, hide_inlinebot, waifutxt
from ..helpers.utils import reply_id

plugin_category = "الترفيه"


async def get_font_file(client, channel_id, search_kw=""):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None,
        search=search_kw,
    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)


@zedub.zed_cmd(
    pattern="نص(?:\s|$)([\s\S]*)",
    command=("نص", plugin_category),
    info={
        "header": "انمي لـ جعل كتابتك ممتعـه",
        "الاستخـدام": "{tr}نص + النص",
        "مثــال": "{tr}نص مرحبا",
    },
)
async def waifu(animu):
    "انمي لـ جعل كتابتك ممتعـه"
    text = animu.pattern_match.group(1)
    reply_to_id = await reply_id(animu)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            return await edit_or_reply(
                animu, "**- قم باضافة نص للامـر ؟!**"
            )
    text = deEmojify(text)
    await animu.delete()
    await waifutxt(text, animu.chat_id, reply_to_id, animu.client)


@zedub.zed_cmd(
    pattern="ستيكر ?(?:(.*?) ?; )?([\s\S]*)",
    command=("ستيكر", plugin_category),
    info={
        "header": "تحويل النص لملصق",
        "الاستخـدام": [
            "{tr}ستيكر + نص",
            "{tr}stcr <font file name> ; <text>",
        ],
        "مثــال": "{tr}ستيكر hello",
    },
)
async def sticklet(event):
    "تحويل النص لملصق"
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    reply_to_id = await reply_id(event)
    font_file_name = event.pattern_match.group(1)
    if not font_file_name:
        font_file_name = ""
    sticktext = event.pattern_match.group(2)
    reply_message = await event.get_reply_message()
    if not sticktext:
        if event.reply_to_msg_id:
            sticktext = reply_message.message
        else:
            return await edit_or_reply(event, "؟!")
    await event.delete()
    sticktext = deEmojify(sticktext)
    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(event.client, "@T_Taiz", font_file_name)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)
    )
    image_stream = io.BytesIO()
    image_stream.name = "zedub.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    # finally, reply the sticker
    await event.client.send_file(
        event.chat_id,
        image_stream,
        caption="cat's Sticklet",
        reply_to=reply_to_id,
    )
    try:
        os.remove(FONT_FILE)
    except BaseException:
        pass


@zedub.zed_cmd(
    pattern="هونك(?:\s|$)([\s\S]*)",
    command=("هونك", plugin_category),
    info={
        "header": "لـ جعل هونك يقول اي شيء",
        "الاستخـدام": "{tr}هونك + نص او بالـرد ع رساله",
        "مثــال": "{tr}honk How you doing?",
    },
)
async def honk(event):
    "لـ جعل هونك يقول اي شيء"
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@honka_says_bot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(event, "** - ماذا يفترض أن يقول هونك أعطه نص ؟!**")
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@zedub.zed_cmd(
    pattern="تغريد(?:\s|$)([\s\S]*)",
    command=("تغريد", plugin_category),
    info={
        "header": "لـ عمل تغريدة رائعة من حسابك",
        "الاستخـدام": "{tr}تغريد + نص او بالـرد ع رساله",
        "مثــال": "{tr}twt zedub",
    },
)
async def twt(event):
    "لـ عمل تغريدة رائعة من حسابك"
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@TwitterStatusBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(event, "**- ماذا يفترض بي ان اغرد اعطني نص ؟!**")
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@zedub.zed_cmd(
    pattern="دوغي(?:\s|$)([\s\S]*)",
    command=("دوغي", plugin_category),
    info={
        "header": "لـ صنع ستيكر كلب رائع.",
        "الاستخـدام": "{tr}دوغي + نص او بالـرد ع رساله",
        "مثــال": "{tr}doge Gib money",
    },
)
async def doge(event):
    "لـ صنع ستيكر كلب رائع."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@DogeStickerBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(event, "**- ماذا يفترض بالكلب ان يقول اعطه نص ؟!**")
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@zedub.zed_cmd(
    pattern="غلاكس(|ر)(?:\s|$)([\s\S]*)",
    command=("غلاكس", plugin_category),
    info={
        "header": "لـ جعل غلاكس التنين ينفخ نصك.",
        "flags": {
            "ر": "Reverse the face of the dragon",
        },
        "الاستخـدام": [
            "{tr}glax <text/reply to msg>",
            "{tr}glaxr <text/reply to msg>",
        ],
        "مثــال": [
            "{tr}glax Die you",
            "{tr}glaxr Die you",
        ],
    },
)
async def glax(event):
    "لـ جعل غلاكس التنين ينفخ نصك."
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    bot_name = "@GlaxScremBot"
    c_lick = 1 if cmd == "ر" else 0
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "**- ماذا يفترض بـ غلاكـس ان يقول اعطه نص ؟!**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(
        event.client, bot_name, text, event.chat_id, reply_to_id, c_lick=c_lick
    )


Fun8_cmd = (
"**╮•❐ اوامـر تسليـه متحـركه 8 ⦂ **\n\n"

"  •  `.نص` + النص\n\n"
"  •  `.ستيكر` + نص\n\n"
"  •  `.هونك` + نص او بالـرد ع رساله\n\n"
"  •  `.تغريد` + نص او بالـرد ع رساله\n\n"
"  •  `.دوغي` + نص او بالـرد ع رساله\n\n"
"  •  `.غلاكس` + نص او بالـرد ع رساله\n\n\n"

"**- اضغـط ع الامـر لـ النسـخ"
)


@zedub.zed_cmd(pattern="تسليه8")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, Fun8_cmd)

