from discord.ext import commands
from discord.ext.commands import bot
from dislash import slash_commands


class SlashCommands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @slash_commands.command(description="Says Hello")
    async def hellu(self, ctx):
        await ctx.send("Hello from first slash command")


def setup(bot):
    bot.add_cog(SlashCommands(bot))
