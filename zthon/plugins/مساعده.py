from telethon import functions

from zthon import zedub

from ..Config import Config
from ..core import CMD_INFO, GRP_INFO, PLG_INFO
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

cmdprefix = Config.COMMAND_HAND_LER
OLDZED = Config.OLDZED

plugin_category = "الادوات"

hemojis = {
    "الادمن": "🧑🏻‍💻",
    "البوت": "🦾",
    "الترفيه": "🎮",
    "الخدمات": "🧩",
    "الادوات": "💡",
    "العروض": "🖥",
    "البحث": "🪄",
    "آخرى": "🖨",
}


def get_key(val):
    for key, value in PLG_INFO.items():
        for cmd in value:
            if val == cmd:
                return key
    return None


def getkey(val):
    for key, value in GRP_INFO.items():
        for plugin in value:
            if val == plugin:
                return key
    return None


async def cmdinfo(input_str, event, plugin=False):
    if input_str[0] == cmdprefix:
        input_str = input_str[1:]
    try:
        about = CMD_INFO[input_str]
    except KeyError:
        if plugin:
            await edit_delete(
                event,
                f"**There is no plugin or command as **`{input_str}`** in your bot.**",
            )
            return None
        await edit_delete(
            event, f"**There is no command as **`{input_str}`** in your bot.**"
        )
        return None
    except Exception as e:
        await edit_delete(event, f"**- خطـأ **\n`{e}`")
        return None
    outstr = f"**- الامــر :** `{cmdprefix}{input_str}`\n"
    plugin = get_key(input_str)
    if plugin is not None:
        outstr += f"**- الاضــافـه :** `{plugin}`\n"
        category = getkey(plugin)
        if category is not None:
            outstr += f"**- الـفـئــه :** `{category}`\n\n"
    outstr += f"**✘  الـوصــف :**\n{about[0]}"
    return outstr


async def plugininfo(input_str, event, flag):
    try:
        cmds = PLG_INFO[input_str]
    except KeyError:
        outstr = await cmdinfo(input_str, event, plugin=True)
        return outstr
    except Exception as e:
        await edit_delete(event, f"**Error**\n`{e}`")
        return None
    if len(cmds) == 1 and (flag is None or (flag and flag != "-p")):
        outstr = await cmdinfo(cmds[0], event, plugin=False)
        return outstr
    outstr = f"**- الاضـافـه : **`{input_str}`\n"
    outstr += f"**- عـدد الاوامــر :** `{len(cmds)}`\n"
    category = getkey(input_str)
    if category is not None:
        outstr += f"**- الـفـئـه :** `{category}`\n\n"
    for cmd in sorted(cmds):
        outstr += f"•  **الامــر :** `{cmdprefix}{cmd}`\n"
        try:
            outstr += f"•  **الـوصـف :** `{CMD_INFO[cmd][1]}`\n\n"
        except IndexError:
            outstr += "•  **الـوصــف :** `None`\n\n"
    outstr += f"**📋 لـ شــرح الاوامــر : ** `{cmdprefix}help <command name>`\
        \n**🖇 مـلاحظــه : **If command name is same as plugin name then use this `{cmdprefix}help -c <command name>`."
    return outstr


async def grpinfo():
    outstr = "**Plugins in ZThon are:**\n\n"
    outstr += f"**👩‍💻 Usage : ** `{cmdprefix}help <plugin name>`\n\n"
    category = ["الادمن", "البوت", "الترفيه", "الخدمات", "الادوات", "العروض", "البحث"]
    if OLDZED:
        category.append("آخرى")
    for cat in category:
        plugins = GRP_INFO[cat]
        outstr += f"**{hemojis[cat]} {cat.title()} **({len(plugins)})\n"
        for plugin in plugins:
            outstr += f"`{plugin}`  "
        outstr += "\n\n"
    return outstr


async def cmdlist():
    outstr = "**Total list of Commands in your ZThon are :**\n\n"
    category = ["الادمن", "البوت", "الترفيه", "الخدمات", "الادوات", "العروض", "البحث"]
    if OLDZED:
        category.append("آخرى")
    for cat in category:
        plugins = GRP_INFO[cat]
        outstr += f"**{hemojis[cat]} {cat.title()} ** - {len(plugins)}\n\n"
        for plugin in plugins:
            cmds = PLG_INFO[plugin]
            outstr += f"• **{plugin.title()} has {len(cmds)} commands**\n"
            for cmd in sorted(cmds):
                outstr += f"  - `{cmdprefix}{cmd}`\n"
            outstr += "\n"
    outstr += f"**👩‍💻 Usage : ** `{cmdprefix}help -c <command name>`"
    return outstr


@zedub.zed_cmd(
    pattern="مساعده ?(-c|-p|-t)? ?([\s\S]*)?",
    command=("مساعده", plugin_category),
    info={
        "header": "To get guide for ZThon.",
        "description": "To get information or guide for the command or plugin",
        "note": "if command name and plugin name is same then you get guide for plugin. So by using this flag you get command guide",
        "flags": {
            "c": "To get info of command.",
            "p": "To get info of plugin.",
            "t": "To get all plugins in text format.",
        },
        "الاستـخـدام": [
            "{tr}help (plugin/command name)",
            "{tr}help -c (command name)",
        ],
        "مثــال": ["{tr}help help", "{tr}help -c help"],
    },
)
async def _(event):
    "To get guide for ZThon."
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if flag and flag == "-c" and input_str:
        outstr = await cmdinfo(input_str, event)
        if outstr is None:
            return
    elif input_str:
        outstr = await plugininfo(input_str, event, flag)
        if outstr is None:
            return
    elif flag == "-t":
        outstr = await grpinfo()
    else:
        results = await event.client.inline_query(Config.TG_BOT_USERNAME, "help")
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
        return
    await edit_or_reply(event, outstr)


@zedub.zed_cmd(
    pattern="مساعدة(?:\s|$)([\s\S]*)",
    command=("مساعدة", plugin_category),
    info={
        "header": "To show list of cmds.",
        "الاستـخـدام": [
            "{tr}cmds for all cmds",
            "{tr}cmds <plugin name> for paticular plugin",
        ],
    },
)
async def _(event):
    "To get list of commands."
    if input_str := event.pattern_match.group(1):
        try:
            cmds = PLG_INFO[input_str]
        except KeyError:
            return await edit_delete(event, "__Invalid plugin name recheck it.__")
        except Exception as e:
            return await edit_delete(event, f"**Error**\n`{e}`")
        outstr = f"• **{input_str.title()} has {len(cmds)} commands**\n"
        for cmd in cmds:
            outstr += f"  - `{cmdprefix}{cmd}`\n"
        outstr += f"**👩‍💻 Usage : ** `{cmdprefix}help -c <command name>`"
    else:
        outstr = await cmdlist()
    await edit_or_reply(
        event, outstr, aslink=True, linktext="Total Commands of ZThon are :"
    )


@zedub.zed_cmd(
    pattern="s ([\s\S]*)",
    command=("s", plugin_category),
    info={
        "header": "To search commands.",
        "الاستـخـدام": "{tr}s song",
    },
)
async def _(event):
    "To search commands."
    cmd = event.pattern_match.group(1)
    if found := [i for i in sorted(list(CMD_INFO)) if cmd in i]:
        out_str = "".join(f"`{i}`    " for i in found)
        out = f"**I found {len(found)} command(s) for: **`{cmd}`\n\n{out_str}"
        out += f"\n\n__For more info check {cmdprefix}help -c <command>__"
    else:
        out = f"I can't find any such command `{cmd}` in ZThon"
    await edit_or_reply(event, out)


@zedub.zed_cmd(
    pattern="المركز$",
    command=("المركز", plugin_category),
    info={
        "header": "To show dc of your account.",
        "الاستـخـدام": "{tr}dc",
    },
)
async def _(event):
    "To get dc of your bot"
    result = await event.client(functions.help.GetNearestDcRequest())
    result = f"**Dc details of your account:**\
              \n**Country :** {result.country}\
              \n**Current Dc :** {result.this_dc}\
              \n**Nearest Dc :** {result.nearest_dc}\
              \n\n**List Of Telegram Data Centres:**\
              \n**DC1 : **Miami FL, USA\
              \n**DC2 :** Amsterdam, NL\
              \n**DC3 :** Miami FL, USA\
              \n**DC4 :** Amsterdam, NL\
              \n**DC5 : **Singapore, SG\
                "
    await edit_or_reply(event, result)
