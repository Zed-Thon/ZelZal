import requests
from validators.url import url

from . import zedub

from ..core.managers import edit_delete, edit_or_reply

plugin_category = "الادوات"


@zedub.zed_cmd(
    pattern="دومين(?:\s|$)([\s\S]*)",
    command=("dns", plugin_category),
    info={
        "header": "To get Domain Name System(dns) of the given link.",
        "الاستخـدام": "{tr}dns <url/reply to url>",
        "مثــال": "{tr}دومين google.com",
    },
)
async def _(event):
    "To get Domain Name System(dns) of the given link."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "**⎉╎بالـرد ع رابـط او باضافـة رابـط مع الامـر ...**", 10
        )
    check = url(input_str)
    if not check:
        catstr = f"http://{input_str}"
        check = url(catstr)
    if not check:
        return await edit_delete(event, "**⎉╎عـذراً .. هـذا الرابـط غيـر مدعـوم ؟!**", 10)
    sample_url = f"https://da.gd/dns/{input_str}"
    if response_api := requests.get(sample_url).text:
        await edit_or_reply(event, f"**⎉╎الدوميـن الخـاص بالرابـط** {input_str} \n**⎉╎هـو :** \n{response_api}")
    else:
        await edit_or_reply(
            event, f"**⎉╎عـذراً .. لا يمكنني العثـور علـى دوميـن الرابـط** {input_str} **على الشبكـة العنكبوتيـه**"
        )


@zedub.zed_cmd(
    pattern="اختصار(?:\s|$)([\s\S]*)",
    command=("اختصار", plugin_category),
    info={
        "header": "To short the given url.",
        "الاستخـدام": "{tr}short <url/reply to url>",
        "مثــال": "{tr}اختصار https://github.com/Zed-Thon/ZelZal",
    },
)
async def _(event):
    "shortens the given link"
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "**⎉╎بالـرد ع رابـط او باضافـة رابـط مع الامـر ...**", 10
        )
    check = url(input_str)
    if not check:
        catstr = f"http://{input_str}"
        check = url(catstr)
    if not check:
        return await edit_delete(event, "**⎉╎عـذراً .. هـذا الرابـط غيـر مدعـوم ؟!**", 10)
    if not input_str.startswith("http"):
        input_str = f"http://{input_str}"
    sample_url = f"https://da.gd/s?url={input_str}"
    if response_api := requests.get(sample_url).text:
        await edit_or_reply(
            event, f"**⎉╎الرابـط المختصر** {response_api} \n**⎉╎الرابـط** {input_str} \n**⎉╎تم انشـاء الإختصـار .. بنجـاح**", link_preview=False
        )
    else:
        await edit_or_reply(event, "**⎉╎خـطأ بالاختصـار .. الرجـاء المحاولـة لاحقـاً**")


@zedub.zed_cmd(
    pattern="الغاء اختصار(?:\s|$)([\s\S]*)",
    command=("unshort", plugin_category),
    info={
        "header": "To unshort the given dagb shorten url.",
        "الاستخـدام": "{tr}الغاء اختصار <url/reply to url>",
        "مثــال": "{tr}الغاء اختصار https://da.gd/rm6qri",
    },
)
async def _(event):
    "To unshort the given dagb shorten url."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "**⎉╎بالـرد ع رابـط او باضافـة رابـط مع الامـر ...**", 10
        )
    check = url(input_str)
    if not check:
        zedstr = f"http://{input_str}"
        check = url(zedstr)
    if not check:
        return await edit_delete(event, "**⎉╎عـذراً .. هـذا الرابـط غيـر مدعـوم ؟!**", 10)
    if not input_str.startswith("http"):
        input_str = f"http://{input_str}"
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await edit_or_reply(
            event,
            f"**⎉╎الرابـط المختصر :** {input_str}\n**⎉╎الرابـط الاصـلي :** {r.headers['Location']}",
            link_preview=False,
        )
    else:
        await edit_or_reply(
            event,
            "Input URL {} returned status_code {}".format(input_str, r.status_code),
        )


# By Priyam Kalra
@zedub.zed_cmd(
    pattern="اخفاء(?:\s|$)([\s\S]*)",
    command=("hl", plugin_category),
    info={
        "header": "To hide the url with white spaces using hyperlink.",
        "الاستخـدام": "{tr}اخفاء <url/reply to url>",
        "مثــال": "{tr}اخفاء https://da.gd/rm6qri",
    },
)
async def _(event):
    "To hide the url with white spaces using hyperlink."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await edit_delete(
            event, "**⎉╎بالـرد ع رابـط او باضافـة رابـط مع الامـر ...**", 10
        )
    check = url(input_str)
    if not check:
        catstr = f"http://{input_str}"
        check = url(catstr)
    if not check:
        return await edit_delete(event, "**⎉╎عـذراً .. هـذا الرابـط غيـر مدعـوم ؟!**", 10)
    await edit_or_reply(event, f"[ㅤㅤㅤㅤㅤㅤㅤ]({input_str})")
