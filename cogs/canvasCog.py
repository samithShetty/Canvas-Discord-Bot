import discord
from discord.ext import commands

class canvasCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
def setup(bot):
    bot.add_cog(canvasCog(bot))
    print("Canvas Cog successfully loaded")