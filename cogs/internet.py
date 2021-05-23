import discord
from discord.ext import commands
import asyncio
import aiohttp
import requests
import json


class internet_sutff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        headers = {"accept": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://icanhazdadjoke.com/', headers=headers) as resp:
                jokes = (await resp.json())
                await ctx.send(jokes['joke'])


def setup(bot):
    bot.add_cog(internet_sutff(bot))
