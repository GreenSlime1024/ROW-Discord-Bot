import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Exam(Cog_Extension):
  @commands.command()
  async def 會考時間表(self, ctx):
    '''
    顯示會考時間表
    '''
    會考時間表 ='```diff\n 第一天:110年5月21日(六)\n 08:20-08:30    考試說明 (10分鐘)\n-08:30-09:40    社會 (70分鐘)\n+09:40-10:20    休息 (40分鐘)\n 10:20-10:30    考試說明 (10分鐘)\n-10:30-11:50    數學 (80分鐘)\n+11:50-13:40    午休 (110分鐘)\n 13:40-13:50    考試說明 (10分鐘)\n-13:50-15:00    國文 (70分鐘)\n+15:00-15:40    休息 (40分鐘)\n 15:40-15:50    考試說明 (10分鐘)\n-15:50-16:40    寫作測驗 (50分鐘)\n\n 第二天:110年5月22日(日)\n 08:20-08:30    考試說明 (10分鐘)\n-08:30-09:40    自然 (70分鐘)\n+09:40-10:20    休息 (40分鐘)\n 10:20-10:30    考試說明 (10分鐘)\n-10:30-11:30    英語-閱讀 (60分鐘)\n+11:30-12:00    休息 (30分鐘)\n 12:00-12:05    考試說明 (5分鐘)\n-12:05-12:30    英語-聽力 (25分鐘)```'
    await ctx.reply(會考時間表, mention_author=False)
    
def setup(bot):
  bot.add_cog(Exam(bot))