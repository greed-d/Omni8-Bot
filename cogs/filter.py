from discord.ext import commands
import discord


class Filter(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.badwords = [
            " fuck ",
            " motherfucker ",
            " mugi ",
            " muji ",
            " fucking ",
            " motherfucking ",
            " dick ",
            " machikne ",
            " shit ",
            " tits ",
            " bitch ",
            " whore ",
            " hoe ",
            " nigga ",
            " nigger ",
            " cunt ",
            " faggot ",
            " pussy ",
            " asshole ",
            " dickhead ",
            " bastard ",
            " wanker ",
            " randi ",
            " radi ",
            " chikne ",
            " chickney ",
            " gede ",
            " lado ",
            " suck my ",
            " lick my ",
            " bhosdi ",
            " madarchut ",
        ]

    @commands.Cog.listener()
    async def on_message(self, message):
        for word in self.badwords:
            # if word.islower() or word.isupper():
            if message.content.lower().find(word.lower()) != -1:
                await message.delete()
                em = discord.Embed(
                    title="**—————————————WARNING—————————————**",
                    description=f"{message.author.name}!! You cannot use that word here",
                    color=discord.Color.purple(),
                )
                await message.channel.send(embed=em)


def setup(bot):
    bot.add_cog(Filter(bot))
