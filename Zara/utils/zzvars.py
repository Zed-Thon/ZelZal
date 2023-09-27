# Zed-Thon
# Copyright (C) 2023 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/tree/Zara/LICENSE/>.
#ههههههههههههههههههههههههههههههههههههه ها خماط شايفك
#معلمك زلزال الهيبه ياولد ^_*
import aiofiles
import aiohttp
import asyncio
import dotenv
import hashlib
import heroku3
import logging
import math
import os
import os.path
import re
import sys
import time
from os.path import basename
from urllib.request import urlretrieve

from hachoir.metadata import extractMetadata
from telethon.errors.rpcerrorlist import MessageNotModifiedError

from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger("Zara")

#Write Code By T.me/zzzzl1l For ZThon T.me/ZThon
#ههههههههههههههههههههههههههههههههههههه ها خماط شايفك
#اخمط واطشك بالقنوات جرب وشوف شراح اسوي بيك
async def set_zthonvar_value(vars, value):
    if (Config.HEROKU_API_KEY is not None) and (Config.HEROKU_APP_NAME is not None):
        Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
        happ = Heroku.app(Config.HEROKU_APP_NAME)
        heroku_config = happ.config()
        if vars not in heroku_config:
            heroku_config[vars] = value
            LOGS.info(f"تم اضافة الفار {vars} تلقائياً بنجاح")
            return True
    else:
        LOGS.info(
            "قم باضافة فار HEROKU_API_KEY وفار HEROKU_APP_NAME الى فارات هيروكو اولاً"
        )
        return