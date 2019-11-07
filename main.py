# Import packages
import tweepy
from credentials import *
from random import random
from time import sleep
from datetime import datetime

# Tweepy initialisation
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Main Function (invoking below)
def main():

    footer =  " \n\nThis is a random bot-message, posted on: " + str(datetime.now()) + ". If you have any complaints, drop me a DM!"
    updatestr = "Hello World! " + str(random()) + footer
    print("Done! Update String: " + updatestr)
    api.update_status(updatestr);


# Destroy all beta tweets
def destroy_all_test_tweets():
    for status in api.user_timeline():
        json = status._json
        id = json['id']

        api.destroy_status(id)


if __name__ == "__main__":
    while True:
        main()
        sleep(30)