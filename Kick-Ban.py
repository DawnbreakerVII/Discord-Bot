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
