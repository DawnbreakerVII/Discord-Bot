import discord
from discord.ext import commands

Intents = discord.Intents.default()
Intents.members = True

Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

BotToken = '' #Bot token
Channel = Numbers #join channel id
Channel2 = Numbers #exit channel id
