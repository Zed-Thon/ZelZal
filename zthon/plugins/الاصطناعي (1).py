import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from zthon import zedub

# الي يخمط ويكول من كتابتي الا امه انيجه وقد اعذر من انذر

@bot.on(admin_cmd(pattern="زينو ?(.*)"))
async def _(event):

    if event.reply_to_msg_id:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ .زينو + ما هو الذكاء الاصطناعي ... ...╰**"
        )
    chat = "@OpenAiChat_bot"
    catevent = await edit_or_reply(event, "**╮•⎚ اصبر جاي اجمع معلومات عنه ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.      
  NewMessage(incoming=True, from_users=5920512566)              
            )
            await event.client.send_message(chat, "/ask {}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @OpenAiChat_bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)
