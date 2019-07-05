import configparser
import praw
import sys
from decimal import Decimal


submission_id = None

def get_reddit(config):
    client_id = config.get('Reddit', 'client_id')
    client_secret = config.get('Reddit', 'client_secret')
    username = config.get('Reddit', 'username')
    password = config.get('Reddit', 'password')
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent='toy bot v1.0 by /u/spoosman')
    return reddit

def create_poll(reddit):
    title = 'TEST2'
    selftext = 'empty selftext'
    submission = reddit.subreddit('spoosman').submit(title, selftext=selftext)
    global submission_id
    submission_id = submission.id

def get_comments(reddit):
    comments = []
    prev_submission = reddit.submission(id='c98ywk')

    # TODO add error handling
    for top_level_comment in prev_submission.comments:
        lines = top_level_comment.body.splitlines()

        # TODO
        # check lines is at least 1 length
        # check line contains ES:
        # remove empty space before/after
        # parse to decimal or float or something
        for line in lines:
            hello = line.split('Hello:')
            if len(hello) > 1:
                try:
                    price = Decimal(hello[1])
                    comments.append( {'user': top_level_comment.author.name, 'price': price})
                except Exception as e:
                    print(e)

    return comments


def announce_winner(comments):
    winner = max(comments, key=lambda x: x['price'])
    print(winner)

def get_config():
    config_path = sys.argv[1] if len(sys.argv) > 1 else '../config.ini'
    config_parser = configparser.ConfigParser()
    config_parser.read(config_path)
    return config_parser

def main():
    config = get_config()
    reddit = get_reddit(config)
    # create_poll(reddit)
    comments = get_comments(reddit)
    announce_winner(comments)


if __name__== "__main__":
    main()
