import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json
from discord_slash import cog_ext

with open('channel.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Wool(Cog_Extension):
    @cog_ext.cog_slash()
    async def wool(self, ctx, 顏色, 大箱:int, 小箱:int , 交貨方式,  要送給誰: discord.abc.User='沒有人', 備註 : str='沒有備註'):
      '''
      產生 $羊毛訂購單$
      '''
      channel = self.bot.get_channel(int(jdata['Order_channel']))
      price = 大箱*8640+小箱*4320
      embed=discord.Embed(title="$羊毛訂購單$", color=0x8280ff, timestamp=datetime.datetime.utcnow())
      embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
      embed.add_field(name="顏色", value=顏色, inline=False)
      embed.add_field(name="數量", value=(f'{大箱} 大箱, {小箱} 小箱'), inline=False)
      embed.add_field(name="交貨方式", value=交貨方式, inline=False)
      embed.add_field(name="要送給誰", value=要送給誰, inline=False)
      embed.add_field(name="備註", value=備註, inline=False)
      embed.add_field(name="價格", value=(f'未來幣 {price} 元'), inline=False)
      embed.set_footer(datetime.datetime.utcnow())
    
      await channel.send(embed=embed)
      await ctx.send(f'訂購成功!', hidden = True)
        
def setup(bot):
  bot.add_cog(Wool(bot))