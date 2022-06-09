import discord
from discord.ext import commands
import json
import keep_alive
import os

with open('setting.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='r! ', intents=intents)

@bot.event
async def on_ready():
  print('>>Bot is online<<')
  #activity = discord.Activity(type=discord.ActivityType.listening, name="音樂")
  #await bot.change_presence(status=discord.Status.dnd, activity=activity)

@bot.command()
async def load(ctx, extension):
  '''
  非開發人員請勿亂用
  '''
  bot.load_extension(f'cmds.{extension}')
  await ctx.reply(f'已載入 [{extension}] :white_check_mark:', mention_author=False)

@bot.command()
async def unload(ctx, extension):
  '''
  非開發人員請勿亂用
  '''
  bot.unload_extension(f'cmds.{extension}')
  await ctx.reply(f'已卸載 [{extension}] :white_check_mark:', mention_author=False)

@bot.command()
async def reload(ctx, extension):
  '''
  非開發人員請勿亂用
  '''
  bot.reload_extension(f'cmds.{extension}')
  await ctx.reply(f'已重載 [{extension}] :white_check_mark:', mention_author=False)

@bot.event
async def on_command_error(ctx, error):
 await ctx.reply(error, mention_author=False)

for filename in os.listdir('./cmds'):
  if filename.endswith('.py'):
    bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(jdata['TOKEN'])