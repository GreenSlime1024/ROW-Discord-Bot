import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord_slash import cog_ext

with open('image.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Image(Cog_Extension):
  @cog_ext.cog_slash()
  async def image(self, ctx, name):
    '''
    查看圖片
    '''
    await ctx.send(jdata[name])

  @cog_ext.cog_slash()
  async def addImage(self, ctx, name, url):
    '''
    新增圖片
    '''
    with open('image.json', 'w', encoding='utf8') as jfile:
      jdata[name] = url
      json.dump(jdata, jfile, ensure_ascii=False, indent=4)
    await ctx.send(f'新增圖片 `{name}` 成功!')

  @cog_ext.cog_slash()
  async def names(self, ctx):
    '''
    查看所有資料庫中的圖片名稱
    '''
    keys = jdata.keys()
    names = ""
    for i in keys:
      names += (f'`{i}` ')
    await ctx.send(names)

def setup(bot): 
  bot.add_cog(Image(bot))