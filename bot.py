import discord
import json
import os
from discord.ext import commands
from discord_slash import SlashCommand


with open('not_token.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='r!', intents=intents, owner_id = 1022080471506624545)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
  print('I am running!')

@slash.slash(name='load', description='load')
@commands.is_owner()
async def load(ctx, extension):
  bot.load_extension(f'cmds.{extension}')
  await ctx.send(f'已載入 **{extension}** ')

@slash.slash(name='unload', description='unload')
@commands.is_owner()
async def unload(ctx, extension):
  bot.unload_extension(f'cmds.{extension}')
  await ctx.send(f'已卸載 **{extension}** ')

@slash.slash(name='reload', description='reload')
@commands.is_owner()
async def reload(ctx, extension):
  bot.reload_extension(f'cmds.{extension}')
  await ctx.send(f'已重載 **{extension}** ')

@bot.event
async def on_command_error(ctx, error):
 await ctx.send(error)

for filename in os.listdir('./cmds'):
  if filename.endswith('.py'):
    bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
  bot.run(jdata['TOKEN'])