from os import name

import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command
from datetime import date, datetime, time, timedelta


class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def botcount(self, ctx) -> int:
        botc = [member for member in ctx.guild.members if member.bot is True]
        bot_count = len(botc)
        return bot_count

    def membcount(self, ctx) -> int:
        guild = ctx.guild
        users = [member for member in guild.members if member.bot is not True]
        mem_count = len(users)
        return mem_count

    def dayscreated(self, ctx) -> int:
        guild = ctx.guild
        created = (
            datetime.utcnow().replace(second=0, microsecond=0)
            - guild.created_at.replace(second=0, microsecond=0)
        ).days
        return created

    def mem_joined(self, member: discord.Member):
        joined = (
            datetime.utcnow().replace(second=0, microsecond=0)
            - member.joined_at.replace(second=0, microsecond=0)
        ).days
        return joined

    def bot_joined(self, ctx):
        member = ctx.guild.me
        botjoined = (
            datetime.utcnow().replace(second=0, microsecond=0)
            - member.joined_at.replace(second=0, microsecond=0)
        ).days
        return botjoined

    def roles(self, ctx):
        role = ctx.guild.roles
        role_name = reversed(
            [i.name for i in role if i.name not in ("@everyone", "───────")]
        )
        role_name = f"{', '.join('`' + role + '`'for role in role_name)}"
        return role_name

    def mem_created(self, member: discord.Member):
        memcreated = (
            datetime.utcnow().replace(second=0, microsecond=0)
            - member.created_at.replace(second=0, microsecond=0)
        ).days
        return memcreated

    @commands.command()
    async def ginfo(self, ctx):
        em = discord.Embed(title="**SERVER INFO**", color=discord.Colour.purple())

        em.add_field(name="**GUILD NAME**", value=f"{ctx.guild.name}")

        em.add_field(name="**SERVER OWNER**", value=f"{ctx.guild.owner}")

        em.add_field(
            name="**VERIFICATION LEVEL**", value=f"{ctx.guild.verification_level}"
        )

        em.add_field(name="**MEMBER COUNT**", value=self.membcount(ctx))

        em.add_field(name="**BOT COUNT**", value=self.botcount(ctx))

        em.add_field(name="**ROLE COUNT**", value=f"{len(ctx.guild.roles)}")

        # em.add_field(name="**ROLES**", value=self.roles(ctx))

        em.add_field(
            name="**CREATED AT**",
            value=f"{(ctx.guild.created_at.replace(minute = 0, second=0, microsecond=0))}\nIt has been {self.dayscreated(ctx)} days since the guild was created",
            inline=False,
        )

        em.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)

        em.set_thumbnail(url=ctx.guild.icon_url)

        await ctx.send(len(em))
        await ctx.send(embed=em)

    @commands.command()
    async def groles(self, ctx):
        em = discord.Embed(
            title="**  ──────────────── SERVER ROLES ────────────────  **",
            description=f"{self.roles(ctx)}",
            color=discord.Colour.purple(),
        )
        await ctx.send(embed=em)

    @commands.command()
    async def minfo(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.send("Please enter a username")

        else:
            mrole = [
                i.name
                for i in member.roles
                if i.name not in ("@everyone", "─────── USER PROFILE ───────")
            ]
            mrole = reversed(mrole)
            em = discord.Embed(
                title=f"**{member.name}**", color=discord.Colour.purple()
            )

            em.add_field(name="MEMBER NAME", value=f"{member.name}")

            em.add_field(name="\u200b", value="\u200b")

            em.add_field(name="**JOINED FOR**", value=f"{self.mem_joined(member)} days")

            em.add_field(
                name="MEMBER'S ROLE",
                value=(f"{', '.join('`' + role + '`'for role in mrole)}"),
                inline=False,
            )

            em.add_field(
                name="**ACCOUNT CREATED FOR**",
                value=f"{self.mem_created(member)} days",
            )

            em.set_thumbnail(url=member.avatar_url)

            em.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
            )

            await ctx.channel.send(embed=em)

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            useravatar = ctx.author.avatar_url
            em = discord.Embed(
                title=f"Avatar for {ctx.author.name}", color=discord.Colour.purple()
            )

            em.set_image(url=useravatar)

            em.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)

            await ctx.send(embed=em)
        else:
            useravatar = member.avatar_url
            em = discord.Embed(
                title=f"Avatar for {member.name}", color=discord.Colour.purple()
            )

            em.set_image(url=useravatar)

            em.set_author(name=f"{member.name}", icon_url=member.avatar_url)

            await ctx.send(embed=em)

    @commands.command()
    async def botinfo(self, ctx):
        em = discord.Embed(title="**BOT INFO**", color=discord.Colour.purple())

        em.add_field(name="**BOT NAME**", value=f"{self.bot.user.name}")

        em.add_field(name="**CREATOR**", value=f"BigDaddy#0860")

        em.add_field(name="**VERSION**", value=f"1.0.0")

        em.add_field(name="**SERVER COUNT**", value=f"{len(self.bot.guilds)}")

        em.add_field(
            name="**REPOSITORY**",
            value="[Omni-Repo](https://github.com/BigDaddy058/Omni8-Bot/tree/main)",
        )

        em.add_field(name="**JOINED FOR**", value=f"{self.bot_joined(ctx)} days")

        em.set_author(name=f"{self.bot.user.name}", icon_url=self.bot.user.avatar_url)

        em.set_thumbnail(url=self.bot.user.avatar_url)

        em.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url
        )

        await ctx.send(embed=em)

    @commands.command()
    async def jgl(self, ctx):

        await ctx.send(
            f"{', '.join('`' + guild.name + '`'for guild in self.bot.guilds)}"
        )

    @commands.command()
    async def uptime(self, ctx):
        timee = datetime.now() - self.bot.upstart
        timee -= timedelta(microseconds=timee.microseconds)
        # # await ctx.send(timee)
        await ctx.send(f"```yaml\n{timee}```")


def setup(bot):
    bot.add_cog(info(bot))
