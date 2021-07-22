import discord
from discord.ext import commands
from datetime import datetime


class Routine(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    DAYS = [
        "SUNDAY",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
    ]

    @commands.command()
    async def routine(self, ctx, day: str = datetime.today().strftime("%A")):
        day = day.upper()

        if day in self.DAYS:

            em = discord.Embed(
                title="**ROUTINE FOR THE DAY : **",
                description=day,
                color=discord.Color.purple(),
            )

            if day == "SUNDAY":
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

            elif day == "MONDAY":
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

            elif day == "TUESDAY":
                em.add_field(
                    name="**7:00AM - 8:40AM**",
                    value="[TOC/SHG](https://meet.google.com/lookup/fsjsnh3agx)",
                    inline=False,
                )
                em.add_field(
                    name="8:40AM - 10:20AM",
                    value="[EDC/AKR](https://meet.google.com/lookup/glirqg5j54)",
                    inline=False,
                )
                em.add_field(
                    name="12:00PM - 2:30PM",
                    value="[OOP LAB A1](https://meet.google.com/lookup/cki5peapz5)",
                    inline=False,
                )
                await ctx.send(embed=em)

            elif day == "WEDNESDAY":
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

            elif day == "THURSDAY":
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

            elif day == "FRIDAY":
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

            elif day == "SATURDAY":
                await ctx.send("NO CLASSES TODAY :slight_smile:")
        else:
            await ctx.send("PLEASE ENTER A VALID DAY")


def setup(bot):
    bot.add_cog(Routine(bot))
