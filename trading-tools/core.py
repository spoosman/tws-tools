import praw
from decimal import Decimal
from config import CONFIG

submission_id = None


def get_reddit():
    client_id = CONFIG.get('Reddit', 'client_id')
    client_secret = CONFIG.get('Reddit', 'client_secret')
    username = CONFIG.get('Reddit', 'username')
    password = CONFIG.get('Reddit', 'password')
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

def main():
    print('asf')
    reddit = get_reddit()
    # create_poll(reddit)
    # comments = get_comments(reddit)
    # announce_winner(comments)


if __name__== "__main__":
    main()
