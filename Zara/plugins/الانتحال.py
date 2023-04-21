import html

from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest

from ..Config import Config
from . import ALIVE_NAME, BOTLOG, BOTLOG_CHATID, zedub, edit_delete, get_user_from_event
from ..sql_helper.globals import gvarstatus

plugin_category = "العروض"
DEFAULTUSER = gvarstatus("FIRST_NAME") or ALIVE_NAME
DEFAULTUSERBIO = Config.DEFAULT_BIO or "- ‏وحدي أضيء، وحدي أنطفئ انا قمري و كُل نجومي..🤍"
ANTHAL = gvarstatus("ANTHAL") or "(اعادة الحساب|اعادة|اعاده)"


@zedub.zed_cmd(pattern="نسخ(?:\s|$)([\s\S]*)")
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        return await edit_delete(event, f"**اووبس خطـأ بالانتحـال:**\n__{e}__")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**⎉╎تـم انتحـال الشخـص .. بنجـاح ༗**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحـــال\n ⪼ تم انتحـال حسـاب الشخـص ↫ [{first_name}](tg://user?id={user_id }) بنجاح ✅",
        )



@zedub.zed_cmd(pattern="انتحال(?:\s|$)([\s\S]*)")
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        return await edit_delete(event, f"**اووبس خطـأ بالانتحـال:**\n__{e}__")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**⎉╎تـم انتحـال الشخـص .. بنجـاح ༗**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحـــال\n ⪼ تم انتحـال حسـاب الشخـص ↫ [{first_name}](tg://user?id={user_id }) بنجاح ✅",
        )


@zedub.zed_cmd(pattern=f"{ANTHAL}$")
async def revert(event):
    firstname = DEFAULTUSER
    lastname = gvarstatus("LAST_NAME") or ""
    bio = DEFAULTUSERBIO
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=firstname))
    await event.client(functions.account.UpdateProfileRequest(last_name=lastname))
    await edit_delete(event, "**⎉╎تمت اعادة الحساب لوضعـه الاصلـي \n⎉╎والغـاء الانتحـال .. بنجـاح ✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#الغـاء_الانتحـال\n**⪼ تم الغـاء الانتحـال .. بنجـاح ✅**\n**⪼ تم إعـاده معلـوماتك الى وضعـها الاصـلي**",
        )
