import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(HelpCog(bot))
    print("Help Cog successfully loaded")