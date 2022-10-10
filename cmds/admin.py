from tkinter import HIDDEN
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord_slash import cog_ext

with open('channel.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Admin(Cog_Extension):
    
    @cog_ext.cog_slash()
    @commands.is_owner()
    async def set_order_channel(self, ctx, channel : discord.TextChannel):
        '''
        設置訂單放置頻道
        '''
        jdata["wool_channel"] = channel.id
        with open('channel.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        self.channel = self.bot.get_channel(channel.id)
        await ctx.send(f'已設置訂單儲存頻道: {self.channel.mention}', hidden = True)

    @cog_ext.cog_slash()
    @commands.is_owner()
    async def set_trade_channel(self, ctx, channel : discord.TextChannel):
        '''
        設置物品上架頻道
        '''
        with open('channel.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata["Trade_channel"] = channel.id
        with open('channel.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
            self.channel = self.bot.get_channel(channel.id)
            await ctx.send(f'已設置物品上架頻道: {self.channel.mention}', hidden = True)
    
    @cog_ext.cog_slash()
    @commands.is_owner()
    async def say(self, ctx, msg):
        '''
        讓他說話
        '''
        await ctx.channel.send(msg)
        await ctx.send('成功送出!', hidden = True)

def setup(bot):
    bot.add_cog(Admin(bot))