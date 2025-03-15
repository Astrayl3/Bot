import discord
from discord.ext import commands
import os
import asyncio

# Bot setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="m!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Load all cogs
async def load_cogs():
    cog_folder = "cogs"
    for filename in os.listdir(cog_folder):
        if filename.endswith(".py") and not filename.startswith("__"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        from config import BOT_TOKEN
        await bot.start(BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
