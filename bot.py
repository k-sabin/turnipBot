import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Hello World!')

####### METHODS #######

#Watch list
#Adds users to the specified group for mentioning later
@client.command(aliases=['bought'])
async def watch(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Stalnks")
    user = ctx.message.author
    await user.add_roles(role)
    await ctx.send('Here\'s hoping for a nice surprise!')

#Unwatch
#Removes users from the specified group
@client.command(aliases=['sold'])
async def unwatch(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Stalnks")
    user = ctx.message.author
    await user.remove_roles(role)
    await ctx.send('Pleasure doin\' business with ya!')

#mention traders
@client.command()
async def selling(ctx, bellAmount, dodoCode: str):
    role = discord.utils.get(ctx.guild.roles, name="Stalnks")
    authorUser = ctx.message.author
    await ctx.send(role.mention + ' ' + authorUser.mention + '\'s island is selling turnips for ' + str(bellAmount) + ' bells!' +
                    '\n Their Dodo Code is: ' + dodoCode)

#stop mention (update previous message to say no longer selling)
@client.command(aliases=['stop'])
async def stopSelling(ctx):
    authorUser = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name="Stalnks")
    messageToEdit = discord.utils.get(client.messages, content= role.mention + ' ' + authorUser.mention)

#set fruit role
@client.command()
async def fruit(ctx, fruit: str):
    authorUser = ctx.message.author
    peachRole = discord.utils.get(ctx.guild.roles, name="just peachy")
    orangeRole = discord.utils.get(ctx.guild.roles, name="orange you glad")
    appleRole = discord.utils.get(ctx.guild.roles, name="apple a day...")
    pearRole = discord.utils.get(ctx.guild.roles, name="thank you pear-y much")
    cherryRole = discord.utils.get(ctx.guild.roles,name="so cherry sweet")

    if(peachRole in authorUser.roles or orangeRole in authorUser.roles or appleRole in authorUser.roles or
            pearRole in authorUser.roles or cherryRole in authorUser.roles):
        await ctx.send("You already have a fruit!")

    else:
        if(fruit == 'cherry'):
            await authorUser.add_roles(cherryRole)
            await ctx.send("You have set your fruit to Cherry!")
        elif(fruit == 'orange'):
            await authorUser.add_roles(orangeRole)
            await ctx.send("You have set your fruit to Orange!")
        elif(fruit == 'peach'):
            await authorUser.add_roles(peachRole)
            await ctx.send("You have set your fruit to Orange!")
        elif(fruit == 'apple'):
            await authorUser.add_roles(appleRole)
            await ctx.send("You have set your fruit to Orange!")
        elif(fruit == 'pear'):
            await authorUser.add_roles(pearRole)
            await ctx.send("You have set your fruit to Orange!")

client.run('NzEwOTA4MjA1NDgzNjg3OTU4.Xr7T6w.MrpU1Jr91UUU5tyYWId9SAgtZzw')
