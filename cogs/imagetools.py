import discord
from discord.ext import commands
import random
from PIL import Image
import requests
import os

class Imagetools(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="slap")
    async def slap(self, ctx, user: discord.Member):
        n = random.randint(1,1000)
        
        slap = Image.open("slap.png")

        try:
            pfp = Image.open(requests.get(user.avatar, stream=True).raw)
            pfp = pfp.resize((230,230))
            slap.paste(pfp, (230, 65))

            slapper = Image.open(requests.get(ctx.message.author.avatar, stream=True).raw)
            slapper = slapper.resize ((230,230))
            slap.paste(slapper, (720, 50))

            slap.save(str(n) + "slap.png")
            await ctx.reply(file=discord.File(str(n) + "slap.png"))
            if os.path.exists(str(n) + "slap.png"):
                os.remove(str(n) + "slap.png")
            else:
                print("Achievement Unlocked: How did we get here?")
        except requests.exceptions.MissingSchema:
            await ctx.send("One of the selected users doesn't have an avatar :(")

            # in future to fix this, try get images another way or subsittue them
            

       


async def setup(bot):
    # Load cog 
    await bot.add_cog(Imagetools(bot))