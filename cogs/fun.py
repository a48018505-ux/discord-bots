from discord.ext import commands
from discord import app_commands
import discord
import random

class Fun(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Ping command"
    )
    async def ping(
        self,
        interaction: discord.Interaction
    ):

        latency = round(
            self.bot.latency * 1000
        )

        await interaction.response.send_message(
            f"🏓 Pong! {latency}ms"
        )

    @app_commands.command(
        name="dice",
        description="Roll dice"
    )
    async def dice(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_message(
            f"🎲 {random.randint(1,6)}"
        )

async def setup(bot):

    await bot.add_cog(
        Fun(bot)
    )