import discord
client = discord.Client()

from discord.ext import commands
import os
import tracebak

bot = commands.Bot(command_prefix="/")
token = os.environ['DISCORD_BOT_TOKEN']

