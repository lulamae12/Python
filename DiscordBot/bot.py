from discord.ext import commands
import discordAPI,discord,sys, asyncio
import youtube_dl
from discord.voice_client import VoiceClient

audioQueue = []

token = discordAPI.botToken
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)
async def play(ctx, url):

    author = ctx.message.author
    voice_channel = author.voice.channel
    vc = await voice_channel.connect()

    player = await vc.audiosource(url)
    player.start()





    
@bot.command()
async def kill(ctx):
    sys.exit()

@bot.command()
async def hello(ctx):
    await ctx.send('I heard you! {0}'.format(ctx.author))





bot.run(token)