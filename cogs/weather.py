from discord.ext import commands
import python_weather
import asyncio
import os

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="weather")
    async def weather(self, ctx, unit,*args):
        location = ""
        for x in args:
            location = str(location) + " " + str(x)
        
        z = python_weather.METRIC
        
        if str(unit.lower()) == "metric":
            z = python_weather.METRIC
        elif str(unit.lower()) == "imperial":
            z = python_weather.IMPERIAL
        else:
            print("Wrong unit.")
            await ctx.reply("Please specify a correct unit. Usage: !weather [metric/imperial]")
            
        d = ""
        async with python_weather.Client(unit=z) as client:
            # fetch a weather forecast from a city
            try:
                weather = await client.get(location)
                if z == python_weather.METRIC:
                    d = "Celsius"
                elif z == python_weather.IMPERIAL:
                    d = "Farenheit"
                    
                await ctx.reply("The weather in: " + str(location) + " is " + str(weather.temperature) + " degrees " +  d)
                
            except Exception as err:
                print(Exception)
    
async def setup(bot):
    await bot.add_cog(Weather(bot))