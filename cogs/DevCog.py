import discord
from discord.ext import commands

DEV_IDS = [255070353926127628, 187587747110846464, 685291675106410507]

def is_dev(ctx):
    return ctx.message.author.id in DEV_IDS

class DevCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong.')


    @commands.command()
    @commands.check(is_dev)
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded {extension}')


    @commands.command()
    @commands.check(is_dev)
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded {extension}')


    @commands.command()
    @commands.check(is_dev)
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded {extension}')    


    @commands.command(aliases = ["66"])
    @commands.check(is_dev)
    async def execute(self, ctx):
        await ctx.send("Entering execute mode, the bot will now be unable to respond to commands. Insert statements to be executed in terminal, type \"break\" in terminal to exit.")
        while(True):
            inp = input("> ")
            if inp.lower() != 'break':
                try:
                    exec(inp)
                except Exception as e:
                    print(e)
            else:
                break
        print("Execution mode has been halted from terminal. Now resuming normal bot functions...")
        await ctx.send("Execution mode has been halted from terminal. Now resuming normal bot functions...")



def setup(bot):
    bot.add_cog(DevCog(bot))
    print("Developer Cog successfully loaded")