import discord
from discord.ext import commands
import asyncio
import os
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print('Successfully logged in and booted')

bot.remove_command("help")

async def main():
    # Automatically load all the cogs on startup
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
            except Exception as e:
                print(f'Error loading cog {filename}:\n{e}')
    await bot.start(DISCORD_TOKEN)

asyncio.run(main())