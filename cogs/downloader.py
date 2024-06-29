import discord
from discord.ext import commands
from pytube import YouTube
import os
import random
class Downloader(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("mp3")
    async def mp3(self, ctx, name, link : str):
        try:
            n = random.randint(1,1000)
            yt = YouTube(link)
            if yt.length > 600:
                await ctx.reply("The video is longer than 5 minutes, please download a video less than 5 minutes long, thank you!")
            else:
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path="")
                new_file = str(n) + "-" + name + ".mp3"
                os.rename(out_file, new_file)
                await ctx.reply(file=discord.File(new_file))
                os.remove(new_file)

                with open("log.txt", 'a') as l:
                    l.write(str(ctx.message.author.id) + " " + ctx.message.author.name + " downloaded (mp3): " + link)
        except Exception as err:
            print(err)
            await ctx.reply("The link you provided is not correct, please provide a youtube.com link.")

    @commands.command("mp4")
    async def mp4(self,ctx, name, link : str):
        try:
            n = random.randint(1,1000)
            yt = YouTube(link)
            if yt.length > 300:
                await ctx.reply("The video is longer than 5 minutes, please download a video less than 5 minutes long, thank you!")
            else:
                video = yt.streams.filter(res="1080p").first()
                out_file = video.download(output_path="")
                new_file = str(n) + "-" + name + ".mp4"
                os.rename(out_file, new_file)
                await ctx.reply(file=discord.File(new_file))
                os.remove(new_file)

                with open("log.txt", 'a') as l:
                    l.write(str(ctx.message.author.id) + " " + ctx.message.author.name + " downloaded (mp4): " + link)
        except Exception as err:
            print(err)
            await ctx.reply("The link you provided is not correct, please provide a youtube.com link.")
        

async def setup(bot):
    # Load Bot
    await bot.add_cog(Downloader(bot))