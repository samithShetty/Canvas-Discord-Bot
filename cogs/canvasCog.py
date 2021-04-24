import discord
from discord.ext import commands
from canvasapi import Canvas
from canvasapi.course import Course, Assignment
import datetime
import pytz
from time import perf_counter
from config import CANVAS_TOKEN

API_URL = 'https://uncc.instructure.com'

EST = pytz.timezone('US/Eastern')
CANVAS_DATE_FORMAT = r'%Y-%m-%dT%H:%M:%SZ'
OUTPUT_DATE_FORMAT = r'%A, %b %d at %I:%M %p'

class CanvasCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.canvas = Canvas(API_URL, CANVAS_TOKEN)
    
    @commands.command(aliases = ["course"])
    async def getCourse(self, ctx, course_code):
        course = self.canvas.get_course(course_code)
        await ctx.send(f"The course corresponding to that code is: {course}")
    
    @commands.command(aliases = ["due", "upcoming", "assignments"])
    async def getAssignments(self, ctx, course_code, num_assignments = 5):
        start_time = perf_counter()
        course = self.canvas.get_course(course_code)
        sorted_assignments = sorted(course.get_assignments(),key = lambda a: a.due_at if a.due_at is not None else " ")
        current_time = datetime.datetime.now()
        
        #Traverse sorted assignments until finding assignment due after current time
        assignment_index = 0
        while assignment_index < len(sorted_assignments) and (sorted_assignments[assignment_index].due_at is None or current_time > datetime.datetime.strptime(sorted_assignments[assignment_index].due_at, CANVAS_DATE_FORMAT)):
            assignment_index += 1
        #Take slice of user-specified size (or until end of list, if that comes sooner)
        upcoming_assignments = sorted_assignments[assignment_index:min(assignment_index+num_assignments,len(sorted_assignments))]
        
        embed = discord.Embed(
            title = course.name,
            description = "Here are the upcoming due dates for this course:"
        )
        for assignment in upcoming_assignments:
            due_date = pytz.utc.localize(datetime.datetime.strptime(assignment.due_at, CANVAS_DATE_FORMAT)) #Convert from str to datetime object
            due_date_est = due_date.astimezone(EST)#convert from default UTC to EST
            embed.add_field(name = assignment.name, value = due_date_est.strftime(OUTPUT_DATE_FORMAT), inline=False)
        response_time = perf_counter() - start_time
        embed.set_footer(text= f"Response time: {response_time:1.3}")
        await ctx.send(embed=embed)
        print(f"Successfully sent upcoming assignments for {course.name:<80} {response_time:1.3}")
    
def setup(bot):
    bot.add_cog(CanvasCog(bot))
    print("Canvas Cog successfully loaded")