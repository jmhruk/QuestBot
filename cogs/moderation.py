import discord
from discord.ext import commands
from discord import Embed

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        embed = discord.Embed(title=f":white_check_mark: {ctx.author} purged {str(limit)} messages.")
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.channel.purge(limit=limit + 2)


async def setup(bot):
    # Load cog 
    await bot.add_cog(Moderation(bot))