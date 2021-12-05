import os
import discord
from discord.ext import commands
import youtube_dl

import music

cogs = [music]

def main():
    DISCORD_API_KEY = os.getenv("DISCORD_SECRET_KEY")
    if DISCORD_API_KEY is None:
        raise Exception("Set environment variable DISCORD_SECRET_KEY")

if __name__ = "__main__":
    main()
