from . import zedub


@zedub.zed_cmd(pattern="غامق(?: |$)(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id and not input_str:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"**{the_real_message}**")
    elif input_str and not event.reply_to_msg_id:
        await event.edit(f"**{input_str}**")
    else:
        await event.edit("**- بالـرد ع رسـالتك او باضافة النص لـ الامـر ؟!**")


@zedub.zed_cmd(pattern="نسخ(?: |$)(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id and not input_str:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"`{the_real_message}`")
    elif input_str and not event.reply_to_msg_id:
        await event.edit(f"`{input_str}`")
    else:
        await event.edit("**- بالـرد ع رسـالتك او باضافة النص لـ الامـر ؟!**")


@zedub.zed_cmd(pattern="مائل(?: |$)(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id and not input_str:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"__{the_real_message}__")
    elif input_str and not event.reply_to_msg_id:
        await event.edit(f"__{input_str}__")
    else:
        await event.edit("**- بالـرد ع رسـالتك او باضافة النص لـ الامـر ؟!**")