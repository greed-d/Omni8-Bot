import discord
from discord.ext import commands


class command_error_handler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = error = getattr(error, "original", error)
        if hasattr(ctx.command, "on_error"):
            return

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(
                "uh oh! This command is not in here, try >help for more info"
            )

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(
                "You don't have the required level of authority to execute this command!!!"
            )

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter all the required argument required")

        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please enter a valid argument for the command!!!")

        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send("The extension is already loaded")

        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send("The extension is not loaded")

        elif isinstance(error, commands.CheckFailure):
            await ctx.send("The check function of the command failed.")

        else:
            raise error


def setup(bot):
    bot.add_cog(command_error_handler(bot))
