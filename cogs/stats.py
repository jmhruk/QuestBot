from discord.ext import commands

v = "Member Count: "

class Stats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(name="setup")
    async def setup(self, ctx):
        server = ctx.guild
        try:
            for x in server.voice_channles:
                if x.name == v + str(server.member_count):
                    await ctx.reply("The feature is already setup.")
                else:
                     await server.create_voice_channel(v + str(server.member_count))
                        
        except Exception as err:
            print(err)
            
    @commands.command(name="updated")
    async def setup(self, ctx):
        server = ctx.guild
        try:
            for x in server.voice_channles:
                if x.name == v + str(server.member_count):
                    await ctx.reply("The feature is up to date")
                elif x.name.startswith(v):
                    #set x name to update
                    #set even in main.py to update function
                    pass
                        
        except Exception as err:
            print(err)
async def setup(bot):
    # Load cog 
    await bot.add_cog(Stats(bot))  