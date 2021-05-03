import discord
from discord.ext import commands
import os
from config import DISCORD_TOKEN

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
bot = commands.Bot(command_prefix=">", intents=intents)


@bot.event
async def on_ready():
    print('Successfully logged in and booted')


bot.remove_command("help")

# Automatically load all the cogs on startup
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            print(f'Error loading cog {filename}:\n{e}')

bot.run(DISCORD_TOKEN)
