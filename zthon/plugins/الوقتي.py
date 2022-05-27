#@ZedThon - زلـزال الهيبـه @ZZZZl1l
#كود الصورة الوقتيه  فكرتي وتعديلي الشخصي ومتعوب عليها + ماموجوده حتى بالسورسات الاجنبيه شلع قلع ..
#اذا تريد تخمط بالعافيه عليك حبي بس اتمنه اتمنه اذا انته صدك مطور وتكول اني مطور تذكر الحقوق .. غيرها انته مطور فاشل ..

import asyncio
import base64
import os
import random
import re
import shutil
import time
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions
from urlextract import URLExtract

from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.global_list import (
    add_to_list,
    get_collection_list,
    is_in_list,
    rm_from_list,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, _zedutils, zedub, edit_delete, logging

plugin_category = "الادوات"
DEFAULTUSERBIO = Config.DEFAULT_BIO or "الحمد الله على كل شئ - @ZedThon"
DEFAULTUSER = Config.DEFAULT_NAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)
CHANGE_TIME = int(gvarstatus("CHANGE_TIME")) if gvarstatus("CHANGE_TIME") else 60
DEFAULT_PIC = gvarstatus("DEFAULT_PIC") or None
ZEDT = Config.CUSTOM_ALIVE_EMZED or " "
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

normzltext = "1234567890"
namerzfont = Config.ZI_FN or "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬"

autopic_path = os.path.join(os.getcwd(), "zthon", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "zthon", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "zthon", "photo_pfp.png")

digitalpfp = Config.DIGITAL_PIC or "https://telegra.ph/file/82f009810be85e941053b.jpg"

COLLECTION_STRINGS = {
    "batmanpfp_strings": [
        "awesome-batman-wallpapers",
        "batman-arkham-knight-4k-wallpaper",
        "batman-hd-wallpapers-1080p",
        "the-joker-hd-wallpaper",
        "dark-knight-joker-wallpaper",
    ],
    "thorpfp_strings": [
        "thor-wallpapers",
        "thor-wallpaper",
        "thor-iphone-wallpaper",
        "thor-wallpaper-hd",
    ],
}


async def autopicloop():
    AUTOPICSTART = gvarstatus("autopic") == "true"
    if AUTOPICSTART and DEFAULT_PIC is None:
        if BOTLOG:
            return await zedub.send_message(
                BOTLOG_CHATID,
                "**عـذرا هنـاك خطـأ**\n وظيفة الصورة التـلقائيـة تحتاج إلى ضبط DIGITAL_PIC var في Heroku vars",
            )
        return
    if gvarstatus("autopic") is not None:
        try:
            counter = int(gvarstatus("autopic_counter"))
        except Exception as e:
            LOGS.warn(str(e))
    while AUTOPICSTART:
        if not os.path.exists(autopic_path):
            downloader = SmartDL(DEFAULT_PIC, autopic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(autopic_path, autophoto_path)
        im = Image.open(autophoto_path)
        file_test = im.rotate(counter, expand=False).save(autophoto_path, "PNG")
        current_time = datetime.now().strftime("  Time: %H:%M \n  Date: %d.%m.%y ")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((150, 250), current_time, font=fnt, fill=(124, 252, 0))
        img.save(autophoto_path)
        file = await zedub.upload_file(autophoto_path)
        try:
            await zedub(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            counter += counter
            await asyncio.sleep(CHANGE_TIME)
        except BaseException:
            return
        AUTOPICSTART = gvarstatus("autopic") == "true"


async def custompfploop():
    CUSTOMPICSTART = gvarstatus("CUSTOM_PFP") == "true"
    i = 0
    while CUSTOMPICSTART:
        if len(get_collection_list("CUSTOM_PFP_LINKS")) == 0:
            LOGS.error("No custom pfp images to set.")
            return
        pic = random.choice(list(get_collection_list("CUSTOM_PFP_LINKS")))
        urllib.request.urlretrieve(pic, "donottouch.jpg")
        file = await zedub.upload_file("donottouch.jpg")
        try:
            if i > 0:
                await zedub(
                    functions.photos.DeletePhotosRequest(
                        await zedub.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await zedub(functions.photos.UploadProfilePhotoRequest(file))
            os.remove("donottouch.jpg")
            await asyncio.sleep(CHANGE_TIME)
        except BaseException:
            return
        CUSTOMPICSTART = gvarstatus("CUSTOM_PFP") == "true"


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("digitalpic") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("  %I:%M ")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        zed = str(base64.b64decode("dXNlcmJvdC9oZWxwZXJzL3N0eWxlcy9aVGhvbi50dGY="))[
            2:36
        ]
        fnt = ImageFont.truetype(zed, 70)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(450, 350, 0))
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
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("digitalpic") == "true"


async def bloom_pfploop():
    BLOOMSTART = gvarstatus("bloom") == "true"
    if BLOOMSTART and DEFAULT_PIC is None:
        if BOTLOG:
            return await zedub.send_message(
                BOTLOG_CHATID,
                "**Error**\n`For functing of bloom you need to set DEFAULT_PIC var in Database vars`",
            )
        return
    while BLOOMSTART:
        if not os.path.exists(autopic_path):
            downloader = SmartDL(DEFAULT_PIC, autopic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        # RIP Danger zone Here no editing here plox
        R = random.randint(0, 256)
        B = random.randint(0, 256)
        G = random.randint(0, 256)
        FR = 256 - R
        FB = 256 - B
        FG = 256 - G
        shutil.copy(autopic_path, autophoto_path)
        image = Image.open(autophoto_path)
        image.paste((R, G, B), [0, 0, image.size[0], image.size[1]])
        image.save(autophoto_path)
        current_time = datetime.now().strftime("\n Time: %H:%M:%S \n \n Date: %d/%m/%y")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 250)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(FR, FG, FB))
        drawn_text.text((95, 250), "      😈", font=ofnt, fill=(FR, FG, FB))
        img.save(autophoto_path)
        file = await zedub.upload_file(autophoto_path)
        try:
            await zedub(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(CHANGE_TIME)
        except BaseException:
            return
        BLOOMSTART = gvarstatus("bloom") == "true"


async def autoname_loop():
    while AUTONAMESTART := gvarstatus("autoname") == "true":
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerzfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await zedub(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autobio_loop():
    while AUTOBIOSTART := gvarstatus("autobio") == "true":
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerzfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await zedub(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


async def animeprofilepic(collection_images):
    rnd = random.randint(0, len(collection_images) - 1)
    pack = collection_images[rnd]
    pc = requests.get(f"http://getwallpapers.com/collection/{pack}").text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = f"http://getwallpapers.com{random.choice(f)}"
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )
    img = requests.get(fy)
    with open("donottouch.jpg", "wb") as outfile:
        outfile.write(img.content)
    return "donottouch.jpg"


async def autopfp_start():
    if gvarstatus("autopfp_strings") is not None:
        AUTOPFP_START = True
        string_list = COLLECTION_STRINGS[gvarstatus("autopfp_strings")]
    else:
        AUTOPFP_START = False
    i = 0
    while AUTOPFP_START:
        await animeprofilepic(string_list)
        file = await zedub.upload_file("donottouch.jpg")
        if i > 0:
            await zedub(
                functions.photos.DeletePhotosRequest(
                    await zedub.get_profile_photos("me", limit=1)
                )
            )
        i += 1
        await zedub(functions.photos.UploadProfilePhotoRequest(file))
        await _zedutils.runcmd("rm -rf donottouch.jpg")
        await asyncio.sleep(CHANGE_TIME)
        AUTOPFP_START = gvarstatus("autopfp_strings") is not None


@zedub.zed_cmd(
    pattern="البروفايل تلقائي$",
    command=("البروفايل تلقائي", plugin_category),
    info={
        "header": "Updates your profile pic every 1 minute with time on it",
        "description": "لوضـع بروفـايل وقتـي لحسابـك يتغيـر تلقائيـاً كـل دقيقـه مـع الوقـت بعـدة زخـارف للوقت",
        "note": "لـ انهـاء البروفـايل الوقتـي ارسـل الامـر انهاء البروفايل'",
        "usage": "{tr}البروفايل تلقائي",
    },
)
async def _(event):
    "To set random colour pic with time to profile pic"
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
        return await edit_delete(event, "**التـغير التـلقائـي لصورتك ممكن بالفعل 𓆰**")
    addgvar("digitalpic", True)
    await edit_delete(event, "**تـم تفـعيل التـغير التـلقائـي لصورتك 𓆰**")
    await digitalpicloop()


@zedub.zed_cmd(
    pattern="الاسم تلقائي$",
    command=("الاسم تلقائي", plugin_category),
    info={
        "header": "Changes your name with time",
        "description": "لوضـع اسـم وقتـي لحسابـك يتغيـر تلقائيـاً كـل دقيقـه مـع الوقـت بعـدة زخـارف للوقت",
        "note": "لـ الانهـاء ارسـل الامـر انهاء الاسم'",
        "usage": "{tr}الاسم تلقائي",
    },
)
async def _(event):
    "To set your display name along with time"
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, "`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autoname_loop()


@zedub.zed_cmd(
    pattern="البايو تلقائي$",
    command=("البايو تلقائي", plugin_category),
    info={
        "header": "Changes your bio with time",
        "description": "لوضـع نبـذه وقتـيـه لحسابـك تتغيـر تلقائيـاً كـل دقيقـه مـع الوقـت بعـدة زخـارف للوقت",
        "note": "لـ الانهـاء ارسـل الامـر انهاء البايو'",
        "usage": "{tr}البايو تلقائي",
    },
)
async def _(event):
    "To update your bio along with time"
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, "** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autobio_loop()


@zedub.zed_cmd(
    pattern="انهاء ([\s\S]*)",
    command=("انهاء", plugin_category),
    info={
        "header": "To stop the functions of autoprofile",
        "description": "If you want to stop autoprofile functions then use this cmd.",
        "options": {
            "autopic": "To stop autopic",
            "digitalpfp": "To stop difitalpfp",
            "bloom": "To stop bloom",
            "autoname": "To stop autoname",
            "autobio": "To stop autobio",
            "thorpfp": "To stop thorpfp",
            "batmanpfp": "To stop batmanpfp",
            "spam": "To stop spam",
        },
        "usage": "{tr}end <option>",
        "examples": ["{tr}end autopic"],
    },
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "thorpfp" and gvarstatus("autopfp_strings") is not None:
        pfp_string = gvarstatus("autopfp_strings")[:-8]
        if pfp_string != "thorpfp":
            return await edit_delete(event, "`thorpfp is not started`")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        delgvar("autopfp_strings")
        return await edit_delete(event, "`thorpfp has been stopped now`")
    if input_str == "batmanpfp" and gvarstatus("autopfp_strings") is not None:
        pfp_string = gvarstatus("autopfp_strings")[:-8]
        if pfp_string != "batmanpfp":
            return await edit_delete(event, "`batmanpfp is not started`")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        delgvar("autopfp_strings")
        return await edit_delete(event, "`batmanpfp has been stopped now`")
    if input_str == "autopic":
        if gvarstatus("autopic") is not None and gvarstatus("autopic") == "true":
            delgvar("autopic")
            if os.path.exists(autopic_path):
                file = await event.client.upload_file(autopic_path)
                try:
                    await event.client(functions.photos.UploadProfilePhotoRequest(file))
                    os.remove(autopic_path)
                except BaseException:
                    return
            return await edit_delete(event, "`Autopic has been stopped now`")
        return await edit_delete(event, "`Autopic haven't enabled`")
    if input_str == "البروفايل تلقائي" or input_str == "البروفايل" or input_str == "البروفايل التلقائي" or input_str == "الصوره الوقتيه" or input_str == "البروفايل الوقتي":
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "** تم انهاء  البروفايل التلقائي الان 𓆰**")
        return await edit_delete(event, "** لم يتم تمكين  البروفايل التلقائي 𓆰**")
    if input_str == "bloom":
        if gvarstatus("bloom") is not None and gvarstatus("bloom") == "true":
            delgvar("bloom")
            if os.path.exists(autopic_path):
                file = await event.client.upload_file(autopic_path)
                try:
                    await event.client(functions.photos.UploadProfilePhotoRequest(file))
                    os.remove(autopic_path)
                except BaseException:
                    return
            return await edit_delete(event, "`Bloom has been stopped now`")
        return await edit_delete(event, "`Bloom haven't enabled`")
    if input_str == "الاسم تلقائي" or input_str == "الاسم" or input_str == "الاسم التلقائي" or input_str == "الاسم الوقتي":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**تم إيقاف لاسم التلقائي الآن 𓆰**")
        return await edit_delete(event, "**لم يتم تمكين الاسم التلقائي 𓆰**")
    if input_str == "البايو تلقائي" or input_str == "البايو" or input_str == "البايو التلقائي" or input_str == "البايو الوقتي" or input_str == "النبذه الوقتيه" or input_str == "النبذه الوقتي":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "** تم انهاء  البايو التلقائي الان 𓆰**")
        return await edit_delete(event, "** لم يتم تمكين  البايو التلقائي 𓆰**")
    if input_str == "spam":
        if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
            delgvar("spamwork")
            return await edit_delete(event, "`Spam cmd has been stopped now`")
        return await edit_delete(event, "`You haven't started spam`")
    END_CMDS = [
        "autopic",
        "البروفايل تلقائي",
        "bloom",
        "الاسم تلقائي",
        "البايو تلقائي",
        "thorpfp",
        "batmanpfp",
        "spam",
    ]
    if input_str not in END_CMDS:
        await edit_delete(
            event,
            f"{input_str} is invalid end command.Mention clearly what should i end.",
            parse_mode=_format.parse_pre,
        )


zedub.loop.create_task(autopfp_start())
zedub.loop.create_task(autopicloop())
zedub.loop.create_task(digitalpicloop())
zedub.loop.create_task(bloom_pfploop())
zedub.loop.create_task(autoname_loop())
zedub.loop.create_task(autobio_loop())
zedub.loop.create_task(custompfploop())
