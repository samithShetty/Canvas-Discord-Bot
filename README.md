# Canvas-Discord-Bot
A Canvas-integration Bot application for the Discord messaging app.

This bot is self-hosted and runs off of your own individual Canvas API key to access your Canvas courses. Anybody in a server with the bot can use its commands, but it can only access the courses that the canvas account associated with the API key has access to.

See below for instructions and resources to help you configure your own instance of the bot.

Developed by Samith Shetty, Marx Costanzo, Himeth Jayakody, and Samir Appikatla as the final project for ITSC 3155 Intro to Software Engineering at UNC Charlotte

## Bot Functionality
### Available Commands
By default, all commands will be prefixed with the `>` symbol, but this can be changed in [main.py](main.py)
- **General Commands**
  - `help` provides information on available commands and usage
  - `get_courses` provides course codes for all available courses that the bot can access
  - `get_assignments` lists upcoming due dates for a given course
- **[Announcement](https://github.com/MCost02/Canvas-Discord-Bot/blob/main/README.md#announcements) Commands**
  - `add_anouncement` subscribes a Discord channel for announcements from a given Canvas course
  - `remove_announcement` removes a subscription to a given Canvas course
  - `list_announcements` lists all announcement subscriptions for that Discord channel
- **[Reminder](https://github.com/MCost02/Canvas-Discord-Bot/blob/main/README.md#reminders) Commands**
  - `add_reminder` creates a reoccuring daily reminder for assignments due each day 
  - `remove_reminders` deletes a daily reminder
  - `list_reminders` lists all daily reminders for the Discord channel

### Announcements
Announcements are a crucial way for teachers to communicate with students using Canvas. This bot provides a way for users to see announcements in Discord itself whenever they are posted.

Announcement in Canvas

![Announcement in Canvas](https://i.ibb.co/cvmxtdx/Canvas-Announcement.png)

Announcement automatically sent in Discord

![Announcement in Discord](https://i.ibb.co/X4L40Bm/Discord-Announcement.png)

Announcement subscriptions are channel-specific, so you can subscribe different channels (across different servers) to different courses.

To setup announcements in a Discord channel, use the `add_announcement` command.

### Reminders
The bot also allows users to subscribe to courses for daily due date reminders. These are called _Reminders_, and they behave similarly to announcements as they are also channel-specific, and come with similar commands for setup and configuration, although reminders are set to run at a specific time everyday.

Reminders set to post daily due date reminders for a Software Engineering course at 3:15

![Example Reminder](https://user-images.githubusercontent.com/71335825/117584228-b53d0900-b0d9-11eb-8d4c-21c2f8bdf10b.PNG)

To setup reminders in a Discord channel, use the `add_reminder` command.

## Setting up your own instance of the Bot
Since the bot can only run on an individual API Key, users can only set up a working bot for their own Canvas courses. **[Note:](https://canvas.instructure.com/doc/api/file.oauth.html#manual-token-generation)** Collecting user API keys to access many different students' courses is against Canvas terms of service. The only proper way to make the bot function for many different people is to get a [Developer Key](https://canvas.instructure.com/doc/api/file.developer_keys.html) from your institution. 

So, rather than trying to use our bot (which has can't access your courses), you can create your own Discord Bot and run it with the code in this repository, using your own API keys instead. To do this you will need to:
### 1. Clone this repository
You can type `git clone https://github.com/MCost02/Canvas-Discord-Bot.git` in your command line or download from the main page of the repo. (Temporary) You'll need to clear the csv files except for the first line so that you can have your own reminders rather than that of this template bot.
### 2. Generate a Canvas API token
Here is a [step-by-step tutorial](https://community.canvaslms.com/t5/Student-Guide/How-do-I-manage-API-access-tokens-as-a-student/ta-p/273) to generate an API key for your Canvas account. Remember to save the token code, as we'll need it later.
### 3. Create a Discord Bot
Here is a [tutorial](https://discordpy.readthedocs.io/en/latest/discord.html) to create the actual Bot account in Discord. This will be the account that send messages and interacts with the user, so you can customize the name and profile picture however you see fit. Remember to save this token as well.
### 4. Create a Heroku account and application to host your bot for free
This step will be the most tedious, so be patient. You can follow the first part of this [tutorial](https://www.youtube.com/watch?v=BPvg9bndP1U&ab_channel=TechWithTim) to set up an account and application, but the Procfile, requirements.txt, and runtime.txt files have already been created. Instead of running `git init`, run the command `git remote add heroku <your heroku git link>`.
### 5. Enter the API keys from Canvas and Discord into Heroku and add Buildpack
In your Heroku app dashboard, go to the Settings Tab and scroll the to Config Vars section. This is where you will put your API keys from earlier, under the names `CANVAS` and `DISCORD` respectively (this is case-sensitive). Right below this should be the buildpack sections, where you should click the "Add Buildpack" button and select Python.
### 6. Activate the bot in Heroku and enjoy
If the bot isn't working as intended, you can check the logs from your Heroku dashboard to see what went wrong.
