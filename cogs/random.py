import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from discord import app_commands


with open("ball.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Random(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Random cog loaded.")

    @app_commands.command(name="Magic 8 ball", description="ask Magic 8 ball a question")
    async def Magic_8_ball(self, interaction: discord.Interaction, question: str):
        random_ball = random.choice(jdata["ball"])
        if random_ball == "https://cdn.discordapp.com/attachments/887330126147256323/919167797240688680/81235.png":
            await interaction.response.send_message("idk but I Never Gonna Give You Up")
        await interaction.response.send_message(random_ball)

    @app_commands.command(name="pa", description="estimate the probability of occurrence of the event")
    async def pa(self, interaction: discord.Interaction, question: str):
        rate = random.randint(0, 100)
        await interaction.response.send_message(f"I estimate the probability of **{question}** is **{rate}%**")


async def setup(bot):
    await bot.add_cog(Random(bot))
