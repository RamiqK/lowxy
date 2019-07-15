import discord
from discord.ext import commands
import asyncio
import time
import os
bot = commands.Bot(command_prefix='!')
bot.remove_command("help")
 
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="!ininal - !ininaldestek"))
    print(bot.user.name)
    print(bot.user.id)
    print('Bot is ready.')

@bot.command()
async def ininal(ctx):
    await ctx.send('4091870393183')

@bot.command()
async def ininaldestek(ctx):
    await ctx.send('İninali olmayan arkadaşlar, ininal alırsanız "mb161358" kodunu kullanınca hem TMU hem siz kazanabilirsiniz!')

bot.run(os.getenv('BOT_TOKEN'))
