'''

@Bot.command(aliases=['del'])
async def delete(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)

@Bot.event
async def on_ready():
    print("Hazır")
    await asyncio.gather(update_status())
    
'''
#In code 

from Api import * #Look at the Api.py

@Bot.command(aliases=['del'])
async def delete(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)

@Bot.event
async def on_ready():
    print("Ready!")
    await asyncio.gather(update_status())

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

Bot.run(BotToken)
