from discord.ext import commands
import asyncio
import discord
from discord.ext.commands.core import bot_has_any_role, command
import motor.motor_asyncio


class ConnectDatabase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = motor.motor_asyncio.AsyncIOMotorClient("localhost", 27017)
        self.db = self.client["bot_database"]
        collection = self.db["guild_collection"]

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        result = await self.db.guild_collection.insert_many(
            [
                {
                    "guild_name": f"{guild.name}",
                    "guild_id": guild.id,
                    "disabled_commands": ["filter"],
                    "channel_data": {
                        str(channel.id): channel.name for channel in guild.channels
                    },
                }
            ]
        )


def setup(bot):
    bot.add_cog(ConnectDatabase(bot))
