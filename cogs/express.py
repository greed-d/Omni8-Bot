from logging import setLogRecordFactory
import discord
from discord import message
from discord.ext import commands, tasks
import random
import aiohttp
import asyncio


class expressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slap_gif = ['https://media.giphy.com/media/gSIz6gGLhguOY/giphy.gif',
                         'https://media.giphy.com/media/uG3lKkAuh53wc/giphy.gif',
                         'https://media.giphy.com/media/u8maN0dMhVWPS/giphy.gif',
                         'https://media.giphy.com/media/l3YSimA8CV1k41b1u/giphy.gif',
                         'https://media.giphy.com/media/10L38gtN2vVpgk/giphy.gif']

        self.pat_gif = ['https://media.giphy.com/media/L2z7dnOduqEow/giphy.gif',
                        'https://media.giphy.com/media/LZTexZNeIrpD3TiRi2/giphy.gif',
                        'https://media.giphy.com/media/ye7OTQgwmVuVy/giphy.gif',
                        'https://media.giphy.com/media/xUA7bahIfcCqC7S4qA/giphy.gif',
                        'https://media.giphy.com/media/N0CIxcyPLputW/giphy.gif'
                        ]

        self.respect_gif = [
            'https://media.giphy.com/media/9JyTQrfpJs8zZ9xLI3/giphy.gif',
            'https://media.giphy.com/media/lEVZJzy4w15qE/giphy.gif',
            'https://media.giphy.com/media/MaJ7An3EUgLCCh4lXS/giphy.gif',
            'https://media.giphy.com/media/WO5Q7FsxJN2pjYc424/giphy.gif']

    @commands.command()
    async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ','.join(x.name for x in members)
        if not ctx.message.mentions:
            await ctx.send(f'{ctx.author.mention} Whom do you want to slap bud?')

        if ctx.author in ctx.message.mentions:
            await ctx.send(f"{ctx.author.mention} Why slap yourself bruh? 🤐🤐")

        elif ctx.message.mentions:
            em = discord.Embed(
                title=f"{slapped} got slapped by {ctx.author.name} for {reason}"
            )
        em.set_image(url=random.choice(self.slap_gif))

        await ctx.send(embed=em)

    @commands.command()
    async def pat(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        patted = ','.join(x.name for x in members)
        if not ctx.message.mentions:
            await ctx.send(f'{ctx.author.mention} Whom do you want to slap bud?')

        if ctx.author in ctx.message.mentions:
            await ctx.send(f"{ctx.author.mention} Why slap yourself bruh? 🤐🤐")

        elif ctx.message.mentions:
            em = discord.Embed(
                title=f"{patted} got patted by {ctx.author.name} for no reason"
            )
            em.set_image(url=random.choice(self.pat_gif))
            await ctx.send(embed=em)

    @commands.command(aliases=['f', 're', 'F'])
    async def respect(self, ctx, member: discord.Member):
        if ctx.author in ctx.message.mentions:
            await ctx.send("Self-Respect I see :slight_smile:")

        else:
            em = discord.Embed(
                title=f"{member.name} got respected by {ctx.author.name}"
            )
            em.set_image(url=random.choice(self.respect_gif))
            await ctx.send(embed=em)

    @respect.error
    async def info_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who do you want to respect man?")


def setup(bot):
    bot.add_cog(expressions(bot))
