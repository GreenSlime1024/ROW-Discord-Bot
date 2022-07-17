import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord_slash import cog_ext


class Main(Cog_Extension):
  @cog_ext.cog_slash(name='ping', description='show ping')
  async def ping(self, ctx):
    await ctx.send(f'pong ({round(self.bot.latency*1000)}ms)')
  
def setup(bot):
  bot.add_cog(Main(bot))