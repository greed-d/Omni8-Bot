from asyncio.windows_events import NULL
from discord.flags import Intents
from dotenv import load_dotenv
from discord.ext.commands.converter import clean_content
from discord.ext import commands, tasks
from discord import message
from itertools import cycle
from functools import partialmethod
import discord
import os
import random
import requests
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')


bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

bot_statuses = cycle([
    "This is OMNI",
    "Made with Python",
    "Work in progress",
    "Help!!!!",
    "My creator is a dumbass"
])


@tasks.loop(seconds=70)
async def bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))


@bot.event
async def on_ready():
    print('Bot {0.user} is ready.'.format(bot))
    bot_status.start()


@bot.command(aliases=['suppun', 'hi'])
async def hello(ctx):

    if ctx.author.id == 775252975643263006:
        await ctx.send("Nice day for fishing ain't it! Hua-ha")

    else:
        await ctx.send(f"Hello to {ctx.author.mention}!!!")


@bot.command()
async def thanks(ctx):
    await ctx.send(f"You're Welcomed :) {ctx.author.mention}")


@bot.command()
async def bye(ctx):
    await ctx.send(f'Byee!!{ctx.author.mention}')


@bot.command(aliases=['re', 'F'])
async def respect(ctx, member: discord.Member):
    if ctx.author in ctx.message.mentions:
        await ctx.send("Self-Respect I see :slight_smile:")

    else:
        await ctx.send(f'{ctx.author.mention} pays respect to {member.mention}')


@respect.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Who do you want to respect man?")


@bot.command()
async def ping(ctx):
    await ctx.send(f"```Pong! {round(bot.latency * 1000)} ms```")


# * Kick, Ban and Unban member
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention}has been kicked')


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been kicked')


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@kick.error
async def info_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send("Oops! You don't have that permission.")


@ban.error
async def info_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send("Oops! You don't have that permission.")


@unban.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Oops! You don't have that permission.")


# * Slap and pat member


'''@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ','.join(x.name for x in members)
    if not ctx.message.mentions:
        await ctx.send(f'{ctx.author.mention} Whom do you want to slap bud?')

    if ctx.author in ctx.message.mentions:
        await ctx.send(f"{ctx.author.mention} Why slap yourself bruh? 🤐🤐")

    elif ctx.message.mentions:
        await ctx.send('{} got slapped for {}'.format(slapped, reason))


@bot.command()
async def pat(ctx, members: commands.Greedy[discord.Member], *, reason=None):
    patted = ','.join(x.name for x in members)
    if not ctx.message.mentions:
        await ctx.send(f'{ctx.author.mention} Do you need a hug??\nIf not mention someone ya moron')

    if ctx.author in ctx.message.mentions:
        print(ctx.message.mentions)
        await ctx.send(f"Are you okay {ctx.author.mention}???? \nYou need a hug???")

    else:
        await ctx.send(' {} got patted '.format(patted))


# * Inspire part from previous bot


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "   -" + json_data[0]['a']
    return(quote)


@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)


# * Games like Fortune Telling and .....


@bot.command(aliases=['ft', 'fortune'])
async def fortune_telling(ctx, *, question):
    response = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    if question.startswith('will') or question.startswith('Will'):
        await ctx.send(f"Question : {question} \nAnswer : {random.choice(response)}")
    else:
        await ctx.send(f"Type a yes/no question starting with 'will' bud")


@fortune_telling.error
async def info_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.sent(f"I am not that intelligent please start it with 'will' 🥺")


@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.errors.CommandNotFound):
        await ctx.send(f"Uh ohh!!!\nI don't think that is a valid argument {ctx.author.mention} \nTry >help for more info")'''

bot.run(TOKEN)
