import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from ..Config import Config
from ..helpers.utils import install_pip
from ..utils import load_module
from . import zedub

plugin_category = "الادوات"

if Config.ZELZAL_A:
    async def install():
        documentss = await zedub.get_messages(
            Config.ZELZAL_A, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        zzz = 0
        for module in range(total):
            if zzz == 5:
                break
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if plugin_name.endswith(".py"):
                if os.path.exists(f"Zara/plugins/{plugin_name}"):
                    return
                downloaded_file_name = await zedub.download_media(
                    await zedub.get_messages(Config.ZELZAL_A, ids=plugin_to_install),
                    "Zara/plugins/",
                )
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                flag = True
                check = 0
                while flag:
                    try:
                        load_module(shortname.replace(".py", ""))
                        zzz += 1
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break

    zedub.loop.create_task(install())
