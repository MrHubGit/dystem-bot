import discord 
import secrets 
from discord.ext.commands import Bot 
from discord.ext import commands 
from discord.voice_client import VoiceClient
import asyncio 
import time 


Client = discord.Client() 
command_bot = commands.Bot(command_prefix="!", description="Hi! I am the dystem bot. Beep.")

@command_bot.event 
async def on_ready(): 
    print("Hello dystem!") 

@command_bot.event
async def wiggle():
    command_bot.say()

@command_bot.event
async def on_message(message):
    print("Message content {}".format(message.content) )
    if (message.content == "!cat"):
        print("<@{}> has triggered the cat ".format(message.author.id) )
        await command_bot.send_message(message.channel, "<@{}> has triggered the cat https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif".format(message.author.id) )

command_bot.run(secrets.TOKEN)

