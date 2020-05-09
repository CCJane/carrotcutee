import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv


client = commands.Bot(command_prefix = '!cc ')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Cutie.py", url="https://www.twitch.tv/lonelyfeels_"))
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
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a douubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good',
                 'Very doubtful.']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    authorperms_clear = ctx.author.permissions_in(ctx.channel)
    if authorperms_clear.manage_messages:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("You don't have the permissions to do that!")

@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def bestgirl(ctx):
    Misaka_Mikoto = 'https://static.zerochan.net/Misaka.Mikoto.full.2216494.png'
    Yumeko_Jabami = 'https://i.pinimg.com/originals/36/92/82/3692825d8ee8da6d4104107cbab866f8.jpg'
    Tsuyu_Asui = 'https://i.pinimg.com/564x/3a/c6/f5/3ac6f56cba77caaa11f6745c26985a6e.jpg'
    Nyu = 'https://vignette.wikia.nocookie.net/villains/images/7/70/Elfen_Lied_Lucy.png/revision/latest/top-crop/width/360/height/450?cb=20180621030452'
    Ruby_Rose = 'https://i.pinimg.com/originals/b4/32/16/b43216122fe121234559fe01c2cdce0f.jpg'
    Himiko_Toga = 'https://i.pinimg.com/originals/57/b4/a8/57b4a865716470f47eba054fd7f3b724.jpg'
    Nejire_Hado = 'https://vignette.wikia.nocookie.net/my-hero/images/e/ee/Nejire_Hado_Heldenkost%C3%BCm_%28Anime%29.png/revision/latest?cb=20191006133625&path-prefix=de'

    girls=['Misaka Mikoto', 'Yumeko Jabami', 'Tsuyu Asui', 'Nyu', 'Ruby Rose', 'Himiko Toga', 'Nejire Hado']

    randomizer=random.choice(girls)

    if randomizer == 'Misaka Mikoto':
        bestgirls=discord.Embed(title='Misaka Mikoto', url=Misaka_Mikoto, description='Anime')
        bestgirls.set_image(url=Misaka_Mikoto)
        await ctx.send(embed=bestgirls)
    elif randomizer == 'Yumeko Jabami':
        bestgirls=discord.Embed(title='Yumeko Jabami', url=Yumeko_Jabami, descritpion='Anime')
        bestgirls.set_image(url=Yumeko_Jabami)
        await ctx.send(embed=bestgirls)
    elif  randomizer == ('Tsuyu Asui'):
        bestgirls=discord.Embed(title='Tsuyu Asui', url=Tsuyu_Asui, description='Anime')
        bestgirls.set_image(url=Tsuyu_Asui)
        await ctx.send(embed=bestgirls)
    elif randomizer == ('Nyu'):
        bestgirls=discord.Embed(title='Nyu', url=Nyu, description='Anime')
        bestgirls.set_image(url=Nyu)
        await ctx.send(embed=bestgirls)
    elif randomizer == ('Ruby Rose'):
        bestgirls=discord.Embed(title='Ruby Rose', url=Ruby_Rose, description='Anime')
        bestgirls.set_image(url=Ruby_Rose)
        await ctx.send(embed=bestgirls)
    elif randomizer == ('Himiko Toga'):
        bestgirls=discord.Embed(title='Himiko Toga', url=Himiko_Toga, descritpion='Anime')
        bestgirls.set_image(url=Himiko_Toga)
        await ctx.send(embed=bestgirls)
    elif randomizer == ('Nejire Hado'):
        bestgirls=discord.Embed(title='Nejire Hado', url=Nejire_Hado, descritpion='Anime')
        bestgirls.set_image(url=Nejire_Hado)
        await ctx.send(embed=bestgirls)

@bestgirl.error
async def bestgirl_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('This command has 1 hour cooldown. Please try again later.')

@client.command()
async def iam(ctx, *, role):
    user = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name=f'{role}')
    if role in user.roles:
        await ctx.send(f"You already have {role} role.")
    else:
        await user.add_roles(role)
        await ctx.send(f"You've been given {role} role.")

@client.command()
async def iamn(ctx, *, role):
    user = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name=f'{role}')
    if role in user.roles:
        await user.remove_roles(role)
        await ctx.send(f"{role} role has been taken from you.")
    else:
        await ctx.send(f"You don't have {role} role.")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 707159506089410560:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if payload.emoji.name == 'TwitchFan':
            role = discord.utils.get(guild.roles, name='Twitch Fan')
        elif payload.emoji.name == '🐛':
            role = discord.utils.get(guild.roles, name='Bugger')
        elif payload.emoji.name == '🐙':
            role = discord.utils.get(guild.roles, name='Octopussy')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role in member.roles:
            await member.send(f"You already have {role} role.")
        else:
            if role is not None:
                if member is not None:
                    await member.add_roles(role)
                    await member.send(f"You've been given {role} role")
                else:
                    pass
            else:
                await member.send('Role not found.')

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 707159506089410560:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if payload.emoji.name == 'TwitchFan':
            role = discord.utils.get(guild.roles, name='Twitch Fan')
        elif payload.emoji.name == '🐛':
            role = discord.utils.get(guild.roles, name='Bugger')
        elif payload.emoji.name == '🐙':
            role = discord.utils.get(guild.roles, name='Octopussy')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role in member.roles:
            if role is not None:
                if member is not None:
                    await member.remove_roles(role)
                    await member.send(f"{role} role has been taken from you.")
                else:
                    pass
            else:
                await member.send('Role not found.')
        else:
            if role is not None:
                await member.send(f"You don't have {role} role.")    
            else:
                await member.send('Role not found.')

client.run(TOKEN)