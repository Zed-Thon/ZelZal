from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply


@zedub.zed_cmd(pattern="انضمام ([\s\S]*)")
async def lol(event):
    a = event.text
    bol = a[5:]
    sweetie = "- جاري الانضمام الى المجموعة انتظر قليلا  ."
    await event.reply(sweetie, parse_mode=None, link_preview=None)
    try:
        await zedub(functions.channels.JoinChannelRequest(bol))
        await event.edit("**- تم الانضمام بنجاح  ✓**")
    except Exception as e:
        await event.edit(str(e))


@zedub.zed_cmd(pattern="اضافه ([\s\S]*)")
async def _(event):
    to_add_users = event.pattern_match.group(1)
    if not event.is_channel and event.is_group:
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                    )
                )
            except Exception as e:
                return await edit_delete(event, f"`{str(e)}`", 5)
    else:
        for user_id in to_add_users.split(" "):
            try:
                await event.client(
                    functions.channels.InviteToChannelRequest(
                        channel=event.chat_id, users=[user_id]
                    )
                )
            except Exception as e:
                return await edit_delete(event, f"`{e}`", 5)

    await edit_or_reply(event, f"**{to_add_users} تم اضافته بنجاح ✓**")


@zedub.zed_cmd(pattern="ضيف ([\s\S]*)", groups_only=True)
async def get_users(event):
    legen_ = event.text[10:]
    input_str = event.pattern_match.group(1)
    zedub_chat = legen_.lower
    zedb = await edit_or_reply(event, f"**جارِ اضأفه الاعضاء من  ** {legen_}")
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await zedb.edit("**⎉╎ جـارِ إتمـام العمليـة إنتظـر ⅏ . . .**")
    else:
        await zedb.edit("**⎉╎ جـارِ إتمـام العمليـة إنتظـر ⅏ . . .**")
    if event.is_private:
        return await zedb.edit("**╮  لا استطـيع اضافـة الاعضـاء هـنا 𓅫╰**")
    s = 0
    f = 0
    error = "None"
    chat = await event.client.get_entity(input_str)
    await zedb.edit("**⎉╎حالة الأضافة:**\n\n**⎉╎تتم جمع معلومات المستخدمين 🔄 ...⏣**")
    async for user in event.client.iter_participants(chat):
        try:
            if error.startswith("Too"):
                return await zedb.edit(f"**حالة الأضافة انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`")
            await zedub(InviteToChannelRequest(channel=event.chat_id, users=[user.id]))
            s = s + 1
            await zedb.edit(f"**⎉╎تتم الأضافة **\n\n• اضيف `{s}` \n•  خطأ بأضافة `{f}` \n\n**× اخر خطأ:** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await zedb.edit(f"**⎉╎اڪتملت الأضافة ✅** \n\n• تم بنجاح اضافة `{s}` \n• خطأ بأضافة `{f}`")
