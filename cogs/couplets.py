import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension
from discord import app_commands


class Couplets(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Couplets cog loaded.")

    @app_commands.command(name="貼春聯", description='在頻道名稱後方加上 "春" 或 "福"')
    async def 貼春聯(self, interaction: discord.Interaction):
        name = interaction.channel.name
        if name.endswith("⟨春⟩") or name.endswith("⟨福⟩"):
            await interaction.response.send_message("已經貼過了呦", ephemeral=True)
        else:
            couplets = random.randint(0, 1)
            if couplets == 0:
                await interaction.channel.edit(name=name + "⟨春⟩")
            else:
                await interaction.channel.edit(name=name + "⟨福⟩")
            await interaction.response.send_message("(貼")

    @app_commands.command(name="撕春聯", description="把頻道名稱後方的春聯撕起來")
    async def 撕春聯(self, interaction: discord.Interaction):
        name = interaction.channel.name
        length = len(name)
        if name.endswith("⟨春⟩") or name.endswith("⟨福⟩"):
            name = name[:length-3]
            await interaction.channel.edit(name=name)
            await interaction.response.send_message("(撕")
        else:
            await interaction.response.send_message("沒有春聯可以撕喔", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Couplets(bot))
