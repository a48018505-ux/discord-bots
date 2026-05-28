from discord.ext import commands
from discord import app_commands
import discord
from datetime import timedelta

class Moderation(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @app_commands.command(
        name="ban",
        description="Ban member"
    )
    @app_commands.checks.has_permissions(
        ban_members=True
    )
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason"
    ):

        await member.ban(
            reason=reason
        )

        await interaction.response.send_message(
            f"🔨 Banned {member.mention}"
        )

    @app_commands.command(
        name="kick",
        description="Kick member"
    )
    @app_commands.checks.has_permissions(
        kick_members=True
    )
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason"
    ):

        await member.kick(
            reason=reason
        )

        await interaction.response.send_message(
            f"👢 Kicked {member.mention}"
        )

    @app_commands.command(
        name="mute",
        description="Mute member"
    )
    @app_commands.checks.has_permissions(
        moderate_members=True
    )
    async def mute(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        minutes: int
    ):

        await member.timeout(
            timedelta(minutes=minutes)
        )

        await interaction.response.send_message(
            f"🔇 Muted {member.mention}"
        )

async def setup(bot):

    await bot.add_cog(
        Moderation(bot)
    )