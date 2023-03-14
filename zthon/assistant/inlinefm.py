# By MineisZarox https://t.me/IrisZarox (Demon)
import asyncio
import io
import os
import time
from pathlib import Path

from telethon import Button, types
from telethon.events import CallbackQuery
from telethon.utils import get_attributes

from zthon import zedub
from zthon.Config import Config
from zthon.core.decorators import check_owner
from zthon.helpers import humanbytes, progress
from zthon.helpers.utils import _zedutils

CC = []
PATH = []  # using list method for some reason
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


# freaking selector
def add_s(msg, num: int):
    fmsg = ""
    msgs = msg.splitlines()
    leng = len(msgs)
    if num == 0:
        valv = leng - 1
        msgs[valv] = msgs[valv] + " ⭕️"
        for ff in msgs:
            fmsg += f"{ff}\n"
    elif num == leng:
        valv = 1
        msgs[valv] = msgs[valv] + " ⭕️"
        for ff in msgs:
            fmsg += f"{ff}\n"
    else:
        valv = num
        msgs[valv] = msgs[valv] + " ⭕️"
        for ff in msgs:
            fmsg += f"{ff}\n"
    buttons = [
        [
            Button.inline("D", data=f"fmrem_{msgs[valv]}|{valv}"),
            Button.inline("X", data=f"fmcut_{msgs[valv]}|{valv}"),
            Button.inline("C", data=f"fmcopy_{msgs[valv]}|{valv}"),
            Button.inline("V", data=f"fmpaste_{valv}"),
        ],
        [
            Button.inline("⬅️", data="fmback"),
            Button.inline("⬆️", data=f"fmup_{valv}"),
            Button.inline("⬇️", data=f"fmdown_{valv}"),
            Button.inline("➡️", data=f"fmforth_{msgs[valv]}"),
        ],
    ]
    return fmsg, buttons


def get_manager(path, num: int):
    if os.path.isdir(path):
        msg = "- المجلدات والملفات في `{}` :\n".format(path)
        lists = sorted(os.listdir(path))
        files = ""
        folders = ""
        for contents in sorted(lists):
            zpath = os.path.join(path, contents)
            if not os.path.isdir(zpath):
                size = os.stat(zpath).st_size
                if str(contents).endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += f"🎧`{contents}`\n"
                if str(contents).endswith((".opus")):
                    files += f"🎤`{contents}`\n"
                elif str(contents).endswith(
                    (".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")
                ):
                    files += f"🎬`{contents}`\n"
                elif str(contents).endswith((".zip", ".tar", ".tar.gz", ".rar")):
                    files += f"📚`{contents}`\n"
                elif str(contents).endswith((".py")):
                    files += f"🐍`{contents}`\n"
                elif str(contents).endswith(
                    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")
                ):
                    files += f"🏞`{contents}`\n"
                else:
                    files += f"📔`{contents}`\n"
            else:
                folders += f"📂`{contents}`\n"
        msg = msg + folders + files if files or folders else f"{msg}__مسار فارغ__"
        PATH.clear()
        PATH.append(path)
        msgs = add_s(msg, int(num))
    else:
        size = os.stat(path).st_size
        msg = "- معلومـات الملـف :\n"
        if str(path).endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎧"
        if str(path).endswith((".opus")):
            mode = "🎤"
        elif str(path).endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
            mode = "🎬"
        elif str(path).endswith((".zip", ".tar", ".tar.gz", ".rar")):
            mode = "📚"
        elif str(path).endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")):
            mode = "🏞"
        elif str(path).endswith((".py")):
            mode = "🐍"
        else:
            mode = "📔"
        time.ctime(os.path.getctime(path))
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        msg += f"**- المـوقع :** `{path}`\n"
        msg += f"**- الايقـونه :** `{mode}`\n"
        msg += f"**- الحجـم :** `{humanbytes(size)}`\n"
        msg += f"**- آخـر تحـديث للملـف :** `{time2}`\n"
        msg += f"**- آخـر وقـت تم الوصـول الى الملـف :** `{time3}`"
        buttons = [
            [
                Button.inline("إعادة تسميه", data=f"fmrem_File|{num}"),
                Button.inline("إرسـال", data="fmsend"),
                Button.inline("X", data=f"fmcut_File|{num}"),
                Button.inline("C", data=f"fmcopy_File{num}"),
            ],
            [
                Button.inline("⬅️", data="fmback"),
                Button.inline("⬆️", data="fmup_File"),
                Button.inline("⬇️", data="fmdown_File"),
                Button.inline("➡️", data="fmforth_File"),
            ],
        ]
        PATH.clear()
        PATH.append(path)
        msgs = (msg, buttons)
    return msgs


# BACK
@zedub.tgbot.on(CallbackQuery(pattern="fmback"))
@check_owner
async def back(event):
    path = PATH[0]
    paths = path.split("/")
    if paths[-1] == "":
        paths.pop()
        paths.pop()
    else:
        paths.pop()
    npath = ""
    for ii in paths:
        npath += f"{ii}/"
    num = 1
    msg, buttons = get_manager(npath, num)
    await asyncio.sleep(1)
    await event.edit(msg, buttons=buttons)


# UP
@zedub.tgbot.on(CallbackQuery(pattern="fmup_(.*)"))
@check_owner
async def up(event):
    num = event.pattern_match.group(1).decode("UTF-8")
    if num == "File":
        await event.answer("هـذا ملـف ياغبـي ؟!", alert=True)
    else:
        num1 = int(num) - 1
        path = PATH[0]
        msg, buttons = get_manager(path, num1)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# DOWN
@zedub.tgbot.on(CallbackQuery(pattern="fmdown_(.*)"))
@check_owner
async def down(event):
    num = event.pattern_match.group(1).decode("UTF-8")
    if num == "File":
        await event.answer("هـذا ملـف ياغبـي ؟!", alert=True)
    else:
        path = PATH[0]
        num1 = int(num) + 1
        msg, buttons = get_manager(path, num1)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# FORTH
@zedub.tgbot.on(CallbackQuery(pattern="fmforth_(.*)"))
@check_owner
async def forth(event):
    npath = event.pattern_match.group(1).decode("UTF-8")
    if npath == "File":
        await event.answer("هـذا ملـف ياغبـي ؟!", alert=True)
    else:
        path = PATH[0]
        npath = npath[2:-4]
        rpath = f"{path}/{npath}"
        num = 1
        msg, buttons = get_manager(rpath, num)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# REMOVE
@zedub.tgbot.on(CallbackQuery(pattern="fmrem_(.*)"))
@check_owner
async def remove(event):
    fn, num = (event.pattern_match.group(1).decode("UTF-8")).split("|", 1)
    path = PATH[0]
    if fn == "File":
        paths = path.split("/")
        if paths[-1] == "":
            paths.pop()
            paths.pop()
        else:
            paths.pop()
        npath = ""
        for ii in paths:
            npath += f"{ii}/"
        rpath = path
    else:
        n_path = fn[2:-4]
        rpath = f"{path}/{n_path}"
        npath = path
    msg, buttons = get_manager(npath, num)
    await asyncio.sleep(1)
    await event.edit(msg, buttons=buttons)
    await _zedutils.runcmd(f"rm -rf '{rpath}'")
    await event.answer(f"- المسـار {rpath} تم حذفـه .. بنجـاح ✓")


# SEND
@zedub.tgbot.on(CallbackQuery(pattern="fmsend"))
@check_owner
async def send(event):
    path = PATH[0]
    startTime = time.time()
    attributes, mime_type = get_attributes(str(path))
    ul = io.open(Path(path), "rb")
    uploaded = await event.client.fast_upload_file(
        file=ul,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(
                d,
                t,
                event,
                startTime,
                "جـارِ الـرفع",
                file_name=os.path.basename(Path(path)),
            )
        ),
    )
    ul.close()
    media = types.InputMediaUploadedDocument(
        file=uploaded,
        mime_type=mime_type,
        attributes=attributes,
        force_file=False,
        thumb=await event.client.upload_file(thumb_image_path)
        if thumb_image_path
        else None,
    )
    await event.edit("hi", file=media)


# CUT
@zedub.tgbot.on(CallbackQuery(pattern="fmcut_(.*)"))
@check_owner
async def cut(event):
    f, n = (event.pattern_match.group(1).decode("UTF-8")).split("|", 1)
    if CC:
        return await event.answer(f"قم بـ لصق {CC[1]} اولا")
    else:
        if f == "File":
            npath = PATH[0]
            paths = npath.split("/")
            if paths[-1] == "":
                paths.pop()
                paths.pop()
            else:
                paths.pop()
            path = ""
            for ii in paths:
                path += f"{ii}/"
            CC.append("cut")
            CC.append(npath)
            await event.answer(f"- جـارِ نقـل المسـار {npath} ...")
        else:
            path = PATH[0]
            npath = f[2:-4]
            rpath = f"{path}/{npath}"
            CC.append("cut")
            CC.append(rpath)
            await event.answer(f"- جـارِ نقـل المسـار {rpath} ...")
        msg, buttons = get_manager(path, n)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# COPY
@zedub.tgbot.on(CallbackQuery(pattern="fmcopy_(.*)"))
@check_owner
async def copy(event):
    f, n = (event.pattern_match.group(1).decode("UTF-8")).split("|", 1)
    if CC:
        return await event.answer(f"قم بـ لصق {CC[1]} اولا")
    else:
        if f == "File":
            npath = PATH[0]
            paths = npath.split("/")
            if paths[-1] == "":
                paths.pop()
                paths.pop()
            else:
                paths.pop()
            path = ""
            for ii in paths:
                path += f"{ii}/"
            CC.append("copy")
            CC.append(npath)
            await event.answer(f"- جـارِ نسـخ المسـار {path} ...")
        else:
            path = PATH[0]
            npath = f[2:-4]
            rpath = f"{path}/{npath}"
            CC.append("copy")
            CC.append(rpath)
            await event.answer(f"- جـارِ نسـخ المسـار {rpath} ...")
        msg, buttons = get_manager(path, n)
        await asyncio.sleep(1)
        await event.edit(msg, buttons=buttons)


# PASTE
@zedub.tgbot.on(CallbackQuery(pattern="fmpaste_(.*)"))
@check_owner
async def paste(event):
    n = event.pattern_match.group(1).decode("UTF-8")
    path = PATH[0]
    if CC:
        if CC[0] == "cut":
            cmd = f"mv '{CC[1]}' '{path}'"
        else:
            cmd = f"cp '{CC[1]}' '{path}'"
        await _zedutils.runcmd(cmd)
        msg, buttons = get_manager(path, n)
        await event.edit(msg, buttons=buttons)
        CC.clear
    else:
        await event.answer("انت لم تقم بنسخ اي شي لعمل له لصق ؟!")
