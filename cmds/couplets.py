import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Couplets(Cog_Extension):
  @commands.command()
  async def 貼春聯(self, ctx):
    '''
    在頻道名稱後方加上 '春'
    '''
    name = ctx.channel.name
    if name.endswith('⟨春⟩'):
     await ctx.reply('已經貼過了呦', mention_author=False)
    else:
      await ctx.channel.edit(name=name + '⟨春⟩')
      await ctx.reply('(貼', mention_author=False)

def setup(bot):
  bot.add_cog(Couplets(bot))