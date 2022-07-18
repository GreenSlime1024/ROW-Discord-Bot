import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from discord_slash import cog_ext


with open('ball.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Random(Cog_Extension):
  @cog_ext.cog_slash()
  async def ball(self, ctx, question):
    '''
    神奇八號球
    '''
    random_ball = random.choice(jdata['ball'])
    if random_ball == "https://cdn.discordapp.com/attachments/887330126147256323/919167797240688680/81235.png":
      await ctx.send("不知道，但我不會放棄你")
    await ctx.send(random_ball)

  @cog_ext.cog_slash()
  async def pa(self, ctx, *, msg):
    '''
    預估某事件發生的機率
    '''
    rate = random.randint(0,100)
    await ctx.send(f'{msg}的機率有 **{rate}%**')


def setup(bot):
  bot.add_cog(Random(bot))