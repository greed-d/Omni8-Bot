from os import name
import discord

# from main import prefix
from discord.ext import commands
from discord.ext.commands.core import command


class basic_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"───────────────────────────────────────────────────\nLogged in as {self.bot.user} : {self.bot.user.id}\n───────────────────────────────────────────────────\nMy prefix is : '>'\n───────────────────────────────────────────────────"
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user in message.mentions:
            await message.channel.send("Please use `>help` for more info")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        mbed = discord.Embed(
            color=(discord.Colour.dark_teal()),
            title="Welcome to server",
            description=(f"Welcome {member.mention}, Server maa tapai lai swagt xa :)"),
        )
        await member.send(embed=mbed)

    @commands.command(aliases=["suppun", "hi"])
    async def hello(self, ctx):
        if ctx.author.id == 775252975643263006:
            await ctx.send("Nice day for fishing ain't it! Hua-ha")

        else:
            await ctx.send(f"Hello {ctx.author.mention}")

    @commands.command(aliases=["arigatoo"])
    async def thanks(self, ctx):
        await ctx.send(f"You're welcome {ctx.author.mention} :)")

    @commands.command()
    async def bye(self, ctx):
        await ctx.send(f"Byee!!{ctx.author.mention}")


def setup(bot):
    bot.add_cog(basic_commands(bot))
