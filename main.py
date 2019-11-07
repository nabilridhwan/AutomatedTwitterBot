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
current_date = str(datetime.now())

# Main Function (invoking below)
def main():
    updatestr = "Hello World! " + str(random()) +" \n\nThis is a random bot-message, posted on: " + current_date + ". If you have any complaints, drop me a DM!"
    print("Done! Update String: " + updatestr)
    api.update_status(updatestr);

if __name__ == "__main__":
    while True:
        main()
        sleep(30)