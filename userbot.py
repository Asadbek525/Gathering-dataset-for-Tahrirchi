# managing userbot
# pip install telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events

from main import get_dataset

# get this value from my.telegram.org
api_id = 'API_ID'
# get this value from my.telegram.org
api_hash = 'your api hash'
# you can get this value by running get_session_string.py
stringSession = 'Your string session'
# create a Telegram session and assign
client = TelegramClient(StringSession(stringSession), api_id, api_hash)

channel_id = 5891431451

# -100 is for channel + channel_id
dataset_channel_id = int('-100' + 'YOUR_CHANNEL_ID')

# get url from message
def get_url(message: str):
    url_start_index = message.find('https://kun.uz')
    for i in range(url_start_index, len(message)):
        if message[i] == ' ' or message[i] == '\n':
            return message[url_start_index:i]
    return message[url_start_index:]

# function to handle the new message
@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.sender_id == channel_id:
        url = get_url(event.message.message)
        print(url)
        dataset, dictionary = get_dataset(url)
        content = ''.join(dataset.iloc[0]['content'])
        
        # convert dictionary to string
        dictionary_str = ''
        for key, value in dictionary.items():
            dictionary_str += f'{key}: {value}\n'

        await client.send_message(dataset_channel_id, url)
        
        # try to send content
        try:
            await client.send_message(dataset_channel_id, "Content\n\n" + content)
        except:
            await client.send_message(dataset_channel_id, "Content\n\n" + content[:1024])
            await client.send_message(dataset_channel_id, "...Content too long")

        # try to send dictionary
        try:
            await client.send_message(dataset_channel_id, "Dictionary\n\n" + dictionary_str)
        except:
            await client.send_message(dataset_channel_id, "Dictionary\n\n" + dictionary_str[:1024])
            await client.send_message(dataset_channel_id, "...Dictionary too long")

        print('Message sent')

        # append dataset to csv file
        dataset.to_csv('dataset.csv', mode='a', header=False)

# start the client
client.start()
print('Client started')

# run the client until manually stopped
client.run_until_disconnected()