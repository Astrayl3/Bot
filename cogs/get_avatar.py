import discord
from discord.ext import commands

class GetAvatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *, avamember: discord.Member = None):
        if avamember is None:
            avamember = ctx.author  # If no user is mentioned, get the author's avatar
        embed = discord.Embed(title=f"{avamember.name}'s Avatar")
        embed.set_image(url=avamember.display_avatar.url)
        await ctx.reply(embed=embed, mention_author=True)

# Add cog to bot
async def setup(bot):
    await bot.add_cog(GetAvatar(bot))
