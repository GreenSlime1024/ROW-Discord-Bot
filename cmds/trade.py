import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json
import random
import asyncio
from discord_slash import cog_ext

with open('setting.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Trade(Cog_Extension):
  @cog_ext.cog_slash()
  async def sell(self, ctx, 物品, 價格:int, 數量:int, 備註 : str='沒有備註'):
    '''
    上架物品
    '''
    global channel
    channel = self.bot.get_channel(int(jdata['Trade_channel']))
    embed=discord.Embed(title="拍賣物品", color=0x8280ff, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(name="物品", value=物品, inline=False)
    embed.add_field(name="價格", value=價格, inline=False)
    embed.add_field(name="數量", value=數量, inline=False)
    embed.add_field(name="備註", value=備註, inline=False)
    embed.set_footer(text=random.randint(100000,999999))

    info = {"物品" : 物品, "價格" : 價格, "數量" : 數量, "備註" : 備註}

    with open('trade.json', mode='r', encoding='utf8') as jfile:
      jdata = json.load(jfile)
    jdata[ctx.author.id] = info
    with open('trade.json', mode='w', encoding='utf8') as jfile:
     json.dump(jdata, jfile, indent=4)
        
    
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await channel.send(embed=embed)
        await ctx.send(f'上架成功 :white_check_mark:')

def setup(bot):
  bot.add_cog(Trade(bot))