# Import packages
import tweepy
from credentials import *
from time import sleep
from TwitterBot import TwitterBot

# Tweepy initialisation
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

new_twitter_bot = TwitterBot(0, api)

# Main Function (invoking below)
def main():
    new_twitter_bot = TwitterBot(0, api)

if __name__ == "__main__":
    # TODO: note that it deletes in interval of 200 tweets
    new_twitter_bot.destroy_all_beta_tweets()

    # while True:
    #     main()
    #     sleep(bot_interval)