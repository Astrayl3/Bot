import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="m!", intents=intents)

# Event: Bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Command: Add
@client.command()
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f'The result of {num1} + {num2} is {result}')

# Command: Subtract
@client.command()
async def subtract(ctx, num1: float, num2: float):
    result = num1 - num2
    await ctx.send(f'The result of {num1} - {num2} is {result}')

# Command: Multiply
@client.command()
async def multiply(ctx, num1: float, num2: float):
    result = num1 * num2
    await ctx.send(f'The result of {num1} * {num2} is {result}')

# Command: Divide
@client.command()
async def divide(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send("Cannot divide by zero!")
    else:
        result = num1 / num2
        await ctx.send(f'The result of {num1} / {num2} is {result}')

# Token
client.run('TOKEN')
