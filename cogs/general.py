from discord.ext import commands
from discord import Embed
import random

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.reply("Pong!")

    @commands.command(name="pong")
    async def pong(self, ctx):
        await ctx.reply("Ping!")

    @commands.command(name="randomnumber")
    async def randomnumber(self, ctx, n1:int, n2:int):
        await ctx.reply(str(random.randint(n1, n2)))


async def setup(bot):
    # Load cog 
    await bot.add_cog(General(bot))