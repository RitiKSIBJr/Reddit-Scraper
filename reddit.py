import csv
from time import time
import praw

def scrape():
    my_client_id = "5CYkvE-CSc7cxOhQvUCzeQ"
    my_client_secret = "hTgsGSNs_j78NKfHEKv2vOxWXkr_kg"
    my_user_agent = "Scraper 1.0"
    reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)

    for submission in reddit.subreddit('learnpython').hot(limit=None):
        title =     submission.title
        author = submission.author
        created_date = submission.created_utc
        url = submission.url

     
        reddit_posts= {"title":title, "author":author, "created_date":created_date, "url":url}
        
        posts = []
        posts.append(reddit_posts)

        with open("posts.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "created_date", "url"])

            for post in posts:

                writer.writerow(post)

        

if __name__ == "__main__":
    scrape()


## Manage duplicate post in the post.csv