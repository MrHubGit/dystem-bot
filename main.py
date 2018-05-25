import discord 
import secrets
import config 
from discord.ext.commands import Bot 
from discord.ext import commands 
from discord.voice_client import VoiceClient
import asyncio 
import time 
from random import randint
import json
import requests

Client = discord.Client() 
command_bot = commands.Bot(command_prefix="!", description="Hi! I am the dystem bot. Beep.")

@command_bot.event 
async def on_ready(): 
    print("Hello dystem!")

#ban any users who have not applied to the rules
@command_bot.event
async def on_message(message):
    #Kick and ban users for posting there server posting
    if "https://discord.gg" in message.content: 
        await command_bot.send_message(message.channel, "<@%s> has had their message deleted for breaking the rule\n2: No spam, we don't want to hear about your coin or your server, posting them will get you banned. https://i.imgur.com/RZ8dbLA.gifv" % (message.author.id) )
        await command_bot.delete_message(message)
    
    if (message.content == "!cat"):
        randomCat = randint(0, 9) + 1
        cat_switcher = {
            1: "http://i0.kym-cdn.com/photos/images/newsfeed/000/431/312/67e.jpg",
            2: "https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif",
            3: "https://media.mnn.com/assets/images/2013/05/ultimatebrutality.jpg",
            4: "https://i.amz.mshcdn.com/r7JSirBOG3KMCExw_iWEiLrueVs=/1200x627/2012%2F12%2F04%2F9d%2F15bestcatme.aH8.jpg",
            5: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWqAPeRZlwct4xiMuAAvoYIK2tsmS3HgKI5yFpdqVAr79fC6W9cA",
            6: "https://i.pinimg.com/originals/1d/c3/51/1dc3519cc3ec8d1148068fd08f42dcd3.jpg",
            7: "https://i.imgur.com/nbNeUCC.gif?noredirect",
            8: "http://2.bp.blogspot.com/-ESreZHheo1M/TxBchPbryFI/AAAAAAAAPn4/gVXXvRth6z4/s1600/monorail.jpeg",
            9: "https://www.sklarwilton.com/wp-content/uploads/2011/10/i-can-has-cheezburger.jpg"
        }
        await command_bot.send_message(message.channel, "{}".format(cat_switcher.get(randomCat, "https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif")) )

    if message.content.startswith("!help"):
        output = "Public blockchainot commands:\n```css\n"
        output = output + "!about : displays current blockchain and prices stats. \n"
        output = output + "!invitelist : lists the top 20 inviters for the server. \n"
        output = output + "!cat : displays a random cat meme for danystem. \n"
        output = output + "!help : lists all of the dystem bot commands and their usage. \n"
        output = output + "```"
        await command_bot.send_message(message.channel, "{}".format(output))
    
    if message.content.startswith("!about"):
        headers = {'content-type': 'application/json'}
        getmasternodecount = json.dumps({"method": 'getmasternodecount', "params": [], "jsonrpc": "2.0"})
        getinfo = json.dumps({"method": 'getinfo', "params": [], "jsonrpc": "2.0"})
        r_getinfo = requests.post('http://127.0.0.1:17100/', auth=(secrets.RPC_USR, secrets.RPC_PWD), headers=headers, data=getinfo)
        r_getmn = requests.post('http://127.0.0.1:17100/', auth=(secrets.RPC_USR, secrets.RPC_PWD), headers=headers, data=getmasternodecount)
        r_getprice = requests.get('https://graviex.net:443//api/v2/tickers/dtembtc.json')
        parsed_info = r_getinfo.json()['result']
        parsed_mn = r_getmn.json()['result']
        parsed_price = r_getprice.json()['ticker']

        #start compiled list of configiured out put
        output = ""
        if config.emoji_logo != "":
            output = output + config.emoji_logo + " "

        #Add coin name + tag line
        if config.coin_name != "":
            output = output + config.coin_name

        if config.coin_tag != "":
            output = output + " - " + config.coin_tag

        output = output + " ```diff\n"

        #Show 24 hour percentage
        if config.exchange ==  "graviex":
            percent = float(parsed_price['change']) * 100
            if percent > 0:
                output = output + "+ 24hr hour change: {0:.2f}%\n".format(percent)
            else:
                output = output + "- 24hr hour change: {0:.2f}%\n".format(percent)

            #Show exchange price listing
            output = output + "# Price:{0:.8f} BTC\n".format(float(parsed_price['last']))
            output = output + "# 24hr volume: {0:.2f} BTC\n".format(float(parsed_price['volbtc']))

        #Block information and details 
        if config.running_node == "yes":
            output = output + "# Block height: " + str(parsed_info["blocks"])  + "\n"
            output = output + "# Total supply: " + str(parsed_info["moneysupply"])  + "\n"
            output = output + "# Active masternodes: " + str(parsed_mn["stable"]) + " \n"
            output = output + "# Current difficulty: " + str(parsed_info["difficulty"]) + " \n"
            output = output + "``` Dystem bot version: " + config.version

        await command_bot.send_message(message.channel, "{}".format(output))

    if message.content.startswith("!invitelist"):
        server = message.channel.server
        invites = await command_bot.invites_from(server)
        sorted_invites = sorted(invites, key=lambda invite: invite.uses, reverse=True)
        output = "Top 20 inviters:\n```css\n"
        count = 1 
        for invite in sorted_invites:
            if count > 20:
                break

            inviter_string = str(invite.inviter)
            inviter_string_short = inviter_string[0:len(inviter_string)-5]
            row = ""
            if invite.uses > 0:
                if count < 10:
                    row = "#" + str(count) + ":  " + inviter_string_short + " "
                else:
                    row = "#" + str(count) + ": " + inviter_string_short +  " "
                
                if len(row) < 30:
                    i = len(row)
                    while i < 30:
                    	if i == 29:
                            row = row + str(invite.uses) + "\n"
                            i = i + 1
                    	else:
                            row = row + " "
                            i = i + 1
                else:
                    row = row + str(invite.uses) + "\n"

                output = output + row
                count = count + 1
        output = output + "```"
        await command_bot.send_message(message.channel, "{}".format(output))
        
command_bot.run(secrets.TOKEN)

