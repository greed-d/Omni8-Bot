from logging import setLogRecordFactory
import discord
from discord.ext import commands, tasks


class expressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ','.join(x.name for x in members)
        if not ctx.message.mentions:
            await ctx.send(f'{ctx.author.mention} Whom do you want to slap bud?')

        if ctx.author in ctx.message.mentions:
            await ctx.send(f"{ctx.author.mention} Why slap yourself bruh? 🤐🤐")

        elif ctx.message.mentions:
            await ctx.send('{} got slapped for {}'.format(slapped, reason))

    @commands.command()
    async def pat(self, ctx, members: commands.Greedy[discord.Member], *, reason=None):
        patted = ','.join(x.name for x in members)
        if not ctx.message.mentions:
            await ctx.send(f'{ctx.author.mention} Do you need a hug??\nIf not mention someone ya moron')

        elif ctx.author in ctx.message.mentions:
            print(ctx.message.mentions)
            await ctx.send(f"Are you okay {ctx.author.mention}???? \nYou need a hug???")

        else:
            await ctx.send(' {} got patted '.format(patted))

    @commands.command(aliases=['re', 'F'])
    async def respect(self, ctx, member: discord.Member):
        if ctx.author in ctx.message.mentions:
            await ctx.send("Self-Respect I see :slight_smile:")

        else:
            await ctx.send(f'{ctx.author.mention} pays respect to {member.mention}')


def setup(bot):
    bot.add_cog(expressions(bot))
