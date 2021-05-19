import discord
from discord.ext import commands


class commandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("uh oh this command is not in here, try >help for more info")

        if hasattr(ctx.command, 'on_error'):
            return


def setup(bot):
    bot.add_cog(commandErrorHandler(bot))
