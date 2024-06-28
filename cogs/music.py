from discord.ext import commands
from discord import Embed

class Music(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot


    #create music functions

    
async def setup(bot):
    # Load cog 
    await bot.add_cog(Music(bot))