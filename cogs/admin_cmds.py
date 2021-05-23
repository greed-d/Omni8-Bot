import discord
from discord.ext import commands
from discord.ext.commands.core import command


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
        if member.id in [ctx.author.id, self.bot.user.id]:
            return await ctx.send("You cannot ban yourself or the bot")

        else:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned')

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

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, time: int):

        if time == None:
            await ctx.channel.edit(slowmode_delay=10)
            await ctx.send("Slowmode set to 10 sec")

        if time == 0:
            await ctx.send('Slowmode ``Deactivated``!')
            await ctx.channel.edit(slowmode_delay=0)
        elif time > 21600:
            await ctx.send("You can't set the slowmode above 6 hours!")
            return
        else:
            await ctx.channel.edit(slowmode_delay=time)
            await ctx.send(f"Slowmode set to {time} seconds!")


def setup(bot):
    bot.add_cog(admin_commands(bot))
