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

@command_bot.command(pass_context=True)
async def test(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    embed.add_field(name="Author", value="<YOUR-USERNAME>")
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
        await command_bot.send_message(message.channel, "<@{}> has triggered the cat https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif".format(message.author.id) )

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

