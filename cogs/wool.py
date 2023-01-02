import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json
from discord import app_commands
from typing import List
from typing import Literal

with open("channel.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Wool(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print("Wool cog loaded.")

    @app_commands.command(name="wool", description="order some wool")
    async def wool(self, interaction: discord.Interaction, color: Literal["白色", "紅色", "粉紅色", "橙色", "黃色", "淺綠色", "綠色", "青色", "淺藍色", "藍色", "洋紅色", "紫色", "淺灰色", "灰色", "棕色", "黑色"], 大箱: int, 小箱: int, 交貨方式: str, 備註: str):
        channel = self.bot.get_channel(int(jdata["wool_channel"]))
        price = 大箱*8640+小箱*4320
        embed = discord.Embed(title="$羊毛訂購單$", color=0x8280ff,
                              timestamp=datetime.datetime.utcnow())
        embed.set_author(name=interaction.user,
                         icon_url=interaction.user.display_avatar)
        embed.add_field(name="顏色", value=color, inline=False)
        embed.add_field(name="數量", value=(f"{大箱} 大箱 {小箱} 小箱"), inline=False)
        embed.add_field(name="交貨方式", value=交貨方式, inline=False)
        embed.add_field(name="備註", value=備註, inline=False)
        embed.add_field(name="價格", value=(f"未來幣 {price} 元"), inline=False)
        embed.set_footer(text="a")

        await channel.send(embed=embed)
        await interaction.response.send_message(f"訂購成功!", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Wool(bot))
