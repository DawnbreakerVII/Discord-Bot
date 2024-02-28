from Api import *

@Bot.event
async def on_ready():
    print("Ready")

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
