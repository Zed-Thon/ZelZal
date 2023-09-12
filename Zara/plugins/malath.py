import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from ..Config import Config
from ..helpers.utils import install_pip
from ..utils import load_module
from . import BOTLOG, BOTLOG_CHATID, zedub

zilzal = zedub.uid
zed_dev = (6275274612, 6246466813, 6582806861, 6191064223, 6106257697, 5830283641, 6246466813, 6550930943, 5196173914, 2057498417, 6269975462, 5992422584)

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


    zedub.loop.create_task(install())
