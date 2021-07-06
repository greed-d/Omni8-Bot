import discord
from discord.ext import commands
from datetime import datetime


class Routine(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def routine(self, ctx):
        em = discord.Embed(
            title="**TODAY'S ROUTINE**",
            description=datetime.today().strftime("%A"),
            color=discord.Color.purple(),
        )

        if datetime.today().strftime("%A") == "Sunday":
            em.add_field(
                name="**7:00AM - 8:40AM**",
                value="[EDC/KKJ](https://meet.google.com/lookup/gueos7ushn)",
                inline=False,
            )
            em.add_field(
                name="8:40AM - 10:20AM",
                value="[OOP/RPS](https://meet.google.com/lookup/b7o3xkrow6)",
                inline=False,
            )
            em.add_field(
                name="12:00PM - 1:40PM",
                value="[ECT/BS](https://meet.google.com/lookup/eay7sjyttk)",
                inline=False,
            )
            em.add_field(
                name="1:40PM - 3:20PM",
                value="[EM/SD](https://meet.google.com/lookup/e7xljvtzki)",
                inline=False,
            )
            await ctx.send(embed=em)

        elif datetime.today().strftime("%A") == "Monday":
            em.add_field(
                name="**7:00AM - 8:40AM**",
                value="[DL/DS](https://meet.google.com/lookup/eodrxelizr)",
                inline=False,
            )
            em.add_field(
                name="8:40AM - 10:20AM",
                value="[MATHS/NPA](https://meet.google.com/lookup/h7eizn5x22)",
                inline=False,
            )
            em.add_field(
                name="12:00PM - 1:40PM",
                value="[ECT/BS](https://meet.google.com/lookup/eay7sjyttk)",
                inline=False,
            )
            em.add_field(
                name="1:40PM - 3:20PM",
                value="[EM/SD](https://meet.google.com/lookup/e7xljvtzki)",
                inline=False,
            )
            await ctx.send(embed=em)

        elif datetime.today().strftime("%A") == "Tuesday":
            em.add_field(
                name="**7:00AM - 8:40AM**",
                value="[TOC/SHG](https://meet.google.com/lookup/fsjsnh3agx)",
                inline=False,
            )
            em.add_field(
                name="8:40AM - 10:20AM",
                value="[EDC/AKR](ttps://meet.google.com/lookup/glirqg5j54)",
                inline=False,
            )
            em.add_field(
                name="12:00PM - 2:30PM",
                value="[OOP LAB A1](https://meet.google.com/lookup/cki5peapz5)",
                inline=False,
            )
            await ctx.send(embed=em)

        elif datetime.today().strftime("%A") == "Wednesday":
            em.add_field(
                name="**7:00AM - 8:40AM**",
                value="[OOP/RPS](https://meet.google.com/lookup/b7o3xkrow6)",
                inline=False,
            )
            em.add_field(
                name="8:40AM - 10:20AM",
                value="[MATHS/GDC](https://meet.google.com/lookup/cwbsi76jn5)",
                inline=False,
            )
            em.add_field(
                name="12:00PM - 1:40PM",
                value="[EM/SD](https://meet.google.com/lookup/e7xljvtzki)",
                inline=False,
            )
            await ctx.send(embed=em)

        elif datetime.today().strftime("%A") == "Thursday":
            em.add_field(
                name="**7:00AM - 8:40AM**",
                value="[TOC/SHG](https://meet.google.com/lookup/fsjsnh3agx)",
                inline=False,
            )
            em.add_field(
                name="8:40AM - 9:30AM",
                value="[MATHS/GBJ](https://meet.google.com/lookup/ccft5zagx4)",
                inline=False,
            )
            em.add_field(
                name="9:30AM - 10:20AM",
                value="[EDC/KKJ](https://meet.google.com/lookup/gueos7ushn)",
                inline=False,
            )
            em.add_field(
                name="12:50PM - 2:30PM",
                value="[MATHS/SA](https://meet.google.com/lookup/g6dcqkqq7v)",
                inline=False,
            )
            await ctx.send(embed=em)

        elif datetime.today().strftime("%A") == "Friday":
            em.add_field(
                name="**7:00AM - 8:40AM**",
                value="[ECT/BS](https://meet.google.com/lookup/eay7sjyttk)",
                inline=False,
            )
            em.add_field(
                name="8:40AM - 10:20AM",
                value="[DL/DS](https://meet.google.com/lookup/eodrxelizr)",
                inline=False,
            )
            em.add_field(
                name="12:50PM - 2:30PM",
                value="[A2 OOP LAB](https://meet.google.com/lookup/cuoqcmwoxk)",
                inline=False,
            )
            await ctx.send(embed=em)
        else:
            await ctx.send("No classes today hurray :D")


def setup(bot):
    bot.add_cog(Routine(bot))
