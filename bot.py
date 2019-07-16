import discord
from discord.ext import commands
import asyncio
import time
import os
bot = commands.Bot(command_prefix='!')
bot.remove_command("help")
 
@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('Bot is ready.')
 
@bot.command(pass_context=True)
async def durum1(ctx):
      if ctx.message.author.id == "452912036670865438":
            await bot.change_presence(game=discord.Game(name=f"!ininal - !ininaldestek", type=1))
            await bot.say('📌 Durum değiştirildi.')
      else:
            await bot.say('📌 Bunu sadece botun yapımcısı yapabilir!')
 
@bot.command(pass_context=True)
async def durum(ctx, *, name):
      if ctx.message.author.id == "452912036670865438":
            await bot.change_presence(game=discord.Game(name=f"{name}", type=1))
            await bot.say(f'📌 Durum başarıyla {name} ile değiştirildi')
      else:
            await bot.say('📌 Bunu sadece botun yapımcısı yapabilir.')    
    
@bot.command(pass_context=True)
async def ininal(ctx):
    await bot.say('İninal Kodu: 4091870393183')
    
@bot.command(pass_context=True)
async def ininaldestek(ctx):
    await bot.say('İninal aldığınızda mb161358 kodunu yazarak hem TMU, hem kendiniz kazanabilirsiniz!')
    
@bot.command(pass_context=True)
async def yardım(ctx):
    embed = discord.Embed(title="TMU - İninal", color=0x5f0bdd)
    embed.add_field(name="İninal Komutları", value="**!ininal:** İninal kodunu gösterir. \n**!ininaldestek:** İninal destek kodunu gösterir.")
    embed.set_footer(text='TMU - İninal Yardım Menüsü', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)
    
bot.run(os.getenv('BOT_TOKEN'))
