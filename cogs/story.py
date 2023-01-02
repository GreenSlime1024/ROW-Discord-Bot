import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension
from discord import app_commands
import json
import random

with open("story.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Story(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Story cog loaded.")

    @app_commands.command(name="講故事", description="講故事")
    async def 講故事(self, interaction: discord.Interaction):
        stories = jdata["stories"]
        random_story = random.choice(stories)
        await interaction.response.send_message(random_story)
        
    @commands.is_owner()
    @app_commands.command(name="加故事", description="添加故事到故事庫")
    async def addimage(self, interaction: discord.Interaction, story: str):
        stories = jdata["stories"]
        stories.append(story)
        with open("story.json", "w", encoding="utf8") as jfile:
            jdata["stories"] = stories
            json.dump(jdata, jfile, ensure_ascii=False, indent=4)
        await interaction.response.send_message(f"add story successfully")


async def setup(bot):
    await bot.add_cog(Story(bot))