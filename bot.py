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
    userMessage = ctx.message
    botMessage = user.mention + ', here\'s hoping for a nice surprise!'
    await user.add_roles(role)
    botMessageEvent = await ctx.send(botMessage)
    await userMessage.delete(delay=1)
    await botMessageEvent.delete(delay=5)

#Unwatch
#Removes users from the specified group
@client.command(aliases=['sold'])
async def unwatch(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Stalnks")
    user = ctx.message.author
    userMessage = ctx.message
    botMessage = user.mention + ', pleasure doin\' business with ya!'
    await user.remove_roles(role)
    botMessageEvent = await ctx.send(botMessage)
    await userMessage.delete(delay=1)
    await botMessagEvent.delete(delay=5)

#Selling
#Mentions the role with the price and the dodo code for travelling
#PARAMETERS:
    # bellAmount: Price at Nook's Cranny on the island
    # dodoCode: Dodo Code from the Airport for travelling
@client.command()
async def selling(ctx, bellAmount, dodoCode: str):
    authorUser = ctx.message.author
    mentionRole = discord.utils.get(ctx.guild.roles, name="Stalnks")
    openRole = discord.utils.get(ctx.guild.roles, name="Open Town")
    await authorUser.add_roles(openRole)
    if(bellAmount and dodoCode):
        await ctx.send(mentionRole.mention + ' ' + authorUser.mention + '\'s island is selling turnips for ' + str(bellAmount) + ' bells!' +
                    '\n Their Dodo Code is: ' + dodoCode)

#buying
#Mentions the role with the price and the dodo code for travelling
#PARAMETERS:
    # bellAmount: Price at Nook's Cranny on the island
    # dodoCode: Dodo Code from the Airport for travelling

@client.command()
async def buying(ctx, bellAmount, dodoCode: str):
    authorUser = ctx.message.authorUser
    mentionRole = discord.utils.get(ctx.guild.roles, name="Stalnks")
    openRole = discord.utils.get(ctx.guild.roles, name="Open Town")
    await authorUser.add_roles(openRole)
    if(bellAmount and dodoCode):
        await ctx.send(mentionRole.mention + ' ' + authorUser.mention + '\'s island is buying turnips for ' + str(bellAmount) + ' bells!' +
                    '\n Their Dodo Code is: ' + dodoCode)

#Stop selling
#Edits the previous message to say that the island is closed
@client.command(aliases=['stop'])
async def stop_selling(ctx):
    channel = ctx.message.channel
    authorUser = ctx.message.author
    openRole = discord.utils.get(ctx.guild.roles, name="Open Town")
    #I have a feeling once a channel has a lot of messages this will become unwieldy
    async for m_id in channel.history().filter(lambda m: authorUser in m.mentions).filter(lambda m: 'island is selling' in m.content).map(lambda m:m):
        messageToEdit = m_id
        await authorUser.remove_roles(openRole)
        await messageToEdit.edit(content=authorUser.mention + ' has closed their town.')
        await messageToEdit.delete(delay=3600)
    #I have a feeling once a channel has a lot of messages this will become unwieldy
    async for m_id in channel.history().filter(lambda m: m.author == authorUser).filter(lambda m: '.selling' in m.content).map(lambda m:m):
        botSummonMessage = m_id
        await botSummonMessage.delete(delay=3)
    await ctx.message.delete(delay=3)

#Set Fruit role
#Set the role in the server based on your Fruit
#PARAMETERS:
    # Fruit: name of the fruit to get role
@client.command()
async def fruit(ctx, fruit: str):
    fruit = fruit.lower()
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

#Help
@client.command()
async def dmhelp(ctx):
    await ctx.send("Why hullo there! I'm Daisy Mae!")
    await ctx.send("Need some help?")

    await ctx.send("Prefix: '.'\nAdd Fruit: **.fruit** [*cherry*,*orange*,*peach*,*apple*,*pear*]\n" +
    "\nAdd to Watchlist: **.bought**/**.watch**\n\nRemove from watchlist: **.sold**/**.unwatch**\n"+
    "\nAnnounce selling & being open: **.selling**\n\nClose town (use after .selling): **.stop**")

client.run('')
