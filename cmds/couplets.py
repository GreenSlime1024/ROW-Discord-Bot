import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension
from discord_slash import cog_ext

class Couplets(Cog_Extension):
  @cog_ext.cog_slash()
  async def 貼春聯(self, ctx):
    '''
    在頻道名稱後方加上 '"春"或"福"'
    '''
    name = ctx.channel.name
    if name.endswith('⟨春⟩') or name.endswith('⟨福⟩'):
     await ctx.send('已經貼過了呦')
    else:
      couplets = random.randint(0, 1)
      if couplets == 0:
        await ctx.channel.edit(name=name + '⟨春⟩')
      else:
        await ctx.channel.edit(name=name + '⟨福⟩')
      await ctx.send('(貼')

  @cog_ext.cog_slash()
  async def 撕春聯(self, ctx):
    '''
    把頻道名稱後方的春聯撕起來
    '''
    name = ctx.channel.name
    length = len(name)
    if name.endswith('⟨春⟩') or name.endswith('⟨福⟩'):
      name = name[:length-3]
      await ctx.channel.edit(name=name)
      await ctx.send('(撕')
    else:
      await ctx.send('沒有春聯可以撕喔')
      
      

def setup(bot):
  bot.add_cog(Couplets(bot))