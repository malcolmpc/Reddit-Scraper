import pandas as pd
import praw
import textstat
import os
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()
AGENT = os.getenv('USER_AGENT')
CLIENT = os.getenv('CLIENT_ID')
SECRET = os.getenv('CLIENT_SECRET')

reddit = praw.Reddit(user_agent=AGENT,
                     client_id=CLIENT, client_secret=SECRET)

posts = []
for submission in reddit.subreddit("nba").new():
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        posts.append(top_level_comment.body)

print(textstat.flesch_kincaid_grade(posts[1]))
