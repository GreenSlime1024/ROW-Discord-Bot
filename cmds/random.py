import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from discord import app_commands


with open('ball.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Random(Cog_Extension):
  @commands.Cog.listener()
  async def on_ready(self):
    print('Random cog loaded.')

  @app_commands.command()
  async def ball(self, interaction: discord.Interaction, question:str):
    '''
    神奇八號球
    '''
    random_ball = random.choice(jdata['ball'])
    if random_ball == "https://cdn.discordapp.com/attachments/887330126147256323/919167797240688680/81235.png":
      await interaction.response.send_message("不知道，但我不會放棄你")
    await interaction.response.send_message(random_ball)

  @app_commands.command()
  async def pa(self, interaction: discord.Interaction, question:str):
    '''
    預估某事件發生的機率
    '''
    rate = random.randint(0,100)
    await interaction.response.send_message(f'我預估 **{question}** 的機率有 **{rate}%**')


async def setup(bot):
  await bot.add_cog(Random(bot))