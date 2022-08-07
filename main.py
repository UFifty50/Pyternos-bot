import os
from python_aternos import Client
from python_aternos.aterrors import ServerStartError
import discord
from discord import Message
from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)

load_dotenv()

aternos = Client.from_credentials(os.getenv('uname'), os.getenv('pswd'))

def getServer():
    servs = aternos.list_servers()
    serv = None
    for testserv in servs:
        if testserv.address == 'eggggggy.aternos.me':
            serv = testserv

starting = False

@bot.event
async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')
        await bot.change_presence(activity=discord.Game(name='>help for help'))
        getServer()

@tasks.loop(seconds=1)
async def bgTask(ctx: Context, msg: Message):
  global serv
  if serv.status != 'online':
    print(serv.status)
    print(serv.status_num)
    aternos.refresh_servers([serv.servid])
    getServer()
    global wait
    wait += 1
    await msg.edit(content=msg.content[0:18] + f" `{wait}`")
  else:
    await ctx.send(f'Server `eggggggy.aternos.me` started in `{wait}` seconds')
    global starting
    starting = False
    bgTask.stop()

@bot.command()
async def start(ctx: Context):
  global starting
  if starting:
    await ctx.send(f"Server `{serv.address}` is already starting")
  else:
    try:
      serv.start(True, True)
      starting = True
      startingMsg = await ctx.send('Starting server...')
      bgTask.start(ctx, startingMsg)
    except ServerStartError:
      await ctx.send(f'Server `{serv.address}` is already running')

bot.run(os.getenv('token'))
