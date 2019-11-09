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

# with open('./credentials.json') as credentials_cfg:
#     credentials_json = json.load(credentials_cfg)
#     print(credentials_json)
#     for data in credentials_json:
#         consumer_token = data["consumer_token"]
#         consumer_secret = data["consumer_secret"]
#         access_key = data["access_key"]
#         access_secret = data["access_secret"]
#         bot_interval = data["bot_interval"]

#  Printing out the credentials (only for debugging!)
# print(consumer_token)
# print(consumer_secret)
# print(access_key)
# print(access_secret)
# print(bot_interval)

auth = tweepy.OAuthHandler(consumer_token, consumer_secret).set_access_token(access_key, access_secret)
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