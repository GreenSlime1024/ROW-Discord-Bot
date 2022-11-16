import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord import app_commands
import os

with open("channel.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Admin(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin cog loaded.")

    @commands.is_owner()
    @app_commands.command()
    async def set_order_channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        jdata["wool_channel"] = channel.id
        with open("channel.json", mode="w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
        self.channel = self.bot.get_channel(channel.id)
        await interaction.response.send_message(f"wool channel set to {self.channel.mention}.", ephemeral=True)

    @commands.is_owner()
    @app_commands.command()
    async def set_trade_channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        with open("channel.json", mode="r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        jdata["Trade_channel"] = channel.id
        with open("channel.json", mode="w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
            self.channel = self.bot.get_channel(channel.id)
            await interaction.response.send_message(f"trade channel set to {self.channel.mention}.", ephemeral=True)
            
    @commands.is_owner()
    @app_commands.command()
    async def say(self, interaction: discord.Interaction, msg:str):
        await interaction.channel.send(msg)
        await interaction.response.send_message(f"message sended", ephemeral=True)

    @commands.is_owner()
    @commands.command()
    async def sync(self, ctx):
        fmt = await ctx.bot.tree.sync()
        await ctx.reply(f"synced {len(fmt)} commands")

    @commands.is_owner()
    @app_commands.command()
    async def system(self, interaction: discord.Interaction, command: str):
        os.system(command)
        await interaction.response.send_message(f"`{command}` sended", ephemeral=False)

    @commands.is_owner()
    @app_commands.command()
    async def load(self, interaction: discord.Interaction, extension: str):
        await self.bot.load_extension(f"cogs.{extension}")
        await interaction.response.send_message(f"loaded `{extension}`", ephemeral=False)

    @commands.is_owner()
    @app_commands.command()
    async def reload(self, interaction: discord.Interaction, extension: str):
        await self.bot.reload_extension(f"cogs.{extension}")
        await interaction.response.send_message(f"reloaded `{extension}`", ephemeral=False)

    @commands.is_owner()
    @app_commands.command()
    async def unload(self, interaction: discord.Interaction, extension: str):
        await self.bot.unload_extension(f"cogs.{extension}")
        await interaction.response.send_message(f"unloaded `{extension}`", ephemeral=False)


async def setup(bot):
    await bot.add_cog(Admin(bot))
