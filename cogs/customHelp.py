from os import name
import discord
from discord.ext import commands, tasks
from discord.ext.commands.core import bot_has_any_role


class cus_help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            title="Help",
            description="Hola!! Here!! Use >help  <command>  for furthur info",
            color=discord.Color.blurple(),
        )

        em.add_field(
            name=" 🛡 Moderation",
            value=" `👢 kick`, `❌ ban`, `❗warn`, `🆘 unban`, `⏳ slowmode`, `🔇 Mute`, `🔊Unmute`, `💥Purge`",
            inline=False,
        )

        em.add_field(
            name=" 😎 Expressions",
            value=" `🧤 pat`, `🤚🏿 slap`,  `🙏 respect`, `🤣joke`",
            inline=False,
        )
        em.add_field(
            name=" 🔥 Basic Commands",
            value=" `👋 hello`, `😀 thanks`, `🙋‍♂️ bye`, `📶 ping`",
            inline=False,
        )
        em.add_field(
            name=" 🏓 Games",
            value=" `ft`",
            inline=False,
        )
        em.add_field(
            name=" ℹ Info",
            value=" `ginfo`, `minfo`, `av`, `roles`,`botinfo`",
            inline=False,
        )

        await ctx.send(embed=em)

    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(
            title="Kick",
            description="``Kicks a member from the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``kick <member/username> [reason]``")

        await ctx.send(embed=em)

    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(
            title="Ban",
            description="``Bans a member from the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``ban <member/username> [reason]``")

        await ctx.send(embed=em)

    @help.command()
    async def unban(self, ctx):
        em = discord.Embed(
            title="Unban",
            description="``Unbans a member from the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(
            name="**SYNTAX**", value=">``unban <member/username # discriminator>``"
        )

        await ctx.send(embed=em)

    @help.command()
    async def warn(self, ctx):
        em = discord.Embed(
            title="Warn",
            description="``Warns a member on the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``warn <member/username> [reason]``")

        await ctx.send(embed=em)

    @help.command()
    async def mute(self, ctx):
        em = discord.Embed(
            title="Mute",
            description="``Mutes a member from the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``mute <member/username>``")

        await ctx.send(embed=em)

    @help.command()
    async def unmute(self, ctx):
        em = discord.Embed(
            title="Unmute",
            description="``Unmutes a member from the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``Unmute <member/username>``")

        await ctx.send(embed=em)

    @help.command()
    async def purge(self, ctx):
        em = discord.Embed(
            title="Purge",
            description="``Purges 'x' amount of message from server``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``purge \n Amount = 1<x<100``")

        await ctx.send(embed=em)

    @help.command()
    async def pat(self, ctx):
        em = discord.Embed(
            title="Pat",
            description="``Pats a member on the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``pat <member/username> [reason]``")

        await ctx.send(embed=em)

    @help.command()
    async def slap(self, ctx):
        em = discord.Embed(
            title="Slap",
            description="``Slaps a member on the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``slap <member(s)/username> [reason]``")

        await ctx.send(embed=em)

    @help.command()
    async def respect(self, ctx):
        em = discord.Embed(
            title="Respect",
            description="``Respects a member on the server 😢``",
            color=ctx.author.color,
        )

        em.add_field(
            name="**SYNTAX**", value=">``respect | f | re | F <member/username>`` "
        )

        await ctx.send(embed=em)

    @help.command()
    async def joke(self, ctx):
        em = discord.Embed(
            title="Joke", description="``Sends a random joke``", color=ctx.author.color
        )

        em.add_field(name="**SYNTAX**", value=">``joke``")

        await ctx.send(embed=em)

    @help.command()
    async def hello(self, ctx):
        em = discord.Embed(
            title="Hello",
            description="``Greets the author ``🙂``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">hello")

        await ctx.send(embed=em)

    @help.command()
    async def thanks(self, ctx):
        em = discord.Embed(
            title="Thanks",
            description="``Politely welcomes to author 🙂``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value="``>thanks``")
        await ctx.send(embed=em)

    @help.command()
    async def bye(self, ctx):
        em = discord.Embed(
            title="Bye",
            description="``Farewells the author 🙂``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">bye")
        await ctx.send(embed=em)

    @help.command()
    async def ping(self, ctx):
        em = discord.Embed(
            title="Ping",
            description="``Checkes ping form bot to server 🙂``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``ping``")
        await ctx.send(embed=em)

    @help.command()
    async def ft(self, ctx):
        em = discord.Embed(
            title="Fortune Telling",
            description="Tells your fortune 🐱‍👤",
            color=ctx.author.color,
        )
        em.add_field(name="**SYNTAX**", value=">``ft | fortu_tellin``")
        await ctx.send(embed=em)

    @help.command()
    async def ginfo(self, ctx):
        em = discord.Embed(
            title="Guild/Server Information",
            description="``Information about the server``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``ginfo``")
        await ctx.send(embed=em)

    @help.command()
    async def minfo(self, ctx):
        em = discord.Embed(
            title="Member Information",
            description="``Information about the member``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``minfo <member/username>``")
        await ctx.send(embed=em)

    @help.command()
    async def av(self, ctx):
        em = discord.Embed(
            title="Member's Avatar",
            description="``Information about the member``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``av | avatar <member/username>``")
        await ctx.send(embed=em)

    @help.command()
    async def botinfo(self, ctx):
        em = discord.Embed(
            title="Bot Information",
            description="``Information about the bot``",
            color=ctx.author.color,
        )

        em.add_field(name="**SYNTAX**", value=">``botinfo ``")
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(cus_help(bot))
