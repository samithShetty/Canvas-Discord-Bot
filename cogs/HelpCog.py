import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "Help", description = "Use >help <command> for information on that command.", color = ctx.author.color)

        em.add_field(name = "General commands", value = "get_assignments, get_courses")
        em.add_field(name = "Announcement commands", value = "add_announcement, remove_announcement, list_announcements")
        em.add_field(name = "Reminder commands", value = "add_reminder, remove_reminder, list_reminders")

        await ctx.send(embed = em)

    @help.command()
    async def add_reminder(self, ctx):
        em = discord.Embed(title = "Add Reminder", description = "Adds a reminder", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">add_reminder <reminder_time> <course_code> <reminder_name>")
        em.add_field(name = "Variables:", value = "*reminder_time*: hh:mm 24 hour format\n*course_code*: go to course page and copy code from url (uncc.instructure.com/courses/######)\n*reminder_name*: type in a name for the reminder", inline= False)
        em.add_field(name = "Aliases:", value = ">add")
        await ctx.send(embed = em)
    
    @help.command()
    async def add_announcement(self, ctx):
        em = discord.Embed(title = "Add Announcement", description = "Subscribes a channel to a Canvas course for announcements", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">add_announcement <course_code>")
        em.add_field(name = "Variables:", value = "*course_code*: Use >get_courses", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def get_assignments(self, ctx):
        em = discord.Embed(title = "Get Assignments", description = "Lists assignments", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">get_assignments <course_code> <num_assignments>")
        em.add_field(name = "Variables:", value = "*course_code*: use >get_courses\n*num_assignments*: type in the number assignments you want to see, default of 5", inline= False)
        em.add_field(name = "Aliases:", value = ">due, >upcoming, >assignments")
        await ctx.send(embed = em)

    @help.command()
    async def get_courses(self, ctx):
        em = discord.Embed(title = "Get Course", description = "Displays all courses along with corresponding codes that the bot has access to", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">get_course <course_code>")
        em.add_field(name = "Aliases:", value = ">courses")
        await ctx.send(embed = em)

    @help.command()
    async def list_reminders(self, ctx):
        em = discord.Embed(title = "List Reminders", description = "Displays current scheduled reminders in this channel", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">list_reminders")
        em.add_field(name = "Aliases:", value = ">reminders", inline= False)
        await ctx.send(embed = em)
    
    @help.command()
    async def list_announcements(self, ctx):
        em = discord.Embed(title = "List Announcements", description = "Displays current Canvas course announcement subscriptions in this channel", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">list_announcements")
        em.add_field(name = "Aliases:", value = ">announcements", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def remove_reminder(self, ctx):
        em = discord.Embed(title = "Remove Reminder", description = "Removes a reminder", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">remove_reminder <reminder_name>")
        em.add_field(name = "Variables:", value = "*reminder_name*: type in the name of the reminder you want to remove", inline= False)
        em.add_field(name = "Aliases:", value = ">remove, >delete")
        await ctx.send(embed = em)
    
    @help.command()
    async def remove_announcements(self, ctx):
        em = discord.Embed(title = "Remove Announcements", description = "Removes an announcement", color = ctx.author.color)
        em.add_field(name = "How to use:", value = ">remove_announcement <course_code>")
        em.add_field(name = "Variables:", value = "*course_code*: use >get_courses to get the course code of the announcement you want to remove", inline= False)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(HelpCog(bot))
    print("Help Cog successfully loaded")