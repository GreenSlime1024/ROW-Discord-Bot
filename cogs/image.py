from pickletools import anyobject
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord import app_commands

with open("image.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Image(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Image cog loaded.")

    @app_commands.command(name="image", description="check image from database")
    async def image(self, interaction: discord.Interaction, name: str):
        await interaction.response.send_message(jdata[name])

    @app_commands.command(name="add-image", description="add image to database")
    async def addimage(self, interaction: discord.Interaction, name: str, url: str):
        with open("image.json", "w", encoding="utf8") as jfile:
            jdata[name] = url
            json.dump(jdata, jfile, ensure_ascii=False, indent=4)
        await interaction.response.send_message(f"add `{name}` successfully")

    @app_commands.command(name="check-images-name", description="check all images" names in database")
    async def names(self, interaction: discord.Interaction):
        keys = jdata.keys()
        names = ""
        for i in keys:
            names += (f"`{i}` ")
        await interaction.response.send_message(names)


async def setup(bot):
    await bot.add_cog(Image(bot))
