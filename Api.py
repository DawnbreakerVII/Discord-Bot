import discord
import openai
from discord.ext import commands
import asyncio

Intents = discord.Intents.default()
Intents.members = True

Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

BotToken = '' #Bot token
Channel = Numbers #join channel id
Channel2 = Numbers #exit channel id
GptToken = '' #OpenAI token
openai.api_key = GptToken
