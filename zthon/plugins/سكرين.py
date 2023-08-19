"""
`Credits` @amnd33p
from ..helpers.utils import _format
Modified by @Zed-Thon
"""

import io
import traceback
from datetime import datetime

import requests
from selenium import webdriver
from validators.url import url

from zthon import zedub

from ..Config import Config
from ..core.managers import edit_or_reply
from . import reply_id

plugin_category = "العروض"


@zedub.zed_cmd(
    pattern="(سكرين|ss) ([\s\S]*)",
    command=("سكرين", plugin_category),
    info={
        "header": "لـ اخذ لقطـة شاشـه لـ المواقـع",
        "الاستخـدام": "{tr}سكرين + رابـط",
        "مثــال": "{tr}سكرين https://github.com",
    },
)
async def _(event):
    "لـ اخذ لقطـة شاشـه لـ المواقـع"
    if Config.CHROME_BIN is None:
        return await edit_or_reply(
            event, "Need to install Google Chrome. Module Stopping."
        )
    zzevent = await edit_or_reply(event, "**- جـارِ اخـذ لقطـة شاشـه للصفحـه...**")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.CHROME_BIN
        await event.edit("**- جـارِ الاتصـال بجـوجل كـروم ...**")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        cmd = event.pattern_match.group(1)
        input_str = event.pattern_match.group(2)
        inputstr = input_str
        rmsg = await event.get_reply_message()
        if not inputstr and rmsg:
            inputstr = rmsg.text
        if not inputstr and not rmsg:
            return await zzevent.edit("**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ...**")
        if cmd == "سكرين":
            caturl = url(inputstr)
            if not inputstr:
                return await zzevent.edit("**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ...**")
            if not caturl:
                inputstr = f"http://{input_str}"
                caturl = url(inputstr)
            if not caturl:
                return await zzevent.edit("**- عـذراً .. الرابـط المدخـل ليس رابـط مدعـوم ؟!**")
        if cmd == "ss":
            inputstr = f"https://www.google.com/search?q={input_str}"
        driver.get(inputstr)
        await zzevent.edit("**- جـارِ رفـع لقطـة شاشـه للصفحـه...**")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
        )
        driver.set_window_size(width + 100, height + 100)
        # Add some pixels on top of the calculated dimensions
        # for good measure to make the scroll bars disappear
        im_png = driver.get_screenshot_as_png()
        # saves screenshot of entire page
        await zzevent.edit("**- تم إغـلاق جوجـل كـروم ✓**")
        driver.close()
        message_id = await reply_id(event)
        end = datetime.now()
        ms = (end - start).seconds
        hmm = f"**⎉╎المـوقع : **{input_str} \n**⎉╎ الوقت المستغـرق : {ms} ثانيـه**\n**⎉╎تم اخـذ لقطـة شاشـه .. بنجـاح ✓**"
        await zzevent.delete()
        with io.BytesIO(im_png) as out_file:
            out_file.name = f"{input_str}.PNG"
            await event.client.send_file(
                event.chat_id,
                out_file,
                caption=hmm,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True,
            )
    except Exception:
        await zzevent.edit(f"`{traceback.format_exc()}`")


@zedub.zed_cmd(
    pattern="لقطه ([\s\S]*)",
    command=("لقطه", plugin_category),
    info={
        "header": "لـ اخذ لقطـة شاشـه لـ المواقـع",
        "الوصـف": "For functioning of this command you need to set SCREEN_SHOT_LAYER_ACCESS_KEY var",
        "الاستخـدام": "{tr}لقطه + رابـط",
        "مثــال": "{tr}لقطه https://github.com",
    },
)
async def _(event):
    "لـ اخذ لقطـة شاشـه لـ المواقـع"
    start = datetime.now()
    message_id = await reply_id(event)
    if Config.SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        return await edit_or_reply(
            event,
            "`Need to get an API key from https://screenshotlayer.com/product and need to set it SCREEN_SHOT_LAYER_ACCESS_KEY !`",
        )
    zzevent = await edit_or_reply(event, "**- جـارِ اخـذ لقطـة شاشـه للصفحـه...**")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    inputstr = input_str
    caturl = url(inputstr)
    if not caturl:
        inputstr = f"http://{input_str}"
        caturl = url(inputstr)
    if not caturl:
        return await zzevent.edit("**- عـذراً .. الرابـط المدخـل ليس رابـط مدعـوم ؟!**")
    response_api = requests.get(
        sample_url.format(
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY, inputstr, "1", "2560x1440", "PNG", "1"
        )
    )
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    end = datetime.now()
    ms = (end - start).seconds
    hmm = f"**⎉╎المـوقع : **{input_str} \n**⎉╎ الوقت المستغـرق : {ms} ثانيـه**\n**⎉╎تم اخـذ لقطـة شاشـه .. بنجـاح ✓**"
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await event.client.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=hmm,
                    force_document=True,
                    reply_to=message_id,
                )
                await zzevent.delete()
            except Exception as e:
                await zzevent.edit(str(e))
    else:
        await zzevent.edit(f"`{response_api.text}`")
