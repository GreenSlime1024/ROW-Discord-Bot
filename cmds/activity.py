import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    async def activiy_task():
      await self.bot.wait_until_ready()
      while not self.bot.is_closed():
        activity = ['SD預計2022.12.31重啟伺服器', '運作平台: 桌機', 'Prefix: /', 'ROW 網站: https://greenslime9392.github.io/posts/21/07/row/', 'Made By GreenSlime#9392']
        for i in range(len(activity)-1):
          await self.bot.change_presence(activity=discord.Game(name=activity[i]))
          await asyncio.sleep(15)
        
    self.bg_task = self.bot.loop.create_task(activiy_task())

def setup(bot):
  bot.add_cog(Task(bot))