import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

# Bot prefix
client = commands.Bot(command_prefix="m!", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def avatar(ctx, *, avamember: discord.Member = None):
    if avamember is None:
        avamember = ctx.client.user  # If no user mentioned, get the avatar of the command author
    userAvatarUrl = avamember.avatar_url
    embed = discord.Embed(title=f"{avamember.name}'s Avatar")
    embed.set_image(url=userAvatarUrl)
    await ctx.reply(embed=embed, mention_author=True)

# Run the bot
client.run('TOKEN')
