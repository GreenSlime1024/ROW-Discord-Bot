import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension

class Couplets(Cog_Extension):
  @commands.command()
  async def 貼春聯(self, ctx):
    '''
    在頻道名稱後方加上 '"春"或"福"'
    '''
    name = ctx.channel.name
    if name.endswith('⟨春⟩') or name.endswith('⟨福⟩'):
     await ctx.reply('已經貼過了呦', mention_author=False)
    else:
      couplets = random.randint(0, 1)
      if couplets == 0:
        await ctx.channel.edit(name=name + '⟨春⟩')
      else:
        await ctx.channel.edit(name=name + '⟨福⟩')
      await ctx.reply('(貼', mention_author=False)
  @commands.command()
  async def 撕春聯(self, ctx):
    '''
    撕春聯
    '''
    name = ctx.channel.name
    length = len(name)
    if name.endswith('⟨春⟩') or name.endswith('⟨福⟩'):
      name = name[:length-3]
      await ctx.channel.edit(name=name)
      await ctx.reply('(撕', mention_author=False)
    else:
      await ctx.reply('沒有春聯可以撕喔', mention_author=False)
      
      

def setup(bot):
  bot.add_cog(Couplets(bot))