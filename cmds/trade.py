import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json
import asyncio
from discord_slash import cog_ext

class Wool(Cog_Extension):
    @cog_ext.cog_slash()
    async def sell(self, ctx, 物品名稱, 價格:float, 數量:int):
        '''
        賣出物品
        '''
        with open('trade.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        count = jdata['count']
        with open('setting.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        channel = self.bot.get_channel(int(jdata['Trade_channel']))
        embed=discord.Embed(title="物品上架", color=0x00ff40, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="物品名稱", value=物品名稱, inline=False)
        embed.add_field(name="價格", value=價格, inline=False)
        embed.add_field(name="數量", value=數量, inline=False)
        embed.set_footer(text=count)

        data = {
            "name": 物品名稱,
            "price": 價格,
            "amount": 數量,
            "id": ctx.author.id,
            "status": True,
            "dtime": str(datetime.datetime.now())
        }

        with open('trade.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        count = jdata['count']
        jdata[count] = data
        with open('trade.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        count += 1
        with open('trade.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['count'] = count
        with open('trade.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)

        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await channel.send(embed=embed)
            await ctx.send(f'上架成功 :white_check_mark:')

    @cog_ext.cog_slash()
    async def buy(self, ctx, 訂單編號, 數量):
        '''
        買入物品
        '''
        with open('setting.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        channel = self.bot.get_channel(int(jdata['Trade_channel']))
        with open('trade.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        data = jdata[訂單編號]
        status = data['status']
        if status:
            name = data['name']
            price = float(data['price'])
            數量 = int(數量)
            amount = data['amount']
            id = data['id']
            user = self.bot.get_user(id)
            embed=discord.Embed(title="物品購買", color=0x006eff, timestamp=datetime.datetime.utcnow())
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="物品名稱", value=name, inline=False)
            embed.add_field(name="價格", value=price, inline=False)
            embed.add_field(name="數量", value=數量, inline=False)
            embed.add_field(name="花費", value=price*數量, inline=False)
            embed.add_field(name="賣家", value=user.name, inline=False)
            
            if amount - 數量 == 0:
                data['status'] = False
                with open('trade.json', mode='w', encoding='utf8') as jfile:
                    json.dump(jdata, jfile, indent=4)
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await channel.send(embed=embed)
                    await ctx.send(f'購買成功 :white_check_mark:')
            if amount - 數量 > 0:
                data['amount'] = amount - 數量
                with open('trade.json', mode='w', encoding='utf8') as jfile:
                    json.dump(jdata, jfile, indent=4)
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await channel.send(embed=embed)
                    await ctx.send(f'購買成功 :white_check_mark:')
            if amount - 數量 < 0:
                await ctx.send(f'目前只剩 {amount} 個')
        else:
            await ctx.send('此商品已售完')

    @cog_ext.cog_slash()
    async def set_trade_channel(self, ctx, channel : discord.TextChannel=None):
        '''
        設置交易頻道
        '''
        with open('setting.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata["Trade_channel"] = channel.id
        with open('setting.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        self.channel = self.bot.get_channel(channel.id)
        await ctx.send(f'已設置訂單儲存頻道: {self.channel.mention} :white_check_mark:') 
        
def setup(bot):
  bot.add_cog(Wool(bot))