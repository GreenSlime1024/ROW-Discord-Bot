import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.counter = 0
    會考日期 = datetime.datetime(2022, 5, 21)
    第三次模擬考日期 = datetime.datetime(2022, 2, 17)
    第四次模擬考日期 = datetime.datetime(2022, 4, 19)
    學測日期 = datetime.datetime(2025, 1, 17)
    async def interval_task():
      await self.bot.wait_until_ready()
      while not self.bot.is_closed():
        now_time = datetime.datetime.now().strftime('%H%M')
        with open('setting.json', mode='r', encoding='utf8') as jfile:
          jdata = json.load(jfile)
        self.channel = self.bot.get_channel(int(jdata['Interval_channel']))
        with open('task.json', mode='r', encoding='utf8') as jfile:
          jdata = json.load(jfile)
        if now_time == jdata['time'] and self.counter == 0:
          now_time_Ymd = datetime.datetime.now()
          會考倒數天數 = (會考日期 - now_time_Ymd).days
          第三次模擬考倒數天數 = (第三次模擬考日期 - now_time_Ymd).days
          第四次模擬考倒數天數 = (第四次模擬考日期 - now_time_Ymd).days
          學測倒數天數 = (學測日期 - now_time_Ymd).days
          await self.channel.send(f'會考倒數 **{會考倒數天數}** 天')
          self.counter = 1
          await asyncio.sleep(1)
        else:
          await asyncio.sleep(1)
          if now_time != jdata['time']:
            self.counter = 0
            await asyncio.sleep(1)
    self.bg_task = self.bot.loop.create_task(interval_task())

  @commands.has_permissions(administrator=True)
  @commands.command()
  async def set_interval_channel(self, ctx, ch:int):
    '''
    非開發人員請勿亂用
    '''
    with open('setting.json', mode='r', encoding='utf8') as jfile:
     jdata = json.load(jfile)
    jdata["Interval_channel"] = ch
    with open('setting.json', mode='w', encoding='utf8') as jfile:
     json.dump(jdata, jfile, indent=4)
    self.channel = self.bot.get_channel(int(jdata['Interval_channel'])) 
    await ctx.reply(f'已設置間隔訊息頻道: {self.channel.mention} :white_check_mark:', mention_author=False)

  @commands.command()
  async def set_interval_time(self, ctx, time):
    '''
    非開發人員請勿亂用
    '''
    with open('task.json', mode='r', encoding='utf8') as jfile:
     jdata = json.load(jfile)
    jdata["time"] = time
    with open('task.json', mode='w', encoding='utf8') as jfile:
     json.dump(jdata, jfile, indent=4)
    await ctx.reply(f'已設置間隔訊息時間: {time} :white_check_mark:', mention_author=False)

def setup(bot):
  bot.add_cog(Task(bot))