import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    toxic = ['ngu', 'ga', 'gà', 'non', 'đần', 'dan', 'dot', 'dốt']
    toxic_respond = ['Ai mà chả có lúc choke', 'Skill Issue', 'Giỏi thì làm kèo 1-1?']

    hello = ['hello', 'Chào', 'chào', 'chao']
    hello_respond = ['Hello my friend', 'Không tiếp!']

    if any(word in message.content for word in hello):
        await message.channel.send(random.choice(hello_respond))

    if any(word in message.content for word in toxic):
        await message.channel.send(random.choice(toxic_respond))

# Token
client.run('TOKEN')