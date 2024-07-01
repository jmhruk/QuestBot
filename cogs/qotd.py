import discord
from discord.ext import commands
import random

types = ["motivational", "health", "belief", "commitment", "choice"]

def getQuote(type):
    global types
    
    if type in types:
        with open("quotes/quotes-" + str(type) + ".txt", 'r', encoding="utf8") as f:
            list = f.readlines()
            q = random.choice(list)
            return q
        
    else: return "Please Select a valid category."


class Qotd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(name="quote")
    async def quote(self, ctx, *args):
        """Usage: !quote {type}. Suitable type parameters are: "motivational", "health", "belief", "commitment", "choice" (more might be added), to get a random quote just run !quote and it will randomly select a type."""
        type = None        
        
        try:
            type = args[0]
        except Exception as err:
            pass
            
        try:
            if type == None:
                x = random.choice(types)
                #get quote
                quote = getQuote(x)
                await ctx.reply(quote)
            else:
                quote = getQuote(str(type))
                await ctx.reply(quote)
                
                
        except Exception as err:
            print(err)
        
async def setup(bot):
    await bot.add_cog(Qotd(bot))