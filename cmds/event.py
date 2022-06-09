import discord
import asyncio
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Event(Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self, msg):
    if '早安' in msg.content and msg.author != self.bot.user:
      async with msg.channel.typing():
        await asyncio.sleep(1)
        await msg.channel.send('咖啡 呼啦')
        
    if '午安' in msg.content and msg.author != self.bot.user:
      async with msg.channel.typing():
        await asyncio.sleep(1)
        await msg.channel.send('午安') 

    if '晚安' in msg.content and msg.author != self.bot.user:
      async with msg.channel.typing():
        await asyncio.sleep(1)
        await msg.channel.send('晚安 :zzz: ')
    
    if '免費nitro' in msg.content and msg.author != self.bot.user:
      async with msg.channel.typing():
        await asyncio.sleep(1)
        await msg.channel.send('https://cdn.discordapp.com/attachments/694534457985597443/882552709083971604/image0.png')
      
    if '真的假的' in msg.content and msg.author != self.bot.user:
      async with msg.channel.typing():
        await asyncio.sleep(1)
        await msg.channel.send('~~假的~~')

    if '<@602037424863969283>' in msg.content and msg.author != self.bot.user:
      async with msg.channel.typing():
        await asyncio.sleep(1)
        await msg.channel.send('虛~ 他在睡覺')
  
def setup(bot):
  bot.add_cog(Event(bot))