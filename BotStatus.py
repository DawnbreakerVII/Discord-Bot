'''
await update_status()

async def update_status():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Movie"))  
'''
'''
#If you want a text loop

import asyncio 

await update_status()

async def update_status():
    while True:
        await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Hey..."))
        await asyncio.sleep(3)   # Time
        await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Are u..."))
        await asyncio.sleep(3)
        await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Sure"))
        await asyncio.sleep(3)
  # if you want u can change activity type: watching, listening, game
'''
# In code : 

from Api import *

@Bot.event
async def on_ready():
    print("Ready")
    await update_status()

async def update_status():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Movie"))  
@Bot.event   
async def on_member_join(member):
    wchannel = Bot.get_channel(Channel)
    await wchannel.send(f"{member.mention} Welcome")
    
@Bot.event  
async def on_member_remove(member):
    bchannel = Bot.get_channel(Channel2)
    await bchannel.send(f"{member.mention} Good Bye")

@Bot.command()
async def Who(msg):
    await msg.send("Hi I'm Bot")


Bot.run(BotToken)
