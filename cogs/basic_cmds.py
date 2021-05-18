import discord
from discord.ext import commands
from discord.ext.commands.core import command


class basic_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot {0.user} is ready".format(self.bot))

    @commands.command(aliases=['suppun', 'hi'])
    async def hello(self, ctx):
        if ctx.author.id == 775252975643263006:
            await ctx.send("Nice day for fishing ain't it! Hua-ha")

        else:
            await ctx.send(f"Hello to {ctx.author.mention}!!!")

    @commands.command(aliases=['arigatoo'])
    async def thanks(self, ctx):
        await ctx.send(f"You're welcome {ctx.author.mention} :)")

    @commands.command()
    async def bye(self, ctx):
        await ctx.send(f'Byee!!{ctx.author.mention}')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"```Pong! {round(self.bot.latency * 1000)} ms```")


def setup(bot):
    bot.add_cog(basic_commands(bot))
