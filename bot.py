import discord
import time
from discord.ext import commands
import asyncio
import random
import os
import aiohttp
from datetime import timedelta, datetime
from pyfiglet import figlet_format, FontError, FontNotFound
from pyfiglet import figlet_format, FontError, FontNotFound
from aiohttp import ClientSession
bot = commands.Bot(command_prefix='rp+')
bot.remove_command("help")
 
 
@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id) 
 
@bot.command(pass_context=True)
async def status1(ctx):
      if ctx.message.author.id == "452912036670865438":
            await bot.change_presence(game=discord.Game(name=f"rp+yardım | Roleplay+ Bot hizmetinizde!", type=1))
            await bot.say('```Durum değiştirildi.```')
      else:
            await bot.say('```Bunu sadece botun yapımcısı yapabilir!```')
 
@bot.command(pass_context=True)
async def status(ctx, *, name):
      if ctx.message.author.id == "452912036670865438":
            await bot.change_presence(game=discord.Game(name=f"{name}", type=1))
            await bot.say(f'```Durum başarıyla {name} ile değiştirildi.```')
      else:
            await bot.say('```Bunu sadece botun yapımcısı yapabilir.```')
 
@bot.command(pass_context=True)
async def wikitürk1(ctx, message):
    await bot.say(f'https://tr.m.wikipedia.org/wiki/{message}')  
   
 
@bot.command(pass_context=True)
async def wikieng1(ctx, message):
    await bot.say(f'https://en.m.wikipedia.org/wiki/{message}')                      
                                   
@bot.command(pass_context=True)
async def wikitürk2(ctx, message, message1):
    await bot.say(f'https://tr.m.wikipedia.org/wiki/{message}_{message1}')          
 
@bot.command(pass_context=True)
async def wikieng2(ctx, message, message1):
    await bot.say(f'https://en.m.wikipedia.org/wiki/{message}_{message1}')  
 
@bot.event
async def on_member_join(member):
    channel = member.server.get_channel("522873873356685312")
    role = discord.utils.get(member.server.roles, id="500967059547750411")
    await bot.send_message(channel, f'Merhabalar! {member.mention}, Roleplay+ Discord Grubuna hoşgeldin. <#522474326797058048> kanalını okumayı unutma!')  
    await bot.add_roles(member, role)
   
@bot.event
async def on_member_remove(member):
    channel = member.server.get_channel("522873873356685312")
    await bot.send_message(channel, f'Hoşçakal! {member.mention}, Fazla şey kaybettin dostum! Roleplay+ seni her zaman bekliyor! Geri gelebilirsin.')       
                           
@bot.command(pass_context=True)
async def yardım(ctx):
    embed = discord.Embed(title="Komutlar bunlardır.", description="Prefixim rp+.", color=0x5f0bdd)
    embed.add_field(name="RP+ ile ilgili komutlar:", value="**rp+sunucubilgi**: Sunucu bilgilerini gösterir. \n**rp+üyebilgi**: Kendinin ya da diğer üyenin bilgilerini gösterir. \n**rp+kurallar**: Kuralları gösterir. \n**rp+link**: Sunucunun sınırsız davet linkini atar.", inline=True)
    embed.add_field(name="Moderasyon komutları:", value="**rp+at <üye>**: Üyeyi atar. \n**rp+ban <üye>**: Üyeyi banlar. \n**rp+sustur <üye>**: Üyeyi susturur. \n**rp+susturaç <üye>**: Üyenin susturulmasını açar. \n**rp+temizle <sayı>**: Belirtilen sayıda mesajı siler. \n**rp+yazıkanalıkur <isim>**: Yazı kanalı kurar. \n**rp+seskanalıkur <isim>**: Ses kanalı kurar. \n**rp+duyuruyap <duyuru>**: Duyuru yapar. \n**rp+uyar <üye>**: Üyeyi uyarır. \n**rp+nickdeğiştir**: Üyenin nickini değiştirir. \n**rp+rolver**: Rol verir. \n**rp+rolsil**: Rolü siler.", inline=True)
    embed.add_field(name="Diğer komutlar:", value="**rp+wikitürk<1 ya da 2>**: Wikipedide yazdığınız yazıyı Türkçe aratır. (1 - Bir haneli bilgiyi aratır, 2 - 2 haneli bilgiyi aratır. Doğru kullanmazsanız hata verir.) \n**rp+wikieng<1 ya da 2>**: Wikipedide yazdığınız yazıyı İngilizce aratır. (1 - Bir haneli bilgiyi aratır, 2 - 2 haneli bilgiyi aratır. Doğru kullanmazsanız hata verir.) \n**rp+ascii <mesaj>**: Mesajı ASCII Arta çevirir. \n**rp+oylama <mesaj>**: Oylama yapar. \n**rp+yaz <mesaj>**: Bota mesajı yazdırır. \n**rp+ping**: Anlık pingi gösterir. \n**rp+avatar**: Senin ya da üyenin ikonunu gösterir. \n**rp+sunucuavatar**: Sunucunun ikonunu gösterir.", inline=True)
    await bot.say('📮 | Bilgileri DM olarak gönderdim.')
    await bot.send_message(ctx.message.author, embed=embed)
   
@bot.command()
async def link():
    await bot.say('https://discord.gg/k2k8Hvt')
 
@bot.command(pass_context=True)
async def kurallar(ctx):
    embed = discord.Embed(title="Kurallar:", description="-Roleplay+'e hoşgeldin! \n1) Sunucuda saygılı olun. \n2) Sunucuda boş boş küfürler savurmayın, susturulursunuz. Devam ederseniz ban yersiniz. \n3) Irka, millete, devlete, soya, manevi değerlere küfür kesinlikle yasaktır. \n4) İroninin tadını kaçırmayın. \n5) Kanalları amacınca kullanın. \n-Pek fazla kuralımız yoktur. Kafanıza göre eğlenin ve yeni Roleplayleri bekleyin. ⚜️", color=0x5f0bdd)
    await bot.say(embed=embed)
 
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def rolsil(ctx, user:discord.User,*,role:discord.Role):
    if role in user.roles:
        await bot.remove_roles(user, role)
        embed = discord.Embed(title="Başarılı. ✓", description=f"Rol silindi!", color=0x5f0bdd)
        embed.set_footer(text=f'İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        return await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Başarısız. ❌", description="Üyede bu rol yok!", color=0x5f0bdd)
        embed.set_footer(text=f'İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
 
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def rolver(ctx, user:discord.User,*,role:discord.Role):
    if role not in user.roles:
        await bot.add_roles(user, role)
        embed = discord.Embed(title="Başarılı. ✓", description=f"Rol başarıyla üyeye verildi.", color=0x5f0bdd)
        embed.set_footer(text=f'İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        return await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Başarısız. ❌", description="Rol zaten var!", color=0x5f0bdd)
        embed.set_footer(text=f'İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
 
     
@bot.command(pass_context=True)
async def sunucuavatar(ctx):
      embed = discord.Embed(title="Sunucu Avatar:", color=0x5f0bdd)
      embed.set_image(url=ctx.message.server.icon_url)
      embed.set_footer(text=f'İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)  
                       
@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 10
    await bot.edit_message(t, new_content='Pong! Al!: {}ms'.format(int(ms)))    
 
@bot.command(pass_context=True)
async def avatar(ctx, member : discord.Member=None):
    if member is None:
        embed = discord.Embed(title="Avatar:", color=0x5f0bdd)
        embed.set_image(url=ctx.message.author.avatar_url)
        embed.set_footer(text=f'İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Avatar:", color=0x5f0bdd)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f'İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
 
     
@bot.command(pass_context=True)
async def nickdeğiştir(ctx, member : discord.Member, *, nickname):
      if ctx.message.author.server_permissions.change_nickname:
            await bot.change_nickname(member, nickname)
            embed = discord.Embed(title="Nick değiştirildi!", description=f"{member.mention} kullanıcısının nicki {nickname} olarak değiştirildi!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            embed = discord.Embed(title="❌ | Nick değiştirilemedi", description="Bunu yapmak için yetkiniz yok.")
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
     
@bot.event
async def on_command_error(error, ctx):
      if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title="❌ | Komut bulunamadı.", description="Böyle bir komut bulunamadı! Komutlar için: ```-yardım```", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.send_message(ctx.message.channel, embed=embed)
           
@bot.command(pass_context=True)
async def sunucubilgi(ctx):
      embed = discord.Embed(title="Sunucu bilgileri:", color=0x5f0bdd)
      embed.add_field(name="İsim:", value=ctx.message.server.name)
      embed.add_field(name="ID:", value=ctx.message.server.id)
      embed.add_field(name="Kurucu:", value=ctx.message.server.owner)
      embed.add_field(name="Üye sayısı:", value=ctx.message.server.member_count)
      embed.add_field(name="Kurulma tarihi:", value=ctx.message.server.created_at)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
     
@bot.command(pass_context=True)
async def üyebilgi(ctx, member : discord.Member=None):
      if member is None:
            embed = discord.Embed(title="Kullanıcı bilgileri", color=0x5f0bdd)
            embed.add_field(name="İsim:", value=f"{ctx.message.author.name}")
            embed.add_field(name="ID", value=f"{ctx.message.author.id}")
            embed.add_field(name="Durum:",  value=f"{ctx.message.author.status}")
            embed.add_field(name="Oyun:", value=f"{ctx.message.author.game}")
            embed.add_field(name="Katılma tarihi:", value=f"{ctx.message.author.joined_at}")
            embed.add_field(name="Hesabı kurma tarihi:", value=f"{ctx.message.author.created_at}")
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            embed = discord.Embed(title="Kullanıcı bilgileri", color=0x5f0bdd)
            embed.add_field(name="İsim:", value=f"{member.name}")
            embed.add_field(name="ID", value=f"{member.id}")
            embed.add_field(name="Durum:",  value=f"{member.status}")
            embed.add_field(name="Oyun:", value=f"{member.game}")
            embed.add_field(name="Katılma tarihi:", value=f"{member.joined_at}")
            embed.add_field(name="Hesabı kurma tarihi:", value=f"{member.created_at}")
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
       
@bot.command()
async def yaz(*, message: str):
      await bot.say(message)  
     
@bot.command(pass_context=True)
async def duyuruyap(ctx, *, message):
      if ctx.message.author.server_permissions.manage_messages:
            embed = discord.Embed(title="📣 Duyuru:", description=f"**{message}**", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            embed = discord.Embed(title="Duyuru yapılmadı!", description="Bu komutu kullanmak için yetkin yok.", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)         
   
@bot.command(pass_context=True)
async def oylama(ctx, *, message):
    embed = discord.Embed(title="Oylama:", description=message, color=0x5f0bdd)
    embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
    message2 = await bot.say(embed=embed)
    await bot.add_reaction(message2, emoji='👍')
    await bot.add_reaction(message2, emoji='👎')
    await bot.add_reaction(message2, emoji='🤷')         
                       
@bot.command(pass_context=True)
async def seskanalıkur(ctx, *, name):
      server = ctx.message.server
      if ctx.message.author.server_permissions.manage_channels:
            await bot.create_channel(server, f'{name}', type=discord.ChannelType.voice)
            embed = discord.Embed(title="Kanal başarıyla kuruldu!", description=f"{name} isimli kanal kuruldu.", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            embed = discord.Embed(title="Kanal kurulamadı", description="Bunu yapmak için yetkiniz yok!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
                               
@bot.command(pass_context=True)
async def ascii(ctx, *, msg):
        'Convert text to ascii art'
        if ctx.invoked_subcommand is None:
            if msg:
                msg = str(figlet_format(msg.strip(), font='big'))
                if len(msg) > 2000:
                    await client.say('**Mesaj çok uzun, :|**')
                else:
                    try:
                        await bot.say('```fix\n{}\n```'.format(msg))
                    except:
                        pass
        else:
            await bot.say('**Çevirmek istediğiniz yazıyı yazın.**')
     
@bot.command(pass_context=True)
async def yazıkanalıkur(ctx, *, name):
      server = ctx.message.server
      if ctx.message.author.server_permissions.manage_channels:
            await bot.create_channel(server, f'{name}', type=discord.ChannelType.text)
            embed = discord.Embed(title="Kanal başarıyla kuruldu!", description=f"{name} isimli kanal kuruldu.", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            embed = discord.Embed(title="Kanal kurulamadı", description="Bunu yapmak için yetkiniz yok!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
 
@bot.command(pass_context = True)
async def sustur(ctx, member: discord.Member):
      if ctx.message.author.server_permissions.manage_roles:
            role = discord.utils.get(member.server.roles, name='Muted')
            if role in member.server.roles:
                  await bot.add_roles(member, role)
                  embed=discord.Embed(title="Kullanıcı susturuldu!", description=f"{member.mention} isimli kullanıcı {ctx.message.author.mention} tarafından susturuldu!", color=0x5f0bdd)
                  embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
                  await bot.say(embed=embed)
            else:
                  await bot.create_role(ctx.message.author.server, name='Muted', colour=discord.Colour(0xffffff))
                  role = discord.utils.get(member.server.roles, name='Muted')
                  await bot.add_roles(member, role)
                  embed=discord.Embed(title="Kullanıcı susturuldu!", description=f"{member.mention} isimli kullanıcı {ctx.message.author.mention} tarafından susturuldu!", color=0x5f0bdd)
                  embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
                  await bot.say(embed=embed)
      else:
           embed=discord.Embed(title="❌ |Kullanıcı susturulamadı!", description="Bu komutu kullanmak için yetkiniz yok.", color=0x5f0bdd)
           embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
           await bot.say(embed=embed)  
       
@bot.command(pass_context = True)
async def susturaç(ctx, member: discord.Member):
    role = discord.utils.get(member.server.roles, name='Muted')
    if role in member.server.roles:
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="Kullanıcı susturuldu!", description=f"{member.mention} isimli kullanıcının susturulması {ctx.message.author.mention} tarafından açıldı!", color=0x5f0bdd)
        embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
        await bot.remove_roles(member, role)
   
@bot.command(pass_context=True)
async def at(ctx, member : discord.Member):
    if ctx.message.author.server_permissions.kick_members:
       await bot.kick(member)
       embed = discord.Embed(title="Kullanıcı atıldı!", description=f"{member.mention} başarıyla sunucudan atıldı!", color=0x5f0bdd)
       embed.set_image(url="https://media.giphy.com/media/26wkzRNIJ14yU76i4/giphy.gif")
       embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
       await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="❌| Kullanıcı atılamadı!", description="Bu komutu kullanmak için yetkin yok!", color=0x5f0bdd)
        embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
       
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    if ctx.message.author.server_permissions.ban_members:
       await bot.ban(member)
       embed = discord.Embed(title="Kullanıcı banlandı!", description=f"{member.mention} başarıyla sunucudan banlandı!", color=0x5f0bdd)
       embed.set_image(url="https://media.giphy.com/media/26wkzRNIJ14yU76i4/giphy.gif")
       embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
       await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="❌| Kullanıcı banlanamadı!", description="Bu komutu kullanmak için yetkin yok!", color=0x5f0bdd)
        embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
       
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def temizle(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)
    await bot.say(f'{number} sayıda mesajlar silindi.')      
       
bot.run(os.getenv('BOT_TOKEN'))
