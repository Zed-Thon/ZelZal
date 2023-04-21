import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from . import zedub

from ..core.managers import edit_or_reply
from . import Build_Poll, reply_id

plugin_category = "البوت"


@zedub.zed_cmd(
    pattern="استفتاء(?:\s|$)([\s\S]*)",
    command=("استفتاء", plugin_category),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(catpoll):
    "To create a poll"
    reply_to_id = await reply_id(catpoll)
    string = "".join(catpoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["- ايي 😊✌️", "- لاع 😏😕", "- مادري 🥱🙄"])
        try:
            await catpoll.client.send_message(
                catpoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="تحبوني ؟",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await catpoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                catpoll, "**⌔∮ الاستفتاء المستخدم غير صالح (قد تكون المعلومات طويلة جدا).**"
            )
        except ForbiddenError:
            await edit_or_reply(catpoll, "**⌔∮ هذه الدردشة تحظر استطلاعات الرأي. **")
        except exception as e:
            await edit_or_reply(catpoll, str(e))
    else:
        catinput = string.split("|")
        if len(catinput) > 2 and len(catinput) < 12:
            options = Build_Poll(catinput[1:])
            try:
                await catpoll.client.send_message(
                    catpoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=catinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await catpoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    catpoll,
                    "**⌔∮ الاستفتاء المستخدم غير صالح (قد تكون المعلومات طويلة جدا).**",
                )
            except ForbiddenError:
                await edit_or_reply(catpoll, "**⌔∮ هذه الدردشة تحظر استطلاعات الرأي. **")
            except Exception as e:
                await edit_or_reply(catpoll, str(e))
        else:
            await edit_or_reply(
                catpoll,
                "**⌔∮عـذراً عـزيـزي .. انت تكتب الامـر بشكـل خاطئ يجب عليك اعـادة كتابتـه بالشكـل التـالي :**\n\n`.استفتاء السؤال | الجواب الاول | الجواب الثاني`\n**⌔∮لا تنسـى كتابـة الرمـز | بيـن كـل جـواب والثـاني**",
            )
