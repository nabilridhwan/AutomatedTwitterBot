# Import packages
import tweepy
from credentials import *
from time import sleep
from TwitterBot import TwitterBot

# Tweepy initialisation "http://docs.tweepy.org/en/v3.5.0/getting_started.html"
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

__TwitterBot__ = TwitterBot(0, api)

# Main Function (invoking below)
def main():
    __TwitterBot__ = TwitterBot(0, api)

if __name__ == "__main__":
    # TODO: note that it deletes in interval of 200 tweets
    __TwitterBot__.destroy_all_beta_tweets()

    # while True:
    #     main()
    #     sleep(bot_interval)