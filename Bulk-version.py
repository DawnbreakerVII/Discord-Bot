import discord
import openai
from discord.ext import commands
import asyncio

Intents = discord.Intents.default()
Intents.members = True

Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

BotToken = '' #Bot token
GptToken = '' #OpenAI token
openai.api_key = GptToken
 
@Bot.event
async def on_ready():
    print("Ready")
    await asyncio.gather(update_status())

async def update_status():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Movie"))

@Bot.event
async def on_guild_join(guild):
    # For example, set a channel as 'welcome channel'
    welcome_channel_name = 'welcome'
    welcome_channel = discord.utils.get(guild.channels, name=welcome_channel_name)

    if not welcome_channel:
        # If the channel doesn't exist, create it
        welcome_channel = await guild.create_text_channel(welcome_channel_name)
        print(f"Bot {Bot.user.name} joined a server. Welcome channel created: {welcome_channel.name}")

    # Create 'goodbye channel'
    goodbye_channel_name = 'goodbye'
    goodbye_channel = await guild.create_text_channel(goodbye_channel_name)
    print(f"Bot {Bot.user.name} joined a server. Goodbye channel created: {goodbye_channel.name}")

@Bot.event
async def on_member_join(member):
    welcome_channel_name = 'welcome'
    welcome_channel = discord.utils.get(member.guild.channels, name=welcome_channel_name)

    if welcome_channel:
        await welcome_channel.send(f"{member.mention} Welcome! Hope you enjoy your time here.")

@Bot.event
async def on_member_remove(member):
    goodbye_channel_name = 'goodbye'
    goodbye_channel = discord.utils.get(member.guild.channels, name=goodbye_channel_name)

    if goodbye_channel:
        await goodbye_channel.send(f"{member.mention} Goodbye! Hope to see you again.")

def chat_with_gpt(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )
    return response['choices'][0]['message']["content"]

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return

    if message.content.startswith('!chat'):
        user_message = message.content[6:].strip()
        gpt_response = chat_with_gpt(user_message)
        await message.channel.send(f'ChatGPT: {gpt_response}')

    await Bot.process_commands(message)
  
@Bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason) #!kick user reason
        await ctx.send(f'{member.mention} succesfully kicked. Reason: {reason}')
    else:
        await ctx.send("You do not have permissions to perform this operation.")

@Bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason) #!ban user reason
        await ctx.send(f'{member.mention} succesfully banned. Reason: {reason}')
    else:
        await ctx.send("You do not have permissions to perform this operation.")
Bot.run(BotToken)







