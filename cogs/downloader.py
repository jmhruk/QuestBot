from discord.ext import commands

class Downloader(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


async def setup(bot):
    # Load Bot
    await bot.add_cog(Downloader(bot))