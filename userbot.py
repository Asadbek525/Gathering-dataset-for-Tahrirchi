# managing userbot
# pip install telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest

import datetime
import asyncio
import time

from main import get_dataset

# get this value from my.telegram.org
api_id = 1547242
# get this value from my.telegram.org
api_hash = 'fd0c71f41851a344864fd934033d3549'
# you can get this value by running get_session_string.py
stringSession = '1ApWapzMBuw0SnzPFAfVB86bYSAS6xxKkVGggydtC5DqKHCV6tU7LZpTC5wDF2p0er7TskR5K-CdgvFA4f_DvItys9oojzMUEFf7CIEMRwkBjWemabDds9lv0NZjSekQnhH-E-FnV7VM_-x_EFTVI-XKcKUcGuBk9l36csy8TSnyvNg3gbJmRwQ-Tpkkn50evrS-YeBJD4vuty8aMAripSWyGDmcMrjLUs3OTO6fnXwMH6KvIvz6Y5ETc1EUTsnDyVYU-d6HEuRNKXKKZ3_vJL0gGLG1Blvfg13Nsdjk38HTq8_9B5tOXgOw6iTsjemkL5OfVZTWA1O07-_ik0-SBhyVXKpn8VLU='

# create a Telegram session and assign
client = TelegramClient(StringSession(stringSession), api_id, api_hash)


motivational_quotes = [
    'The best way to predict the future is to create it.',
    'The best revenge is massive success.',
    'The best way to get started is to quit talking and begin doing.',
    'The distance between insanity and genius is measured only by success.',
    'The secret of getting ahead is getting started.',
]
counter = 0

async def change_bio():
    global counter
    try:
        await client(UpdateProfileRequest(
            about = motivational_quotes[counter]
        ))
    except Exception as e:
        print(e)
    print('Bio changed to: ', motivational_quotes[counter])
    counter = (counter + 1) % 5

    

# start the client
client.start()
print('Client started')
while True:
    client.loop.run_until_complete(change_bio())
    time.sleep(10)
# run the client until manually stopped
client.run_until_disconnected()