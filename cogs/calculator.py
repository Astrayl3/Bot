from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, num1: float, num2: float):
        await ctx.send(f'The result of {num1} + {num2} is {num1 + num2}')

    @commands.command()
    async def subtract(self, ctx, num1: float, num2: float):
        await ctx.send(f'The result of {num1} - {num2} is {num1 - num2}')

    @commands.command()
    async def multiply(self, ctx, num1: float, num2: float):
        await ctx.send(f'The result of {num1} * {num2} is {num1 * num2}')

    @commands.command()
    async def divide(self, ctx, num1: float, num2: float):
        if num2 == 0:
            await ctx.send("Cannot divide by zero!")
        else:
            await ctx.send(f'The result of {num1} / {num2} is {num1 / num2}')

# Add cog to bot
async def setup(bot):
    await bot.add_cog(Calculator(bot))
