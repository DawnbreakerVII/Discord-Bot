from Api import * # Not need Channel ID's

@Bot.event
async def on_ready():
    print("Ready")
    await asyncio.gather(update_status())

async def update_status():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Ceiling"))

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


Bot.run(BotToken)
