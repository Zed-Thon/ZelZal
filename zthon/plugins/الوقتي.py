# @Zed-Thon - ZelZal
# Copyright (C) 2022 pp_g3 . All Rights Reserved
#< https://t.me/pp_g3 >
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.
#كـود الصورة الوقتيه كتـابتي وتعديلـي من زمان ومتعوب عليها 
#+ كـود زخـرفة الصورة الوقتيه
#+ دددي لا ابلـع حســابك بـانـد بطـعـم الليمــون 🍋😹🤘
#زلــزال الهيبــه يـ ولــد - حقــوق لـ التــاريـخ ®
#هههههههههههههههههههههههههههههههههههههههههههههههههه

import asyncio
import math
import base64
import os
import shutil
import time
import requests
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import edit_delete, zedub, logging

plugin_category = "الادوات"
DEFAULTUSER = gvarstatus("ALIVE_NAME") or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)
CHANGE_TIME = int(gvarstatus("CHANGE_TIME")) if gvarstatus("CHANGE_TIME") else 60
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

normzltext = "1234567890"

autopic_path = os.path.join(os.getcwd(), "zthon", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "zthon", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "zthon", "photo_pfp.png")


NAUTO = gvarstatus("Z_NAUTO") or "(الاسم تلقائي|الاسم الوقتي|اسم وقتي|اسم تلقائي)"
PAUTO = gvarstatus("Z_PAUTO") or "(البروفايل تلقائي|الصوره الوقتيه|الصورة الوقتية|صوره وقتيه|البروفايل)"
BAUTO = gvarstatus("Z_BAUTO") or "(البايو تلقائي|البايو الوقتي|بايو وقتي|نبذه وقتيه|النبذه الوقتيه)"


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("digitalpic") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            digitalpfp = gvarstatus("DIGITAL_PIC")
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        zedfont = gvarstatus("DEFAULT_PIC") or "zthon/helpers/styles/Papernotes.ttf"
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(f"{zedfont}", 35)
        drawn_text.text((140, 70), current_time, font=fnt, fill=(280, 280, 280))
        img.save(autophoto_path)
        file = await zedub.upload_file(autophoto_path)
        try:
            if i > 0:
                await zedub(
                    functions.photos.DeletePhotosRequest(
                        await zedub.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await zedub(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(CHANGE_TIME)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("digitalpic") == "true"


async def autoname_loop():
    while AUTONAMESTART := gvarstatus("autoname") == "true":
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namerzfont = gvarstatus("ZI_FN") or "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬"
              namefont = namerzfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        ZEDT = gvarstatus("CUSTOM_ALIVE_EMZED") or "⏐"
        name = f"{HM}{ZEDT}"
        LOGS.info(name)
        try:
            await zedub(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autobio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namerzfont = gvarstatus("ZI_FN") or "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬"
              namefont = namerzfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله على كل شئ -@pp_g3"
        bio = f"{DEFAULTUSERBIO} ⏐ {HM}"
        LOGS.info(bio)
        try:
            await zedub(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


@zedub.zed_cmd(pattern=f"{PAUTO}$")
async def _(event):
    digitalpfp = gvarstatus("DIGITAL_PIC")
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("DIGITAL_PIC") is None:
        return await edit_delete(event, "**- فار الصـورة الوقتيـه غيـر موجـود ؟!**\n**- ارسـل صورة ثم قم بالـرد عليهـا بالامـر :**\n\n`.اضف صورة الوقتي`")
    if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
        return await edit_delete(event, "**⎉╎البروفـايل الوقتـي .. تم تفعيلهـا سابقـاً**")
    addgvar("digitalpic", True)
    await edit_delete(event, "**⎉╎تـم بـدء البروفـايل الوقتـي .. بنجـاح ✓**")
    await digitalpicloop()


@zedub.zed_cmd(pattern=f"{NAUTO}$")
async def _(event):
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, "**⎉╎الاسـم الوقتـي .. تم تفعيلـه سابقـاً**")
    addgvar("autoname", True)
    await edit_delete(event, "**⎉╎تـم بـدء الاسـم الوقتـي .. بنجـاح ✓**")
    await autoname_loop()


@zedub.zed_cmd(pattern=f"{BAUTO}$")
async def _(event):
    if gvarstatus("DEFAULT_BIO") is None:
        return await edit_delete(event, "**- فار النبـذة الوقتيـه غيـر موجـود ؟!**\n**- ارسـل نـص النبـذه ثم قم بالـرد عليهـا بالامـر :**\n\n`.اضف البايو`")
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, "**⎉╎النبـذه الوقتـيه .. مفعلـه سابقـاً**")
    addgvar("autobio", True)
    await edit_delete(event, "**⎉╎تـم بـدء الـنبذة الوقتيـه .. بنجـاح ✓**")
    await autobio_loop()


@zedub.zed_cmd(
    pattern="الغاء ([\s\S]*)",
    command=("الغاء", plugin_category),
    info={
        "header": "To stop the functions of autoprofile",
        "description": "If you want to stop autoprofile functions then use this cmd.",
        "options": {
            "digitalpfp": "To stop difitalpfp",
            "autoname": "To stop autoname",
            "autobio": "To stop autobio",
        },
        "usage": "{tr}end <option>",
        "examples": ["{tr}end autopic"],
    },
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "البروفايل تلقائي" or input_str == "البروفايل" or input_str == "البروفايل التلقائي" or input_str == "الصوره الوقتيه" or input_str == "الصورة الوقتية":
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف البروفـايل الوقتـي .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎البروفـايل الوقتـي .. غيـر مفعـل اصـلاً ؟!**")
    if input_str == "الاسم تلقائي" or input_str == "الاسم" or input_str == "الاسم التلقائي" or input_str == "الاسم الوقتي" or input_str == "اسم الوقتي":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف الاسـم الوقتـي .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎الاسـم الوقتـي .. غيـر مفعـل اصـلاً ؟!**")
    if input_str == "البايو تلقائي" or input_str == "البايو" or input_str == "البايو التلقائي" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه" or input_str == "النبذة الوقتية" or input_str == "بايو الوقتي" or input_str == "نبذه الوقتي":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله على كل شئ -@pp_g3"
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف النبـذه الوقتيـه .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎النبـذه الوقتيـه .. غيـر مفعـله اصـلاً ؟!**")


@zedub.zed_cmd(
    pattern="ايقاف ([\s\S]*)",
    command=("ايقاف", plugin_category),
    info={
        "header": "To stop the functions of autoprofile",
        "description": "If you want to stop autoprofile functions then use this cmd.",
        "options": {
            "digitalpfp": "To stop difitalpfp",
            "autoname": "To stop autoname",
            "autobio": "To stop autobio",
        },
        "usage": "{tr}end <option>",
        "examples": ["{tr}end autopic"],
    },
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "البروفايل تلقائي" or input_str == "البروفايل" or input_str == "البروفايل التلقائي" or input_str == "الصوره الوقتيه" or input_str == "الصورة الوقتية":
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف البروفـايل الوقتـي .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎البروفـايل الوقتـي .. غيـر مفعـل اصـلاً ؟!**")
    if input_str == "الاسم تلقائي" or input_str == "الاسم" or input_str == "الاسم التلقائي" or input_str == "الاسم الوقتي" or input_str == "اسم الوقتي" or input_str == "اسم وقتي" or input_str == "اسم تلقائي":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف الاسـم الوقتـي .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎الاسـم الوقتـي .. غيـر مفعـل اصـلاً ؟!**")
    if input_str == "البايو تلقائي" or input_str == "البايو" or input_str == "البايو التلقائي" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه" or input_str == "النبذة الوقتية" or input_str == "بايو الوقتي" or input_str == "نبذه الوقتي":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله على كل شئ -@pp_g3"
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف النبـذه الوقتيـه .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎النبـذه الوقتيـه .. غيـر مفعـله اصـلاً ؟!**")



@zedub.zed_cmd(
    pattern="انهاء ([\s\S]*)",
    command=("انهاء", plugin_category),
    info={
        "header": "To stop the functions of autoprofile",
        "description": "If you want to stop autoprofile functions then use this cmd.",
        "options": {
            "digitalpfp": "To stop difitalpfp",
            "autoname": "To stop autoname",
            "autobio": "To stop autobio",
        },
        "usage": "{tr}end <option>",
        "examples": ["{tr}end autopic"],
    },
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "البروفايل تلقائي" or input_str == "البروفايل" or input_str == "البروفايل التلقائي" or input_str == "الصوره الوقتيه" or input_str == "الصورة الوقتية":
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف البروفـايل الوقتـي .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎البروفـايل الوقتـي .. غيـر مفعـل اصـلاً ؟!**")
    if input_str == "الاسم تلقائي" or input_str == "الاسم" or input_str == "الاسم التلقائي" or input_str == "الاسم الوقتي" or input_str == "اسم الوقتي" or input_str == "اسم وقتي" or input_str == "اسم تلقائي":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف الاسـم الوقتـي .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎الاسـم الوقتـي .. غيـر مفعـل اصـلاً ؟!**")
    if input_str == "البايو تلقائي" or input_str == "البايو" or input_str == "البايو التلقائي" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه" or input_str == "النبذة الوقتية" or input_str == "بايو الوقتي" or input_str == "نبذه الوقتي":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله على كل شئ - @devpokemon"
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "**⎉╎تم إيقـاف النبـذه الوقتيـه .. بنجـاح ✓**")
        return await edit_delete(event, "**⎉╎النبـذه الوقتيـه .. غيـر مفعـله اصـلاً ؟!**")
    END_CMDS = [
        "البروفايل تلقائي",
        "الصوره الوقتيه",
        "الاسم تلقائي",
        "الاسم الوقتي",
        "اسم تلقائي",
        "اسم وقتي",
        "البايو تلقائي",
        "البايو الوقتي",
        "النبذه الوقتيه",
        "البروفايل",
        "الاسم",
        "البايو",
    ]
    if input_str not in END_CMDS:
        await edit_delete(
            event,
            f"{input_str} is invalid end command.Mention clearly what should i end.",
            parse_mode=_format.parse_pre,
        )


zedub.loop.create_task(digitalpicloop())
zedub.loop.create_task(autoname_loop())
zedub.loop.create_task(autobio_loop())
