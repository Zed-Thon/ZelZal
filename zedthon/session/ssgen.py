import os
from time import sleep


def spinner(x):
    if x == "tele":
        print("Checking if Telethon is installed...")
    else:
        print("Checking if Pyrogram is installed...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print("ZThon Session Pyrogram")
    print("\n---------------------------\n")
    try:
        API_ID = int(input("Please enter your API ID: "))
    except ValueError:
        print("APP ID must be an integer.\nQuitting...")
        exit(0)
    API_HASH = input("Please enter your API HASH: ")
    print("\n---------------------------\n")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner("tele")
        x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except ImportError:
        print("Installing Telethon...")
        os.system("pip uninstall telethon -y && pip install -U telethon")

        x = "\bDone. Installed and imported Telethon."
    clear_screen()
    print(x)

    # the imports

    from telethon.errors.rpcerrorlist import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        UserIsBotError,
    )
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as zthon:
            print("Generating a string session for •ZThon•")
            try:
                zthon.send_message(
                    "me",
                    f"**- هـذا هو كـود سيشـن تيليثـون الخـاص بـك ☑️**:\n\n`{zthon.session.save()}`\n\n**- لا تشـارك هـذا الكـود مع اي احـد ⚠️؟!**\n**- فقـط قم بنسخـه ولصقـه في مربعـات التنصيب 🛃**\n\n**- سـورس زدثــون : @ZThon**",
                )
                print(
                    "Your SESSION has been generated. Check your Telegram saved messages!"
                )
                return
            except UserIsBotError:
                print("You are trying to Generate Session for your Bot's Account?")
                print("Here is That \n{zthon.session.save()}\n\n")
                print("NOTE: You can't use that as User Session..")
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."
        )
        exit(0)
    except ValueError:
        print("API HASH must not be empty!\nQuitting...")
        exit(0)
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nQuitting...")
        exit(0)
    except Exception as er:
        print("Unexpected Error Occurred while Creating Session")
        print(er)
        print("If you think It as a Bug, Report to @zzzzzl1l\n\n")


def pyro_session():
    try:
        spinner("pyro")
        from pyrogram import Client

        x = "\bFound an existing installation of Pyrogram...\nSuccessfully Imported.\n\n"
    except BaseException:
        print("Installing Pyrogram...")
        os.system("pip install pyrogram tgcrypto")
        x = "\bDone. Installed and imported Pyrogram."
        from pyrogram import Client

    clear_screen()
    print(x)

    # generate a session
    API_ID, API_HASH = get_api_id_and_hash()
    print("Enter phone number when asked.\n\n")
    with Client(
        name="zthon", api_id=API_ID, api_hash=API_HASH, in_memory=True
    ) as pyro:
        ss = pyro.export_session_string()
        pyro.send_message(
            "me",
            f"`{ss}`\n\n**- الكـود الـذي في الاعلـى هو كـود سيشـن بايـروجـرام ⬆️**\n**- لا تشـاركه مع اي احد كـود مهم وخطير ⚠️**\n\n**- قم بنسخـه ولصقـه في مربعـات التنصيب 🛃**",
        )
        print("Session has been sent to your saved messages!")
        exit(0)


def main():
    clear_screen()
    try:
        type_of_ss = int(
            input(
                "\nZThon Userbot\n\nWhich session do you want to generate?\n1. Telethon Session.\n2. Pyrogram Session.\n\nEnter choice:  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        pyro_session()
    elif type_of_ss == 2:
        pyro_session()
    else:
        print("Invalid choice.")
    x = input("Run again? (Y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)


main()
