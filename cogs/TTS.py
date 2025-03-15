import discord
from discord.ext import commands
from gtts import gTTS
import os

class TTS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Bot joins the user's voice channel."""
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            if ctx.voice_client is not None:  # If already connected, move to new channel
                await ctx.voice_client.move_to(channel)
            else:
                await channel.connect()
            await ctx.send(f"✅ Joined **{channel.name}**")
        else:
            await ctx.send("❌ You need to join a voice channel first.")

    @commands.command()
    async def leave(self, ctx):
        """Bot leaves the voice channel."""
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("👋 Left the voice channel.")
        else:
            await ctx.send("❌ I'm not in a voice channel.")

    @commands.command()
    async def speak(self, ctx, *, text: str):
        """Converts text to speech and plays it in the voice channel."""
        if ctx.voice_client:  # Check if bot is in a voice channel
            tts = gTTS(text=text, lang="en")
            tts.save("tts.mp3")

            audio_source = discord.FFmpegPCMAudio("tts.mp3")

            if not ctx.voice_client.is_playing():
                ctx.voice_client.play(audio_source, after=lambda e: print("Finished playing."))
                await ctx.send(f"🔊 Speaking: **{text}**")
            else:
                await ctx.send("❌ Wait until the current speech is finished.")
        else:
            await ctx.send("❌ I'm not in a voice channel. Use `m!join` first.")

async def setup(bot):
    await bot.add_cog(TTS(bot))
