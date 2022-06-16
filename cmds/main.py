import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
  @commands.command()
  async def ping(self, ctx):
    '''
    顯示 ping
    '''
    await ctx.reply(f'pong ({round(self.bot.latency*1000)}ms)', mention_author=False)

  @commands.command()
  async def sayd(self, ctx, *, msg):
    '''
    [想要讓機器人說的話]
    '''
    await ctx.message.delete()
    await ctx.send(msg)

  @commands.command()
  async def avatar(self, ctx, *,  avamember : discord.Member=None):
    '''
    [@某人]
    '''
    userAvatarUrl = avamember.avatar_url
    await ctx.reply(userAvatarUrl , mention_author=False)

  @commands.command()
  async def ROW(self, ctx):
    '''
    關於 ROW 的網頁
    '''
    await ctx.send('https://greenslime9392.github.io/posts/21/07/row/')

def setup(bot):
  bot.add_cog(Main(bot))