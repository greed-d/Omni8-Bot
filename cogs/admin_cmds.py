import discord
from discord.ext import commands


class admin_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention}has been kicked')

    @kick.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Oops! You don't have that permission.")

        if ctx.author.id == ctx.guild.owner_id:
            await ctx.send("You are the owner!!! Why kick yourself?")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned')

    @ban.error
    async def info_error(ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send("Oops! You don't have that permission.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @unban.error
    async def info_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Oops! You don't have that permission.")


def setup(bot):
    bot.add_cog(admin_commands(bot))
