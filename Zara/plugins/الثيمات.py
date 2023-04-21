# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.
#حقوق زد ثـون ومتعوب عليها .. تخمط اذكر المصدر لو اهينك

import random

from . import zedub
from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id as rd 
from ..helpers import get_user_from_event
from zedthon.malath.theem import *

from . import *

@zedub.zed_cmd(pattern="ث1$")
async def stsTHMAT(zelzal):
    if zelzal.fwd_from:
        return
    zel = await rd(zelzal)
    if sts_attheme:
        zelzal_c = f"**{THMAT}**\n"
        await zelzal.client.send_file(zelzal.chat_id, sts_attheme, caption=zelzal_c, reply_to=zel)


@zedub.zed_cmd(pattern="ث2$")
async def stsTHMAT(lon):
    if lon.fwd_from:
        return
    lonid = await rd(lon)
    if sts_attheme2:
        zed_c = f"**{THMAT}**\n"
        await lon.client.send_file(lon.chat_id, sts_attheme2, caption=zed_c, reply_to=lonid)


@zedub.zed_cmd(pattern="ث3$")
async def stsTHMAT(i):
    if i.fwd_from:
        return
    sic_id = await rd(i)
    if sts_attheme3:
        tumc = f"**{THMAT}**\n"
        await i.client.send_file(i.chat_id, sts_attheme3, caption=tumc, reply_to=sic_id)


@zedub.zed_cmd(pattern="ث4$")
async def stsTHMAT(lon):
    if lon.fwd_from:
        return
    reply_to_id = await rd(lon)
    if sts_attheme4:
        tumc = f"**{THMAT}**\n"
        await lon.client.send_file(
            lon.chat_id, sts_attheme4, caption=tumc, reply_to=reply_to_id
        )


@zedub.zed_cmd(pattern="ث5$")
async def stsTHMAT(malat):
    if malat.fwd_from:
        return
    reply_to_id = await rd(malat)
    if sts_attheme5:
        tumc = f"**{THMAT}**\n"
        await malat.client.send_file(
            malat.chat_id, sts_attheme5, caption=tumc, reply_to=reply_to_id
        )


@zedub.zed_cmd(pattern="ث6$")
async def stsTHMAT(zelzalo):
    if zelzalo.fwd_from:
        return
    reply_to_id = await rd(zelzalo)
    if sts_attheme6:
        tumc = f"**{THMAT}**\n"
        await zelzalo.client.send_file(
            zelzalo.chat_id, sts_attheme6, caption=tumc, reply_to=reply_to_id
        )


@zedub.zed_cmd(pattern="ث7$")
async def stsTHMAT(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_attheme7:
        tumc = f"**{THMAT}**\n"
        await zed.client.send_file(
            zed.chat_id, sts_attheme7, caption=tumc, reply_to=reply_to_id
        )
        
        
@zedub.zed_cmd(pattern="ث8$")
async def stsTHMAT(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_attheme8:
        tumc = f"**{THMAT}**\n"
        await zed.client.send_file(
            zed.chat_id, sts_attheme8, caption=tumc, reply_to=reply_to_id
        )
        
@zedub.zed_cmd(pattern="ث9$")
async def stsTHMAT(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_attheme9:
        tumc = f"**{THMAT}**\n"
        await zed.client.send_file(
            zed.chat_id, sts_attheme9, caption=tumc, reply_to=reply_to_id
        )

@zedub.zed_cmd(pattern="ث10$")
async def stsTHMAT(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_attheme10:
        tumc = f"**{THMAT}**\n"
        await zed.client.send_file(
            zed.chat_id, sts_attheme10, caption=tumc, reply_to=reply_to_id
        )
        
@zedub.zed_cmd(pattern="ث11$")
async def stsTHMAT(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_attheme11:
        tumc = f"**{THMAT}**\n"
        await zed.client.send_file(
            zed.chat_id, sts_attheme11, caption=tumc, reply_to=reply_to_id
        )
        
@zedub.zed_cmd(pattern="ث12$")
async def stsTHMAT(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_attheme12:
        tumc = f"**{THMAT}**\n"
        await zed.client.send_file(
            zed.chat_id, sts_attheme12, caption=tumc, reply_to=reply_to_id
        )



@zedub.zed_cmd(pattern="ن1$")
async def stsfanan(zelzal):
    if zelzal.fwd_from:
        return
    zel = await rd(zelzal)
    if sts_fanan:
        zelzal_c = f"**{FANAN}**\n"
        zelzal_c += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        zelzal_c += f"**⪼ ثيـم علـم العـراق 🇮🇶♥️**\n"
        zelzal_c += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث1`"
        await zelzal.client.send_file(zelzal.chat_id, sts_fanan, caption=zelzal_c, reply_to=zel)


@zedub.zed_cmd(pattern="ن2$")
async def stsfanan(lon):
    if lon.fwd_from:
        return
    lonid = await rd(lon)
    if sts_fanan2:
        zed_c = f"**{FANAN}**\n"
        zed_c += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        zed_c += f"**⪼ ثيم البشير شو HD غير مضر للعيون ❤️ ...**\n"
        zed_c += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث2`"
        await lon.client.send_file(lon.chat_id, sts_fanan2, caption=zed_c, reply_to=lonid)


@zedub.zed_cmd(pattern="ن3$")
async def stsfanan(i):
    if i.fwd_from:
        return
    sic_id = await rd(i)
    if sts_fanan3:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم البشير_شو2..ثيم تجريبي🧸❤️ **\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث3`"
        await i.client.send_file(i.chat_id, sts_fanan3, caption=tumc, reply_to=sic_id)


@zedub.zed_cmd(pattern="ن4$")
async def stsfanan(lon):
    if lon.fwd_from:
        return
    reply_to_id = await rd(lon)
    if sts_fanan4:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم احمر وازرق بخلفية جوكر بنت كارتونيه متدرج بأحترافيه🧸🧡**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث4`"
        await lon.client.send_file(
            lon.chat_id, sts_fanan4, caption=tumc, reply_to=reply_to_id
        )


@zedub.zed_cmd(pattern="ن5$")
async def stsfanan(malat):
    if malat.fwd_from:
        return
    reply_to_id = await rd(malat)
    if sts_fanan5:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم بخلفية بناتية بألوان متنوعة ومتدرجه ولماعة جداً غير مضر للعيون🎁🤍**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث5`"
        await malat.client.send_file(
            malat.chat_id, sts_fanan5, caption=tumc, reply_to=reply_to_id
        )


@zedub.zed_cmd(pattern="ن6$")
async def stsfanan(zelzalo):
    if zelzalo.fwd_from:
        return
    reply_to_id = await rd(zelzalo)
    if sts_fanan6:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم للفنانة (بيلي اليش) الثيم ازرق فاتح وأبيض غير مضر للعيون🧸💙**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث6`"
        await zelzalo.client.send_file(
            zelzalo.chat_id, sts_fanan6, caption=tumc, reply_to=reply_to_id
        )


@zedub.zed_cmd(pattern="ن7$")
async def stsfanan(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_fanan7:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم اخضر وأبيض للفنانه بيلي اليش🧸💚...**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث7`"
        await zed.client.send_file(
            zed.chat_id, sts_fanan7, caption=tumc, reply_to=reply_to_id
        )
        
        
@zedub.zed_cmd(pattern="ن8$")
async def stsfanan(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_fanan8:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم فرقه ( BTS ) الثيم متناسق مع قليل من الشفافيه 🧸🌌...**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث8`"
        await zed.client.send_file(
            zed.chat_id, sts_fanan8, caption=tumc, reply_to=reply_to_id
        )
        
@zedub.zed_cmd(pattern="ن9$")
async def stsfanan(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_fanan9:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم لفرقة bts الكورية باللون الأسود🧸🌌..**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث9`"
        await zed.client.send_file(
            zed.chat_id, sts_fanan9, caption=tumc, reply_to=reply_to_id
        )

@zedub.zed_cmd(pattern="ن10$")
async def stsfanan(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_fanan10:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم لفرقة bts الكورية بلون فاتح غير مضر للعيون 🧸🌁...**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث10`"
        await zed.client.send_file(
            zed.chat_id, sts_fanan10, caption=tumc, reply_to=reply_to_id
        )
        
@zedub.zed_cmd(pattern="ن11$")
async def stsfanan(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_fanan11:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم أنمي برسائل شفافه غير مضر للعيون 🧸🤍...**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث11`"
        await zed.client.send_file(
            zed.chat_id, sts_fanan11, caption=tumc, reply_to=reply_to_id
        )
        
@zedub.zed_cmd(pattern="ن12$")
async def stsfanan(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if sts_fanan12:
        tumc = f"**{FANAN}**\n"
        tumc += f"•━─━─━─━─𝙕𝞝𝘿─━─━─━─━•\n\n"
        tumc += f"**⪼ ثيم داكن أزرق غامق وأبيض خفيف، بقليل من الشفافية🤍...**\n"
        tumc += f"**⪼ لـ تحميـل الثيـم ارســل ↫** `.ث12`"
        await zed.client.send_file(
            zed.chat_id, sts_fanan12, caption=tumc, reply_to=reply_to_id
        )


@zedub.zed_cmd(pattern="ثيمات")
async def zed(zelzal):
    await edit_or_reply(zelzal, ZL)

@zedub.zed_cmd(pattern="الثيمات")
async def zed(zelzal):
    await edit_or_reply(zelzal, ZL)
