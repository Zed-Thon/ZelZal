import asyncio
import random, re
from telethon import events
from Zara.utils import admin_cmd 

@borg.on(admin_cmd(pattern="همسه ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    wspr_bot = "@BYYiBoT"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    ton = await bot.inline_query(wspr_bot, input_str) 
    await ton[0].click(event.chat_id)
    await event.delete()
    
@borg.on(admin_cmd(pattern="اهمس ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    wspr_bot = "@BYYiBoT"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    ton = await bot.inline_query(wspr_bot, input_str) 
    await ton[0].click(event.chat_id)
    await event.delete()
