import datetime
import inspect
import re
import sys
import traceback
from pathlib import Path

from .. import CMD_LIST, LOAD_PLUG, SUDO_LIST
from ..Config import Config
from ..core.data import _sudousers_list, blacklist_chats_list
from ..core.events import MessageEdited, NewMessage
from ..core.logger import logging
from ..core.session import zedub
from ..helpers.utils.format import paste_message
from ..helpers.utils.utils import runcmd
from ..sql_helper.globals import gvarstatus

LOGS = logging.getLogger(__name__)


def admin_cmd(pattern=None, command=None, **args):  # sourcery no-metrics
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    if pattern is not None:
        if pattern.startswith(r"\#"):
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        else:
            if len(Config.COMMAND_HAND_LER) == 2:
                zedreg = "^" + Config.COMMAND_HAND_LER
                reg = Config.COMMAND_HAND_LER[1]
            elif len(Config.COMMAND_HAND_LER) == 1:
                zedreg = "^\\" + Config.COMMAND_HAND_LER
                reg = Config.COMMAND_HAND_LER
            args["pattern"] = re.compile(zedreg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
    args["outgoing"] = True
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        args["incoming"] = True
        del args["allow_sudo"]
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
    if gvarstatus("blacklist_chats") is not None:
        args["blacklist_chats"] = True
        args["chats"] = blacklist_chats_list()
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]
    return NewMessage(**args)


def sudo_cmd(pattern=None, command=None, **args):  # sourcery no-metrics
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith(r"\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                SUDO_LIST[file_test].append(cmd)
            except BaseException:
                SUDO_LIST.update({file_test: [cmd]})
        else:
            if len(Config.SUDO_COMMAND_HAND_LER) == 2:
                zedreg = "^" + Config.SUDO_COMMAND_HAND_LER
                reg = Config.SUDO_COMMAND_HAND_LER[1]
            elif len(Config.SUDO_COMMAND_HAND_LER) == 1:
                zedreg = "^\\" + Config.SUDO_COMMAND_HAND_LER
                reg = Config.COMMAND_HAND_LER
            args["pattern"] = re.compile(zedreg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                SUDO_LIST[file_test].append(cmd)
            except BaseException:
                SUDO_LIST.update({file_test: [cmd]})
    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(_sudousers_list())
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]
    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
    # add blacklist chats, UB should not respond in these chats
    if gvarstatus("blacklist_chats") is not None:
        args["blacklist_chats"] = True
        args["chats"] = blacklist_chats_list()
    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]
    # check if the plugin should listen for outgoing 'messages'
    if gvarstatus("sudoenable") is not None:
        return NewMessage(**args)


def errors_handler(func):
    async def wrapper(errors):
        try:
            await func(errors)
        except BaseException:
            if Config.PRIVATE_GROUP_BOT_API_ID != 0:
                return
            date = (datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
            ftext = f"\nيتم تحميل هذا الملف فقط هنا ،\
                                  \n\nنسجل فقـط تقريـر الخطـأ وتـاريخـه ،\
                                  \n\nفقـط قـم بإعـادة توجيـه هـذه الرسـالة إلى مطـور السـورس @zzzzl1l\
                                  \n\n-------- معلومات عن الخطـأ--------\
                                  \nالتاريخ: {date}\nايدي المجموعه: {str(check.chat_id)}\
                                  \nايدي المرسل: {str(check.sender_id)}\
                                  \n\nمشغل الحدث:\n{str(check.text)}\
                                  \n\nمعلومات المشكله:\n{str(traceback.format_exc())}\
                                  \n\nنص الخطأ:\n{str(sys.exc_info()[1])}"
            new = {
                "error": str(sys.exc_info()[1]),
                "date": datetime.datetime.now(),
            }

            ftext += "\n\n--------معلومات عن الخطـأ--------"
            command = 'git log --pretty=format:"%an: %s" -5'
            ftext += "\n\n\nاخر 5 تعديلات:\n"
            output = (await runcmd(command))[:2]
            result = output[0] + output[1]
            ftext += result
            pastelink = await paste_message(ftext)
            text = "**هنالك مشكله معينه لديك**\n\n"
            link = "[𐇮 𝙕𝞝𝙇𝙕𝘼𝙇 الهہـيـٖ͡ـ͢ـبـه 𐇮](https://t.me/zzzzl1l)"
            text += "اذا اردت يمكنك التبليغ عن المشكله"
            text += f"- فقط قم بتوجيه الرسالة الى  {link}.\n"
            text += f"**التقرير عن الخطأ : ** [{new['error']}]({pastelink})"
            await check.client.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
            )

    return wrapper


def register(**args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", True)
    allow_sudo = args.get("allow_sudo", False)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass

            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        except BaseException:
            pass

    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    if gvarstatus("blacklist_chats") is not None:
        args["blacklist_chats"] = True
        args["chats"] = blacklist_chats_list()

    def decorator(func):
        if not disable_edited:
            zedub.add_event_handler(func, MessageEdited(**args))
        zedub.add_event_handler(func, NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def command(**args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    allow_sudo = args.get("allow_sudo", None)
    allow_edited_updates = args.get("allow_edited_updates", False)
    args["incoming"] = args.get("incoming", False)
    args["outgoing"] = True
    if bool(args["incoming"]):
        args["outgoing"] = False
    try:
        if pattern is not None and not pattern.startswith("(?i)"):
            args["pattern"] = "(?i)" + pattern
    except BaseException:
        pass
    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        except BaseException:
            pass
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        args["incoming"] = True
    del allow_sudo
    try:
        del args["allow_sudo"]
    except BaseException:
        pass
    if gvarstatus("blacklist_chats") is not None:
        args["blacklist_chats"] = True
        args["chats"] = blacklist_chats_list()

    def decorator(func):
        if allow_edited_updates:
            zedub.add_event_handler(func, MessageEdited(**args))
        zedub.add_event_handler(func, NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except BaseException:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator
