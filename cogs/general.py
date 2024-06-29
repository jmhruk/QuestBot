from discord.ext import commands
from jokeapi import Jokes
import random
import wikipedia

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

    @commands.command(name="membercount")
    async def membercount(self, ctx):
        await ctx.reply("Current Member Count: " + str(ctx.guild.member_count))

    @commands.command(name="wikipedia")
    async def wikipedia(self, ctx, *query):
        d = ""
        try:
            page = wikipedia.page(query)
            await ctx.reply(wikipedia.summary(query, 10))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            for x in e.options:
                d = d + " " + x
            await ctx.reply("**The Bot couldn't decide what you were looking for, please be more specific and run the same command with one of the items from the next list:** " + d +",")

        #await ctx.reply(wikipedia.summary(query, 10))
    @commands.command(name="joke")
    async def joke(self, ctx):
        #learning joke imports (api)
        j = await Jokes()
        joke = await j.get_joke()
        if joke["type"] == "single":
            await ctx.reply(joke["joke"])
        else:    
            setup = joke["setup"]
            delivery = joke["delivery"]
            await ctx.reply(str(setup) + "\n" + str(delivery))
#   
#      Coming soon
#
    @commands.command(name="trivia")
    async def trivia(self, ctx):
        pass
    @commands.command(name="translate")
    async def translate(self, ctx):
        pass

async def setup(bot):
    # Load cog 
    await bot.add_cog(General(bot))