import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord import app_commands

class Main(Cog_Extension):
  @commands.Cog.listener()
  async def on_ready(self):
    print('Main cog loaded.')

  @app_commands.command()
  async def ping(self, interaction: discord.Interaction):
    '''
    Check ping
    '''
    await interaction.response.send_message(f'pong ({round(self.bot.latency*1000)}ms)')

  @app_commands.command()
  async def avatar(self, interaction: discord.Interaction, member:discord.Member=None):
    '''
    Check someone's avatar
    '''
    if member == None:
      member = interaction.user
    userAvatarUrl = member.display_avatar
    await interaction.response.send_message(str(userAvatarUrl))
    
  @app_commands.command()
  async def row(self, interaction: discord.Interaction):
    '''
    Check the blog about ROW
    '''
    await interaction.response.send_message('https://greenslime1024.github.io/posts/row/')

  @app_commands.command()
  async def author(self, interaction: discord.Interaction):
    '''
    Check GreenSlime's blog
    '''
    await interaction.response.send_message('https://greenslime1024.github.io/')

  @app_commands.command()
  async def repo(self, interaction: discord.Interaction):
    '''
    Check ROW Bot's repo
    '''
    await interaction.response.send_message('https://github.com/GreenSlime1024/ROW-Discord-Bot')
    
  @app_commands.command()
  async def guild(self, interaction: discord.Interaction):
    '''
    Check guilds which i provide services
    '''
    embed=discord.Embed(title="Server List", color=0x8280ff)
    for guild in self.bot.guilds:
      embed.add_field(name=guild, value=guild.id, inline=False)
    await interaction.response.send_message(embed=embed)
  
async def setup(bot):
  await bot.add_cog(Main(bot))