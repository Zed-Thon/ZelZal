""" ترجمـة جوجل الصوتيـه
الاوامر المتاحـه هـي :
.صوت جوجل ar/en  بالرد على النص
.صوت جوجل ar/en | نص الى صوت
"""

import os
import subprocess
from datetime import datetime

from gtts import gTTS

from . import zedub

from ..core.managers import edit_delete, edit_or_reply
from . import deEmojify, reply_id

plugin_category = "الخدمات"


@zedub.zed_cmd(
    pattern="صوت جوجل(?:\s|$)([\s\S]*)",
    command=("صوت جوجل", plugin_category),
    info={
        "header": "Text to speech command.",
        "usage": [
            "{tr}tts <text>",
            "{tr}tts <reply>",
            "{tr}tts <language code> ; <text>",
        ],
    },
)
async def _(event):
    "text to speech command"
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    reply_to_id = await reply_id(event)
    if ";" in input_str:
        lan, text = input_str.split(";")
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    else:
        if not input_str:
            return await edit_or_reply(event, "**⌔∮ قم برد على الرساله**")
        text = input_str
        lan = "en"
    catevent = await edit_or_reply(event, "**- جـاري الترجمـه**")
    text = deEmojify(text.strip())
    lan = lan.strip()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    required_file_name = "./temp/" + "voice.ogg"
    try:
        # https://github.com/SpEcHiDe/UniBorg/commit/17f8682d5d2df7f3921f50271b5b6722c80f4106
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
            required_file_name,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            f"{required_file_name}.opus",
        ]

        try:
            t_response = subprocess.check_output(
                command_to_execute, stderr=subprocess.STDOUT
            )
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await catevent.edit(str(exc))
            # continue sending required_file_name
        else:
            os.remove(required_file_name)
            required_file_name = f"{required_file_name}.opus"
        end = datetime.now()
        ms = (end - start).seconds
        await event.client.send_file(
            event.chat_id,
            required_file_name,
            reply_to=reply_to_id,
            allow_cache=False,
            voice_note=True,
        )
        os.remove(required_file_name)
        await edit_delete(
            catevent,
            "**⌔∮ تم معـالجـة {} خـلال {} ثانيـه !**".format(text[:20], ms),
        )

    except Exception as e:
        await edit_or_reply(catevent, f"**- خطـأ:**\n`{e}`")
