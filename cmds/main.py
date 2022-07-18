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
  async def avatar(self, ctx, avamember : discord.Member=None):
    '''
    查看使用者的頭像
    '''
    print(1)
    userAvatarUrl = avamember.avatar_url
    print(2)
    await ctx.send(str(userAvatarUrl))
    print(3)
    
  @cog_ext.cog_slash()
  async def ROW(self, ctx):
    '''
    ROW 的介紹網站
    '''
    await ctx.send('https://greenslime9392.github.io/posts/21/07/row/')

  @cog_ext.cog_slash()
  async def author(self, ctx):
    '''
    GreenSlime 的網站
    '''
    await ctx.send('https://greenslime9392.github.io/')
  
def setup(bot):
  bot.add_cog(Main(bot))