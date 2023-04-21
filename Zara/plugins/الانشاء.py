from telethon.tl import functions

from .. import zedub
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..utils.tools import create_supergroup

plugin_category = "الادوات"


@zedub.zed_cmd(
    pattern="انشاء (كروب|خارق|قناه) ([\s\S]*)",
    command=("انشاء", plugin_category),
    info={
        "header": "لـ إنشـاء (كروب خارق/كروب/قناه) باستخـدام البـوت",
        "امر اضافي": {
            "خارق": "لـ إنشـاء مجمـوعـة خـارقـه",
            "كروب": "لـ إنشـاء مجمـوعـة",
            "قناه": "لـ إنشـاء قنـاة",
        },
        "الاستخـدام": "{tr}انشاء (خارق/كروب/قناه) + اسـم (القنـاة/الكـروب)",
        "مثــال": "{tr}انشاء قناه زدثون",
    },
)
async def _(event):
    "لـ إنشـاء (كروب خارق/كروب/قناه) باستخـدام البـوت"
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "قناه":
        descript = "**⎉╎هـذه القنـاة تم إنشائهـا بواسطـة .. زدثــون™**"
    else:
        descript = "**⎉╎هـذا المجمـوعـه تم إنشائهـا بواسطـة .. زدثــون™**"
    if type_of_group == "كروب":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(
                    users=[Config.TG_BOT_USERNAME],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event, f"**⎉╎الكـروب `{group_name}` تم إنشـائه.. بنجـاح✓** \n**⎉╎الرابـط** {result.link}"
            )
        except Exception as e:
            await edit_delete(event, f"**- خطـأ :**\n{str(e)}")
    elif type_of_group == "قناه":
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=descript,
                    megagroup=False,
                )
            )
            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event,
                f"**⎉╎القنـاة `{group_name}` تم انشائهـا .. بنجـاح✓** \n**⎉╎الرابـط** {result.link}",
            )
        except Exception as e:
            await edit_delete(event, f"**- خطـأ :**\n{e}")
    elif type_of_group == "خارق":
        answer = await create_supergroup(
            group_name, event.client, Config.TG_BOT_USERNAME, descript
        )
        if answer[0] != "error":
            await edit_or_reply(
                event,
                f"**⎉╎الكـروب الخـارق `{group_name}` تم إنشـائه.. بنجـاح✓** \n**⎉╎الرابـط** {answer[0].link}",
            )
        else:
            await edit_delete(event, f"**- خطـأ :**\n{answer[1]}")
    else:
        await edit_delete(event, "**- عـذراً .. قم باستخـدام الامـر بشكـل صحيـح ...**")
