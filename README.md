# AutomatedTwitterBot
> A project hosted on c9.io and is running at https://twitter.com/skruraibot.

# Use-your-own (UYO) docs
1. Fill up credentials details and config in `credentials_demo.json`
2. Rename the file from `credentials_demo.json` to `credentials.json` so that the program can read the file
3. Edit away in main.py in the main function! (Seperate docs will be written for this!)

# TwitterBot class
- text(self, input_push_string)
    - Returns a string that you inputted as argument.
- random_yes_no(self)
    - Returns a "Yes" or "No" randomly.
- destroy_all_beta_tweets(self)
    - Removes 200 tweets (maxium) at a time - will remove limitation in the futute.
