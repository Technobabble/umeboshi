import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is now online and connected to Discord!")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
    
    if message.content.upper() == "!MUTRUT":
        await client.send_message(message.channel, "https://www.twitch.tv/mutrut32")
    if message.content.upper() == "!HIADNE":
        await client.send_message(message.channel, "https://www.twitch.tv/hiadne")
    

client.run("NDU3NjM5MzM4MDA4NjQxNTY2.DgcC5w.ofwjM118f0T9WhZ23jsJ39zjBMk")
