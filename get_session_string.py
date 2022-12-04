# creating userbot for TELEGRAM


# generate new strings session
# pip install telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org""")
print("""Login using your Telegram account""")
print("""Click on API Development Tools""")
print("""Create a new application, by entering the required details""")
print("""Copy the 'API ID' and 'API Hash'""")
API_KEY = int(input("API ID: "))
API_HASH = input("API Hash: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
    print("""Your TELEGRAM String Session has been sent to your Telegram Saved Messages""")
    print("""Please check your Telegram Saved Messages""")
    print("""Thank You""")
