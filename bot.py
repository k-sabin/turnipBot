import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Hello World!')


@client.command()
async def watch(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Stalk Market Trader")
    user = ctx.message.author
    await user.add_roles(role)
    await ctx.send('Watched!')


client.run('NzEwOTA4MjA1NDgzNjg3OTU4.Xr7T6w.MrpU1Jr91UUU5tyYWId9SAgtZzw')
