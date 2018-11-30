import discord
from discord.ext import commands
import asyncio
import random
import datetime
from pyfiglet import figlet_format, FontError, FontNotFound
from pyfiglet import figlet_format, FontError, FontNotFound
bot = commands.Bot(command_prefix='-')
bot.remove_command("help")

@bot.event
async def on_ready():
	print(bot.user.name)
	print(bot.user.id)

@bot.command(pass_context=True)
async def status(ctx):
      if ctx.message.author.id == "452912036670865438":
            await bot.change_presence(game=discord.Game(name=f"-yardım | -silahlar eklendi! | {str(len(bot.servers))} Sunucu ve {str(len(set(bot.get_all_members())))} Kullanıcı!", type=1))
            await bot.say('```Başarılı.```')
      else:
            await bot.say('```Bunu sadece botun yapımcısı yapabilir!```')

@bot.command(pass_context=True)
async def yardım(ctx):
      embed = discord.Embed(title="LowxyBot | Lowxynin komutları bunlardır:", description="Botun prefixi: -", color=0x5f0bdd)
      embed.add_field(name="🎉 Eğlence", value="-kirpi - Birbirinden tatlı kirpi resimleri. >,< \n-kedi - Birbirinden tatlı kedilerrrr.. ♥-♥ \n-köpek - Tatlı mı tatlı Köpeklerr! ^-^ \n-sarıl [kişi] - Etiketlediğiniz kişiye sarılırsınız. \n-uç [bölge], \n-çekiçat [kişi] - Etiketlediğiniz kişiye çekiç atılır, \n-sigara - Sigara yakar. :/, \n-aşkölçer [kişi] - Aşk Ölçer :) \n-öp [kişi] - Etiketlediğiniz kişiyi öpersiniz. \n-tokatla [kişi] - etiketlediğiniz kişiyi tokatlarsınız. \n-silahlar - Silahlar hakkında bilgi alabileceğiniz kategoriyi açar. \n-hack [kişi] - Etiketlediğiniz kişi hacklenir. \n-söv [kişi] - Etiketlediğiniz kişi sövülür. (Olacaklardan sorumlu değiliz. xD) \n-penis - Bot penisinizi ölçer. :D \n-gay - Bot gaylık seviyenizi ölçer. \n-iq - Bot İQnüzü ölçer.", inline=True)
      embed.add_field(name="💻 Bot",  value="-yardım - Şuan olduğunuz yardım menüsünü gösterir. \n-yaz [yazı] - Bota yazı yazdırır. \n-oylama [yazı] - Bota oylama yaptırır. \n-rakam - Bot 1 ve 100 aralığında rakam söyler. \n-versiyon - Botun güncel versiyonunu gösterir. \n-davet - Botu sunucunuza davet linkini gösterir. \n-destek - Botun destek sunucusunu gösterir. \n-yapımcı - Yapımcının Discord Hesabını gösterir. \n-gizlimesaj [kişi] [yazı] - Etiketlediğiniz kişiye gizli mesaj atar. \n-duyuruyap [duyuru] - Duyuru yaparsınız. \n-ping - Anlık pingi gösterir. \n-ascii [yazı] - Yazdığınız yazıyı ASCII-ye çevirir.", inline=True)
      embed.add_field(name="📁 Bilgiler", value="-sunucubilgi - Sunucu bilgilerini gösterir. \n-üyebilgi - Kullanıcı bilgilerini gösterir. \n-ikonum - İkonunuzu gösterir. \n-sunucuikon - Sunucu ikonunu gösterir. \n-id - Kendinizin ve ya etiketlediğiniz kişinin IDsini gösterir.", inline=True)
      embed.add_field(name="🛠️ Moderasyon", value="-at - Etiketlediğiniz kişiyi sunucudan atar. \n-ban - Etiketlediğiniz kişiyi sunucudan banlar. \n-sustur - Etiketlediğiniz kişiyi susturur. (Botun oluşturduğu rolün mesaj gönderme yetkisi kapatılmalı.) \n-susturaç - Etiketlediğiniz kişinin susturulmasını açar. \n-temizle - 2 ve 100 arası sayıda mesajı siler. \n-nickdeğiştir - Etiketlediğiniz kişinin nickini değiştirir. \n-uyar [kişi] - Etiketlediğiniz kişiyi uyarırsınız. \n-yazıkanalıkur [isim] - Yazı kanalı kurarsınız. \n-seskanalıkur [isim] - Ses kanalı kurarsınız.", inline=True)
      embed.set_footer(text='İçin oluşturuldu. | Yardım Menüsü', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def sarıl(ctx, member : discord.Member):
      embed = discord.Embed(title="Sarılma!", description=f"{ctx.message.author.mention}, {memner.mention} isimli kullanıcıya sarıldı!", color=0x5f0bdd)
      embed.set_image(url="http://gph.is/YZrpPA")
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
            
@bot.command(pass_context=True)
async def köpek(ctx):
      köpek = ["https://i.pinimg.com/236x/36/47/c3/3647c312ab9fbdf3ee602839d6459111.jpg", "https://i.pinimg.com/564x/19/fc/59/19fc59925398de44f22dd6a8914ba5e7.jpg", "https://i.pinimg.com/236x/ed/78/28/ed78287cbcea512f7638fb13c725ed62.jpg", "https://i.pinimg.com/564x/9f/4a/e6/9f4ae61abcbfbdd59720d29688b7e962.jpg", "https://i.pinimg.com/236x/59/f0/79/59f0795e7742dd059f88226f9af1fdc0.jpg", "https://i.pinimg.com/564x/50/ed/72/50ed72e9cfc5ad8f60afc4c00c38fe6b.jpg", "https://i.pinimg.com/564x/c5/ed/b3/c5edb33d4f77b96b051a9130fa63c47c.jpg", "https://i.pinimg.com/564x/2a/f0/af/2af0af8d0073ab1c862644a02dace162.jpg", "https://i.pinimg.com/564x/06/ce/f6/06cef6a1d2de575594abddeeefbc9dad.jpg", "https://i.pinimg.com/564x/7d/27/84/7d27843988f6fe075041dd18d96fe734.jpg", "https://i.pinimg.com/564x/73/b8/91/73b891ecc0d1d7e19a21050cff631016.jpg", "https://i.pinimg.com/564x/af/1d/1d/af1d1d278ba18f12742a0830f3269434.jpg", "https://i.pinimg.com/564x/83/04/d4/8304d4a434dca0fe63b10e0c1dc912c4.jpg"]
      köpekler = random.choice(köpek)
      embed = discord.Embed(title="Bu köpekler çok tatlı.. °-°", color=0x5f0bdd)
      embed.set_image(url=köpekler)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def id(ctx, member : discord.Member=None):
      if member is None:
            await bot.say(f'``{ctx.message.author.id}``')
      else:
            await bot.say(f'``{member.id}``')  
            
@bot.command(pass_context=True)
async def söv(ctx, member : discord.Member=None):
      if member is None:
            embed = discord.Embed(title="Komut yapılamadı! -_-", description="Sövmem için birini etiketlemen gerek!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            küfür = [f"{member.mention} sen has orospu çocuğusun.", f"{member.mention} anneni sövmek istemem ama, seni doğduğu için orospu!", f"{member.mention} Senin ananın amını sikerim. Hadi uza!", f"{member.mention} Anasını siktiğimin çocuğu.", f"{member.mention} Teletabilerin antenini ananın amına sokarım, ananın amında ulusal porno açarım.", f"{member.mention} Seni Azerbaycandan gelib sikerem", f"{member.mention} Kurwa.", f"{member.mention} Baban gay."]
            küfürler = random.choice(küfür)
            embed = discord.Embed(title="Ulan!", description=küfürler, color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)            
                        
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
async def sunucuikon(ctx):
      embed = discord.Embed(title="Sunucu İkonu:", color=0x5f0bdd)
      embed.set_image(url=ctx.message.server.icon_url)
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
async def tokatla(ctx, member : discord.Member):
      embed = discord.Embed(title="Tokatlandın!", description=f"{member.mention}! {ctx.message.author.mention} tarafından tokatlandın!", color=0x5f0bdd)
      embed.set_image(url="https://gph.is/H3sAeI")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      embed.set_image(url="http://gph.is/YZrpPA")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def iq(ctx, member : discord.Member=None):
      if member is None:
            number = random.randint(1, 100)
            embed = discord.Embed(title="IQün:", description=f"{ctx.message.author.mention}, senin İQün: {number}!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)
      else:
            number = random.randint(1, 100)
            embed = discord.Embed(title="İQü:", description=f"{member.mention} adlı kullanıcının İQsü: {number}!", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.say(embed=embed)        
      
@bot.command(pass_context=True)
async def sigara(ctx):
      a = await bot.say("🚬🕯️")
      await bot.edit_message(a, new_content="🚬💨")
      await bot.edit_message(a, new_content="🚬💨💨💨")
      await bot.edit_message(a, new_content="🚬💨💨")
      await bot.edit_message(a, new_content="🚬💨")
      await bot.edit_message(a, new_content="🚬🗑️")
      await bot.edit_message(a, new_content="Sigara içmek sağlığınıza zararlıdır.")
      
@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 10
    await bot.edit_message(t, new_content='Pong! Al!: {}ms'.format(int(ms)))
      
@bot.command(pass_context=True)
async def ikonum(ctx):
      embed = discord.Embed(title="İkonun:", color=0x5f0bdd)
      embed.set_image(url=ctx.message.author.avatar_url)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def öp(ctx, member : discord.Member):
      embed = discord.Embed(title="<3 Öpüş..", description=f"{ctx.message.author.mention}, {member.mention} isimli kişiyi öptü!", color=0x5f0bdd)
      embed.set_image(url="https://giphy.com/gifs/hug-love-winnie-the-pooh-llmZp6fCVb4ju")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def aşkölçer(ctx, member : discord.Member):
      number = random.randint(1, 100)
      embed = discord.Embed(title="Aşk Ölçer!", description=f"{ctx.message.author.mention} {number}%❤ {member.mention}", color=0x5f0bdd)
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
async def uç(ctx, *, message):
      embed = discord.Embed(title="Uçuyorsunuzz!!", description=f"Lowxy sizi {message} taraflara uçurdu!", color=0x5f0bdd)
      embed.set_image(url="https://giphy.com/gifs/harry-potter-daniel-radcliffe-pYCZPDymIVjeo")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)  
      
@bot.command(pass_context=True)
async def silahlar(ctx):
      embed = discord.Embed(title="2 Kategori bulunmaktadır.", description="-keskinnişancı - Keskin nişancı silahları hakkında bilgi. \n-tüfek - Piyade tüfekleri hakkında bilgi.", color=0x5f0bdd)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def versiyon(ctx):
      embed = discord.Embed(title="LowxyBotun güncel versiyonu:", description="<:discord:515202807968694287>  | Version0.2.3", color=0x5f0bdd)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def çekiçat(ctx, member : discord.Member):
      embed = discord.Embed(title="Çekiç atıldı!", description=f"{member.mention} 🔨 Çekiç sana değdi, canın acımış olmalı..", color=0x5f0bdd)
      embed.set_image(url="https://giphy.com/gifs/thor-dc-universe-hawkman-Nmmb3MW2tABiw")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
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
		
@bot.command()
async def yaz(*, message: str):
      await bot.say(message)   
    
@bot.command(pass_context=True)
async def oylama(ctx, *, message):
    embed = discord.Embed(title="Oylama:", description=message, color=0x5f0bdd)
    embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
    message2 = await bot.say(embed=embed)
    await bot.add_reaction(message2, emoji='👍')
    await bot.add_reaction(message2, emoji='👎')
    await bot.add_reaction(message2, emoji='🤷')
 
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
    await bot.say(f'<a:okedoke:500731619213049856> | {number} sayıda mesajlar silindi.')   
     
@bot.command(pass_context=True)
async def rakam(ctx):
	number = random.randint(1, 100)
	embed = discord.Embed(title="Rakam:", description=number, color=0x5f0bdd)
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
async def davet(ctx):
      embed = discord.Embed(title="Beni sunucuna eklemek istiyorsan:", color=0x5f0bdd)
      embed.add_field(name="Davet linki:", value="https://tiny.cc/LowxyBot <a:okedoke:500731619213049856>")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def destek(ctx):
      embed = discord.Embed(title="Destek sunucumuza gelerek bize yardım edebilirsiniz!", description="https://discord.gg/UbpzJJ", color=0x5f0bdd)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
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
            
@bot.command(pass_context=True)
async def yapımcı(ctx):
      embed = discord.Embed(title="LowxyBotun Yapımcısı:", color=0x5f0bdd)
      embed.add_field(name="RamiqK#5502", value="Arkadaşlık atarak isteklerinizi yazabilirsiniz.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.event
async def on_command_error(error, ctx):
      if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title="❌ | Komut bulunamadı.", description="Böyle bir komut bulunamadı! Komutlar için: ```-yardım```", color=0x5f0bdd)
            embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
            await bot.send_message(ctx.message.channel, embed=embed)
          
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
          
@bot.command(pass_context=True)
async def istiglal(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Istiglal.jpg/220px-Istiglal.jpg")
      embed.add_field(name="İsmi:", value="Istiglal Anti-Materyal tüfeği")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Azerbaycan, Azerbaycan Savunma Sanayi")
      embed.add_field(name="Fişek:", value="14.5x114mm")
      embed.add_field(name="Tip:", value="Geri tepme işletmeli, Dönen sürgü")
      embed.add_field(name="Üretime başlandığı yıl", value="2008")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def accarctic(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Accuracy_International_Arctic_Warfare_-_Psg_90.jpg/300px-Accuracy_International_Arctic_Warfare_-_Psg_90.jpg")
      embed.add_field(name="İsmi:", value="Accuracy International Arctic Warfare")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Birleşik Krallık, Accuracy International")
      embed.add_field(name="Fişek:", value=".243 Winchester, 7.62x51mm NATO, .308 Winchester, .300 Winchester Magnum, .338 Lapua Magnum")
      embed.add_field(name="Tip:", value="Kurmalı")
      embed.add_field(name="Üretime başlandığı yıl", value="1982")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def jng90(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="http://modernfirearms.net/userfiles/images/sniper/sn98/bora_jng90.jpg")
      embed.add_field(name="İsmi:", value="MKEK JNG-90")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Türkiye, MKEK")
      embed.add_field(name="Fişek:", value="7.62x51mm NATO")
      embed.add_field(name="Tip:", value="Kurmalı")
      embed.add_field(name="Üretime başlandığı yıl", value="2004")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def a91(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/A-91.jpg/300px-A-91.jpg")
      embed.add_field(name="İsmi:", value="A-91")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Rusya, KBP")
      embed.add_field(name="Mühimmat:", value="7.62x39mm, 9x19mm Parabellum, 5.45x39mm, 5.56x45mm, NATO(5,56A-91), VOG-25 (bombaatar)")
      embed.add_field(name="Kalibre:", value="7.62 mm, 5.56 mm, 5.45 mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1991")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def aek971(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/AEK971IRL.jpg/300px-AEK971IRL.jpg")
      embed.add_field(name="İsmi:", value="AEK-971")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Sovyetler B., Sergey I. Koksharov")
      embed.add_field(name="Uzunluk:", value="960 mm")
      embed.add_field(name="Ağırlık:", value="3.3 kg")
      embed.add_field(name="Üretime başlandığı yıl", value="1970")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ak107(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/AK-107_with_grenade_launcher.jpg/300px-AK-107_with_grenade_launcher.jpg")
      embed.add_field(name="İsmi:", value="AK-107")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Sovyetler B., Mihail Kalaşnikov")
      embed.add_field(name="Mühimmat:", value="5.45 x 39 mm, AK-1075.56x45mm, NATO AK-108")
      embed.add_field(name="Kalibre:", value="5.45 mm, 5.56 mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Yeni.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ak47(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/AKMS_and_AK-47_DD-ST-85-01270.jpg/300px-AKMS_and_AK-47_DD-ST-85-01270.jpg")
      embed.add_field(name="İsmi:", value="AK-47")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Sovyetler B., Mihail Kalaşnikov")
      embed.add_field(name="Mühimmat:", value="7.62x39 mm")
      embed.add_field(name="Kalibre:", value="7.62")
      embed.add_field(name="Üretime başlandığı yıl", value="1949")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ak74(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Ak74assault.jpg/300px-Ak74assault.jpg")
      embed.add_field(name="İsmi:", value="AK-74")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Sovyetler B., Mihail Kalaşnikov")
      embed.add_field(name="Mühimmat:", value="5.45 x 39 mm")
      embed.add_field(name="Kalibre:", value="5.45")
      embed.add_field(name="Üretime başlandığı yıl", value="1974")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def an94(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Rifle_AN-94.jpg/270px-Rifle_AN-94.jpg")
      embed.add_field(name="İsmi:", value="AN-94")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Rusya, İzhmash")
      embed.add_field(name="Mühimmat:", value="5.45 x 39 mm")
      embed.add_field(name="Kalibre:", value="5.45")
      embed.add_field(name="Üretime başlandığı yıl", value="1994")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ar10(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/AR-10_in_the_National_Firearms_Museum.jpg/300px-AR-10_in_the_National_Firearms_Museum.jpg")
      embed.add_field(name="İsmi:", value="AR-10")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD")
      embed.add_field(name="Mühimmat:", value="7.62×51mm NATO, .308 Winchester")
      embed.add_field(name="Kalibre:", value="7.62 mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1960")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def asval(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/AS_Val_%28541-03%29.jpg/300px-AS_Val_%28541-03%29.jpg")
      embed.add_field(name="İsmi:", value="AS Val")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Sovyetler B., Tula Silah Fabrikası")
      embed.add_field(name="Mühimmat:", value="9x39mm")
      embed.add_field(name="Kalibre:", value="9 mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1987")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
   
@bot.command(pass_context=True)
async def barx160(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Beretta_AR_with_thermal_sight_and_grenade_launcher.jpg/300px-Beretta_AR_with_thermal_sight_and_grenade_launcher.jpg")
      embed.add_field(name="İsmi:", value="Beretta ARX 160")
      embed.add_field(name="Üretici ülke ve Üretici:", value="İtalya, Pietro Beretta")
      embed.add_field(name="Mühimmat:", value="5.45x39mm Soviet, .56x45mm NATO, 6.8x43mm Remington SPC, 7.62x39mm M43 Soviet")
      embed.add_field(name="Atış hızı:", value="700 rpm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def daek1(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Carbine_Daewoo_K1.jpg/300px-Carbine_Daewoo_K1.jpg")
      embed.add_field(name="İsmi:", value="Daewoo K1")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Güney More")
      embed.add_field(name="Mühimmat:", value=".56x45mm NATO")
      embed.add_field(name="Atış hızı:", value="700-900 rpm")
      embed.add_field(name="Üretime başlandığı yıl", value="1980")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def daek2(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Daewoo_K2_kzl.JPG/300px-Daewoo_K2_kzl.JPG")
      embed.add_field(name="İsmi:", value="Daewoo K2")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Güney More")
      embed.add_field(name="Mühimmat:", value=".56x45mm NATO")
      embed.add_field(name="Atış hızı:", value="700-900 rpm")
      embed.add_field(name="Üretime başlandığı yıl", value="1984")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def dc7a1(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/C7A1_with_IronSights.JPG/300px-C7A1_with_IronSights.JPG")
      embed.add_field(name="İsmi:", value="Diemaco C7A1")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Kanada")
      embed.add_field(name="Mühimmat:", value="5.56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1982")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def famas(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/FAMAS_dsc06877.jpg/280px-FAMAS_dsc06877.jpg")
      embed.add_field(name="İsmi:", value="FAMAS")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Fransa")
      embed.add_field(name="Mühimmat:", value="5.56x45mm")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def fara83(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/FARA_83.JPG/300px-FARA_83.JPG")
      embed.add_field(name="İsmi:", value="Fara 83")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Arjantin")
      embed.add_field(name="Mühimmat:", value="5.56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1984")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def fnf2000(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/FN_F2000_S.jpg/200px-FN_F2000_S.jpg")
      embed.add_field(name="İsmi:", value="FN F2000")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Belçika")
      embed.add_field(name="Mühimmat:", value="5.56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def fnscar(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.add_field(name="İsmi:", value="FN SCAR")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Belçika")
      embed.add_field(name="Mühimmat:", value="5.56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def gwhr98(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Mauser_m98.jpg/300px-Mauser_m98.jpg")
      embed.add_field(name="İsmi:", value="Gewehr 98")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Alman imp.")
      embed.add_field(name="Mühimmat:", value="7,92x57mm")
      embed.add_field(name="Kalibre:", value="7,92mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1898")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def hazri(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.add_field(name="İsmi:", value="Hazri")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Alman imp.")
      embed.add_field(name="Mühimmat:", value="5,45x39mm")
      embed.add_field(name="Kalibre:", value="5,45mm")
      embed.add_field(name="Üretime başlandığı yıl", value="2011")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hkg11(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Gewehr_G11_sk.jpg/300px-Gewehr_G11_sk.jpg")
      embed.add_field(name="İsmi:", value="Heckler & Koch G11")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Batı Almanya")
      embed.add_field(name="Mühimmat:", value="4,73x33mm")
      embed.add_field(name="Kalibre:", value="4,73mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hkg41(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Gewehr_G11_sk.jpg/300px-Gewehr_G11_sk.jpg")
      embed.add_field(name="İsmi:", value="Heckler & Koch G41")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Almanya, H&K")
      embed.add_field(name="Mühimmat:", value="5,56x45mm")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hkg417(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/HK_417_080810_44.jpg/200px-HK_417_080810_44.jpg")
      embed.add_field(name="İsmi:", value="Heckler & Koch G417")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Almanya, H&K")
      embed.add_field(name="Mühimmat:", value="7,62x51mm")
      embed.add_field(name="Kalibre:", value="7,62mm")
      embed.add_field(name="Üretime başlandığı yıl", value="2008")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ht89(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Type_89_Assault_Rifle_JGSDF.jpg/300px-Type_89_Assault_Rifle_JGSDF.jpg")
      embed.add_field(name="İsmi:", value="Howa Type 89")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Japonya")
      embed.add_field(name="Mühimmat:", value="5,65x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,65mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def imblmd(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Imbel_md2.jpg/300px-Imbel_md2.jpg")
      embed.add_field(name="İsmi:", value="İMBEL MD")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Brezilya")
      embed.add_field(name="Mühimmat:", value="5,65x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,65mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def imitavor21(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Tavor-latrun-exhibition-1.jpg/250px-Tavor-latrun-exhibition-1.jpg")
      embed.add_field(name="İsmi:", value="İMİ Tavor TAR-21")
      embed.add_field(name="Üretici ülke ve Üretici:", value="İsrail, İMİ")
      embed.add_field(name="Mühimmat:", value="5,65x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,65mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Bilinmiyor.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def insas(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/INSAS_Rifle.jpg/300px-INSAS_Rifle.jpg")
      embed.add_field(name="İsmi:", value="İNSAS")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Hindistan")
      embed.add_field(name="Mühimmat:", value="5,65x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,65mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1997")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def krbnr98k(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/En-Kar98k_rifle.jpeg/300px-En-Kar98k_rifle.jpeg")
      embed.add_field(name="İsmi:", value="Karabiner 98k")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Nazi Almanyası, SS")
      embed.add_field(name="Mühimmat:", value="7,92x57mm")
      embed.add_field(name="Kalibre:", value="7,92mm")
      embed.add_field(name="Üretime başlandığı yıl", value="Sadece 1935.")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def beryl(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Beryl_rifle_POL.jpg/300px-Beryl_rifle_POL.jpg")
      embed.add_field(name="İsmi:", value="Beryl")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Polonya")
      embed.add_field(name="Mühimmat:", value="5,56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1996")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def khaybar(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/KH-2002_Khaybar_Illustration_%28v2%29.png/300px-KH-2002_Khaybar_Illustration_%28v2%29.png")
      embed.add_field(name="İsmi:", value="Khaybar KH2002")
      embed.add_field(name="Üretici ülke ve Üretici:", value="İran")
      embed.add_field(name="Mühimmat:", value="5,56x45mm")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="2004")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def l85a1(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/SA-80_rifle_1996.jpg/300px-SA-80_rifle_1996.jpg")
      embed.add_field(name="İsmi:", value="L85A1")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Birleşik Krallık, RSAC")
      embed.add_field(name="Mühimmat:", value="5,56x45mm")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1985")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def m16(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/M16a1m16a2m4m16a45wi.jpg/300px-M16a1m16a2m4m16a45wi.jpg")
      embed.add_field(name="İsmi:", value="M16")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD")
      embed.add_field(name="Mühimmat:", value="5,56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1960")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def mhmtçk1(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.add_field(name="İsmi:", value="Mehmetçik1")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Türkiye, MKEK")
      embed.add_field(name="Mühimmat:", value="5,56x45mm")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="2008")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def mpt76(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/MPT-76_Assault_Rifle.jpg/260px-MPT-76_Assault_Rifle.jpg")
      embed.add_field(name="İsmi:", value="MKEK MPT-76")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Türkiye, MKEK")
      embed.add_field(name="Mühimmat:", value="5,56x45mm")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="2014")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def otsgroza(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/GrozaOC14.svg/600px-GrozaOC14.svg.png")
      embed.add_field(name="İsmi:", value="OTs-14 Groza")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Rusya")
      embed.add_field(name="Mühimmat:", value="7,62x39mm")
      embed.add_field(name="Kalibre:", value="7,62mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1994")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def qbz95(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Rifle_Type_95.jpg/300px-Rifle_Type_95.jpg")
      embed.add_field(name="İsmi:", value="QBZ-95")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Çin")
      embed.add_field(name="Mühimmat:", value="5,8x42mm")
      embed.add_field(name="Kalibre:", value="5,8mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1997")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def racr(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Impulse_buy_%2812721727313%29.jpg/300px-Impulse_buy_%2812721727313%29.jpg")
      embed.add_field(name="İsmi:", value="Remington ACR")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD")
      embed.add_field(name="Mühimmat:", value="5,56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="2010")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def sgsg550(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Stgw_90.jpg/300px-Stgw_90.jpg")
      embed.add_field(name="İsmi:", value="SİG SG 550")
      embed.add_field(name="Üretici ülke ve Üretici:", value="İsviçre")
      embed.add_field(name="Mühimmat:", value="5,56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1990")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def saug(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/AUG_A1_508mm_04.jpg/312px-AUG_A1_508mm_04.jpg")
      embed.add_field(name="İsmi:", value="Steyr AUG")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Avusturya")
      embed.add_field(name="Mühimmat:", value="5,56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1978")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def vktr4(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/VektorR4.png/300px-VektorR4.png")
      embed.add_field(name="İsmi:", value="Vektor R4")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Güney Afrika")
      embed.add_field(name="Mühimmat:", value="5,56x45mm NATO")
      embed.add_field(name="Kalibre:", value="5,56mm")
      embed.add_field(name="Üretime başlandığı yıl", value="1980")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def accas50(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.add_field(name="İsmi:", value="Accuracy İnternational AS50")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Birleşik Krallık")
      embed.add_field(name="Fişek:", value=".50 BMG")
      embed.add_field(name="Tip:", value="Gaz işletmeli, Dönen Sürgü")
      embed.add_field(name="Üretime başlandığı yıl", value="2006")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def barrm99(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Barrett_M99.jpg/300px-Barrett_M99.jpg")
      embed.add_field(name="İsmi:", value="Barrett M99")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD")
      embed.add_field(name="Fişek:", value=".50 BMG")
      embed.add_field(name="Tip:", value="Gaz tepme işletmeli, Dönen Sürgü")
      embed.add_field(name="Üretime başlandığı yıl", value="1999")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def barrm82(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/M107_1.jpg/300px-M107_1.jpg")
      embed.add_field(name="İsmi:", value="Barrett M82")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD")
      embed.add_field(name="Fişek:", value=".50 BMG")
      embed.add_field(name="Tip:", value="Gaz tepme işletmeli, Dönen Sürgü")
      embed.add_field(name="Üretime başlandığı yıl", value="1980")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def hkgpsg1(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Evers_PSG-1.PNG/300px-Evers_PSG-1.PNG")
      embed.add_field(name="İsmi:", value="H&K PSG1")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Batı Almanya")
      embed.add_field(name="Fişek:", value="7.62 NATO")
      embed.add_field(name="Tip:", value="Gaz tepme işletmeli, Dönen Sürgü")
      embed.add_field(name="Üretime başlandığı yıl", value="1980")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def kefefs(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.add_field(name="İsmi:", value="Kefefs")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Yunanistan")
      embed.add_field(name="Fişek:", value="7.62 NATO")
      embed.add_field(name="Tip:", value="Kurmalı")
      embed.add_field(name="Üretime başlandığı yıl", value="1995")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def m21(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Rifle_M21_1.jpg/200px-Rifle_M21_1.jpg")
      embed.add_field(name="İsmi:", value="M21")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD, ABD SK")
      embed.add_field(name="Fişek:", value="7.62 NATO")
      embed.add_field(name="Tip:", value="Yarı Otomatik")
      embed.add_field(name="Üretime başlandığı yıl", value="1969")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def m40(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/M40_01.jpg/200px-M40_01.jpg")
      embed.add_field(name="İsmi:", value="M40")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD, ABD SK")
      embed.add_field(name="Fişek:", value="7.62 NATO")
      embed.add_field(name="Tip:", value="Kurmalı")
      embed.add_field(name="Üretime başlandığı yıl", value="1966")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def mcmlln(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Tac50.jpg/330px-Tac50.jpg")
      embed.add_field(name="İsmi:", value="McMillan Tac50")
      embed.add_field(name="Üretici ülke ve Üretici:", value="ABD, ABD SK")
      embed.add_field(name="Fişek:", value=".50 BMG")
      embed.add_field(name="Tip:", value="Kurmalı")
      embed.add_field(name="Üretime başlandığı yıl", value="1980")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def sakotrg(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Sako_TRG-42.jpg/300px-Sako_TRG-42.jpg")
      embed.add_field(name="İsmi:", value="Sako TRG")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Finlanda")
      embed.add_field(name="Fişek:", value="7x62")
      embed.add_field(name="Tip:", value="Kurmalı")
      embed.add_field(name="Üretime başlandığı yıl", value="1989")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def sv98(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/SV-98_Engineering_technologies_-_2010.jpg/300px-SV-98_Engineering_technologies_-_2010.jpg")
      embed.add_field(name="İsmi:", value="SV-98")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Rusya, İzhmash")
      embed.add_field(name="Fişek:", value="7x62")
      embed.add_field(name="Tip:", value="Kurmalı")
      embed.add_field(name="Üretime başlandığı yıl", value="2003")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context=True)
async def vssvint(ctx):
      embed = discord.Embed(title="Silah bilgileri:", color=0x5f0bdd)
      embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Vss_vintorez_01.jpeg/300px-Vss_vintorez_01.jpeg")
      embed.add_field(name="İsmi:", value="VSS Vintorez (Yapımcının favorisi <3)")
      embed.add_field(name="Üretici ülke ve Üretici:", value="Sovyetler Birliği")
      embed.add_field(name="Fişek:", value="9x39")
      embed.add_field(name="Tip:", value="Gaz işletmeli, Dönen Sürgü")
      embed.add_field(name="Üretime başlandığı yıl", value="1987")
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
     
@bot.command(pass_context=True)
async def keskinnişancı(ctx):
      embed=discord.Embed(title="Keskin Nişancılar:", description="Toplamda 15 tane bulunmaktadır.", color=0x5f0bdd)
      embed.add_field(name="A", value="-accarctic, \n-accas50", inline=True)
      embed.add_field(name="B", value="-barrm82, \n-barrm99", inline=True)
      embed.add_field(name="H", value="-hkg417, \n-hkgpsg1", inline=True)
      embed.add_field(name="İ", value="-istiglal", inline=True)
      embed.add_field(name="K", value="-kefefs", inline=True)
      embed.add_field(name="J", value="-jng90", inline=True)
      embed.add_field(name="M", value="-m21, \n-m40, \n-mcmlln", inline=True)
      embed.add_field(name="S", value="-sakotrg, \n-sv98", inline=True)
      embed.add_field(name="V", value="-vssvint", inline=True)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)
      
@bot.command(pass_context=True)
async def tüfek(ctx):
      embed=discord.Embed(title="Piyade Tüfekleri:", description="Toplamda 37 tane bulunmaktadır.", color=0x5f0bdd)
      embed.add_field(name="A", value="-a91, \n-aek971, \n-ak107, \n-ak47, \n-ak74, \n-an94, \n-ar10, \n-asval", inline=True)
      embed.add_field(name="B", value="-barx160 \n-beryl", inline=True)
      embed.add_field(name="D", value="-daek1, \n-daek2, \n-dc7a1", inline=True)
      embed.add_field(name="F", value="-famas, \n-fara83, \n-fnf2000, \n-fnscar", inline=True)
      embed.add_field(name="G", value="-gwhr98", inline=True)
      embed.add_field(name="H", value=" \n-hazri, \n-hkg11, \n-hkg41, \n-ht89", inline=True)
      embed.add_field(name="İ", value="-imblmd, \n-imitavor21, \n-insas", inline=True)
      embed.add_field(name="K", value="-krbnr98k, \n-khaybar", inline=True)
      embed.add_field(name="L", value="-l85a1", inline=True)
      embed.add_field(name="M", value="-m16, \n-mhmtçk1, \n-mpt76", inline=True)
      embed.add_field(name="O", value="-otsgroza", inline=True)
      embed.add_field(name="Q", value="-qbz95", inline=True)
      embed.add_field(name="R", value="-racr", inline=True)
      embed.add_field(name="S", value="-sgsg550, \n-saug", inline=True)
      embed.add_field(name="V", value="-vktr4", inline=True)
      embed.set_footer(text='İçin oluşturuldu.', icon_url=ctx.message.author.avatar_url)
      await bot.say(embed=embed)     
      
bot.run(os.getenv('BOT_TOKEN'))
