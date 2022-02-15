from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError, ApiIdInvalidError

tornado = input("✵ Enter y/yes to continue: ")
if tornado == 'y' or 'yes':
 print("\nPlease go to my.telegram.org and get your API Id and API Hash to proceed\n\n 𒊹︎︎︎ɢɪᴛʜᴜʙ ʀᴇᴘᴏ ɪs ➪➪ https://github.com/TornadoBotOP/TornadoBot")
print("""\n\nWelcome To TornadoBot String Session\nGenerator By @THETORNADOTEAM\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @TornadoBot_Support For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing TornadoBot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +918925534834! Kindly Retry"
        )
        print("")
        continue
    break
