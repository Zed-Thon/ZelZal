# اذا تخمط اذكر الحقوق رجـاءا  - 
# كتابة وتعديل وترتيب  ~ @lMl10l
# For ~ @Jepthon
#تعديل Reda / رضا
#من تعرف تخمط اذكر حقوق لتسوي نفسك مطور
from ..sql_helper.group import auto_g, del_auto_g, get_auto_g
import webcolors
import asyncio
import base64
import os
import shutil
import time
from datetime import datetime
from telethon import events
from zthon import get_string
from telethon.errors import ChatAdminRequiredError
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError, ChannelInvalidError
from telethon.tl import functions
from telethon import types
from zthon import BOTLOG_CHATID
from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import AUTONAME, DEFAULT_GROUP, DEFAULT_BIO, edit_delete, l313l, logging
from colour import Color

plugin_category = "tools"
# لتخمط ابن الكحبة
DEFAULTUSERBIO = DEFAULT_BIO or "﴿ لا تَحزَن إِنَّ اللَّهَ مَعَنا ﴾ "
DEFAULTUSERGRO = DEFAULT_GROUP or ""
DEFAULTUSER = AUTONAME or ""
LOGS = logging.getLogger(__name__)

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

autopic_path = os.path.join(os.getcwd(), "joker", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "joker", "digital_pic.png")
digital_group_pic_path = os.path.join(os.getcwd(), "joker", "digital_group_pic.png")
autophoto_path = os.path.join(os.getcwd(), "joker", "photo_pfp.png")
auto_group_photo_path = os.path.join(os.getcwd(), "joker", "photo_pfp.png")

digitalpfp = Config.DIGITAL_PIC or "https://telegra.ph/file/63a826d5e5f0003e006a0.jpg"
digitalgrouppfp = Config.DIGITAL_GROUP_PIC or "https://telegra.ph/file/63a826d5e5f0003e006a0.jpg"
lMl10l = Config.TIME_JEP or ""
jep = Config.DEFAULT_PIC or "joker/helpers/styles/PaybAck.ttf"
normzltext = "1234567890"
namerzfont = Config.JP_FN or "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
namew8t = Config.NAME_ET or "اسم وقتي"
biow8t = Config.BIO_ET or "بايو وقتي"
phow8t = Config.PHOTO_ET or "الصورة الوقتية"

def check_color(color):
    try:
        color = color.replace(" ", "")
        Color(color)
        return True
    except ValueError:
        return False

async def digitalpicloop():
    colorco = gvarstatus("digitalpiccolor") or Config.DIGITAL_PIC_COLOR
    if colorco is None:
        colorco = "white"
    if not check_color(colorco):
        colorco = "red"
    colo = webcolors.name_to_rgb(colorco)
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
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(jep, 65)
        drawn_text.text((200, 200), current_time, font=fnt, fill=colo)
        img.save(autophoto_path)
        file = await l313l.upload_file(autophoto_path)
        try:
            if i > 0:
                await l313l(
                    functions.photos.DeletePhotosRequest(
                        await l313l.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await l313l(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("digitalpic") == "true"

#Reda
#اننننسخخخخخ هههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههههه
async def digitalgrouppicloop():
    "2KjZiNin2LPYt9ipINiz2YjYsdizINis2YrYqNir2YjZhiAo2KfYsNinINin2LPYqtio2K/ZhNiq2Ycg2LHYp9itINiq2KvYqNiqINmB2LTZhNmDKSDZhdi5INiq2K3Zitin2KrZiiDYp9iu2YjZg9mFINix2LbYpyBAcmQwcjA="

    dgp = gvarstatus("digitalgrouppic")
    colorco = gvarstatus("digitalgrouppiccolor") or Config.DIGITAL_PIC_COLOR
    if colorco is None:
        colorco = "white"
    if not check_color(colorco):
        colorco = "red"
    colo = webcolors.name_to_rgb(colorco)
    i = 0
    DIGITALPICSTART = gvarstatus("digitalgrouppic") != None
    while DIGITALPICSTART:
        if not os.path.exists(digital_group_pic_path):
            downloader = SmartDL(digitalgrouppfp, digital_group_pic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digital_group_pic_path, autophoto_path)
        Image.open(auto_group_photo_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(auto_group_photo_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(jep, 65)
        drawn_text.text((200, 200), current_time, font=fnt, fill=colo)
        img.save(auto_group_photo_path)
        file = await l313l.upload_file(auto_group_photo_path)
        try:
            if i > 0:
                async for photo in l313l.iter_profile_photos(int(dgp), limit=1) :
                    await l313l(
                    functions.photos.DeletePhotosRequest(id=[types.InputPhoto( id=photo.id, access_hash=photo.access_hash, file_reference=photo.file_reference )])
                    )
            i += 1
            await l313l(functions.channels.EditPhotoRequest(int(dgp), file))
            os.remove(auto_group_photo_path)
            await asyncio.sleep(60)
        except ChatAdminRequiredError:
            return await l313l.tgbot.send_message(BOTLOG_CHATID, "**يجب ان يكون لديك صلاحية تغيير صورة الكروب لتغيير صورة الكروب الوقتية •**")
        except ChannelInvalidError:
            return
        except FloodWaitError:
            return LOGS.warning("FloodWaitError! خطأ حظر مؤقت من التيليجرام")
        DIGITALPICSTART = gvarstatus("digitalgrouppic") != None
        base64m = 'QnkgQEplcHRob24gLyBSZWRhIEByZDByMCBkb24ndCByZW1vdmUgaXQ='
        message = base64.b64decode(base64m)
        messageo = message.decode()
        LOGS.info(messageo)

async def group_loop():
    ag = get_auto_g()
    AUTONAMESTAR = ag != None
    while AUTONAMESTAR:
        time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{DEFAULTUSERGRO} {HM}"
        try:
            await l313l(functions.channels.EditTitleRequest(
                channel=await l313l.get_entity(int(ag)),
                title=name
            ))
        except ChatAdminRequiredError:
            await l313l.tgbot.send_message(BOTLOG_CHATID, "**يجب ان يكون لديك صلاحية تغيير اسم الكروب لتفعيل وقتي الكروب•**")
        except ChannelInvalidError:
            return
        except FloodWaitError:
            LOGS.warning("FloodWaitError! خطأ حظر مؤقت من التيليجرام")
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTAR = get_auto_g() != None


async def autoname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{lMl10l} {HM}"
        LOGS.info(name)
        try:
            await l313l(functions.account.UpdateProfileRequest(last_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(120)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autobio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        time.strftime("%d.%m.%Y")
        HI = time.strftime("%I:%M")
        for normal in HI:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HI = HI.replace(normal, namefont)
        bio = f"{DEFAULTUSERBIO} {HI}"
        LOGS.info(bio)
        try:
            await l313l(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


@zedub.on(admin_cmd(pattern=f"{phow8t}(?:\s|$)([\s\S]*)"))
async def _(event):
    "To set random colour pic with time to profile pic"
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
        return await edit_delete(event, "**الصـورة الـوقتية شغـالة بالأصـل 🧸♥**")
    addgvar("digitalpic", True)
    await edit_delete(event, "**تم تفـعيل الصـورة الـوقتية بنجـاح ✓**")
    await digitalpicloop()

@zedub.on(admin_cmd(pattern="كروب وقتي"))
async def _(event):
    ison = get_auto_g()
    if event.is_group or event.is_channel:
        if ison is not None and ison == str(event.chat_id):
            return await edit_delete(event, "**الاسم الوقتي شغال للكروب/القناة**")
        chid = event.chat_id
        auto_g(str(chid))
        await edit_delete(event, "**تم تفـعيل الاسـم الوقتي للقناة/الكروب ✓**")
        await group_loop()
    else:
        return await edit_delete(event, "**يمكنك استعمال الاسم الوقتي في الكروب او في القناة فقط**")

@zedub.on(admin_cmd(pattern="كروب صورة وقتي"))
async def _(event):
    ison = gvarstatus("digitalgrouppic")
    if event.is_group or event.is_channel:
        if ison is not None and ison == str(event.chat_id):
            return await edit_delete(event, "**الصورة الوقتية شغالة للكروب/القناة**")
        chid = event.chat_id
        addgvar("digitalgrouppic", str(chid))
        await edit_delete(event, "**تم تفعيل الصورة الوقتية للكروب/ القناة ✓**")
        await digitalgrouppicloop()
    else:
        return await edit_delete(event, "**يمكنك استعمال الصورة الوقتية في كروب او قناة**")

@zedub.on(admin_cmd(pattern=f"{namew8t}(?:\s|$)([\s\S]*)"))
async def _(event):
    "To set your display name along with time"
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, "**الاسـم الـوقتي شغـال بالأصـل 🧸♥**")
    addgvar("autoname", True)
    await edit_delete(event, "**تم تفـعيل اسـم الـوقتي بنجـاح ✓**")
    await autoname_loop()


@zedub.on(admin_cmd(pattern=f"{biow8t}(?:\s|$)([\s\S]*)"))
async def _(event):
    "To update your bio along with time"
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, "**الـبايو الـوقتي شغـال بالأصـل 🧸♥**")
    addgvar("autobio", True)
    await edit_delete(event, "**تم تفـعيل البـايو الـوقتي بنجـاح ✓**")
    await autobio_loop()


@zedub.zed_cmd(
    pattern="انهاء ([\s\S]*)",
    command=("انهاء", plugin_category),
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "الصورة الوقتية":
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "**تم ايقاف الصورة الوقتية بنـجاح ✓ **")
        return await edit_delete(event, "**لم يتم تفعيل الصورة الوقتية بالأصل 🧸♥**")
    if input_str == "اسم وقتي":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(last_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**تم ايقاف  الاسم الوقتي بنـجاح ✓ **")
        return await edit_delete(event, "**لم يتم تفعيل الاسم الوقتي بالأصل 🧸♥**")
    if input_str == "بايو وقتي":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "**  تم ايقاف البايو الوقـتي بنـجاح ✓**")
        return await edit_delete(event, "**لم يتم تفعيل البايو الوقتي 🧸♥**")
    if input_str == "كروب صورة وقتي":
        if gvarstatus("digitalgrouppic") is not None:
            delgvar("digitalgrouppic")
            return await edit_delete(event, "**  تم ايقاف صورة الكروب الوقتية بنجاح ✓**")
        return await edit_delete(event, "**لم يتم تفعيل صورة الكروب/ القناة الوقتية بالأصل**")
    if input_str == "كروب وقتي":
        if get_auto_g() is not None:
            del_auto_g()
            return await edit_delete(event, "** تـم ايقاف الاسم الوقتي للكروب/القناة ✓**")
        return await edit_delete(event, "** لم يتم تفعيل الاسم الوقتي للكروب/القناة بالأصل **")
    END_CMDS = [
        "الصورة الوقتية",
        "اسم وقتي",
        "بايو وقتي",
        "كروب وقتي",
        "كروب صورة وقتي",
    ]
    if input_str not in END_CMDS:
        await edit_delete(
            event,
            f"عـذرا يجـب استـخدام الامـر بشـكل صحـيح 🧸♥",
            parse_mode=_format.parse_pre,
        )


zedub.loop.create_task(digitalpicloop())
zedub.loop.create_task(digitalgrouppicloop())
zedub.loop.create_task(autoname_loop())
zedub.loop.create_task(autobio_loop())
zedub.loop.create_task(group_loop())
