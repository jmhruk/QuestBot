import discord
from discord.ext import commands
from discord import Embed
import os
import valo_api
import valo_api.endpoint
import valo_api.responses
import valo_api.responses.store_offers

key = os.getenv("VAL-API")
valo_api.set_api_key(str(key))


class Valorant(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="valorant-agents")
    async def agents(self, ctx):
        agents = ["Breach", "Fade", "Reyna"]
        a = ""
        for x in agents:
            a = a + ", " + x
        
        await ctx.reply(agents)
        
    @commands.command(name="valorant-maps")
    async def maps(self, ctx):
        with open("maps.txt", 'r') as f:
            maps = f.readlines()
        
        a = ""
        for x in maps:
            a = a+", " + x
        await ctx.reply(a)
    
    @commands.command(name="valtest")
    async def valtest(self, ctx):
        
        #wtf why no worky :()
        print(valo_api.endpoints.get_store_offers())
        
        
async def setup(bot):
    # Load cog 
    await bot.add_cog(Valorant(bot))  