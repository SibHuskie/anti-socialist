import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS

Client = discord.Client()
bot_prefix= ["a?", "A?"]
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='539355100397699092')
footer_text = "Anti-Social Club"
error_img = ':warning:'
default_invite = 'https://discord.gg/jNNeex6'
banner = 'https://imgur.com/a/IR8j588'

#############################################################EMOTES#############################################################

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

patlinks = ["https://i.imgur.com/8eApUKG.gif",
            "https://i.imgur.com/qVcP9Pt.gif",
            "https://i.imgur.com/X9hKO2p.gif",
            "https://i.imgur.com/v8cRPH9.gif",
            "https://i.imgur.com/N6C7C30.gif",
            "https://i.imgur.com/M9QPcY6.gif",
            "https://i.imgur.com/oUSdjX6.gif",
            "https://i.imgur.com/mFFr4e0.gif",
            "https://i.imgur.com/3F7kmCd.gif",
            "https://i.imgur.com/7yFvJ6m.gif",
            "https://i.imgur.com/y3La9yP.gif"]

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

nomlinks = ["https://i.imgur.com/E1eQPfu.gif",
            "https://i.imgur.com/UUZY3Rb.gif",
            "https://i.imgur.com/Zd6fIpA.gif",
            "https://i.imgur.com/i2NaBS7.gif",
            "https://i.imgur.com/Up5J6Nn.gif",
            "https://i.imgur.com/J5MLku7.gif",
            "https://i.imgur.com/7yYgZXE.gif"]

throwlinks = ["https://i.imgur.com/o9j2oNi.gif",
              "https://i.imgur.com/wSb8aux.gif",
              "https://i.imgur.com/QO8TrkK.gif",
              "https://i.imgur.com/Ts3Cc52.gif",
              "https://i.imgur.com/D3ggzfW.gif",
              "https://i.imgur.com/eD5mE7R.gif",
              "https://i.imgur.com/JCUipZJ.gif",
              "https://i.imgur.com/VSg0YLw.gif",
              "https://i.imgur.com/8mUufrm.gif"]

bitelinks = ["https://i.imgur.com/E0jIIa9.gif",
             "https://i.imgur.com/Nvkw6hN.gif",
             "https://i.imgur.com/wr7l06j.gif",
             "https://i.imgur.com/uce91VI.gif"]

bloodsucklinks = ["https://i.imgur.com/UbaeYIq.gif",
                  "https://i.imgur.com/qi83Eft.gif",
                  "https://i.imgur.com/CtwmzpG.gif",
                  "https://i.imgur.com/DAuEJ2F.gif",
                  "https://i.imgur.com/By6IGzq.gif"]

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

highfivelinks = ["https://i.imgur.com/hjoQeOt.gif",
                 "https://i.imgur.com/9nhheqT.gif",
                 "https://i.imgur.com/yw3xMOu.gif",
                 "https://i.imgur.com/Y4g5fsT.gif",
                 "https://i.imgur.com/p6Hvx5r.gif",
                 "https://i.imgur.com/33nuO9D.gif",
                 "https://i.imgur.com/uFQnmYa.gif",
                 "https://i.imgur.com/9KG3k2n.gif",
                 "https://i.imgur.com/nHCC1ps.gif",
                 "https://i.imgur.com/aKvaNba.gif",
                 "http://i.imgur.com/hnHR29x.gif"]

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]


punchlinks = ["https://i.imgur.com/T2HdIv8.gif",
              "https://i.imgur.com/LZz65rg.gif",
              "https://i.imgur.com/FqPBIf3.gif",
              "https://i.imgur.com/KmqPDQG.gif",
              "https://i.imgur.com/yEx4aKu.gif"]

starelinks = ["https://i.imgur.com/f8rFNH0.gif",
              "https://i.imgur.com/ACCQDj4.gif",
              "https://i.imgur.com/1Co1i9t.gif",
              "https://i.imgur.com/uPZHQxV.gif",
              "https://i.imgur.com/wXQLAb3.gif",
              "https://i.imgur.com/hY7ZngK.gif"]

facepalmlinks = ["http://media.giphy.com/media/8BYLSNmnJYQxy/giphy.gif",
                 "https://uploads.disquscdn.com/images/84e9a7cef36a59ae605fad98c7ac567841be388820bf3fb936fd21b646a1d605.gif",
                 "https://media1.tenor.com/images/74199573d51d1bd9b61029b611ee7617/tenor.gif?itemid=5695432",
                 "http://i0.kym-cdn.com/photos/images/original/000/173/877/Facepalm.gif",
                 "http://i.imgur.com/gXOcRsW.gif",
                 "https://media.giphy.com/media/8cPpgUhTMjhF6/giphy.gif",
                 "https://media1.tenor.com/images/a0282083ab6b592ab419659e4fb08624/tenor.gif?itemid=4745847"]

crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif"]

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]




# a?hug <user>
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x7c7c7c, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to hug.")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":black_medium_square: EMOTE :black_medium_square: ", value="<@{}> got a hug from <@{}>! I ship it.".format(user.id, author.id))
    await client.say(embed=msg)

# a?cry
@client.command(pass_context=True)
async def cry(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x7c7c7c, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(crylinks)))
    msg.add_field(name=":black_medium_square: EMOTE :black_medium_square: ", value="<@{}> is crying. ;-;".format(author.id))
    await client.say(embed=msg)

# a?kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x7c7c7c, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to kiss.")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":black_medium_square: EMOTE :black_medium_square: ", value="<@{}> got a kiss from <@{}>! owo what's this?".format(user.id, author.id))
    await client.say(embed=msg)

# a?cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x7c7c7c, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to cuddle.")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":black_medium_square: EMOTE :black_medium_square: ", value="<@{}> cuddled <@{}>! Aww.".format(author.id, user.id))
    await client.say(embed=msg)

# a?pat <user>
@client.command(pass_context=True)
async def pat(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x7c7c7c, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to pat.")
    else:
        msg.set_image(url="{}".format(random.choice(patlinks)))
        msg.add_field(name=":black_medium_square: EMOTE :black_medium_square: ", value="<@{}> got a pat from <@{}>! uwu".format(user.id, author.id))
    await client.say(embed=msg)

##############################################################FUN#####################################################################

# a?roast <user>
@client.command(pass_context=True)
async def roast(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x7c7c7c, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention a user you want to roast.")
    else:
        a = ["<@{}>: Hey, <@{}>! I saw a piece of shit today... it reminded me of you.".format(author.id, user.id),
             "<@{}>: You look familiar, <@{}>. Oh yeah! I see you in the trash.".format(author.id, user.id),
             "<@{}>: Don't worry, <@{}>, you're not adopted. We're still searching for someone who wants you.".format(author.id, user.id),
             "<@{}>: If I wanted to kill myself, I'd jump climb up your ego and jump in your IQ, <@{}>.".format(author.id, user.id),
             "<@{}>: <@{}>, you are so stupid that you got hit by a parked car.".format(author.id, user.id),
             "<@{}>: <@{}>, you are so fat and so old that when God created light, you were asked to move out of the way.".format(author.id, user.id),
             "<@{}>: I heard <@{}> sucks so much that they were used as a vacuum cleaner.".format(author.id, user.id),
             "<@{}>: Hey, <@{}>! Try to not spit when you talk, we don't need a public shower here.".format(author.id, user.id),
             "<@{}>: I can't breathe when I see you, <@{}>... cause I'm suffocating from your bullshit.".format(author.id, user.id),
             "<@{}>: <@{}>, you have the right to remain silent cause anything you say is probably going to be stupid anyway.".format(author.id, user.id),
             "<@{}>: It's really hard to ignore <@{}>. Mostly cause they smell like shit.".format(author.id, user.id),
             "<@{}>: <@{}>, did you fall from Heaven? Cause so did Satan.".format(author.id, user.id),
             "<@{}>: <@{}>, were you sent to kill people? Cause your face is killing me.".format(author.id, user.id),
             "<@{}>: If laughter is the best medicine, your face must be curing the world, <@{}>.".format(author.id, user.id),
             "<@{}>: The only way you'll ever get laid is if you crawl up a chicken's ass and wait, <@{}>.".format(author.id, user.id),
             "<@{}>: <@{}>, your family tree must be a cactus. Cause everyone on it is a prick.".format(author.id, user.id),
             "<@{}>: <@{}>, save your breath, you'll need it to blow your date.".format(author.id, user.id),
             "<@{}>: <@{}>, the zoo called. They are wondering how you got out of your cage?".format(author.id, user.id),
             "<@{}>: <@{}>, you're so ugly that when you look in the mirror your reflection looks the away.".format(author.id, user.id),
             "<@{}>: <@{}>, it's better to let someone think you're stupid than open your mouth and prove it.".format(author.id, user.id),
             "<@{}>: I just stepped in something that is smarter than you, <@{}>... It smelled better too.".format(author.id, user.id),
             "<@{}>: <@{}>, you're stupid just like your father when he thought he didn't need a condom.".format(author.id, user.id),
             "<@{}>: <@{}> is so stupid that they stopped at a stop sign and waited for it to say go.".format(author.id, user.id),
             "<@{}>: <@{}>, you're so ugly that you have to trick or treat over the phone.".format(author.id, user.id),
             "<@{}>: <@{}>, you're so fat that your school photo was a double picture.".format(author.id, user.id),
             "<@{}>: I'd like to kick <@{}> in the teeth but that would be an improvement for them.".format(author.id, user.id),
             "<@{}>: <@{}> is so old that when they were in school there was no history class.".format(author.id, user.id),
             "<@{}>: <@{}> is so stupid that they called me to ask me for my phone number.".format(author.id, user.id),
             "<@{}>: <@{}>, at least my mom pretends to love me.".format(author.id, user.id),
             "<@{}>: <@{}>, don't play hard to get when you are hard to want.".format(author.id, user.id),
             "<@{}>: <@{}>, you're hating yourself too much for me to roast you.".format(author.id, user.id),
             "<@{}>: <@{}>, I can't even call you ugly. Nature has beaten me to it.".format(author.id, user.id),
             "<@{}>: People like you, <@{}>, are the reason God doens't talk to us anymore.".format(author.id, user.id),
             "<@{}>: We all dislike you, <@{}>. But not quite enough to think about you.".format(author.id, user.id),
             "<@{}>: <@{}>, you are a stupid.".format(author.id, user.id),
             "<@{}>: <@{}>, I'd like to invite you to a nice, warming cup of shut the fuck up.".format(author.id, user.id),
             "<@{}>: <@{}>, your mother might have told you, you can be whatever you want to but a cunt wasn't what she meant.".format(author.id, user.id),
             "<@{}>: <@{}> is so fat, Thanos had to clap.".format(author.id, user.id)]
        msg.add_field(name=":fire: Roast Machine", value="{}".format(random.choice(a)))
    await client.say(embed=msg)
##################################
client.run(os.environ['BOT_TOKEN'])
