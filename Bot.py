import discord
import praw
import random
import asyncio
from datetime import datetime, timedelta

# Reddit API credentials
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Discord Bot Token
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"

# Discord client
client = discord.Client()

# Subreddit to fetch images from
SUBREDDIT = "memes"

# Discord Channel ID to post images
CHANNEL_ID = 1234567890  # Replace with your Discord channel ID

# Time to post the image (in 24-hour format)
POST_TIME_HOUR = 12  # Example: 12 PM
POST_TIME_MINUTE = 0  # Example: 00 minutes

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await post_image_at_specific_time()

async def post_image_at_specific_time():
    while not client.is_closed():
        # Get the current time
        now = datetime.now()
        target_time = datetime(now.year, now.month, now.day, POST_TIME_HOUR, POST_TIME_MINUTE)
        
        # Calculate the time until the target time
        delta_t = target_time - now
        if delta_t.days < 0:
            target_time += timedelta(days=1)
            delta_t = target_time - now
        
        # Wait until the target time
        await asyncio.sleep(delta_t.total_seconds())

        # Post the image
        await post_image()

async def post_image():
    channel = client.get_channel(CHANNEL_ID)
    # Get a random submission from the subreddit
    submissions = reddit.subreddit(SUBREDDIT).hot()
    post = random.choice([submission for submission in submissions])
    
    # Ensure the post is an image (you can add more checks if necessary)
    if post.url.endswith(('png', 'jpg', 'jpeg', 'gif')):
        # Post the image to Discord
        await channel.send(post.url)
        print(f"Posted {post.url} to Discord")

# Run the bot
client.run(DISCORD_TOKEN)