# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import os
import praw

# Set up Reddit credentials (use environment variables for security)
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Define the subreddit to fetch recipes from
subreddit_name = 'recipes'

# Fetch the top 10 posts from the subreddit
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(limit=10)

# Process and display the recipes
for post in top_posts:
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"URL: {post.url}")
    print(f"Selftext: {post.selftext[:500]}...")  # Print the first 500 characters of the post
    print("-" * 40)

