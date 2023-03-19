import os
import asyncio
import time

import aiohttp
from telethon.errors import ChatAdminRequiredError as no_admin
from telethon.tl.functions.messages import ExportChatInviteRequest

from zthon import zedub

from ..helpers import get_user_from_event
from . import *


@zedub.zed_cmd(pattern="الطقس(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**- ارسـل .طقس + اسـم المدينـة**\n\n**- مثــال :**\n.طقس بغداد")


@zedub.zed_cmd(pattern="طقس (.*)")
async def _(event):
    if event.fwd_from:
        return
    Zed = "adf0cf22618186fc11e9f89c090cb356"
    sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str, Zed))
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await edit_or_reply(
            event,
            """**🗺┊حالات الطقس لـ مدينـة** {}
**🔅┊الحـرارة :** {}°С
**🏜┊درجة الحرارة الصغرى :** {}°С
**🌋┊درجة الحرارة العظمى :** {}°С
**🏖┊الرطـوبة :** {}%
**🎑┊الـرياح :** {}m/s
**🌁┊السحـاب :** {}hpa
**🌄┊شروق الشمس :** {} {}
**🌅┊غروب الشمس :** {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %I:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %I:%M:%S", time.gmtime(sun_set_time)),
                country_code,
            ),
        )
    else:
        await edit_or_reply(event, response_api["message"])


@zedub.zed_cmd(pattern="وهمي كتابه(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع الكتابه الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@zedub.zed_cmd(pattern="وهمي صوت(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع ارسال تسجيل الصوت الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@zedub.zed_cmd(pattern="وهمي فيديو(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع ارسال الفيديو الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@zedub.zed_cmd(pattern="وهمي لعبه(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع اللعب الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)

