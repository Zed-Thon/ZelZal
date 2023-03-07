#    Credts @Mrconfused
from geopy.geocoders import Nominatim
from telethon.tl import types

from zthon import zedub

from ..core.managers import edit_or_reply
from ..helpers import reply_id

plugin_category = "الادوات"


@zedub.zed_cmd(
    pattern="الموقع ([\s\S]*)",
    command=("الموقع", plugin_category),
    info={
        "header": "لـ اعطائـك خريـطـه للمـوقـع الـذي طلبتــه",
        "الاسـتخـدام": "{tr}الموقع + المنطقـه/المدينـه",
        "مثــال": "{tr}الموقع بغداد",
    },
)
async def gps(event):
    "لـ اعطائـك خريـطـه للمـوقـع الـذي طلبتــه"
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "**جـارِ**")
    geolocator = Nominatim(user_agent="catuserbot")
    if geoloc := geolocator.geocode(input_str):
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**- المـوقع : **`{input_str}`",
            reply_to=reply_to_id,
        )
        await catevent.delete()
    else:
        await catevent.edit("**- عــذراً .. لـم احصـل عـلى المـوقع اعـد البحـث ...**")
