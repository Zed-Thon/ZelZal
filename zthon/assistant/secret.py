import json
import os
import re

from telethon.events import CallbackQuery

from zthon import zedub


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./zthon/secrets.txt"):
        jsondata = json.load(open("./zthon/secrets.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, zedub.uid]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "مطـي الهمسـه مـو الك 🧑🏻‍🦯🦓"
        except KeyError:
            reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في سيـرفرات زدثــون"
    else:
        reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في سيـرفرات زدثــون"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
