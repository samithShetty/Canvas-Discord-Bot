import discord
from discord import Client
from discord.ext import commands, tasks
from canvasapi import Canvas
from canvasapi.course import Course, Assignment
import datetime
import pytz
from time import perf_counter
import pandas as pd
from config import CANVAS_TOKEN

API_URL = 'https://uncc.instructure.com'

EST = pytz.timezone('US/Eastern')
CANVAS_DATE_FORMAT = r'%Y-%m-%dT%H:%M:%SZ'
OUTPUT_DATE_FORMAT = r'%A, %b %d at %I:%M %p'

class CanvasCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.canvas = Canvas(API_URL, CANVAS_TOKEN)
        self.df = pd.read_csv('pandasTest.csv')
        self.reminder_timer.start()
    

    @commands.command(aliases = ["course"])
    async def get_course(self, ctx, course_id):
        course = self.canvas.get_course(course_id)
        await ctx.send(f"The course corresponding to that code is: {course}")
    

    @commands.command(aliases = ["due", "upcoming", "assignments"])
    async def get_assignments(self, ctx, course_id, num_assignments = 5):
        start_time = perf_counter()
        embed = discord.Embed(
            description = "Retrieving upcoming assignments for course..."
        )
        message = await ctx.send(embed=embed)

        course = self.canvas.get_course(course_id)
        sorted_assignments = sorted(course.get_assignments(),key = lambda a: a.due_at if a.due_at is not None else " ")
        current_time = datetime.datetime.now()
        
        #Traverse sorted assignments until finding assignment due after current time
        assignment_index = 0
        while assignment_index < len(sorted_assignments) and (sorted_assignments[assignment_index].due_at is None or current_time > datetime.datetime.strptime(sorted_assignments[assignment_index].due_at, CANVAS_DATE_FORMAT)):
            assignment_index += 1
        #Take slice of user-specified size (or until end of list, if that comes sooner)
        upcoming_assignments = sorted_assignments[assignment_index:min(assignment_index+num_assignments,len(sorted_assignments))]
        
        
        for assignment in upcoming_assignments:
            due_date = pytz.utc.localize(datetime.datetime.strptime(assignment.due_at, CANVAS_DATE_FORMAT)) #Convert from str to datetime object
            due_date_est = due_date.astimezone(EST)#convert from default UTC to EST
            embed.add_field(name = assignment.name, value = due_date_est.strftime(OUTPUT_DATE_FORMAT), inline=False)
        embed.title = course.name
        embed.description = "Here are the upcoming due dates for this course"
        response_time = perf_counter() - start_time
        embed.set_footer(text= f"Response time: {response_time:1.3}")
        await message.edit(embed=embed)
        print(f"Successfully sent upcoming assignments for {course.name:<80} {response_time:1.3}")
    

    async def send_reminder(self, channel_id, course_id, today):
        channel = self.bot.get_channel(int(channel_id))
        course = self.canvas.get_course(int(course_id))
        due_today = []
        
        embed = discord.Embed(
            title = f"Automatic Reminder for {course.name}"
        )

        for assignment in course.get_assignments():
            if assignment.due_at:
                due_date = pytz.utc.localize(datetime.datetime.strptime(assignment.due_at, CANVAS_DATE_FORMAT)).astimezone(EST)
                if due_date.day == today.day and due_date.month == today.month and due_date.year == today.year:
                    due_today.append((assignment,due_date))
        
        for assignment in sorted(due_today,key = lambda a: a[1]):
            embed.add_field(name=assignment[0].name, value = assignment[1].strftime(OUTPUT_DATE_FORMAT), inline=False)
        
        if len(due_today) == 0:
            embed.description = "There are no assignments due today for this course"
        
        await channel.send(embed=embed)

    @tasks.loop(minutes = 1)
    async def reminder_timer(self):
        current_datetime = datetime.datetime.now().astimezone(EST)
        time = current_datetime.strftime("%H:%M")
        print(f"Checking for reminders to send at {time}")

        
        reminders_to_send = self.df[self.df["Time"] == time].itertuples()
        for reminder in reminders_to_send:
            await self.send_reminder(reminder.Channel_ID, reminder.Course_ID, current_datetime)
    

    @reminder_timer.before_loop 
    async def before_reminder(self):
        await self.bot.wait_until_ready() #Wait for bot to fully start up before starting the automatic due date reminders
    

    @commands.command(aliases = ['reminders'])
    async def list_reminders(self, ctx):
        embed = discord.Embed(
            title = "Scheduled reminders for this channel",
            description = "This channel does not currently have any scheduled due date reminders"
        )
        channel_reminders = self.df[self.df["Channel_ID"] == ctx.channel.id].itertuples()
        for reminder in channel_reminders:
            embed.add_field(name= "Name", value = reminder.Name)
            embed.add_field(name= "Time", value = reminder.Time)
            embed.add_field(name= "Course", value = self.canvas.get_course(reminder.Course_ID))
            embed.description = ''

        await ctx.send(embed=embed)
        

    @commands.command(aliases = ['add'])
    async def add_reminder(self, ctx, reminder_time, course_id, *reminder_name_args):
        name = " ".join(reminder_name_args)
        new_reminder = pd.DataFrame([[reminder_time, ctx.channel.id, course_id, name]], columns = self.df.columns)
        self.df = self.df.append(new_reminder, ignore_index = True)
        course = self.canvas.get_course(course_id)
        embed = discord.Embed(
            title =  'Successfully scheduled automatic due date reminder',
            description = f'This channel will now recieve daily due date reminders at {reminder_time} EST. To remove the reminder, use the remove_reminder command'
        )
        embed.add_field(name = 'Reminder name', value = name)
        embed.add_field(name = 'Time', value = reminder_time)
        embed.add_field(name = 'Course', value = course.name)
        await ctx.send(embed=embed)
        self.df.to_csv('pandasTest.csv', index = False)
    

    @commands.command(aliases = ['remove', 'delete'])
    async def remove_reminder(self, ctx, *name_words):
        name = " ".join(name_words)
        channel_reminders = self.df[self.df["Channel_ID"] == ctx.channel.id]
        to_be_deleted = channel_reminders[channel_reminders["Name"] == name]
        self.df = self.df.drop(to_be_deleted.index.tolist())
        
        embed = discord.Embed(
            title =  'Successfully removed automatic due date reminder',
            description = f'Removed "{name}" reminder'
        )
        await ctx.send(embed=embed)
        self.df.to_csv('pandasTest.csv', index = False)


    
def setup(bot):
    bot.add_cog(CanvasCog(bot))
    print("Canvas Cog successfully loaded")