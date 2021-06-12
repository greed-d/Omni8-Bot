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
            async with session.get(
                "https://icanhazdadjoke.com/", headers=headers
            ) as resp:
                jokes = await resp.json()
                await ctx.send(jokes["joke"])

    def get_quote():
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]["q"] + "   -" + json_data[0]["a"]
        return quote

    @commands.command()
    async def inspire(self, ctx):
        quote = self.get_quote()
        await ctx.send(quote)


def setup(bot):
    bot.add_cog(internet_sutff(bot))
