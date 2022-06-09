import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

def reload_setting():
  global jdata
  with open('image.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
reload_setting()

class Image(Cog_Extension):
  @commands.command()
  async def i(self, ctx,*,msg):
    '''
    [圖片名稱]
    '''
    await ctx.reply(jdata[msg], mention_author=False)

  @commands.command()
  async def iadd(self, ctx, name, url):
    '''
    [新圖片名稱] [新圖片url]
    '''
    with open('image.json', 'w', encoding='utf8') as jfile:
      jdata[name] = url
      json.dump(jdata, jfile, ensure_ascii=False, indent=4)
    reload_setting()
    await ctx.reply(f'已新增 [{name}] :white_check_mark:', mention_author=False)

def setup(bot): 
  bot.add_cog(Image(bot))