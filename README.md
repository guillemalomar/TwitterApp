# Tweet Ranking Checker

*    Title: Tweet Ranking Checker         
*    Author: Guillem Nicolau Alomar Sitjes      
*    Date: July 30th, 2017                      
*    Code version: 0.1                         
*    Availability: Public                    

This is an app to check which have been your most successful tweets.

Requirements:
- Python +2.7 (can be downloaded from here: https://www.python.org/downloads/release/python-2713/)
- You will need an official account at Twitter (in fact, you should already have one, as without it this app will be quite useless)
- And an official twitter api account. This is really easy to do, just go to https://apps.twitter.com/ being logged in, and ask to 'Create a New App'.
- Now, from your terminal, you will have to set some environment variables with your official app keys:
```
export TWITTER_CONSUMER_KEY='YOUR-CONSUMER-KEY'
export TWITTER_CONSUMER_SECRET='YOUR-CONSUMER-SECRET'
export TWITTER_ACCESS_TOKEN='YOUR-ACCESS-TOKEN'
export TWITTER_ACCESS_SECRET='YOUR-ACCESS-SECRET'
```
- And install tweepy: sudo pip install tweepy==3.3.0

To execute it, get in the main folder and run:

    python TwitterRanking.py

Then:    
1) insert the total number of tweets to analyze (the bigger this number is, the longer it will take to finish).
2) insert the length of the ranking to be shown.

The output will be a list with your top tweets (ordered by number of favs), your most replied users and most used hashtags, and some statistics.

Aknowledgements:
I got inspired by this blog, check it out if you want to learn to do some more cool things!
https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
