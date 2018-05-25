import discord 
import secrets 
from discord.ext.commands import Bot 
from discord.ext import commands 
from discord.voice_client import VoiceClient
import asyncio 
import time 
from random import randint

Client = discord.Client() 
command_bot = commands.Bot(command_prefix="!", description="Hi! I am the dystem bot. Beep.")

@command_bot.event 
async def on_ready(): 
    print("Hello dystem!")

@command_bot.command(pass_context=True)
async def test(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    embed.add_field(name="Author", value="Dystem")
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")
    await ctx.send(embed=embed)

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
        output = "<:dystem:445979324210741250> Dystem - Empowering open source development.\n```"
        output = output + "Price: TBC \n"
        output = output + "Block height: TBC \n"
        output = output + "```"
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

