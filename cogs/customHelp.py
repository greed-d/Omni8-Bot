from os import name
import discord
from discord.ext import commands, tasks
from discord.ext.commands.core import bot_has_any_role


class cusHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            title="Help", description="Use >help  <command>  for furthur info")

        em.add_field(name=" 🛠 Moderation", value=' 👢 kick, ❌ ban, ❗ warn')
        em.add_field(name=' 😎 Expressions',
                     value=' 🧤 pat, 🤚🏿 slap,  🙏 respect')
        em.add_field(name=" 🔥 Basic Commands",
                     value=" 👋 hello, 😀 thanks, 🙋‍♂️ bye, ping")
        em.add_field(name=' 🏓 Games',
                     value=' 🔮 Fortune telling and more coming on the way')

        await ctx.send(embed=em)

    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(
            title="Kick", description="Kicks a member from the server 😢", color=ctx.author.color)

        em.add_field(name='**SYNTAX**',
                     value=">kick <member/username> [reason]")

        await ctx.send(embed=em)

    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(
            title="Ban", description="Bans a member from the server 😢", color=ctx.author.color)

        em.add_field(name='**SYNTAX**',
                     value=">ban <member/username> [reason]")

        await ctx.send(embed=em)

    @help.command()
    async def warn(self, ctx):
        em = discord.Embed(
            title="Warn", description="Warns a member on the server 😢", color=ctx.author.color)

        em.add_field(name='**SYNTAX**',
                     value=">warn <member/username> [reason]")

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(cusHelp(bot))
