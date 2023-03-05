# plugin by @Dar4k ~ @R0R77
# ported to ZThon by @zzzzl1l
import asyncio
import random

import requests
import telethon
from telethon.sync import functions
from user_agent import generate_user_agent

from zthon import zedub

a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"
z = 'sdfghjklzwerty1234567890uioxcvbqpanm'


ZelzalChecler_cmd = (
    "𓆩 [𝖈𝖗 𝖘𝖔𝖚𝖗𝖈𝖊 - اوامـر الصيـد والتشيكـر](t.me/S_EG_P) 𓆪\n\n"
    "**✾╎قـائمـة اوامـر تشيكـر صيـد معـرفات تيليجـرام :** \n\n"
    "**- النـوع :**\n"
    "**(** `سداسي حرفين`/`ثلاثيات`/`سداسيات`/`بوتات`/`خماسي حرفين`/`خماسي`/`سباعيات` **)**\n\n"
    "`.صيد` + النـوع\n"
    "**⪼ لـ صيـد يـوزرات عشوائيـه على حسب النـوع**\n\n"
    "`.تثبيت` + اليوزر\n"
    "**⪼ لـ تثبيت اليـوزر بقنـاة معينـه اذا اصبح متاحـاً يتم اخـذه**\n\n"
    "`.حالة الصيد`\n"
    "**⪼ لـ معرفـة حالـة تقـدم عمليـة الصيـد**\n\n"
    "`.حالة التثبيت`\n"
    "**⪼ لـ معرفـة حالـة تقـدم التثبيت التلقـائـي**\n\n"
    "`.ايقاف الصيد`\n"
    "**⪼ لـ إيقـاف عمليـة الصيـد الجاريـه**\n\n"
    "`.ايقاف التثبيت`\n"
    "**⪼ لـ إيقـاف عمليـة التثبيت التلقـائـي**\n\n"
)


trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "ثلاثيات":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    elif choice == "سداسيات":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        # random.shuffle(f)
        username = "".join(f)
        username = username + "bot"

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)

        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعيات":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        return "error"
    return username


@zedub.zed_cmd(pattern="الصيد")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalChecler_cmd)


@zedub.zed_cmd(pattern="صيد (.*)")
async def hunterusername(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"**- جاري بـدء الصيـد علـى القنـاة** ⎌ @{ch} ")
    except:
        try:
            ch = await zedub(
                functions.channels.CreateChannelRequest(
                    title="⎉ تشيكــر كرستين 𝖈𝖗 𝖘𝖔𝖚𝖗𝖈𝖊 ⎉",
                    about="This channel to hunt username by - @S_EG_P ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**⎉╎تم بـدء الصيـد .. بنجـاح ☑️**\n**⎉╎لمعرفـة حالة تقـدم عمليـة الصيـد ارسـل (**`.حالة الصيد`**)**")
        except Exception as e:
            await zedub.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
            )
    isclaim.clear()
    isclaim.append("on")
    for i in range(19000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يـرجى وضـع النـوع بشكـل صحيـح ...!!**")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await zedub(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"**⎉╎تم صيـد المعـرف (** @{username} **)** 🎣\n**⎉╎بواسطـة كرستين :** @S_EG_P\n**⎉╎سجل العمليـة :** {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await zedub.send_message(
                    event.chat_id,
                    f"**- للاسف تبندت .. مدة الباند ({e.seconds}) ثانية ..**",
                    event.chat_id,
                    f"**- للاسف تبندت .. مدة الباند ({e.seconds}) ثانية ..**",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await zedub.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")
    await event.client.send_message(event.chat_id, "**- تم الانتهاء من الصيد .. بنجـاح ☑️**")


@zedub.zed_cmd(pattern="تثبيت (.*)")
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await zedub(
                functions.channels.CreateChannelRequest(
                    title="⎉ تشيكــر كرستين 𝖈𝖗 𝖘𝖔𝖚𝖗𝖈𝖊 ⎉",
                    about="This channel to hunt username by - @S_EG_P ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بـدء التثبيت .. بنجـاح ☑️**")
        except Exception as e:
            await zedub.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    for i in range(1000000000000):
        isav = check_user(username)
        if isav == True:
            try:
                await zedub(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"**⎉╎تم تثبيت المعـرف (** @{username} **)** 🎣\n**⎉╎بواسطـة كرستين :** @S_EG_P\n**⎉╎سجل العمليـة :** {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"**- المعرف @{username} غير صالح ؟!**"
                )
                break
            except telethon.errors.FloodError as e:
                await zedub.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await zedub.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                break
        else:
            pass
        trys2[0] += 1

        await asyncio.sleep(1.3)
    isclaim.clear()
    isclaim.append("off")
    await zedub.send_message(event.chat_id, "**- تم الانتهاء من التثبيت .. بنجـاح ☑️**")


@zedub.zed_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"**- الصيد وصل لـ({trys[0]}) من المحـاولات**")
    elif "off" in isclaim:
        await event.edit("**- لا توجد عمليـة صيد جاريـه حاليـاً ؟!**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@zedub.zed_cmd(pattern="حالة التثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        await event.edit("**-لقد حدث خطأ ما وتوقف الامر لديك**")


@zedub.zed_cmd(pattern="ايقاف الصيد")
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        return await event.edit("**- تم إيقـاف عمليـة الصيـد .. بنجـاح ✓**")
    elif "off" in isclaim:
        return await event.edit("**- لا توجد عمليـة صيد جاريـه حاليـاً ؟!**")
    else:
        return await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@zedub.zed_cmd(pattern="ايقاف التثبيت")
async def _(event):
    if "on" in isauto:
        isauto.clear()
        isauto.append("off")
        return await event.edit("**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in isauto:
        return await event.edit("**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        return await event.edit("**-لقد حدث خطأ ما وتوقف الامر لديك**")

