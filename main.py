import discord
import os
import requests
import json
from asyncio.windows_events import NULL
from discord.flags import Intents
from dotenv import load_dotenv
from discord.ext import commands, tasks
from itertools import cycle


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

bot.remove_command("help")


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 532960958381817857:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send("The cog has been loaded")


@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 532960958381817857:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send("The cog has been unloaded")

    else:
        await ctx.sent("You don't have the required permission")


@bot.command(aliases=['rl'])
async def re_load(ctx, extension):
    if ctx.author.id == 532960958381817857:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send("Cogs reloaded")

    elif ctx.author.id != bot.is_owner:
        await ctx.sent("You don't have the required permission")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Found {filename}")


@re_load.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter the name of package you want to reload")

    if isinstance(error, FileNotFoundError):
        await ctx.send("the file is not found")


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "   -" + json_data[0]['a']
    return(quote)


@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)


'''
@fortune_telling.error
async def info_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.sent(f"I am not that intelligent please start it with 'will' 🥺")'''


bot.run(TOKEN)
