import asyncio
import contextlib
import os
import sys
from asyncio.exceptions import CancelledError

import heroku3
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot import HEROKU_APP, UPSTREAM_REPO_URL, zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _zedutils
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)

plugin_category = "الادوات"
cmdhd = Config.COMMAND_HAND_LER
ENV = bool(os.environ.get("ENV", False))
LOGS = logging.getLogger(__name__)
# -- Constants -- #

HEROKU_APP_NAME = Config.HEROKU_APP_NAME or None
HEROKU_API_KEY = Config.HEROKU_API_KEY or None
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
OLDZED = Config.OLDZED
heroku_api = "https://api.heroku.com"

UPSTREAM_REPO_BRANCH = Config.UPSTREAM_REPO_BRANCH

REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)


# -- Constants End -- #

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requirements_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"  • {c.summary} ({c.committed_datetime.strftime(d_form)}) <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


async def print_changelogs(event, ac_br, changelog):
    changelog_str = (
        f"𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n** ⪼ يوجـد تحـديث جديد لسورس زد ثـون ༗.**\n\n`{changelog}`\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆰 𝙎𝙊𝙐𝙍𝘾𝞝 𝘿𝙀𝙑 - @ZedThon 𓆪"
    )
    if len(changelog_str) > 4096:
        await event.edit("`Changelog is too big, view the file to see it.`")
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
        )
        os.remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id,
            changelog_str,
            reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def update_bot(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    sandy = await event.edit(
        "𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ تم التحديث بنجاح ✅**\n ** جارٍ إعادة تشغيل بوت زد ثـون ، انتظر 𓆰.**"
    )
    await event.client.reload(sandy)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is None:
        return await event.edit("`Please set up`  **HEROKU_API_KEY**  ` Var...`")
    heroku = heroku3.from_key(HEROKU_API_KEY)
    heroku_applications = heroku.apps()
    if HEROKU_APP_NAME is None:
        await event.edit(
            "`Please set up the` **HEROKU_APP_NAME** `Var`"
            " to be able to deploy your userbot...`"
        )
        repo.__del__()
        return
    heroku_app = next(
        (app for app in heroku_applications if app.name == HEROKU_APP_NAME),
        None,
    )

    if heroku_app is None:
        await event.edit(
            f"{txt}\n" "بيانات اعتماد هيروكو غير صالحة لتنصيب زد ثـون"
        )
        return repo.__del__()
    sandy = await event.edit(
        "**تنصيب تحديث زد ثـون قيد التقدم ، يرجى الانتظار حتى تنتهي العملية ، وعادة ما يستغرق التحديث من 4 إلى 5 دقائق.**"
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS.error(e)
    ups_rem.fetch(ac_br)
    repo.git.reset("--hard", "FETCH_HEAD")
    heroku_git_url = heroku_app.git_url.replace(
        "https://", f"https://api:{HEROKU_API_KEY}@"
    )

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(heroku_git_url)
    else:
        remote = repo.create_remote("heroku", heroku_git_url)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as error:
        await event.edit(f"{txt}\n**Error log:**\n`{error}`")
        return repo.__del__()
    build_status = heroku_app.builds(order_by="created_at", sort="desc")[0]
    if build_status.status == "failed":
        return await edit_delete(
            event, "`Build failed!\n" "Cancelled or there were some errors...`"
        )
    try:
        remote.push("master:main", force=True)
    except Exception as error:
        await event.edit(f"{txt}\n**Here is the error log:**\n`{error}`")
        return repo.__del__()
    await event.edit("`Deploy was failed. So restarting to update`")
    with contextlib.suppress(CancelledError):
        await event.client.disconnect()
        if HEROKU_APP is not None:
            HEROKU_APP.restart()


@zedub.zed_cmd(
    pattern="تحديث(| الان)?$",
    command=("update", plugin_category),
    info={
        "header": "لـ تحـديث بــوت زدثـــون",
        "الاستـخـدام": [
            "{tr}تحديث",
            "{tr}تحديث الان",
            "{tr}تحديث البوت",
        ],
    },
)
async def upstream(event):
    "To check if the bot is up to date and update if specified"
    conf = event.pattern_match.group(1).strip()
    event = await edit_or_reply(event, "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ جاري البحث عن التحديثات  🌐.. 𓆰،**")
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    if ENV and (HEROKU_API_KEY is None or HEROKU_APP_NAME is None):
        return await edit_or_reply(
            event, "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n** ⪼ اضبط الفـارات المطلوبة أولاً لتحديث بوت زدثــون 𓆰،**"
        )
    try:
        txt = (
            "**- عـذراً .. لا يمكن لبرنامج التحديث المتابعة بسبب** "
            + "**حـدوث بعض المشـاكل**\n\n**تتبع السجل:**\n"
        )

        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\nالدليل {error} غير موجود")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`فشل مبكر! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`Unfortunately, the directory {error} does not seem to be a git repository.\nBut we can fix that by force updating the userbot using .update now.`"
            )

        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            "**[UPDATER]:**\n"
            f"`Looks like you are using your own custom branch ({ac_br}). "
            "in that case, Updater is unable to identify "
            "which branch is to be merged. "
            "please checkout to any official branch`"
        )
        return repo.__del__()
    with contextlib.suppress(BaseException):
        repo.create_remote("upstream", off_repo)
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    # Special case for deploy
    if changelog == "" and not force_update:
        await event.edit(
            "\n𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿  - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ سورس زد ثـون محدث لأخر اصدار ༗. **"
        )
        return repo.__del__()
    if conf == "" and not force_update:
        await print_changelogs(event, ac_br, changelog)
        await event.delete()
        return await event.respond("𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n⪼ اضغط هنا **للتحديث السريع ↫ **[`{}تحديث الان`] او اضغط هنا **لتنصيب التحديث** وقد يستغرق 5 دقائق ↫ [`{}تحديث البوت`]")
    if force_update:
        await event.edit(
            "`Force-Syncing to latest stable userbot code, please wait...`"
        )
    if conf == "الان":
        await event.edit("𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ يتـم تحـديث بـوت زدثــون انتظـر 🌐..𓆰،**")
        await update_bot(event, repo, ups_rem, ac_br)
    return


@zedub.zed_cmd(
    pattern="تحديث البوت$",
)
async def upstream(event):
    if ENV:
        if HEROKU_API_KEY is None or HEROKU_APP_NAME is None:
            return await edit_or_reply(
                event, "`Set the required vars first to update the bot`"
            )
    elif os.path.exists("config.py"):
        return await edit_delete(
            event,
            f"I guess you are on selfhost. For self host you need to use `{cmdhd}update now`",
        )
    event = await edit_or_reply(event, "𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ يتم تنصيب التحديث  انتظر 🌐 𓆰،**")
    off_repo = "https://github.com/Zed-Thon/nekopack"
    os.chdir("/app")
    try:
        txt = (
            "`Oops.. Updater cannot continue due to "
            + "some problems occured`\n\n**LOGTRACE:**\n"
        )

        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    with contextlib.suppress(BaseException):
        repo.create_remote("upstream", off_repo)
    ac_br = repo.active_branch.name
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    await event.edit("**تنصيب تحديث زد ثـون قيد التقدم ، يرجى الانتظار حتى تنتهي العملية ، وعادة ما يستغرق التحديث من 4 إلى 5 دقائق.**")
    await deploy(event, repo, ups_rem, ac_br, txt)


@zedub.zed_cmd(
    pattern="(2|1)زد$",
    command=("switch", plugin_category),
    info={
        "header": "To switch between ZThon2 & ZThon1(For extra nsfw and gali).",
        "الاستـخـدام": [
            "{tr}زد2",
            "{tr}زد1",
        ],
    },
)
async def variable(event):
    "To switch between 1 & 2 ZThon"
    switch = "OLDZED"
    cmd = event.pattern_match.group(1).lower()
    if ENV:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            return await edit_delete(
                event,
                "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",
            )
        app = Heroku.app(Config.HEROKU_APP_NAME)
        heroku_var = app.config()
        if cmd == "2":
            if OLDZED:
                await edit_or_reply(
                    event, "`Changing ZThon1 to ZThon2 wait for 2-3 minutes.`"
                )
                del heroku_var[switch]
                return
            await edit_delete(event, "`You already using ZThon2`", 6)
        else:
            if OLDZED:
                return await edit_delete(event, "`You already using ZThon1`", 6)
            await edit_or_reply(
                event, "`Changing ZThon2 to ZThon1 wait for 2-3 minutes.`"
            )
            heroku_var[switch] = "True"
    elif os.path.exists(config):
        string = ""
        match = None
        with open(config, "r") as f:
            configs = f.readlines()
        for i in configs:
            if switch in i:
                match = True
            else:
                string += f"{i}"
        if cmd == "2":
            if match and not OLDZED:
                zed = await edit_or_reply(
                    event, f"`Changing ZThon1 to ZThon2 wait for 2-3 minutes.`"
                )
                with open(config, "w") as f1:
                    f1.write(string)
                    f1.close()
                await _zedutils.runcmd("rm -rf badcatext")
                return await event.client.reload(zed)
            await edit_delete(event, "`You already using ZThon2`")
        elif cmd == "1":
            if match and OLDZED:
                return await edit_or_reply(event, "`You already using ZThon1`")
            string += f'    {switch} = "True"\n'
            zed = await edit_or_reply(
                event, "`Changing ZThon2 to ZThon1 wait for 2-3 minutes.`"
            )
            with open(config, "w") as f1:
                f1.write(string)
                f1.close()
            await event.client.reload(zed)
    else:
        await edit_delete(event, "`There no Config file , You can't use this plugin.`")
