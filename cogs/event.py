import discord
import asyncio
from discord.ext import commands
from core.classes import Cog_Extension


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print('Event cog loaded.')

    async def on_message(self, msg):
        if msg.content == '早安' and msg.author != self.bot.user:
            async with msg.channel.typing():
                await asyncio.sleep(1)
                await msg.channel.send('早安')

        if msg.content == '午安' and msg.author != self.bot.user:
            async with msg.channel.typing():
                await asyncio.sleep(1)
                await msg.channel.send('午安')

        if msg.content == '晚安' and msg.author != self.bot.user:
            async with msg.channel.typing():
                await asyncio.sleep(1)
                await msg.channel.send('晚安')

        if '免費nitro' in msg.content and msg.author != self.bot.user:
            async with msg.channel.typing():
                await asyncio.sleep(1)
                await msg.channel.send('https://cdn.discordapp.com/attachments/694534457985597443/882552709083971604/image0.png')

        if msg.content == '真的假的' and msg.author != self.bot.user:
            async with msg.channel.typing():
                await asyncio.sleep(1)
                await msg.channel.send('~~假的~~')

        if msg.content == '<@1022080471506624545>' and msg.author != self.bot.user:
            async with msg.channel.typing():
                await asyncio.sleep(1)
                await msg.channel.send('虛~ 他在睡覺')


async def setup(bot):
    await bot.add_cog(Event(bot))
