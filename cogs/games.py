from discord.ext import commands
from pytrivia import Category, Diffculty, Type, Trivia
import random

total = []
questions = []
answers = []

#file where question is first then next line is answer.
with open("trivia.txt", 'rb') as f:
    for x in f:
        total.append(x)

for x in total:
    if total.index(x) % 2 == 0:
        questions.append(x)
    else:
        answers.append(x)

class Games(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(name="trivia")
    async def trivia(self, ctx):
        question = random.choice(questions)
        answer = answers[questions.index(question)]
        message = "**Trivia:**\nQuestion:" + str(question) +"\n||" + str(answer) + "||"
        await ctx.reply(message)
        
async def setup(bot):
    # Load cog 
    await bot.add_cog(Games(bot))