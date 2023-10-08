# Zed-Thon
# Copyright (C) 2023 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/tree/Zara/LICENSE/>.

""" وصـف الملـف : تخصيص الاوامــر🤘 تخمـط اطشـك للنـاس
حقــوق زدثــون : @ZThon
@zzzzl1l - كتـابـة الملـف :  زلــزال الهيبــه"""

import asyncio
import math
import os
import random
import string
from datetime import datetime

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_display_name

from Zara import zedub
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)


ZelzalCP_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗭𝗧𝗵𝗼𝗻 - اوامـر التخصيـص](t.me/ZThon) 𓆪\n\n"
    "**⎉╎قائـمـة تخصيـص الاوامــر الخاصـه بـ سـورس زدثــون 🦾 :** \n\n"
    "⪼ `.تخصيص كتم` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص حظر` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص طرد` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص تفليش` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص تفليش بالبوت` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص حظر_الكل` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص كتم_الكل` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص ايدي` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص رفع مشرف` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص تنزيل مشرف` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص مكرر` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص ايقاف مكرر` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص مؤقت` **+ الامـر الجديـد**\n\n"
    "⪼ `.تخصيص ايقاف مؤقت` **+ الامـر الجديـد**\n\n"
    "**- سيتـم اضـافة المزيـد مـن تخصيصـات الاوامــر بالتحديثـات الجايـه 🛃**\n\n\n"
)


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern=r"تخصيص (.*)")
async def variable(event):
    old_var = event.pattern_match.group(1)
    new_var = event.pattern_match.group(2)
    new_var = reply.text
    zed = await edit_or_reply(event, "**⎉╎جـاري تخصيص الامـر الجديـد ...**")
    # All Rights Reserved for "Zed-Thon" "زلـزال الهيبـه"
    if old_var == "مؤقت" or old_var == "مكرر":
        variable = "Z_SPAM"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "ايقاف مؤقت" or old_var == "ايقاف مكرر":
        variable = "Z_UNSPAM"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "كتم" or old_var == "الكتم":
        variable = "Z_KTM"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "رفع مشرف":
        variable = "Z_ADMIN"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "تنزيل مشرف":
        variable = "UNADMZ"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "حظر" or old_var == "الحظر":
        variable = "Z_BAN"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "الغاء حظر" or old_var == "الغاء الحظر":
        variable = "UNBANN"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "طرد" or old_var == "الطرد":
        variable = "Z_KICK"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "تفليش" or old_var == "التفليش":
        variable = "Z_TFSH"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "حظر_الكل" or old_var == "تفليش بالبوت":
        variable = "Z_HDRALL"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "كتم_الكل":
        variable = "Z_KTMALL"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    elif old_var == "ايدي":
        variable = "Z_ZZID"
        await asyncio.sleep(1.5)
        if gvarstatus(variable) is None:
            await zed.edit("**⎉╎تم تغييـر امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        else:
            await zed.edit("**⎉╎تم تحـديث امـر (** {} **) بنجـاح ☑️**\n**⎉╎الامـر الجديـد (** {} **)**".format(old_var, new_var))
        addgvar(variable, new_var)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#تخصيـص_الاوامــر\
                        \n**- تم تغييـر الامـر {old_var}  الـى {new_var} .. بنجـاح ✓**",
            )
    else:
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك امـر بإسـم {}\n⎉╎مضـاف لـ التخصيـص ؟!..\n⎉╎ارسـل (.اوامر التخصيص) لـعرض الاوامـر**".format(old_var))


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="حذف تخصيص(?:\s|$)([\s\S]*)")
async def variable(event):
    old_var = event.text[11:]
    zed = await edit_or_reply(event, "**⎉╎جـاري حـذف التخصيـص مـن بـوتك 🚮...**")
    # All Rights Reserved for "Zed-Thon" "زلـزال الهيبـه"
    if old_var == "مؤقت" or old_var == "مكرر":
        variable = "Z_SPAM"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "ايقاف مؤقت" or old_var == "ايقاف مكرر":
        variable = "Z_UNSPAM"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "كتم" or old_var == "الكتم":
        variable = "Z_KTM"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "رفع مشرف":
        variable = "Z_ADMIN"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "تنزيل مشرف":
        variable = "UNADMZ"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "حظر" or old_var == "الحظر":
        variable = "Z_BAN"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "الغاء حظر" or old_var == "الغاء الحظر":
        variable = "UNBANN"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "طرد" or old_var == "الطرد":
        variable = "Z_KICK"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "تفليش" or old_var == "التفليش":
        variable = "Z_TFSH"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "حظر_الكل" or old_var == "تفليش بالبوت":
        variable = "Z_HDRALL"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "كتم_الكل":
        variable = "Z_KTMALL"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    elif old_var == "ايدي":
        variable = "Z_ZZID"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تم حـذف تخصيـص {} .. بنجـاح ☑️**\n**⎉╎الامـر المحـذوف (** {} **)**".format(old_var, vvar،))
        delgvar(variable)
    else:
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك امـر بإسـم {}\n⎉╎مضـاف لـ التخصيـص ؟!..\n⎉╎ارسـل (.اوامر التخصيص) لـعرض الاوامـر**".format(old_var))


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="جلب تخصيص(?:\s|$)([\s\S]*)")
async def custom_zed(event):
    old_var = event.text[11:]
    zed = await edit_or_reply(event, "**⎉╎جــاري جلـب معلـومـات التخصيـص 🛂. . .**")
    if old_var == "مؤقت" or old_var == "مكرر":
        variable = "Z_SPAM"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "ايقاف مؤقت" or old_var == "ايقاف مكرر":
        variable = "Z_UNSPAM"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "كتم" or old_var == "الكتم":
        variable = "Z_KTM"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "رفع مشرف":
        variable = "Z_ADMIN"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "تنزيل مشرف":
        variable = "UNADMZ"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "حظر" or old_var == "الحظر":
        variable = "Z_BAN"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "الغاء حظر" or old_var == "الغاء الحظر":
        variable = "UNBANN"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "طرد" or old_var == "الطرد":
        variable = "Z_KICK"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "تفليش" or old_var == "التفليش":
        variable = "Z_TFSH"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "حظر_الكل" or old_var == "تفليش بالبوت":
        variable = "Z_HDRALL"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "كتم_الكل":
        variable = "Z_KTMALL"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    elif old_var == "ايدي":
        variable = "Z_ZZID"
        vvar = gvarstatus(variable)
        await asyncio.sleep(1.5)
        if vvar is None:
        	return await zed.edit("**⎉╎عـذࢪاً عـزيـزي .. انت لـم تقـم باضـافـة تخصيـص {} اصـلاً...**".format(old_var))
        await zed.edit("**⎉╎تخصـيص الـ {} .. مـوجـود ☑️**\n**⎉╎الامـر المخصـص (** {} **)**".format(old_var, vvar،))
    else:
        return await edit_or_reply(event, "**⎉╎عـذࢪاً .. لايوجـد هنالك امـر بإسـم {}\n⎉╎مضـاف لـ التخصيـص ؟!..\n⎉╎ارسـل (.اوامر التخصيص) لـعرض الاوامـر**".format(old_var))


@zedub.zed_cmd(pattern="اوامر التخصيص")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalCP_cmd)

@zedub.zed_cmd(pattern="التخصيص")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalCP_cmd)
