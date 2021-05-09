# Canvas-Discord-Bot
A Canvas-integration Bot application for the Discord messaging app.

This bot is self-hosted and runs off of your own individual Canvas API key to access your Canvas courses. Anybody in a server with the bot can use its commands, but it can only access the courses that the canvas account associated with the API key has access to.

See below for instructions on how to clone repo and configure your own instance of the bot.

Developed by Samith Shetty, Marx Costanzo, Himeth Jayakody, and Samir Appikatla as the final project for ITSC 3155 Intro to Software Engineering at UNC Charlotte

## Bot Functionality
### Available Commands
By default, all commands will be prefixed with the `>` symbol, but this can be changed in [main.py](main.py)
- **General Commands**
  - `help` provides information on available commands and usage
  - `get_courses` provides course codes for all available courses that the bot can access
  - `get_assignments` lists upcoming due dates for a given course
- **Announcement Commands**
  - `add_anouncement` subscribes a Discord channel for announcements from a given Canvas course
  - `remove_announcement` removes a subscription to a given Canvas course
  - `list_announcements` lists all announcement subscriptions for that Discord channel
- **Reminder Commands**
  - `add_reminder` creates a reoccuring daily reminder for assignments due each day 
  - `remove_reminders` deletes a daily reminder
  - `list_reminders` llists all daily reminders for the Discord channel

### Announcements
Announcements are a crucial way for teachers to communicate with students using Canvas. This bot provides a way for users to see announcements in Discord itself whenever they are posted.

Announcement in Canvas

![Announcement in Canvas](https://i.ibb.co/cvmxtdx/Canvas-Announcement.png)

Announcement automatically sent in Discord

![Announcement in Discord](https://i.ibb.co/X4L40Bm/Discord-Announcement.png)

Announcement subscriptions are channel-specific, so you can subscribe different channels (across different servers) to different courses.

To setup announcements in a Discord channel, use the `add_announcement` command.

### Reminders
The bot is also capable of providing assignment reminders the day they are due. These are called _Reminders_, and they behave similarly to announcements as they are also channel-specific, and come with similar commands for setup and configuration, although reminders are set to run at a specific time everyday.

Reminders set to post daily due date reminders for a Software Engineering course at 3:15

![Example Reminder](https://user-images.githubusercontent.com/71335825/117584228-b53d0900-b0d9-11eb-8d4c-21c2f8bdf10b.PNG)

To setup reminders in a Discord channel, use the `add_reminder` command.
