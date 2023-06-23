import praw 
user_agent = "https://github.com/apoorvapendse";
reddit = praw.Reddit(
    client_id="axhrfHILsS7sSnVWeP4CVA",
    client_secret="ApvM3QXdvH1z30oppvjhPN8upqFD_Q",
    user_agent = user_agent
)

redditPosts = [];

headlines = set()
for submission in reddit.subreddit("politics").hot(limit=10):
    
    redditPosts.append({submission.title,submission.upvote_ratio})

for post in redditPosts:
    print(post);