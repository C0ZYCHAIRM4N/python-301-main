# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

from flask import Flask, render_template, jsonify
import os
import praw

app = Flask(__name__)

# Fetch credentials from environment variables
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')


# Create a Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Function to fetch posts from subreddits
def fetch_posts(subreddits, limit=10):
    posts = []
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.hot(limit=limit):
            posts.append({
                'title': submission.title,
                'url': submission.url,
                'score': submission.score,
                'comments': submission.num_comments
            })
    return posts

@app.route('/')
def index():
    # Example subreddits
    subreddits = ['recipes', 'food']
    posts = fetch_posts(subreddits)
    return render_template('index.html', posts=posts)

@app.route('/api/posts', methods=['GET'])
def api_posts():
    subreddits = ['recipes', 'food']  # Change to your preferred subreddits
    posts = fetch_posts(subreddits)
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
