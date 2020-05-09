import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '+')

TOKEN = 'NzA2MTgxODAyNDAxOTg4Njc4.XraVsw.Zu3Iogj10IIvtX-Xp1849MJNZqc'

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Member')    
    await ctx.add_roles(role)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Höchstwahrscheinlich',
                 'Ja, natürlich',
                 'Ohne jeden Zweifel',
                 'definitiv',
                 'Mach dich darauf gefasst',
                 'So wie ich das seha, ja',
                 'Sehr Wahrscheinlich',
                 'Gute Aussichten',
                 'Ja!',
                 'Sieht gut aus',
                 'Weiß ich nicht',
                 'Frag später noch mal',
                 'Das sag ich dir besser nicht',
                 'Kann ich dir jetzt nicht sagen',
                 'Konzentrier dich und Frag nochmal',
                 "Verlass dich besser nicht darauf",
                 'Computer sagt: Nein',
                 'Ich würde nein sagen',
                 'Eher nein',
                 'Ich habe meine Zweifel'
                 'Definitiv nein!']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    authorperms_clear = ctx.author.permissions_in(ctx.channel)
    if authorperms_clear.manage_messages:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("Du hast keine Berechtigungen für diesen Befehl")

@client.command()
async def Railgun(ctx):  
    MisakaMikoto=discord.Embed(title="Misaka Mikoto", url="https://toarumajutsunoindex.fandom.com/wiki/Misaka_Mikoto", description="A Certain Scientific Railgun", color=0xff0000)
    MisakaMikoto.set_image(url='https://static.zerochan.net/Misaka.Mikoto.full.2216494.png')
    await ctx.send(embed=MisakaMikoto)

@client.command()
async def bestgirl(ctx):
    Misaka_Mikoto = 'https://i.pinimg.com/originals/3f/45/7f/3f457fc4e52978ce66e85d002f3bfb79.png'
    Yumeko_Jabami = 'https://i.pinimg.com/originals/36/92/82/3692825d8ee8da6d4104107cbab866f8.jpg'
    Tsuyu_Asui = 'https://i.pinimg.com/originals/7f/7c/b2/7f7cb22d201890d527b2072e78840ba9.jpg'

    girls=['Misaka Mikoto','Yumeko Jabami','Tsuyu Asui']

    randomizer=random.choice(girls)

    if randomizer == 'Misaka Mikoto':
        bestgirl=discord.Embed(title='Misaka Mikoto', url=Misaka_Mikoto, description='A Certain Scientic Railgun', color=0x000000)
        bestgirl.set_image(url=Misaka_Mikoto)
        await ctx.send(embed=bestgirl)
    if randomizer == 'Tsuyu Asui':
        bestgirl=discord.Embed(title='Tsuyu Asui', url=Tsuyu_Asui, description='My Hero Academia', color=0x000000)
        bestgirl.set_image(url=Tsuyu_Asui)
        await ctx.send(embed=bestgirl)
    if randomizer == 'Yumeko Jabami':
        bestgirl=discord.Embed(title='Yumeko Jabami', url=Yumeko_Jabami, description='Kakegurui', color=0x000000)
        bestgirl.set_image(url=Yumeko_Jabami)
        await ctx.send(embed=bestgirl)
            
client.run(TOKEN)
