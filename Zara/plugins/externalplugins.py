import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from ..Config import Config
from ..helpers.utils import install_pip
from ..utils import load_module
from . import BOTLOG, BOTLOG_CHATID, zedub

plugin_category = "الادوات"
zilzal = zedub.uid
zed_dev = (925972505, 1895219306, 5426390871, 5176749470, 2095357462)

if Config.PLUGIN_CHANNEL:
zelzal_by in zed_dev:
    async def install():
        if zilzal not in zed_dev:
            return
        documentss = await zedub.get_messages(
            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"Zara/plugins/{plugin_name}"):
                return
            downloaded_file_name = await zedub.download_media(
                await zedub.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),
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
                    f"**- تم تنصيب ملف**  `{os.path.basename(downloaded_file_name)}`  **.. بنجـاح ✅**",
                )

    zedub.loop.create_task(install())