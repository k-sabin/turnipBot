import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Hello World!')


client.run('NzEwOTA4MjA1NDgzNjg3OTU4.Xr7T6w.MrpU1Jr91UUU5tyYWId9SAgtZzw')
