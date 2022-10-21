import csv
from time import time
import praw

def scrape():

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


