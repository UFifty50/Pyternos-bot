import os
from python_aternos import Client
import discord
from discord.ext import commands

intents = discord.Intents.default()
#intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

aternos = Client.from_hashed(os.environ['uname'], os.environ['pswd'])

servs = aternos.list_servers()
serv = None
for testserv in servs:
    if serv.address == 'eggggggy.aternos.me':
        serv = testserv
        
@bot.command()
async def start(ctx):
    await ctx.send('Starting server...')
    serv.start()
    await ctx.send('Server `eggggggy.aternos.me` started!')

bot.run(os.environ['token'])
