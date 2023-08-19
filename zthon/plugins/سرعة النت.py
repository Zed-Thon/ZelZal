from time import time

import speedtest

from zthon import zedub

from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "الادوات"


def convert_from_bytes(size):
    power = 2**10
    n = 0
    units = {0: "", 1: "Kbps", 2: "Mbps", 3: "Gbps", 4: "Tbps"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"


@zedub.zed_cmd(pattern="الانترنت(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    as_text = False
    as_document = False
    if input_str == "صورة":
        as_document = False
    elif input_str == "ملف":
        as_document = True
    elif input_str == "نص":
        as_text = True
    zedevent = await edit_or_reply(
        event, "** ▷ جـاري قيـاس سرعـة الانتـرنت... ◃**"
    )
    start = time()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = time()
    ms = round(end - start, 2)
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = await reply_id(event)
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await zedevent.edit(
                """**قياس سرعـه الانترنت اكتمـلت في {} ثانيـه**

**التحميـل ⦂** {}
**الرفـع ⦂** {}
**بنـك ⦂** {}
**مزود خدمـة الإنترنت ⦂** {}
**مـعدل ISP ⦂** {}""".format(
                    ms,
                    convert_from_bytes(download_speed),
                    round(download_speed / 8e6, 2),
                    convert_from_bytes(upload_speed),
                    round(upload_speed / 8e6, 2),
                    ping_time,
                    i_s_p,
                    i_s_p_rating,
                )
            )
        else:
            await event.client.send_file(
                event.chat_id,
                speedtest_image,
                caption="**قياس سرعـه الانترنت اكتمـلت في {} ثانيـه**".format(ms),
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False,
            )
            await event.delete()
    except Exception as exc:
        await zedevent.edit(
            """**- قياس سرعـه الانتـرنت اكتمـلت في {} ثانيـه**
**التحميـل ⦂** {} (or) {} MB/s
**الرفـع ⦂** {} (or) {} MB/s
**البنـج ⦂** {} ms

__**- مـع الاخطـاء الناتجـه**__
{}""".format(
                ms,
                convert_from_bytes(download_speed),
                round(download_speed / 8e6, 2),
                convert_from_bytes(upload_speed),
                round(upload_speed / 8e6, 2),
                ping_time,
                str(exc),
            )
        )
