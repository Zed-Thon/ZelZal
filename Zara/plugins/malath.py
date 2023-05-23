import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from ..Config import Config
from ..helpers.utils import install_pip
from ..utils import load_module
from . import BOTLOG, BOTLOG_CHATID, zedub

plugin_category = "الادوات"
zilzal = zedub.uid
zed_dev = (925972505, 1895219306, 5426390871, 5176749470, 2095357462, 5429537647, 5746412340, 5885458185, 5938244235, 5996295952, 5261694915, 5376382875, 5617945420, 5731271118, 6020309390, 5903321707, 6174195692)

if Config.ZELZAL_Z and zilzal in zed_dev:
    async def install():
        if zilzal not in zed_dev:
            return
        documentss = await zedub.get_messages(
            Config.ZELZAL_Z, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"Zara/plugins/{plugin_name}"):
                return
            downloaded_file_name = await zedub.download_media(
                await zedub.get_messages(Config.ZELZAL_Z, ids=plugin_to_install),
                "Zara/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await zedub.send_message(
                    BOTLOG_CHATID,
                    f"**- تم تثبيت**  `{os.path.basename(downloaded_file_name)}`  **.. بنجـاح ✅**",
                )

    zedub.loop.create_task(install())
