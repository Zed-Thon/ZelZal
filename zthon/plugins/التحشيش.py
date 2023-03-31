import os
import shutil
from asyncio import sleep
import random

from telethon import events

from zthon import zedub
from zthon.core.logger import logging
from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id, get_user_from_event
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

zel_dev = (5176749470, 5426390871)
########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################

import random

from telethon import events


@zedub.zed_cmd(pattern="رابط الحذف")
async def _(zed):
    await edit_or_reply (zed, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 - 𝘿𝙀𝙇𝙀𝙏𝙀](t.me/ZedThon) 🗑♻️𓆪\n**𓍹━─━─━─━─𝙕𝞝𝘿─━─━─━─━𓍻**\n\n **✵│رابـط الحـذف ↬** https://telegram.org/deactivate \n\n\n **✵│بـوت الحـذف  ↬** @LC6BOT ")

########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################

@zedub.zed_cmd(pattern="رفع جلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n**✾╎تم رفعـه جلب 🐕‍🦺 في البـوت**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################

@zedub.zed_cmd(pattern="رفع مرتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه مـࢪتك مـشي نخـلف 🤰🏻😹🤤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################

@zedub.zed_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه تـاج 👑🔥**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################
 
@zedub.zed_cmd(pattern="رفع بكلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه بڪلبك 🖤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################

@zedub.zed_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم ** [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه بــ قلبـك .. نبـضك والوريـد 🖤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################

@zedub.zed_cmd(pattern="رفع قلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم ** [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه بــ قلبـك .. نبـضك والوريـد 🖤**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################
 
@zedub.zed_cmd(pattern="رفع جريذي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تـم رفعـه جـࢪيذي ۿنـا 😹🐀** ",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################


@zedub.zed_cmd(pattern="رفع فرخ(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**✾╎المستخـدم**  [{tag}](tg://user?id={user.id}) \n\n**✾╎تم رفعه فرخ هنا 🖕😹**",
    )


########################  SOURCE ZED ~ BY: ZelZal (@zzzzl1l)  ########################

ZelzalTHS_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗭𝗘𝗗𝗧𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر التحشيش](t.me/ZEDthon) 𓆪\n\n"
    "**- اضغـط ع الامـر للنسـخ ثـم قـم بالـرد ع الشخـص** \n\n"
    "**⪼** `.اوصف` \n"
    "**⪼** `.هينه` \n"
    "**⪼** `.نسبه الحب` \n"
    "**⪼** `.نسبه الانوثه` \n"
    "**⪼** `.نسبه الغباء` \n"
    "**⪼** `.نسبه الانحراف` \n"
    "**⪼** `.نسبه المثليه` \n"
    "**⪼** `.نسبه النجاح` \n"
    "**⪼** `.نسبه الكراهيه` \n"
    "**⪼** `.رفع تاج` \n"
    "**⪼** `.رفع بقلبي` \n"
    "**⪼** `.رفع مرتي` \n"
    "**⪼** `.رفع صاك` \n"
    "**⪼** `.رفع صاكه` \n"
    "**⪼** `.رفع حات` \n"
    "**⪼** `.رفع حاته` \n"
    "**⪼** `.رفع ورع` \n"
    "**⪼** `.رفع مزه` \n"
    "**⪼** `.رفع مرتبط` \n"
    "**⪼** `.رفع مرتبطه` \n"
    "**⪼** `.رفع حبيبي` \n"
    "**⪼** `.رفع خطيبتي` \n"
    "**⪼** `.رفع جلب` \n"
    "**⪼** `.رفع جريذي` \n"
    "**⪼** `.رفع فرخ` \n"
    "**⪼** `.رفع مطي` \n"
    "**⪼** `.رفع حمار` \n"
    "**⪼** `.رفع خروف` \n"
    "**⪼** `.رفع حيوان` \n"
    "**⪼** `.رفع بزون` \n"
    "**⪼** `.رفع زباله` \n"
    "**⪼** `.رفع منشئ` \n"
    "**⪼** `.رفع مدير` \n"
    "**⪼** `.رفع كواد` \n"
    "🛃 سيتـم اضـافة المزيـد من تخصيص الاوامـر بالتحديثـات الجـايه\n"
)


kettuet = [  
  "اكثر شي ينرفزك .. ؟!",
  "اخر مكان رحتله ..؟!",
  "سـوي تـاك @ لـ شخص تريـد تعترفلـه بشي ؟",
  "تغار ..؟!",
  "هـل تعتقـد ان في أحـد يراقبـك 👩🏼‍💻..؟!",
  "أشخاص ردتهم يبقون وياك ومن عرفو هلشي سوو العكس صارت معك؟",
  "ولادتك بنفس المكان الي هسة عايش بي او لا؟",
  "اكثر شي ينرفزك ؟",
  "تغار ؟",
  "كم تبلغ ذاكرة هاتفك؟",
  "صندوق اسرارك ؟",
  "شخص @ تعترفلة بشي ؟",
  "يومك ضاع على ؟",
  "اغرب شيء حدث في حياتك ؟",
  " نسبة حبك للاكل ؟",
  " حكمة تأمان بيها ؟",
  " اكثر شي ينرفزك ؟",
  " هل تعرضت للظلم من قبل؟",
  " خانوك ؟",
  " تزعلك الدنيا ويرضيك ؟",
  " تاريخ غير حياتك ؟",
  " أجمل سنة ميلادية مرت عليك ؟",
  " ولادتك بنفس المكان الي هسة عايش بي او لا؟",
  " تزعلك الدنيا ويرضيك ؟",
  " ماهي هوايتك؟",
  " دوله ندمت انك سافرت لها ؟",
  "شخص اذا جان بلطلعة تتونس بوجود؟",
  " تاخذ مليون دولار و تضرب خويك؟",
  " تاريخ ميلادك؟",
  "اشكم مره حبيت ؟",
  " يقولون ان الحياة دروس ، ماهو أقوى درس تعلمته من الحياة ؟",
  " هل تثق في نفسك ؟",
  " كم مره نمت مع واحده ؟",
  " اسمك الثلاثي ؟",
  "كلمة لشخص خذلك؟",
  "هل انت متسامح ؟",
  "طريقتك المعتادة في التخلّص من الطاقة السلبية؟",
  "عصير لو قهوة؟",
  " صديق أمك ولا أبوك. ؟",
  "تثق بـ احد ؟",
  "كم مره حبيت ؟",
  "اكمل الجملة التالية..... قال رسول الله ص،، انا مدينة العلم وعلي ؟",
  " اوصف حياتك بكلمتين ؟",
  " حياتك محلوا بدون ؟",
  " وش روتينك اليومي؟",
  " شي تسوي من تحس بلملل؟",
  " يوم ميلادك ؟",
  " اكثر مشاكلك بسبب ؟",
  " تزعلك الدنيا ويرضيك ؟",
  " تتوقع فيه احد حاقد عليك ويكرهك ؟",
  "كلمة غريبة من لهجتك ومعناها؟",
"   هل تحب اسمك أو تتمنى تغييره وأي الأسماء ستختار" ,
"  كيف تشوف الجيل ذا؟",
"  تاريخ لن تنساه📅؟",
"  هل من الممكن أن تقتل أحدهم من أجل المال؟",
"  تؤمن ان في حُب من أول نظرة ولا لا ؟.",
"  ‏ماذا ستختار من الكلمات لتعبر لنا عن حياتك التي عشتها الى الآن؟💭",
"  طبع يمكن يخليك تكره شخص حتى لو كنت تُحبه🙅🏻‍♀️؟",
"  ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
"  أطول مدة نمت فيها كم ساعة؟",
"  كلمة غريبة من لهجتك ومعناها؟🤓",
"  ردة فعلك لو مزح معك شخص م تعرفه ؟",
"  شخص تحب تستفزه😈؟",
"  تشوف الغيره انانيه او حب؟",
"  مع او ضد : النوم افضل حل لـ مشاكل الحياة؟",
"  اذا اكتشفت أن أعز أصدقائك يضمر لك السوء، موقفك الصريح؟",
"  ‏للشباب | آخر مرة وصلك غزل من فتاة؟🌚",
"  أوصف نفسك بكلمة؟",
"  شيء من صغرك ماتغير فيك؟",
"  ردة فعلك لو مزح معك شخص م تعرفه ؟",
"  | اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث شو راح تكون ؟.",
"  كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
"  حاجة تشوف نفسك مبدع فيها ؟",
"  يهمك ملابسك تكون ماركة ؟",
"  يومك ضاع على؟",
"  اذا اكتشفت أن أعز أصدقائك يضمر لك"," السوء، موقفك الصريح؟",
"  هل من الممكن أن تقتل أحدهم من أجل المال؟",
"  كلمه ماسكه معك الفترة هذي ؟",
"  كيف هي أحوال قلبك؟",
"  صريح، مشتاق؟",
"  اغرب اسم مر عليك ؟",
"  تختار أن تكون غبي أو قبيح؟",
"  آخر مرة أكلت أكلتك المفضّلة؟",
"  دوله ندمت انك سافرت لها😁؟",
"  اشياء صعب تتقبلها بسرعه ؟",
"  كلمة لشخص غالي اشتقت إليه؟💕",
"  اكثر شيء تحس انه مات ف مجتمعنا؟",
"  هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",
"  آخر شيء ضاع منك؟",
"  تشوف الغيره انانيه او حب؟",
"  لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",
"  شيء كل م تذكرته تبتسم ...",
"  هل تحبها ولماذا قمت باختيارها؟",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
"  أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟", 
"  هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
"  هل تشعر أن هنالك مَن يُحبك؟",
"  وش الشيء الي تطلع حرتك فيه و زعلت ؟",
"  صوت مغني م تحبه",
"  كم في حسابك البنكي ؟",
"  اذكر موقف ماتنساه بعمرك؟",
"  ردة فعلك لو مزح معك شخص م تعرفه ؟",
"  عندك حس فكاهي ولا نفسية؟",
"  من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",
"  ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
"  شيء من صغرك ماتغير فيك؟",
"  هل يمكنك أن تضحي بأكثر شيء تحبه وتعبت للحصول عليه لأجل شخص تحبه؟",
"  هل تحبها ولماذا قمت باختيارها؟",
"  لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",
"  كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
"  كم مره تسبح باليوم",
"  أفضل صفة تحبه بنفسك؟",
"  أجمل شيء حصل معك خلال هاليوم؟",
"  ‏شيء سمعته عالق في ذهنك هاليومين؟",
"  هل يمكنك تغيير صفة تتصف بها فقط لأجل شخص تحبه ولكن لا يحب تلك الصفة؟",
"  ‏أبرز صفة حسنة في صديقك المقرب؟",
"  ما الذي يشغل بالك في الفترة الحالية؟",
"  آخر مرة ضحكت من كل قلبك؟",
"  احقر الناس هو من ...",
"  اكثر دوله ودك تسافر لها🏞؟",
"  آخر خبر سعيد، متى وصلك؟",
"  ‏نسبة احتياجك للعزلة من 10📊؟",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  أكثر جملة أثرت بك في حياتك؟",
"  لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",
"  هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
"  آخر مرة ضحكت من كل قلبك؟",
"  وش الشيء الي تطلع حرتك فيه و زعلت ؟",
"  تزعلك الدنيا ويرضيك ؟",
"  متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
"  تعتقد فيه أحد يراقبك👩🏼‍💻؟",
"  احقر الناس هو من ...",
"  شيء من صغرك ماتغير فيك؟",
"  وين نلقى السعاده برايك؟",
"  هل تغارين من صديقاتك؟",
"  أكثر جملة أثرت بك في حياتك؟",
"  كم عدد اللي معطيهم بلوك👹؟",
"  أجمل سنة ميلادية مرت عليك ؟",
"  أوصف نفسك بكلمة؟",
 ]

wasf = [
    "لا خلقۿ ولا اخلاق لحاله عايش ☹.",
    "سڪر محلي محطوط على ڪريما 🤤🍰.",
    "؏ـسل × ؏ـسل 🍯.",
    "أنسان مرتب وڪشاخ بس مشكلتۿ يجذب هواي 😂.",
    "ملڪ جمال ألعالم 🥺💘.",
    "أنسان زباله ومكضيها نوم 🙂.",
    "يعني بشرفك هوه هذا يستاهل اوصفه؟",
    "أنسان ڪيمر 😞💘.",
    "جنۿ جڪليته يربيـﮧ 🍬.",
    "شمأ اوصف بي قليل 🥵💞.",
    "وجۿا جنة كاهي من ألصبحـﮧ ☹♥.",
    "هذا واحد يهودي دير بالك منه 🙂💘.",
    "هذا انسان يحب مقتدئ ابتعد عنه 😂💞.",
    "بس تزحف ع الولد وهيه زرڪة 😂.",
    "جنۿ مرڪة شجر شبيك يول 😂😔.",
    "هذا حبيبي ، أحبة ڪولش 🙊💘",
    "جمالهـﮧ خبلني 😞💞.",
    "چنۿ ڪريمة ؏ـلى ڪيك 😞💘.",
    "انسان مينطاق 🙂💔.",
    "فد أنسان مرتب وريحتة تخبل 🥺💞",
    "شڪد حلو هذا ومؤدب 😭💞💘💕.",
    "وفف مو بشر ضيم لضيعه من ايدڪك نصيحة 🥺💞.",
    "نتا مخلوق من ڪتله مال عارية 🙂😂.",
    "لضيعۿ من أيدك خوش أنسانن وحباب رتبط بي احسلڪك 🥺.",
    "با؏ هذا الصاڪك يربي شنو مخلوق منعسل 🥺🧿.",
    "شني عمي مو بشر ڪيك ورب 🥺💞.",
    "عوفه ضلعي هذا انسان زباله 🙂😂.",
    "انسان ساقط لتحجي وياه انطي بلوڪك بدون تفاهم 🙂🤦‍♀️.",
    "باع منو شون بشر هوه وجۿا يطرد النعمة 🙂.",
    "عيع فد أنسان وصخ 😂♥.",
    "يول هذا طاڪك قطة احسلك 😂💞.",
    "لازم واحد يضمه بقوطيه ويقفل عليه لان هالبشر ڪيك 🤤💘.",
    "هذا الله غاضب عليه 🌚💔.",
    "شنو شنو ؟ تسرسح يله 😒💘.",
    "وردة مال الله ، فدوا اروحله 🤤💞.",
    "أنسان مؤدب من البيت للجامع ، ومن الجامع للبيت 😞💞.",
    "انسان بومة وبس نايم مدري شلون اهله ساكتيله 🌚💞.",
    "أنت شايف وجها من يكعد الصبح ؟ عمي خلينا ساكتين 🙂😂.",
    "الله وكيلك هذا اهله كلشي ممستافدين من عنده 🥲💞.",
    "لكشنو من جمالل هذا يربييييي 😭💞.",
    "يومة فديته جنه زربه 😭😂💞.",
]

heno = [
    "تنجب وما تندك بأسيادك فاهم؟ ",
    "تعال ابن القندرة اليوم انعل والديك",
    "لك حيوان كواد استقر لك",
    "مااهين حيوانات اني 😹😭💘.",
]

mth = [
    "100% تحبك وتخاف عليك",
    "100% يحبج ويخاف عليج",
    "91% جـزء من قـلبه 💞",
    "81% تموت عليك ههاي ",
    "81% يموت عليج ههذا ",
    "40% واحد حيوان ومصلحه عوفه ",
    "50% شوف شعندك وياه ",
    "30% خاين نصحيا عوفيه ميفيدج ",
    "25% مصادق غيرج ويكلج احبج",
    "25% واحد كلب ابن كلب عوفه",
    "0% يكهرك ",
    "0% تكرهك ",
]

zid = [
    "100%",
    "99%",
    "98%",
    "97%",
    "96%",
    "95%",
    "90%",
    "89%",
    "88%",
    "87%",
    "86%",
    "85%",
    "80%",
    "79%",
    "78%",
    "77%",
    "76%",
    "75%",
    "70%",
    "69%",
    "68%",
    "67%",
    "66%",
    "65%",
    "60%",
    "59%",
    "58%",
    "57%",
    "56%",
    "55%",
    "50%",
    "48%",
    "47%",
    "46%",
    "45%",
    "40%",
    "39%",
    "38%",
    "37%",
    "36%",
    "35%",
    "30%",
    "29%",
    "28%",
    "27%",
    "25%",
    "20%",
    "19%",
    "18%",
    "17%",
    "16%",
    "15%",
    "10%",
    "9%",
    "8%",
    "7%",
    "6%",
    "5%",
    "4%",
    "3%",
    "2%",
    "1%",
    "0%",

]

@zedub.zed_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    medo = random.choice(kettuet)
    await edit_or_reply(mention, f"**⌔╎{medo}**")

@zedub.zed_cmd(pattern="(نسبه الحب|نسبة الحب)(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(mth)
    await edit_or_reply(mention, f"**✾╎نـسبـة حبكـم انـت و**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 😻♥️**")
@zedub.zed_cmd(pattern="(نسبه الانوثة|نسبة الانوثه|نسبه الانوثه|نسبة الانوثة)(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الانوثه لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤰**")
@zedub.zed_cmd(pattern="(نسبه الغباء|نسبة الغباء)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الغبـاء لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 😂💔**")
@zedub.zed_cmd(pattern="(نسبه الانحراف|نسبة الانحراف)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الانحـراف لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🥵🖤**")
@zedub.zed_cmd(pattern="(نسبه المثليه|نسبة المثليه)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة المثليـه لـ**  [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤡 🏳️‍🌈.**")
@zedub.zed_cmd(pattern="(نسبه النجاح|نسبة النجاح)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة النجـاح لـ** [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤓.**") 
@zedub.zed_cmd(pattern="(نسبه الكراهية|نسبة الكراهيه|نسبه الكراهيه|نسبة الكراهية)(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedt = random.choice(zid)
    await edit_or_reply(mention, f"**✾╎نسبـة الكراهيـة لـ** [{zedth}](tg://user?id={user.id}) **هـي {zedt} 🤮.**")
@zedub.zed_cmd(pattern="رفع ورع(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه ورع القـروب .. بنجـاح😹🙇🏻.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مزه(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخـدم ه ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـها مـزة الكروب .. بنجـاح 🥳💃.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مطي(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مطي سبورتي 🐴.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حمار(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حمار جحا 😂🐴.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع خروف(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه خـروف 🐑.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **🐑╎ تم رفعـه حيـوان .** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع بزون(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(
        mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **🐈╎ تم رفعـه بـزون .** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} "
    )
@zedub.zed_cmd(pattern="رفع زباله(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه زباله معفنه 🗑.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع منشئ(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه منشئ الكروب 👷‍♂️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مدير(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مدير الكروب 🤵‍♂️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع كواد(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه كـواد .. بنجـاح 👀. ** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مرتبط(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـه مرتبـط .. بنجـاح 💍💞** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع مرتبطه(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخـدم ه ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـهـا مرتبطـه .. بنجـاح 💍💞. .** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حبيبي(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حبيبـج .. بنجـاح 💍🤵‍♂👰🏻‍♀.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع خطيبتي(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخـدم ه ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـهـا خطيبتك .. بنجـاح 💍👰🏼‍♀️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@zedub.zed_cmd(pattern="رفع صاك(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه صاك 🤴 .** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@zedub.zed_cmd(pattern="رفع صاكه(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـها صاكه 👸🏼.** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حات(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه حـات الكـروب 🤴 .** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@zedub.zed_cmd(pattern="رفع حاته(?: |$)(.*)")
async def zed(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth2 = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخـدم  ⪼ • ** [{zedth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـها حـاتـه الكـروب 👸🏼.** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@zedub.zed_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك هـذا مطـور . . شما حجيت ماكـدر اوصفـه 🙊💘 ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك هـذا زلـزال الهيبـه . . شما حجيت ماكـدر اوصفـه 🙊💘 ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    owsf = random.choice(wasf)
    await edit_or_reply(mention, f"**- {owsf}**")
@zedub.zed_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id in zel_dev:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا احـد المطـورين المساعديـن  ❏╰**")
    if user.id == 925972505 or user.id == 1895219306 or user.id == 2095357462:
        return await edit_or_reply(mention, f"**╮ ❐ لك دي . . هـذا مطـور السـورس  ❏╰**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    hah = random.choice(heno)
    await edit_or_reply(mention, f"**- {hah}**")


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="التحشيش")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalTHS_cmd)

