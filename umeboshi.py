import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

_roleList = []
_userID = ""
def saveRoles(roleList, userID):
    _roleList = list(roleList)
    global _userID
    _userID = userID
    print (_roleList)
    print (_userID)
    

@client.event
async def on_ready():
    print("Bot is now online and connected to Discord!")
    
@client.event
async def on_member_join(member):
    #server = discord.Server()
    #print(await message.mentions[0].id)
    print(member.id)
    #print(server.get_member(_userID))
    print(_userID)
    if member.id == _userID:
        #await client.replace_roles(member.id, _roleList)
        role = discord.utils.get(member.server.roles, name='Butthurt Baby')
        await client.replace_roles(member, role)
        
    else:
        role = discord.utils.get(member.server.roles, name='Suspect')
        await client.replace_roles(member, role)

@client.event
async def on_message(message):
    channel = client.get_channel('457753436101017603')
    if message.channel.id == '457753436101017603':
        await client.delete_message(message)
    
    if message.content.upper().startswith('!WALL'):
        await client.send_message(message.channel, "Currently a work in progress, type !accept to join the server!")
    
    if message.content.upper().startswith('!ACCEPT'):
        if "457754871794368512" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(discord.Object(id='389016178489556996'), "<@%s> promises not to  be a beta cuck! We'll see!" % (userID))
            role = discord.utils.get(message.server.roles, name='New Guy')
            await client.replace_roles(message.author, role)
            await client.delete_message(message)

    if message.content.upper().startswith('!PING'):
        if "389523728146497536" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Pong!" % (userID))
        else:
            userID = message.author.id
            await client.send_message(message.channel, "Your testosterone levels are too low, <@%s>!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if "389523728146497536" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
            #args[0] = !SAY
            #args[1] = Hey
            #args[2] = There
        else:
            userID = message.author.id
            await client.send_message(message.channel, "Your testosterone levels are too low, <@%s>!" % (userID))
        
    if message.content.upper() == "!MUTRUT":
        if "389523728146497536" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "https://www.twitch.tv/mutrut32")
        else:
            userID = message.author.id
            await client.send_message(message.channel, "Your testosterone levels are too low, <@%s>!" % (userID))
            
    if message.content.upper() == "!HIADNE":
        if "389523728146497536" in [role.id for role in message.author.roles]:
          await client.send_message(message.channel, "https://www.twitch.tv/hiadne")
        else:
            userID = message.author.id
            await client.send_message(message.channel, "Your testosterone levels are too low, <@%s>!" % (userID))
            
    if message.content.upper().startswith('!OP.GG'):
        if "389523728146497536" in [role.id for role in message.author.roles]:
            new = list(message.content[7:])
            print(new)
            
            for i in range(len(new)):
                new = [i.replace(' ', "+") for i in new]

            await client.send_message(message.channel, "http://na.op.gg/summoner/userName="+"".join(new))
        else:
            userID = message.author.id
            await client.send_message(message.channel, "Your testosterone levels are too low, <@%s>!" % (userID))
    
    if message.content.upper().startswith('!BUTTHURT'):
        if message.author.id == "388486377521807362":
            #test = discord.utils.get(message.server.roles, name='Da Black Attack Crew')
            role = discord.utils.get(message.server.roles, name='Butthurt Baby')
            roleList = list(message.mentions[0].roles)
            userID =message.mentions[0].id
            #roleList = message.mentions[0].roles[:]
            saveRoles(roleList, userID)
            #await client.send_message(message.channel, test)
            #await client.send_message(message.channel, "YES!!!")
            #if message.mentions[0].roles == "389540396532891650" or message.mentions[0].roles == "389523728146497536":
            if "389540396532891650" in [role.id for role in message.mentions[0].roles] or "389523728146497536" in [role.id for role in message.mentions[0].roles]:
                await client.replace_roles(message.mentions[0], role)
                await client.delete_message(message)
                #break
            await client.add_roles(message.mentions[0], role)
            await client.delete_message(message)
        else:
            userID = message.author.id
            await client.send_message(message.channel, "Your testosterone levels are too low, <@%s>!" % (userID))
            
    
    if message.content.upper().startswith('!TEST'):
        if message.author.id == "388486377521807362":
            await client.send_message(message.channel, _roleList)
            
    
client.run("NDU3NjM5MzM4MDA4NjQxNTY2.DgcC5w.ofwjM118f0T9WhZ23jsJ39zjBMk")
