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

    @commands.command()
    async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ','.join(x.mention for x in members)
        if not ctx.message.mentions:
            await ctx.send(f'{ctx.author.mention} Whom do you want to slap bud?')

        if ctx.author in ctx.message.mentions:
            await ctx.send(f"{ctx.author.mention} Why slap yourself bruh? 🤐🤐")

        elif ctx.message.mentions:
            await ctx.send(f"{slapped} got slapped by {ctx.author.mention} for {reason}")
            slap_gif = ['https://tenor.com/view/cat-spank-pia-mad-slap-gif-17761999',
                        'https://tenor.com/view/couple-cute-angry-mad-hit-head-gif-17327764',
                        'https://tenor.com/view/couple-hit-smack-beat-notty-gif-15960722',
                        'https://tenor.com/view/go-to-sleep-slapping-face-gif-15440023',
                        'https://tenor.com/view/slap-bears-gif-10422113'
                        ]
            await ctx.send(random.choice(slap_gif))

    @commands.command()
    async def pat(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        patted = ','.join(x.mention for x in members)
        if not ctx.message.mentions:
            await ctx.send(f'{ctx.author.mention} Whom do you want to slap bud?')

        if ctx.author in ctx.message.mentions:
            await ctx.send(f"{ctx.author.mention} Why slap yourself bruh? 🤐🤐")

        elif ctx.message.mentions:
            await ctx.send(f"{patted} got patted by {ctx.author.mention} for {reason}")
            pat_gif = ['https://tenor.com/view/pat-good-boy-gif-7220650',
                       'https://tenor.com/view/kitten-pat-caress-love-care-gif-13912621    ',
                       'https://tenor.com/view/big-hero6-baymax-there-there-patting-head-pat-head-gif-4086973',
                       'https://tenor.com/view/kanna-dragonmaid-dragon-maid-misskobayashi-gif-8053566',
                       'https://tenor.com/view/funny-dog-cat-patting-head-gif-4953911'
                       ]
            await ctx.send(random.choice(pat_gif))

    @commands.command(aliases=['f', 're', 'F'])
    async def respect(self, ctx, member: discord.Member):
        if ctx.author in ctx.message.mentions:
            await ctx.send("Self-Respect I see :slight_smile:")

        else:
            await ctx.send(f'{ctx.author.mention} pays respect to {member.mention}')
            respect_gif = [
                'https://tenor.com/view/respect-gif-7551965',
                'https://tenor.com/view/respect-bow-bruce-lee-gif-14266999',
                'https://tenor.com/view/respect-davis-boreanaz-salute-uniform-gif-11216021',
                'https://tenor.com/view/school-of-rock-jack-black-dewey-finn-salute-respect-gif-4980602'

            ]
            await ctx.send(random.choice(respect_gif))

    @respect.error
    async def info_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who do you want to respect man?")

    @commands.command()
    async def joke(self, ctx):
        headers = {"accept": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://icanhazdadjoke.com/', headers=headers) as resp:
                hehe = (await resp.json())
                await ctx.send(hehe['joke'])


def setup(bot):
    bot.add_cog(expressions(bot))
