import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json
import random
import asyncio

with open('setting.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Wool(Cog_Extension):
  @commands.command()
  async def buyw(self, ctx, 顏色, 數量, 交貨方式 ,*,備註):
    '''
    [顏色] [數量] [交貨方式] [備註]
    '''
    channel = self.bot.get_channel(int(jdata['Order_channel']))
    price = float(數量)*8640
    embed=discord.Embed(title="羊毛訂購單", color=0x8280ff, timestamp=datetime.datetime.now())
    embed.set_author(name=ctx.author, icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="顏色", value=顏色, inline=False)
    embed.add_field(name="數量", value=(f'{數量}小箱'), inline=False)
    embed.add_field(name="交貨方式", value=交貨方式, inline=False)
    embed.add_field(name="備註", value=備註, inline=False)
    embed.add_field(name="價格", value=(f'未來幣 {price} 元'), inline=False)
    embed.set_footer(text=random.randint(100000,999999))
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await channel.send(embed=embed)
        await ctx.reply(f'訂購成功 :white_check_mark:', mention_author=False)

  @commands.has_permissions(administrator=True)
  @commands.command()
  async def set_order_channel(self, ctx, channel : discord.TextChannel=None):
    '''
    非開發人員請勿亂用
    '''
    with open('setting.json', mode='r', encoding='utf8') as jfile:
      jdata = json.load(jfile)
    jdata["Order_channel"] = channel.id
    with open('setting.json', mode='w', encoding='utf8') as jfile:
     json.dump(jdata, jfile, indent=4)
    self.channel = self.bot.get_channel(int(jdata['Order_channel'])) 
    await ctx.reply(f'已設置訂單儲存頻道:{self.channel.mention} :white_check_mark:', mention_author=False) 
        
def setup(bot):
  bot.add_cog(Wool(bot))