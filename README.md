# AutomatedTwitterBot
> A project hosted on c9.io and is running at https://twitter.com/skruraibot.

# Use-your-own (UYO) docs
1. Fill up credentials details and config in `credentials_demo.json`
2. Rename the file from `credentials_demo.json` to `credentials.json` so that the program can read the file
3. Edit away in main.py in the main function! (Seperate docs will be written for this!)

# The TwitterBot class
> Each function returns a string, this string can be used in the update status

You can initialize an instance by assigning it to a variable `__TwitterBot__ = TwitterBot(0, api)``

- \_\_init\_\_(self, input_footer, input_api_object)
    - Takes in a string for footer (if there is non, please input 0) that will end up behind your tweet (use \n\n to leave a line). Also takes in an api_object (from Tweepy intialisation)
- text(self, input_push_string)
    - Returns a string that you inputted as argument.
- random_yes_no(self)
    - Returns a "Yes" or "No" randomly.
- destroy_all_beta_tweets(self)
    - Removes 200 tweets (maximum) at a time - will remove limitation in the futute.
