import discord
from discord.ext import commands
import random


class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.responses = ["It is certain.",
                          "It is decidedly so.",
                          "Without a doubt.",
                          "Yes - definitely.",
                          "You may rely on it.",
                          "As I see it, yes.",
                          "Most likely.",
                          "Outlook good.",
                          "Yes.",
                          "Signs point to yes.",
                          "Reply hazy, try again.",
                          "Ask again later.",
                          "Better not tell you now.",
                          "Cannot predict now.",
                          "Concentrate and ask again.",
                          "Don't count on it.",
                          "My reply is no.",
                          "My sources say no.",
                          "Outlook not so good.",
                          "Very doubtful."]

    @commands.command()
    async def hellu(self, ctx):
        await ctx.send("Hellu")

    @commands.command(aliases=['ft', 'fortune'])
    async def fortu_tellin(self, ctx, *, question):
        if question.startswith('will'):
            await ctx.send(f':crystal_ball: Question: {question}\n:8ball: Answer: {random.choice(self.responses)}')

        else:
            await ctx.send(f"Please start a sensible question starting with 'will'")


def setup(bot):
    bot.add_cog(games(bot))
