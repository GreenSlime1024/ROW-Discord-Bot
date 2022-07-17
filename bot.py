import discord
import json
import os
from discord.ext import commands
from discord_slash import SlashCommand


with open('not_token.json', mode='r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='r!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
  print('>>Bot is online<<')

@slash.slash()
async def load(ctx, extension):
  '''
  非開發人員請勿亂用
  '''
  bot.load_extension(f'cmds.{extension}')
  await ctx.send(f'已載入 [{extension}] :white_check_mark:')

@slash.slash()
async def unload(ctx, extension):
  '''
  非開發人員請勿亂用
  '''
  bot.unload_extension(f'cmds.{extension}')
  await ctx.send(f'已卸載 [{extension}] :white_check_mark:')

@slash.slash()
async def reload(ctx, extension):
  '''
  非開發人員請勿亂用
  '''
  bot.reload_extension(f'cmds.{extension}')
  await ctx.send(f'已重載 [{extension}] :white_check_mark:')

@bot.event
async def on_command_error(ctx, error):
 await ctx.send(error)

for filename in os.listdir('./cmds'):
  if filename.endswith('.py'):
    bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
  bot.run(jdata['TOKEN'])