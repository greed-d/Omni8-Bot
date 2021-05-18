from logging import setLogRecordFactory
import discord
from discord.ext import commands, tasks


class expressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

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


def setup(bot):
    bot.add_cog(expressions(bot))
