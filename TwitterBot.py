from random import random
from datetime import datetime
import json

bot_interval = None

#  TODO: READ CREDENTIALS CONFIG FROM CREDENTIALS.JSON!
with open('./credentials.json') as credentials_cfg:
    # TODO: To give a better work around to read from json file
    credentials_json = json.load(credentials_cfg)
    bot_interval = credentials_json["bot_interval"]

class TwitterBot:
    def __init__(self, input_footer, input_api_object):
        self.update_string = ""
        self.api_object = input_api_object

        if(input_footer == 0):
            self.footer =  " \n\nThis is a random bot-message, posted on: " + str(datetime.now()) + ". If you have any complaints, drop me a DM! Interval: " + str(bot_interval) + " Sec(s)"
        else:
            self.footer = input_footer

    def text(self, input_push_string):
        self.update_string = input_push_string
        return self.update_string + self.footer

    def random_yes_no(self):
        if(round(random()) != 1):
            self.update_string = "Yes"
        else:
            self.update_string = "No"

        return self.update_string + self.footer

    # Destroy all beta tweets
    def destroy_all_beta_tweets(self):
        try:

            # TODO: Load 200 tweets all at once "https://www.reddit.com/r/learnpython/comments/6rffh2/how_to_load_all_or_much_more_than_200_of_a_users/"
            for status in self.api_object.user_timeline(count=200):
                json = status._json
                id = json['id']

                print("Destroyed tweet: " + str(id))
                self.api_object.destroy_status(id)
            return 0

        except:
            print("Error while deleting all the tweets. Please check the bot's twitter")
            return 1