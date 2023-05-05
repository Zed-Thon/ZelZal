# PLUGIN MADE BY @RRRLz FOR @ZedThon
# 𝖹Ꭵᥣᴢᥲ️ᥣ

import random, re
import asyncio
from telethon import events
from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply


@zedub.on(events.NewMessage(pattern=""))
async def _(event):
    user = await event.get_sender()
    zed_dev = (5093806483, 5683567042, 5902372255)
    if user.id in zed_dev:
        await event.reply(f"**-    ** [{user.first_name}](tg://user?id={user.id}) ")
