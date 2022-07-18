import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord_slash import cog_ext

def reload_setting():
  global jdata
  with open('image.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
reload_setting()

class Image(Cog_Extension):
  @cog_ext.cog_slash()
  async def i(self, ctx,*,msg):
    '''
    查看圖片
    '''
    await ctx.send(jdata[msg])

  @cog_ext.cog_slash()
  async def iadd(self, ctx, name, url):
    '''
    新增圖片
    '''
    with open('image.json', 'w', encoding='utf8') as jfile:
      jdata[name] = url
      json.dump(jdata, jfile, ensure_ascii=False, indent=4)
    reload_setting()
    await ctx.send(f'已新增 [{name}] :white_check_mark:')

def setup(bot): 
  bot.add_cog(Image(bot))