# Encryption's Discord Reddit Bot

## Details:
Encryption:     Dong-Ha Nguyen
Date:           March 18, 2024
System:         MacOS

## Overview
This project is a Discord bot written in Python that fetches images from Reddit and posts them to a designated Discord channel.

## Features
- Fetches images from a specified subreddit on Reddit.
- Posts images to a designated Discord channel.
- Runs automatically at a specified time each day.

## Requirements
- Python 3.x
- PRAW (Python Reddit API Wrapper)
- Discord.py

## API Set Up
1. Get API Key: API Key
https://www.reddit.com/prefs/apps
Info:
Name:           DiscordPoster
Description:    Discord Bot to post images to certain channels created by Encryption 2024
About Url:      http://localhost:8080
Redirect Url:   http://localhost:8080

2. https://support.reddithelp.com/hc/en-us/requests
What do you need assistance with?                           API Support and Inquires
From what position are you reaching out for support?        I'm a developer
What is your inquiry?                                       Register to use free tier of API
Purpose?                                                    Academic
Reddit API Use Case                                         Bot to post daily images
Developer Platform                                          Web App
OAUTH Client ID(s)                                          {Step 1}

## Setup
1. Download python 3 to local machine
2. Clone this repository to your local machine.
3. Install the required Python packages:
   ```
   pip install praw discord.py
   python3 -m pip install praw
   ```
   Or
   ```
   python3 -m pip install -r requirements.txt
   ```
4. Obtain credentials from Reddit and Discord for API access.
5. Replace the placeholders in the script (`YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, `YOUR_USER_AGENT`, `YOUR_DISCORD_BOT_TOKEN`, `CHANNEL_ID`) with your actual credentials.
6. Adjust the subreddit and Discord channel settings as needed.
7. Run the script:
   ```
   python bot.py
   ```
