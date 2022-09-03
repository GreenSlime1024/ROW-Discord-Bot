import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord_slash import cog_ext

class Main(Cog_Extension):
  @cog_ext.cog_slash()
  async def ping(self, ctx):
    '''
    查看目前的 ping
    '''
    await ctx.send(f'pong ({round(self.bot.latency*1000)}ms)')

  @cog_ext.cog_slash()
  async def avatar(self, ctx, avamember:discord.Member=None, size:int=1024):
    if avamember == None:
      avamember = ctx.author
    '''
    查看使用者的頭像
    '''
    userAvatarUrl = avamember.avatar_url_as(size=size)
    await ctx.send(str(userAvatarUrl))
    
  @cog_ext.cog_slash()
  async def ROW(self, ctx):
    '''
    查看ROW 的介紹網站
    '''
    await ctx.send('https://greenslime9392.github.io/posts/21/07/row/')

  @cog_ext.cog_slash()
  async def author(self, ctx):
    '''
    查看GreenSlime 的網站
    '''
    await ctx.send('https://greenslime9392.github.io/')
  
def setup(bot):
  bot.add_cog(Main(bot))