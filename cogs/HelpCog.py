import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "Help", description = "Use >help <command> for information on that command.", color = ctx.author.color)

        em.add_field(name = "Canvas commands", value = "add_reminder, get_assignments, get_course, list_reminders, printdf, remove_reminder")

        await ctx.send(embed = em)

    @help.command()
    async def add_reminder(self, ctx):
        em = discord.Embed(title = "Add Reminder", description = "Adds a reminder", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">add_reminder <reminder_time> <course_code> <reminder_name>")
        em.add_field(name = "Variables:", value = "*reminder_time*: hh:mm 24 hour format\n*course_code*: got to course page and copy code from url (uncc.instructure.com/courses/######)\n*reminder_name*: type in a name for the reminder", inline= False)
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(HelpCog(bot))
    print("Help Cog successfully loaded")