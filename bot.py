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

##################################
client.run(os.environ['BOT_TOKEN'])
