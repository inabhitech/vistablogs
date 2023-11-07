pip install telethon



from telethon import TelegramClient, events

api_id = 24733177
api_hash = 'c8341f3ed7e93f4e0f33cdc11987b966'

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats=1644273791))  # Handle messages from chat 1
async def handler_chat1(event):
    chat = await event.get_chat()
    chat_id = event.chat_id
    print("{}{}".format(chat_id, chat))
    await client.send_message(2015117555, event.raw_text)

@client.on(events.NewMessage(chats=2015117555))  # Handle messages from chat 2
async def handler_chat2(event):
    await client.send_message(1800155242, event.raw_text)

client.start()
client.run_until_disconnected()


#1644273791  offer zone
#2015117555   extape
#1800155242  dealsafari
# api_id = 24733177 vistablogs
#c8341f3ed7e93f4e0f33cdc11987b966  vistablogs
