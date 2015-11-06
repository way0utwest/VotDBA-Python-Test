import sys
import tweepy

def send_a_tweet(tweettext):
    consumer_key = "X1GWqgKpPP4OuR1XNqWJZ7hw6"
    consumer_secret = "QW3EkMHlyzFxytHOxQr5mEy69AHn8DjyWyRG5CAQ0wjK9RqUZ2"
    access_token = '14607509-MqpeZFsljo0JzS0VGgTSik1fq5klvJpqc1x6HAsiu'
    access_token_secret = '7wIZlLHEv1PbIqXtczc2LOsJgjMP3dCRRw5ajMvkjEspF'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    api.update_status(status=tweettext)

if __name__ == '__main__':
    send_a_tweet(sys.argv[1])

