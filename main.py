import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# ---------------- LOAD COGS ---------------- #

async def load_cogs():

    for file in os.listdir("./cogs"):

        if file.endswith(".py"):

            await bot.load_extension(
                f"cogs.{file[:-3]}"
            )

# ---------------- READY ---------------- #

@bot.event
async def on_ready():

    try:

        synced = await bot.tree.sync()

        print(f"✅ Logged in as {bot.user}")
        print(f"✅ Synced {len(synced)} commands")

    except Exception as e:

        print(f"❌ Sync Error: {e}")

# ---------------- MAIN ---------------- #

async def main():

    async with bot:

        await load_cogs()

        await bot.start(
            os.getenv("TOKEN")
        )

asyncio.run(main())