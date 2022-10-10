import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord_slash import cog_ext

with open('admin.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Admin(Cog_Extension):
    
    @cog_ext.cog_slash()
    @commands.is_owner()
    async def set_order_channel(self, ctx, channel : discord.TextChannel):
        '''
        設置訂單放置頻道
        '''
        jdata["Order_channel"] = channel.id
        with open('setting.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        self.channel = self.bot.get_channel(channel.id)
        await ctx.send(f'已設置訂單儲存頻道: {self.channel.mention}')

    @cog_ext.cog_slash()
    @commands.is_owner()
    async def set_trade_channel(self, ctx, channel : discord.TextChannel):
        '''
        設置物品上架頻道
        '''
        with open('setting.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata["Trade_channel"] = channel.id
        with open('setting.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
            self.channel = self.bot.get_channel(channel.id)
            await ctx.send(f'已設置物品上架頻道: {self.channel.mention} ')

def setup(bot):
    bot.add_cog(Admin(bot))