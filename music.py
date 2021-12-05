import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Get in a voice channel to play music 4head...")

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        ffmpeg_opts = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        ydl_opts = {'format': 'besaudio'}
        voice_chat = ctx.voice_client

        with youtube_dl.Youtube(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info('formats')[0]['url']
            source = await discord.flatten_error_dict
            source = lol


def setup(client):
    client.add_cog(music(client))
