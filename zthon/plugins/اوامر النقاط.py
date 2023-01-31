from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

import requests
import asyncio
from time import sleep

import telethon
from telethon import events

from zthon import zedub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

session = Config.STRING_SESSION
c = requests.session()
bot_milyar = '@t06bot'


ZelzalCoins_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗭𝗧𝗵𝗼𝗻 - اوامـر تجميـع النقـاط](t.me/ZEDthon) 𓆪\n\n"
    "**✾╎قـائمـة اوامـر تجميـع نقـاط بوتـات تمـويـل الخاص بسـورس زدثـــون🦾 :** \n\n"
    "`.تجميع المليار`\n"
    "**⪼ يشتـرك بقنـوات بـوت المليـار تلقـائـي ✓**\n\n"
    "`.تجميع الجوكر`\n"
    "**⪼ يشتـرك بقنـوات بـوت الجوكـر تلقـائـي ✓**\n\n"
    "`.تجميع الجنرال`\n"
    "**⪼ يشتـرك بقنـوات بـوت الجنـرال تلقـائـي ✓**\n\n"
    "`.تجميع المليون`\n"
    "**⪼ يشتـرك بقنـوات بـوت المليـون تلقـائـي ✓**\n\n"
    "**- مـلاحظــه :**\n"
    "**⪼ سيتم اضـافـه المزيـد من البوتـات بالتحديثـات الجايـه .. اذا تريـد اضافـة بـوت محـدد راسـل مطـور السـورس @zzzzl1l**"
)


@zedub.zed_cmd(pattern="اوامر النقاط")
async def cmd(zilzal):
    await edit_or_reply(zilzal, ZelzalCoins_cmd)


@zedub.zed_cmd(pattern="المليار$")
async def _(event):
    await event.edit(bot_milyar)


@zedub.zed_cmd(pattern="تجميع المليار$")
async def _(event):
    await event.edit("**✾╎حسنـاً .. اولاً تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري الاسـاسيـه لـ بـوت المليـار ( @t06bot ) لتجنب الأخطـاء**")
    channel_entity = await zedub.get_entity(bot_milyar)
    await zedub.send_message('@t06bot', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@t06bot', limit=1)

    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@t06bot', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@t06bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await zedub.send_message(event.chat_id, f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            await zedub.send_message(event.chat_id, f"**✾╎خطـأ .. ممكـن تبنـدت**")
            break
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. بنجـاح ✓**")



@zedub.zed_cmd(pattern="تجميع الجوكر$")
async def _(event):
    await event.edit("**✾╎حسنـاً .. اولاً تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري الاسـاسيـه لـ بـوت الجوكـر ( @A_MAN9300BOT ) لتجنب الأخطـاء**")
    channel_entity = await zedub.get_entity(bot_milyar)
    await zedub.send_message('@A_MAN9300BOT', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@A_MAN9300BOT', limit=1)

    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@A_MAN9300BOT', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await zedub.send_message(event.chat_id, f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            await zedub.send_message(event.chat_id, f"**✾╎خطـأ .. ممكـن تبنـدت**")
            break
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. بنجـاح ✓**")


@zedub.zed_cmd(pattern="تجميع الجنرال$")
async def _(event):
    await event.edit("**✾╎حسنـاً .. اولاً تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري الاسـاسيـه لـ بـوت الجنـرال ( @MARKTEBOT ) لتجنب الأخطـاء**")
    channel_entity = await zedub.get_entity(bot_milyar)
    await zedub.send_message('@MARKTEBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@MARKTEBOT', limit=1)

    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@MARKTEBOT', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await zedub.send_message(event.chat_id, f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            await zedub.send_message(event.chat_id, f"**✾╎خطـأ .. ممكـن تبنـدت**")
            break
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. بنجـاح ✓**")



@zedub.zed_cmd(pattern="تجميع المليون$")
async def _(event):
    await event.edit("**✾╎حسنـاً .. اولاً تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري الاسـاسيـه لـ بـوت المليـون ( @qweqwe1919bot ) لتجنب الأخطـاء**")
    channel_entity = await zedub.get_entity(bot_milyar)
    await zedub.send_message('@qweqwe1919bot', '/start')
    await asyncio.sleep(4)
    msg0 = await zedub.get_messages('@qweqwe1919bot', limit=1)

    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await zedub.get_messages('@qweqwe1919bot', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await zedub(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**✾╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await zedub.send_message(event.chat_id, f"**✾╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await zedub(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await zedub(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await zedub.send_message(event.chat_id, f"**✾╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            await zedub.send_message(event.chat_id, f"**✾╎خطـأ .. ممكـن تبنـدت**")
            break
    await zedub.send_message(event.chat_id, "**✾╎تم الانتهـاء مـن تجميـع النقـاط .. بنجـاح ✓**")

