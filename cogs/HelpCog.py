import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "Help", description = "Use >help <command> for information on that command.", color = ctx.author.color)

        em.add_field(name = "Canvas commands", value = "add_reminder, get_assignments, get_course, list_reminders, remove_reminder")

        await ctx.send(embed = em)

    @help.command()
    async def add_reminder(self, ctx):
        em = discord.Embed(title = "Add Reminder", description = "Adds a reminder", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">add_reminder <reminder_time> <course_code> <reminder_name>")
        em.add_field(name = "Variables:", value = "*reminder_time*: hh:mm 24 hour format\n*course_code*: got to course page and copy code from url (uncc.instructure.com/courses/######)\n*reminder_name*: type in a name for the reminder", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def get_assignments(self, ctx):
        em = discord.Embed(title = "Get Assignments", description = "Lists assignments", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">get_assignments <course_code> <num_assignments>")
        em.add_field(name = "Variables:", value = "*course_code*: got to course page and copy code from url (uncc.instructure.com/courses/######)\n*num_assignments*: type in the number assignments you want to see, default of 5", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def get_course(self, ctx):
        em = discord.Embed(title = "Get Course", description = "Displays corresponding course to inputted course code", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">get_course <course_code>")
        em.add_field(name = "Variables:", value = "*course_code*: got to course page and copy code from url (uncc.instructure.com/courses/######)", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def list_reminders(self, ctx):
        em = discord.Embed(title = "List Reminders", description = "Display current reminders", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">list_reminders")
        await ctx.send(embed = em)

    @help.command()
    async def remove_reminder(self, ctx):
        em = discord.Embed(title = "Remove Reminder", description = "Removes a reminder", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">add_reminder <reminder_name>")
        em.add_field(name = "Variables:", value = "*reminder_name*: type in the name of the reminder you want to remove", inline= False)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(HelpCog(bot))
    print("Help Cog successfully loaded")