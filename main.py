import os
import discord
from discord.ext import commands
import youtube_dl

import music

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def main():
    DISCORD_API_KEY = os.getenv("DISCORD_SECRET_KEY")
    if DISCORD_API_KEY is None:
        raise Exception("Set environment variable DISCORD_SECRET_KEY")

    client.add_cog(music.music(client))

    client.run(DISCORD_API_KEY)

if __name__ == "__main__":
    main()
