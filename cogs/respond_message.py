import discord
import random
from discord.ext import commands

class RespondMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        toxic = ['ngu', 'ga', 'gà', 'non', 'đần', 'dan', 'dot', 'dốt']
        toxic_respond = ['Ai mà chả có lúc choke', 'Skill Issue', 'Giỏi thì làm kèo 1-1?']

        hello = ['hello', 'Chào', 'chào', 'chao']
        hello_respond = ['Hello my friend', 'Không tiếp!']

        if any(word in message.content.lower() for word in hello):
            await message.channel.send(random.choice(hello_respond))

        if any(word in message.content.lower() for word in toxic):
            await message.channel.send(random.choice(toxic_respond))

# Add cog to bot
async def setup(bot):
    await bot.add_cog(RespondMessage(bot))
