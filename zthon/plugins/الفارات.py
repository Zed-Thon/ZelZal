# Zed-Thon
# Copyright (C) 2022 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

""" وصـف الملـف : اوامـر اضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
اضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @ZedThon
@zzzzl1l - كتـابـة الملـف :  زلــزال الهيبــه"""
#زلـزال_الهيبـه يولـد هههههههههههههههههههههههههه

import asyncio
import math
import os

import heroku3
import requests
import urllib3
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from zthon import zedub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"


telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


ZelzalVP_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗭𝗘𝗗𝗧𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر الفـارات](t.me/ZEDthon) 𓆪\n\n"
    "**✾╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات\n\n\n"
    "**✾╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف كليشة الحماية` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف كليشة الفحص` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف كروب الرسائل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف كروب السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف رسائل الحماية` بالـرد ع رقـم لعدد رسائل حماية الخاص\n\n\n"
    "⪼ `.جلب` + اسـم الفـار\n\n"
    "⪼ `.حذف` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر\n\n"
    "⪼ `.حذف المطورين`\n\n"
    "**✾╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "🛃 سيتـم اضـافة المزيـد من الدول قريبـاً\n\n"
    "\n𓆩 [𐇮 𝙕𝞝𝙇𝙕𝘼𝙇 الهہـيـٖ͡ـ͢ـبـه 𐇮](t.me/zzzzl1l) 𓆪"
)


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern=r"اضف (.*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    heroku_var = app.config()
    zed = await edit_or_reply(event, "**✾╎جـاري اضـافة الفـار الـى بـوتك ...**")
    # All Rights Reserved for "Zed-Thon" "زلـزال الهيبـه"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ZED_MEDIA"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغير : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغير : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMZED"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "ZI_FN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "الوقت" or input_str == "الساعه":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغيـر المنطقـة الزمنيـه**\n **✾╎المتغير : دولـة مصـر 🇪🇬**\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")
        else:
            await zed.edit("**✾╎تم اعـادة تغيـر المنطقـة الزمنيـه**\n **✾╎المتغير : دولـة مصـر 🇪🇬**\n\n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")
        heroku_var[variable] = vinfo
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "قناة الملفات" or input_str == "قناة الاضافات":
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "التوكن" or input_str == "توكن البوت":
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "الريبو" or input_str == "السورس":
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر {} بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**✾╎تم اضافـة {} بنجـاح ☑️** \n**✾╎المضاف اليه :**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    else:
        if input_str:
            return await zed.edit("**✾╎عـذراً .. لايوجـد هنالك فـار بإسـم {} ؟!..**".format(input_str))

        return await edit_or_reply(event, "**✾╎عـذراً .. لايوجـد هنالك فـار بإسـم {} ؟!..**".format(input_str))


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="حذف(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.text[5:]
    heroku_var = app.config()
    zed = await edit_or_reply(event, "**✾╎جـاري حـذف الفـار مـن بـوتك 🚮...**")
    # All Rights Reserved for "Zed-Thon" "زلـزال الهيبـه"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ZED_MEDIA"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "صورة الفحص" or input_str == "صوره الفحص":
        variable = "ALIVE_PIC"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "صورة الحماية" or input_str == "صوره الحمايه" or input_str == "صورة الحمايه" or input_str == "صوره الحماية":
        variable = "pmpermit_pic"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "صورة الوقتي" or input_str == "صوره الوقتي":
        variable = "DIGITAL_PIC"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMZED"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "ZI_FN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "قناة الملفات" or input_str == "قناة الاضافات":
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "التوكن" or input_str == "توكن البوت":
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "الريبو" or input_str == "السورس":
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "المطور" or input_str == "المطورين":
        variable = "SUDO_USERS"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
        	return await zed.edit("**✾╎عـذراً .. فـار {} غير موجود اصـلاً...**".format(input_str))

        await zed.edit("**✾╎تم حـذف {} بنجـاح ☑️**\n**✾╎المتغيـر المحـذوف : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, heroku_var[variable]))
        del heroku_var[variable]
    else:
        if input_str:
            return await zed.edit("**✾╎عـذراً .. لايوجـد هنالك فـار بإسـم {} ؟!..**".format(input_str))

        return await edit_or_reply(event, "**✾╎عـذراً .. لايوجـد هنالك فـار بإسـم {} ؟!..**".format(input_str))


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="جلب(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.text[5:]
    heroku_var = app.config()
    zed = await edit_or_reply(event, "**✾╎جـاري جلـب الفـار مـن بـوتك 🛂...**")
    # All Rights Reserved for "Zed-Thon" "زلـزال الهيبـه"
    if input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMZED"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "زخرفه الوقتي" or input_str == "زخرفة الوقتي":
        variable = "ZI_FN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "الوقت" or input_str == "الساعه":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغيـر المنطقـة الزمنيـه**\n **✾╎المتغير : دولـة مصـر 🇪🇬**\n\n**✾╎قنـاة السـورس : @ZEDThon**")
        else:
            await zed.edit("**✾╎تم اعـادة تغيـر المنطقـة الزمنيـه**\n **✾╎المتغير : دولـة مصـر 🇪🇬**\n\n**✾╎قنـاة السـورس : @ZEDThon**")
        heroku_var[variable] = "Africa/Cairo"
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "السجل" or input_str == "كروب السجل":
        variable = "PRIVATE_GROUP_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "السجل 2" or input_str == "كروب السجل 2":
        variable = "PRIVATE_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "قناة السجل" or input_str == "قناة السجلات":
        variable = "PRIVATE_CHANNEL_BOT_API_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "قناة الملفات" or input_str == "قناة الاضافات":
        variable = "PLUGIN_CHANNEL"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "ايديي" or input_str == "ايدي الحساب":
        variable = "OWNER_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "نقطة الاوامر" or input_str == "نقطه الاوامر":
        variable = "COMMAND_HAND_LER"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "التوكن" or input_str == "توكن البوت":
        variable = "TG_BOT_TOKEN"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "معرف البوت" or input_str == "معرف بوت":
        variable = "TG_BOT_USERNAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
 
    elif input_str == "الريبو" or input_str == "السورس":
        variable = "UPSTREAM_REPO"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))

    elif input_str == "اسمي التلقائي" or input_str == "الاسم التلقاائي":
        variable = "AUTONAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))

    elif input_str == "المطور" or input_str == "المطورين":
        variable = "SUDO_USERS"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎المطـور {} موجـود 🧑🏻‍💻☑️**\n**✾╎ايدي المطـور : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ المطـور {} غيـر موجـود 🧑🏻‍💻❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص":
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎الفـار {} موجـود ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))
        else:
            await zed.edit("**✾╎ الفـار {} غيـر موجـود ❌** \n**✾╎المتغيـر :**\n `{}` \n**✾╎قنـاة السـورس : @ZEDThon**".format(input_str, heroku_var[variable]))

    else:
        if input_str:
            return await zed.edit("**✾╎عـذراً .. لايوجـد هنالك فـار بإسـم {} ؟!..**".format(input_str))

        return await edit_or_reply(event, "**✾╎عـذراً .. لايوجـد هنالك فـار بإسـم {} ؟!..**".format(input_str))


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="وقت(?:\s|$)([\s\S]*)")
async def variable(event):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            event,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    input_str = event.text[5:]
    viraq = "Asia/Baghdad"
    vmsr = "Africa/Cairo"
    heroku_var = app.config()
    zed = await edit_or_reply(event, "**✾╎جـاري أعـداد المنطقـه الزمنيـه لـ زدثــون 🌐...**")
    # All Rights Reserved for "Zed-Thon" "زلـزال الهيبـه"
    if input_str == "العراق" or input_str == "عراق":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المتغير : ↶**\n دولـة `{}` 🇮🇶 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**✾╎تم اضـافـة المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المضـاف اليـه : ↶**\n دولـة `{}` 🇮🇶 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        heroku_var[variable] = viraq
    elif input_str == "اليمن" or input_str == "يمن":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المتغير : ↶**\n دولـة `{}` 🇾🇪 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**✾╎تم اضـافـة المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المضـاف اليـه : ↶**\n دولـة `{}` 🇾🇪 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        heroku_var[variable] = viraq
    elif input_str == "سوريا" or input_str == "سوريه":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المتغير : ↶**\n دولـة `{}` 🇸🇾 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**✾╎تم اضـافـة المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المضـاف اليـه : ↶**\n دولـة `{}` 🇸🇾 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        heroku_var[variable] = viraq
    elif input_str == "مصر" or input_str == "المصري" or input_str == "القاهرة":
        variable = "TZ"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**✾╎تم تغييـر المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المتغير : ↶**\n دولـة `{}` 🇪🇬 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        else:
            await zed.edit("**✾╎تم اضـافـة المنطقـه الزمنيـه .. بنجـاح ☑️**\n**✾╎المضـاف اليـه : ↶**\n دولـة `{}` 🇪🇬 \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str))
        heroku_var[variable] = vmsr
 

# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="اضف (صورة|صوره) (الحماية|الحمايه|الفحص|الوقتي) ?(.*)")
async def _(tosh):
    if tosh.fwd_from:
        return
    if Config.HEROKU_API_KEY is None:
        return await ed(
            var,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            var,
            "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    heroku_var = app.config()
    zed = await edit_or_reply(tosh, "**✾╎جـاري اضـافة فـار الصـورة الـى بـوتك ...**")
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
        #     if BOTLOG:
        await tosh.client.send_message(
            BOTLOG_CHATID,
            "**✾╎تم إنشاء حساب Telegraph جديد {} للدورة الحالية‌‌** \n**✾╎لا تعطي عنوان url هذا لأي شخص**".format(
                auth_url
            ),
        )
    optional_title = tosh.pattern_match.group(2)
    if tosh.reply_to_msg_id:
        start = datetime.now()
        r_message = await tosh.get_reply_message()
        input_str = tosh.pattern_match.group(1)
        if input_str in ["الحماية", "الحمايه"]:
            downloaded_file_name = await tosh.client.download_media(
                r_message, Config.TEMP_DIR
            )
            end = datetime.now()
            ms = (end - start).seconds
            await zed.edit(
                f"**✾╎تم تحميل {downloaded_file_name} في وقت {ms} ثانيه.**"
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await zed.edit("**✾╎خطا : **" + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                vinfo = ("https://telegra.ph{}".format(media_urls[0]))
                heroku_var["pmpermit_pic"] = vinfo
                await zed.edit("**✾╎تم تغييـر صـورة {} .. بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        elif input_str in ["الفحص", "السورس"]:
            downloaded_file_name = await tosh.client.download_media(
                r_message, Config.TEMP_DIR
            )
            end = datetime.now()
            ms = (end - start).seconds
            await zed.edit(
                f"**✾╎تم تحميل {downloaded_file_name} في وقت {ms} ثانيه.**"
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await zed.edit("**✾╎خطا : **" + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                vinfo = ("https://telegra.ph{}".format(media_urls[0]))
                heroku_var["ALIVE_PIC"] = vinfo
                await zed.edit("**✾╎تم تغييـر صـورة {} .. بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))
        elif input_str in ["الوقتي", "البروفايل"]:
            downloaded_file_name = await tosh.client.download_media(
                r_message, Config.TEMP_DIR
            )
            end = datetime.now()
            ms = (end - start).seconds
            await zed.edit(
                f"**✾╎تم تحميل {downloaded_file_name} في وقت {ms} ثانيه.**"
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await zed.edit("**✾╎خطا : **" + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                vinfo = ("https://telegra.ph{}".format(media_urls[0]))
                heroku_var["DIGITAL_PIC"] = vinfo
                await zed.edit("**✾╎تم تغييـر صـورة {} .. بنجـاح ☑️**\n**✾╎المتغيـر : ↶**\n `{}` \n**✾╎يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(input_str, vinfo))


    else:
        await zed.edit(
            "**✾╎بالـرد ع صـورة لتعييـن الفـار ...**",
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="اوامر الفارات")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalVP_cmd)

