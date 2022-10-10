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
  async def avatar(self, ctx, member:discord.Member=None, size:int=1024):
    if member == None:
      member = ctx.author
    '''
    查看使用者的頭像
    '''
    userAvatarUrl = member.avatar_url_as(size=size)
    await ctx.send(str(userAvatarUrl))
    
  @cog_ext.cog_slash()
  async def ROW(self, ctx):
    '''
    查看 ROW 的介紹網站
    '''
    await ctx.send('https://greenslime1024.github.io/posts/row/')

  @cog_ext.cog_slash()
  async def author(self, ctx):
    '''
    查看 GreenSlime 的網站
    '''
    await ctx.send('https://greenslime1024.github.io/')

  @cog_ext.cog_slash()
  async def guild(self, ctx):
    '''
    查看此機器人服務的伺服器
    '''
    embed=discord.Embed(title="伺服器列表", color=0x8280ff)
    for guild in self.bot.guilds:
      embed.add_field(name=guild, value=guild.id, inline=False)
    await ctx.send(embed=embed)
  
def setup(bot):
  bot.add_cog(Main(bot))