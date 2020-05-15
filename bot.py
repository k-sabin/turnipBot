import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Hello World!')



#Add to the mention list
@client.command(aliases=['bought'])
async def watch(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Stalk Market Trader")
    user = ctx.message.author
    await user.add_roles(role)
    await ctx.send('Here\'s hoping for a nice surprise!')

#Remove from the mention list
@client.command(aliases=['sold'])
async def unwatch(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Stalk Market Trader")
    user = ctx.message.author
    await user.remove_roles(role)
    await ctx.send('Pleasure doin\' business with ya!')

client.run('NzEwOTA4MjA1NDgzNjg3OTU4.Xr7T6w.MrpU1Jr91UUU5tyYWId9SAgtZzw')
