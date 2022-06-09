import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('ball.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Random(Cog_Extension):
  @commands.command()
  async def ball(self, ctx, msg):
    '''
    [想要問的問題]
    '''
    random_ball = random.choice(jdata['ball'])
    if random_ball == "https://cdn.discordapp.com/attachments/887330126147256323/919167797240688680/81235.png":
      await ctx.reply("不知道，但我不會放棄你", mention_author=False)
    await ctx.reply(random_ball, mention_author=False)

  @commands.command()
  async def pa(self, ctx, *, msg):
    '''
    [想要問的問題]
    '''
    rate = random.randint(0,100)
    await ctx.reply(f'{msg}的機率有 **{rate}%**', mention_author=False)


def setup(bot):
  bot.add_cog(Random(bot))