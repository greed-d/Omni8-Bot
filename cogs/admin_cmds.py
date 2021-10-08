import asyncio
import discord
from discord import channel
from discord import message

# from discord import client
from discord.ext import commands
from discord.ext.commands import bot, check, Context
from discord.ext.commands.core import command


def in_any_channel(self, *guilds):
    async def predicate(ctx: Context):
        return ctx.guild.id in guilds

    return check(predicate)


class admin_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member.id in [ctx.author.id, self.bot.user.id]:
            return await ctx.send("You cannot kick yourself or the bot")

        else:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention}has been kicked")

    @kick.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Oops! You don't have that permission.")

        if ctx.author.id == ctx.guild.owner_id:
            await ctx.send("You are the owner!!! Why kick yourself?")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member.id in [ctx.author.id, self.bot.user.id]:
            return await ctx.send("You cannot ban yourself or the bot")

        else:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} has been banned")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):

        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def softmute(self, ctx, member: discord.Member, time: int):
        if member.id == 841547916199329812:
            await ctx.channel.send("You cannot mute the bot", delete_after=5)

        elif ctx.author.id == member.id:
            await ctx.channel.send("You cannot mute yourself", delete_after=5)

        elif time >= 86400:
            await ctx.channel.send(
                "Use mute if you want to mute someone longer than 24 hours",
                delete_after=5,
            )

        else:
            var = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(var)
            await ctx.channel.send(
                f"{member.mention} has been **MUTED** for {round(time/60, 2)} minutes",
                delete_after=5,
            )
            await asyncio.sleep(time)
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_roles(role)
            await ctx.channel.send(
                f"{member.mention} has been **UNMUTED**", delete_after=5
            )

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, time: int):

        if time == None:
            await ctx.channel.edit(slowmode_delay=10)
            await ctx.send("Slowmode set to 10 sec")

        if time == 0:
            await ctx.send("Slowmode ``Deactivated``!")
            await ctx.channel.edit(slowmode_delay=0)
        elif time > 21600:
            await ctx.send("You can't set the slowmode above 6 hours!")
            return
        else:
            await ctx.channel.edit(slowmode_delay=time)
            await ctx.send(f"Slowmode set to {time} seconds!")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member):
        if member.id == 841547916199329812:
            await ctx.channel.send("You cannot mute the bot")

        elif ctx.author.id == member.id:
            await ctx.channel.send("You cannot mute yourself")

        else:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            if not role:
                perms = discord.Permissions(send_messages=False, read_messages=True)
                role = await ctx.guild.create_role(
                    name="Muted",
                    permissions=perms,
                )
            pos = ctx.guild.me.top_role.position - 1
            await role.edit(position=pos)
            await member.add_roles(role)
            await ctx.channel.send(f"{member.mention} has been **MUTED**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.channel.send(f"{member.mention} has been **UNMUTED**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        if amount == 0:
            await ctx.channel.send(f"Please enter a number ", delete_after=5)

        elif amount > 100:
            await ctx.channel.send(
                f"Please don't enter a number greater than 100", delete_after=5
            )

        else:
            deleted = await ctx.channel.purge(limit=amount + 1)
            await ctx.channel.send(
                "Deleted {} message(s)".format(len(deleted)), delete_after=8
            )

    def is_bot(self, m):
        return m.author.bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def bmpurge(self, ctx, amount: int):
        if amount == 0:
            await ctx.channel.send(f"Please enter a number ", delete_after=5)

        elif amount > 100:
            await ctx.channel.send(
                f"Please don't enter a number greater than 100", delete_after=5
            )

        else:
            deleted = await ctx.channel.purge(limit=amount, check=self.is_bot)
            await ctx.channel.send(
                "Deleted {} message(s)".format(len(deleted)), delete_after=3
            )

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = message.guild
        channel = message.channel
        if guild.id == 856018962231197726:
            if channel == self.bot.get_channel(856024909407191050):
                if "https://" not in message.content:
                    if message.author.bot:
                        return
                    else:
                        await message.delete()
                        em = discord.Embed(
                            description="Only links here", color=discord.Color.red()
                        )
                        await channel.send(embed=em, delete_after=5)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def rules(self, ctx):
        em = discord.Embed(
            title="**───────────────────  RULES ───────────────────**",
            description="Here are the rules for server",
            color=discord.Color.purple(),
            align="center",
        )
        em.add_field(
            name="1.",
            value="No hate, toxic behavior, sexism, or racism of any kind.",
            inline=False,
        )
        em.add_field(
            name="2.",
            value="Don't spam, spoil things, flood chat with CAPS, or line-split.",
            inline=False,
        )
        em.add_field(
            name="3.",
            value="Starting or participating in drama of any kind is strictly forbidden.",
            inline=False,
        )
        em.add_field(
            name="4.",
            value="Disrespecting other members or servers is not allowed.",
            inline=False,
        )
        em.add_field(
            name="5.",
            value="Rule evasion or attempts to test the limits of what is possible is not allowed.",
            inline=False,
        )
        em.add_field(
            name="6.",
            value="Don't promote cruelty, violence, self-harm, suicide or pornography.",
            inline=False,
        )
        em.add_field(
            name="7.", value="No begging, stalking or threatening.", inline=False
        )
        em.add_field(
            name="8.",
            value="Raiding or planning raids is strictly forbidden.",
            inline=False,
        )
        em.add_field(
            name="9.", value="Keep things in the correct channels.", inline=False
        )
        em.add_field(
            name="10.",
            value="Don't advertise. Especially DM advertising another Discord server is strictly forbidden.",
            inline=False,
        )
        em.add_field(
            name="11.",
            value="Controversial topics such as religion or politics is not allowed.",
            inline=False,
        )
        em.add_field(
            name="12.",
            value="Catfishing and any sort of fake identities is forbidden.",
            inline=False,
        )
        em.add_field(
            name="13.",
            value="Don't attempt to bypass any blocked words.",
            inline=False,
        )
        em.add_field(
            name="14.",
            value="Refrain from talking about banned members and anything regarding them. If you have problems regarding a ban feel free to directly message a staff member.",
            inline=False,
        )
        em.add_field(
            name="15.",
            value="We dont allow any NSFW Content / Avatars on any of the sfw channels",
            inline=False,
        )
        await ctx.channel.send(embed=em)

    @commands.command(name="ping")
    @in_any_channel(764505370684817448)
    async def ping(self, ctx: Context):
        await ctx.send(f"```Pong! {round(self.bot.latency * 1000)} ms```")


def setup(bot):
    bot.add_cog(admin_commands(bot))
