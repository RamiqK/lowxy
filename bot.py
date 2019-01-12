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
            await bot.change_presence(game=discord.Game(name=f"rp+yardım", type=1))
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
    await bot.send_message(channel, f'Hoşçakal! {member.name}, Fazla şey kaybettin dostum! Roleplay+ seni her zaman bekliyor! Geri gelebilirsin.')      
           
@bot.command(pass_context=True)
async def köpek(ctx):
      köpek = ["https://i.pinimg.com/236x/36/47/c3/3647c312ab9fbdf3ee602839d6459111.jpg", "https://i.pinimg.com/564x/19/fc/59/19fc59925398de44f22dd6a8914ba5e7.jpg", "https://i.pinimg.com/236x/ed/78/28/ed78287cbcea512f7638fb13c725ed62.jpg", "https://i.pinimg.com/564x/9f/4a/e6/9f4ae61abcbfbdd59720d29688b7e962.jpg", "https://i.pinimg.com/236x/59/f0/79/59f0795e7742dd059f88226f9af1fdc0.jpg", "https://i.pinimg.com/564x/50/ed/72/50ed72e9cfc5ad8f60afc4c00c38fe6b.jpg", "https://i.pinimg.com/564x/c5/ed/b3/c5edb33d4f77b96b051a9130fa63c47c.jpg", "https://i.pinimg.com/564x/2a/f0/af/2af0af8d0073ab1c862644a02dace162.jpg", "https://i.pinimg.com/564x/06/ce/f6/06cef6a1d2de575594abddeeefbc9dad.jpg", "https://i.pinimg.com/564x/7d/27/84/7d27843988f6fe075041dd18d96fe734.jpg", "https://i.pinimg.com/564x/73/b8/91/73b891ecc0d1d7e19a21050cff631016.jpg", "https://i.pinimg.com/564x/af/1d/1d/af1d1d278ba18f12742a0830f3269434.jpg", "https://i.pinimg.com/564x/83/04/d4/8304d4a434dca0fe63b10e0c1dc912c4.jpg"]
      köpekler = random.choice(köpek)
      embed = discord.Embed(title="Bu köpekler çok tatlı.. °-°", color=0x5f0bdd)
      embed.set_image(url=köpekler)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)            
                           
@bot.command(pass_context=True)
async def yardım(ctx):
    embed = discord.Embed(title="Komutlar bunlardır.", description="Prefixim rp+.", color=0x5f0bdd)
    embed.add_field(name="RP+ ile ilgili komutlar:", value="**rp+sunucubilgi**: Sunucu bilgilerini gösterir. \n**rp+üyebilgi**: Kendinin ya da diğer üyenin bilgilerini gösterir. \n**rp+link**: Sunucunun sınırsız davet linkini atar.", inline=True)
    embed.add_field(name="Moderasyon komutları:", value="**rp+at <üye>**: Üyeyi atar. \n**rp+ban <üye>**: Üyeyi banlar. \n**rp+sustur <üye>**: Üyeyi susturur. \n**rp+susturaç <üye>**: Üyenin susturulmasını açar. \n**rp+temizle <sayı>**: Belirtilen sayıda mesajı siler. \n**rp+yazıkanalıkur <isim>**: Yazı kanalı kurar. \n**rp+seskanalıkur <isim>**: Ses kanalı kurar. \n**rp+duyuruyap <duyuru>**: Duyuru yapar. \n**rp+uyar <üye>**: Üyeyi uyarır. \n**rp+nickdeğiştir**: Üyenin nickini değiştirir. \n**rp+rolver**: Rol verir. \n**rp+rolsil**: Rolü siler.", inline=True)
    embed.add_field(name="Diğer komutlar:", value="**rp+wikitürk<1 ya da 2>**: Wikipedide yazdığınız yazıyı Türkçe aratır. (1 - Bir haneli bilgiyi aratır, 2 - 2 haneli bilgiyi aratır. Doğru kullanmazsanız hata verir.) \n**rp+wikieng<1 ya da 2>**: Wikipedide yazdığınız yazıyı İngilizce aratır. (1 - Bir haneli bilgiyi aratır, 2 - 2 haneli bilgiyi aratır. Doğru kullanmazsanız hata verir.) \n**rp+ascii <mesaj>**: Mesajı ASCII Arta çevirir. \n**rp+oylama <mesaj>**: Oylama yapar. \n**rp+yaz <mesaj>**: Bota mesajı yazdırır. \n**rp+ping**: Anlık pingi gösterir. \n**rp+avatar**: Senin ya da üyenin ikonunu gösterir. \n**rp+sunucuavatar**: Sunucunun ikonunu gösterir.", inline=True)
    embed.add_field(name="Eğlence:", value="**rp+hack <kişi>**: Etiketlediğiniz kişiyi hackler. \n**rp+köpek**: Rastgele köpek resimleri atar. \n**rp+kirpi**: Rastgele kirpi resimleri atar. \n**rp+kedi**: Rastgele kedi resimleri atar. \n**rp+penis**: °-° \n**rp+gay**: Gaylık seviyenizi ölçer. \n**rp+sor**: Bota soru sorun. \n**rp+gizlimesaj <kişi>**: Bot etiketlediğiniz kişiye gizli mesaj yollar. \n**rp+aşkölçer <kişi>**: <3. \n**rp+iq**: IQ Ölçer.", inline=True)
    await bot.say('📮 | Bilgileri DM olarak gönderdim.')
    await bot.send_message(ctx.message.author, embed=embed)
     
@bot.command(pass_context=True)
async def iq(ctx, member : discord.Member=None):
      if member is None:
            number = random.randint(1, 100)
            embed = discord.Embed(title="IQ Ölçer:", description=f"{ctx.message.author.mention}, bence senin IQ seviyen: {number}!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            number = random.randint(1, 100)
            embed = discord.Embed(title="IQ Ölçer:", description=f"{member.mention}, bence onun IQ Seviyesi: {number}!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
     
@bot.command(pass_context=True)
async def aşkölçer(ctx, member : discord.Member):
      number = random.randint(1, 100)
      embed = discord.Embed(title="Aşk Ölçer!", description=f"{ctx.message.author.mention} {number}%❤ {member.mention}", color=0x5f0bdd)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
         
@bot.command(pass_context=True)
async def sor(ctx):
      cevap = ["Evet.", "Hayır.", "Kesinlikle.", "Bence değil.", "Olabilir.", "Kes!", "Kesinlikle değil.", "Peki.", "Siktir lan!", "Aynen öyle.", "He, he, aynen!"]
      cevaplar = random.choice(cevap)
      await bot.say(cevaplar)
 
@bot.command(pass_context=True)
async def gizlimesaj(ctx, member : discord.Member, *, message):
      await bot.delete_message(ctx.message)
      await bot.send_message(member, message)    
 
@bot.command(pass_context=True)
async def uyar(ctx, member: discord.Member, *, message):
      if ctx.message.author.server_permissions.kick_members:
            embed = discord.Embed(title="Kullanıcı uyarıldı!", description=f"{member.mention}, {message} için uyarıldı. {member.name} Bir dahakine dikkat et ;)", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            embed = discord.Embed(title="❌ | Kullanıcı uyarılamadı!", description="Bunu yapmak için yetkin yok.", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
 
@bot.command(pass_context=True)
async def penis(ctx, member : discord.Member=None):
      if member is None:
            penisler = [f"{ctx.message.author.mention}, senin penisin __Yok.__", f"{ctx.message.author.mention}, senin penisin: \n8=>", f"{ctx.message.author.mention}, senin penisin: \n8==>", f"{ctx.message.author.mention}, senin penisin: \n8===>", f"{ctx.message.author.mention}, senin penisin: \n8====>", f"{ctx.message.author.mention}, senin penisin: \n8=====>", f"{ctx.message.author.mention}, senin penisin: \n8======>", f"{ctx.message.author.mention}, senin penisin: \n8=======>🔥"]
            penisim = random.choice(penisler)
            embed = discord.Embed(title="Penis ölçüldü..", description=penisim, color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
        penisler = [f"{member.mention} kullanıcısının penisi: __Yok.__", f"{member.mention} kullanıcısının penisi: 8=>", f"{member.mention} kullanıcısının penisi: 8==>", f"{member.mention} kullanıcısının penisi: 8===>", f"{member.mention} kullanıcısının penisi: 8====>", f"{member.mention} kullanıcısının penisi: 8=====>", f"{member.mention} kullanıcısının penisi: 8======>", f"{member.mention} kullanıcısının penisi: 8=======>🔥"]
        penisim = random.choice(penisler)
        embed = discord.Embed(title=f"Penis ölçüldü..", description=penisim, color=0x5f0bdd)
        await bot.say(embed=embed)
           
@bot.command(pass_context=True)
async def gay(ctx, member : discord.Member=None):
    if member is None:
        number = random.randint(1, 100)
        embed = discord.Embed(title="Gaylık ölçüldü..", description=f"{ctx.message.author.mention}, sen {number}% gaysın!", color=0x5f0bdd)
        embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        number = random.randint(1, 100)
        embed = discord.Embed(title="Gaylık ölçüldü..", description=f"{member.mention}, sen {number}% gaysın!", color=0x5f0bdd)
        embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)        
     
@bot.command(pass_context=True)
async def kedi(ctx):
      kedi = ["https://i.pinimg.com/564x/0d/11/6c/0d116c8e58fa9a039115ee55fa57027d.jpg", "https://i.pinimg.com/564x/eb/92/d9/eb92d9ce8485a137a9946443c054913d.jpg", "https://i.pinimg.com/564x/36/47/f6/3647f6339f0d7acc9b4348cb27b9ed1b.jpg", "https://i.pinimg.com/564x/89/4b/81/894b813dffb6484734091af5910487c6.jpg", "https://i.pinimg.com/564x/36/01/31/3601311295c515abf1232ff70a77477e.jpg", "https://i.pinimg.com/564x/ec/76/ed/ec76ed0f05260a370a087d8bba2efbd1.jpg", "https://i.pinimg.com/564x/46/0c/5c/460c5c7dc40d4ef1191eb974ef4f8afb.jpg", "https://i.pinimg.com/564x/bf/c5/49/bfc54910fa33ea6914822dbc607be853.jpg", "https://i.pinimg.com/564x/ce/ba/e8/cebae8b23eb2b1c3c808f8727d842db1.jpg", "https://i.pinimg.com/564x/69/7a/e3/697ae31579bb6a4d326964c1b19008bc.jpg", "https://i.pinimg.com/564x/43/f2/c6/43f2c6dadc9708a3ea8f63f9ee253506.jpg", "https://i.pinimg.com/564x/7c/7e/c3/7c7ec3c8ec43faa8c944a1da9a8a416c.jpg", "https://i.pinimg.com/564x/b2/3e/1a/b23e1a203d704e77025acaf157612c16.jpg", "https://i.pinimg.com/564x/dd/90/60/dd90608f2941f2d6d7dcb36a509719ff.jpg", "https://i.pinimg.com/564x/22/a1/7b/22a17bceee3c5c30a53360946c18073c.jpg", "https://i.pinimg.com/564x/43/94/02/4394028c97f4e7d9fb66e02062834e51.jpg", "https://i.pinimg.com/564x/88/63/9f/88639f36e583b6d3db9ecc07a5dd18c8.jpg", "https://i.pinimg.com/564x/9a/f1/b6/9af1b6b966ef5e4ba0edacdb61658380.jpg", "https://i.pinimg.com/564x/75/29/b0/7529b0868666c34fb3103bb4bc894185.jpg", "https://i.pinimg.com/564x/f6/46/34/f64634c6bc11e6c17f9db0e66fba0d0d.jpg"]
      kediler = random.choice(kedi)
      embed = discord.Embed(title="Tatlı kedilerrr.. •.•", color=0x5f0bdd)
      embed.set_image(url=kediler)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
 
@bot.command(pass_context=True)
async def kirpi(ctx):
      kirpi = ["https://i.pinimg.com/originals/ef/a8/f2/efa8f2dcfb868214f2bf1358fe154187.png", "https://i.pinimg.com/originals/53/a0/38/53a038a08b2b6687aa22553651d6a8b2.jpg", "https://i.pinimg.com/originals/ef/a8/f2/efa8f2dcfb868214f2bf1358fe154187.png", "https://i.pinimg.com/originals/bd/22/7b/bd227b3db2194d5019b7264120014f8b.jpg", "https://i.pinimg.com/originals/80/dd/c5/80ddc587f0dadb6fde3cdda3c891d577.jpg", "https://i.pinimg.com/564x/48/44/a6/4844a6c2cc18da33571ef8c09337fb0f.jpg", "https://i.pinimg.com/originals/17/6c/ed/176ced87b63f0aa412c1bfcc6920a7af.jpg", "https://i.pinimg.com/564x/ad/98/63/ad9863b18b8c2c9381881a4397faa008.jpg", "https://i.pinimg.com/564x/de/dd/0f/dedd0f2c2a17d43bca1c7bb2b018e835.jpg", "https://i.pinimg.com/originals/3f/d6/3f/3fd63f0d84ba22279838c694ab79b1ce.jpg", "https://i.pinimg.com/564x/ad/98/63/ad9863b18b8c2c9381881a4397faa008.jpg", "https://i.pinimg.com/564x/fa/32/2c/fa322cffb6ef187ff105eb5b2681e55a.jpg", "https://i.pinimg.com/originals/1d/65/03/1d650368a85e82fdb15bd42ab415f9da.jpg", "https://i.pinimg.com/originals/9e/e4/9d/9ee49dae54cba763155fff0840ca6ffd.jpg", "https://i.pinimg.com/originals/70/e5/ba/70e5bab3e47af70b9f0cf7bf3c75326f.jpg", "https://i.pinimg.com/236x/25/c1/20/25c120bed8e6f401c6e6005fcb29a2e1.jpg", "https://i.pinimg.com/originals/43/f6/a5/43f6a55f2f4ba5b20ff3b21bd095c497.jpg", "https://i.pinimg.com/originals/27/53/22/2753227371e30b6bc60c6536ca47c149.jpg", "https://i.pinimg.com/564x/90/16/8a/90168a19cecb160e2a80b81b46fd9a6d.jpg", "https://i.pinimg.com/564x/54/ce/40/54ce4031b1ccd6bf2a2251caf52fcb89.jpg", "https://i.pinimg.com/564x/3f/b3/1d/3fb31dcd9d12df97fe2c04b843c6a2da.jpg", "https://i.pinimg.com/564x/43/b6/98/43b698f7897374049adcc8b0c68451db.jpg", "https://i.pinimg.com/564x/22/1b/4b/221b4b3abbd3ed799d34049137107557.jpg", "https://i.pinimg.com/564x/29/7b/7e/297b7e21f66f4e2dbcc589f911154e90.jpg", "https://i.pinimg.com/564x/2f/a9/6e/2fa96eb608d636899e700387f12250e0.jpg", "https://i.pinimg.com/564x/70/e5/ba/70e5bab3e47af70b9f0cf7bf3c75326f.jpg", "https://i.pinimg.com/564x/27/53/22/2753227371e30b6bc60c6536ca47c149.jpg"]
      kirpiler = random.choice(kirpi)
      embed = discord.Embed(title="Bir birinden tatlı kirpiler >.< <3", color=0x5f0bdd)
      embed.set_image(url=kirpiler)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
     
@bot.command(pass_context=True)
async def hack(ctx, member: discord.Member):
      a = await bot.say(f'{member.name} hacklemek için hazırlanıyor..')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'{member.name} kullanıcısının discord hesabı hackleniyor..')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'`` email: {member.name}****@gmail.com \nşifre: ********``')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'Facebook hesabı aranıyor..')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'Bulundu ve hacklendi.')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'İP adresi aranıyor..')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'Bulundu. ✓')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'Diğer sosyal medya hesapları aranıyor..')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'Bulundu ve hacklendi!')
      await asyncio.sleep(4)
      await bot.edit_message(a, new_content=f'{member.name} Başarıyla hacklendi!')
                 
@bot.command()
async def link():
    await bot.say('https://discord.io/roleplayplus')
 
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
            embed = discord.Embed(title="❌ | Komut bulunamadı.", description="Böyle bir komut bulunamadı! Komutlar için: ```rp+yardım```", color=0x5f0bdd)
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
