# Import packages
import tweepy
from credentials import *
from time import sleep
import json
from TwitterBot import TwitterBot

# Tweepy initialisation "http://docs.tweepy.org/en/v3.5.0/getting_started.html"
consumer_token = None
consumer_secret = None
access_key = None
access_secret = None
bot_interval = None

#  TODO: READ CREDENTIALS CONFIG FROM CREDENTIALS.JSON!
with open('./credentials.json') as credentials_cfg:

    # TODO: To give a better work around to read from json file
    credentials_json = json.load(credentials_cfg)

    consumer_token = credentials_json[0]["consumer_token"]
    consumer_secret = credentials_json[1]["consumer_secret"]
    access_key = credentials_json[2]["access_key"]
    access_secret = credentials_json[3]["access_secret"]
    bot_interval = credentials_json[4]["bot_interval"]


auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_key, access_secret)
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