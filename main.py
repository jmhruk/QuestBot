from dotenv import load_dotenv
import discord
from discord import Intents
from discord.ext import commands
import os

load_dotenv()

token = os.getenv("TOKEN")

intents = Intents.all()
bot = commands.Bot(intents=intents, command_prefix="!")
bot.author_id = [733735829222195321]

@bot.event
async def on_ready():
    
    await bot.load_extension("cogs.general")
    await bot.load_extension("cogs.moderation")	

    await bot.change_presence(activity=discord.Activity(
       type=discord.ActivityType.watching, name="Watching your server..."))
    
    print("Bot is online!")

bot.run(token)  # Starts the bot