import discord
import os
from discord import channel

# from asyncio.windows_events import NULL
from discord.flags import Intents
from dotenv import load_dotenv
from discord.ext import commands, tasks
from itertools import cycle


load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())


bot_statuses = cycle(
    [
        "This is OMNI",
        "Made with Python",
        "Work in progress",
        "Help!!!!",
        "My creator is a dumbass",
        "Playing >help ",
    ]
)


@tasks.loop(seconds=70)
async def bot_status():
    await bot.wait_until_ready()  # Waits for internal cache to be ready
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))


bot_status.start()

bot.remove_command("help")

# loads a cog
@bot.command()
async def load(ctx, extension):
    if ctx.author.id in (532960958381817857, 822867678745853963):
        print("start")
        bot.load_extension(f"cogs.{extension}")
        print("done")
        await ctx.send("The cog has been loaded")


# unpacks a cog
@bot.command()
async def unload(ctx, extension):
    if ctx.author.id in (532960958381817857, 822867678745853963):
        print("start")
        bot.unload_extension(f"cogs.{extension}")
        print("done")
        await ctx.send("The cog has been unloaded")

    else:
        await ctx.sent("You don't have the required permission")


# reloads the whole cogs in the bot
@bot.command(aliases=["rl"])
async def re_load(ctx, extension):
    if ctx.author.id == 532960958381817857:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs reloaded")

    elif ctx.author.id != bot.is_owner:
        await ctx.sent("You don't have the required permission")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Found {filename[:-3]}")


@re_load.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter the name of package you want to reload")

    if isinstance(error, FileNotFoundError):
        await ctx.send("the file is not found")


bot.run(TOKEN)
