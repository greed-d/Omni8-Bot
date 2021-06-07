import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands.core import command


class admin_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.badwords = ['fuck', 'motherfucker', 'mugi', 'muji', 'fucking', 'motherfucking', 'dick', 'machikne', 'shit', 'tits',
                         'bitch', 'whore', 'hoe', 'nigga', 'nigger', 'cunt', 'faggot', 'pussy', 'asshole', 'dickhead', 'bastard',
                         'wanker', 'randi', 'radi', 'chikne', 'chickney', 'gede', 'lado', 'suck my', 'lick my'
                         ]

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

    @commands.Cog.listener()
    async def on_message(self, message):

        for i in self.badwords:
            if i.lower() in message.content.lower() or i.upper() in message.content.upper():
                if message.author.id == 532960958381817857:
                    return
                else:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} you cannot use that word here", delete_after=5)
                    self.bot.dispatch('profanity', message, i)
                    return

    @commands.Cog.listener()
    async def on_profanity(self, message, word):
        guild = message.guild
        if guild.id == 841550614344237057:
            channel = self.bot.get_channel(847342532438655017)
            embed = discord.Embed(title='**PROFANITY ALERT**',
                                  description=f"{message.author.name} just said the word ||{word}||", color=discord.Color.blurple()
                                  )
            await channel.send(embed=embed)

        elif guild.id == 839543471412477952:
            channel = self.bot.get_channel(847375614406950933)
            embed = discord.Embed(title='**PROFANITY ALERT**',
                                  description=f"{message.author.name} just said the word ||{word}||", color=discord.Color.blurple()
                                  )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        perms = discord.Permissions(send_messages=False, read_messages=True)
        role = await guild.create_role(name="Muted", permissions=perms)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member):
        if member.id == 841547916199329812:
            await ctx.channel.send("You cannot mute the bot")

        elif ctx.author.id == member.id:
            await ctx.channel.send("You cannot mute yourself")

        else:
            var = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.add_roles(var)
            await ctx.channel.send(f"{member.mention} has been **MUTED**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role)
        await ctx.channel.send(f"{member.mention} has been **UNMUTED**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        if amount == 0:
            await ctx.channel.send(f"Please enter a number ", delete_after=5)

        elif amount > 100:
            await ctx.channel.send(f"Please don't enter a number greater than 100", delete_after=5)

        else:
            deleted = await ctx.channel.purge(limit=amount+1)
            await ctx.channel.send("Deleted {} message(s)".format(len(deleted)), delete_after=8)


def setup(bot):
    bot.add_cog(admin_commands(bot))
