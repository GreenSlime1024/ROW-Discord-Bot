from pickletools import anyobject
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord import app_commands

with open('image.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Image(Cog_Extension):
  @commands.Cog.listener()
  async def on_ready(self):
    print('Image cog loaded.')

  @app_commands.command()
  async def image(self, interaction: discord.Interaction, name:str):
    '''
    查看圖片
    '''

    await interaction.response.send_message(jdata[name])

  @app_commands.command()
  async def addimage(self, interaction: discord.Interaction, name:str, url:str):
    '''
    新增圖片
    '''
    with open('image.json', 'w', encoding='utf8') as jfile:
      jdata[name] = url
      json.dump(jdata, jfile, ensure_ascii=False, indent=4)
    await interaction.response.send_message(f'新增圖片 `{name}` 成功!')

  @app_commands.command()
  async def names(self, interaction: discord.Interaction):
    '''
    查看所有資料庫中的圖片名稱
    '''
    keys = jdata.keys()
    names = ""
    for i in keys:
      names += (f'`{i}` ')
    await interaction.response.send_message(names)

async def setup(bot): 
  await bot.add_cog(Image(bot))