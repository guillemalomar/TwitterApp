#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import tweepy
import os
import sys
sys.path.append("../src")
from src.Connect import Connection
from src.TextParser import preprocess


# Method to check if the user wants to finish the application
def check_input(input_var):
    if input_var == 'exit':
        print "The application will now end."
        clean_screen()
        raise SystemExit
    else:
        if input_var != None:
            try:
                _ = int(input_var)
            except:
                print "Input not correct. You must specify an integer number."
                return False
        else:
            return False
    return True


# Method called to do a 'clear', just for application visualization purposes
def clean_screen():
    print(chr(27) + "[2J")

if __name__ == '__main__':
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_secret = os.environ['TWITTER_ACCESS_SECRET']

    input_var = None
    ready = False
    while not ready:
        total_tweets_checked = raw_input("Insert total number of tweets to analyze:")
        ready = check_input(total_tweets_checked)
    limit = 20

    my_connection = Connection()
    my_connection.new_twitterapi_connection(consumer_key, consumer_secret, access_token, access_secret)

    messages_liked = 0
    message_favs = {}
    total_favs = 0
    for status in tweepy.Cursor(my_connection.api.user_timeline).items(int(total_tweets_checked)):
        if status.favorite_count > 0:
            message_favs[status.id] = preprocess(status.text), status.favorite_count, str(status.created_at)
            messages_liked += 1
            total_favs += status.favorite_count

    print ("% Tweets with at least one favourite in the last " +
          str(total_tweets_checked) + " tweets: " +
          str(float(messages_liked) / float(total_tweets_checked)))

    print ("Average favs per tweet in the last " +
          str(total_tweets_checked) + " tweets: " +
          str(float(total_favs) / float(total_tweets_checked)))

    list_of_messages = message_favs.items()
    list_of_messages.sort(key=lambda x: x[1][1], reverse=True)
    for ind, message in enumerate(list_of_messages):
        if ind == limit:
            break
        formatting1 = int((ind + 1) < 10) + int((ind + 1) < 100)
        formatting2 = int(message[1][1] < 10) + int(message[1][1] < 100) + int(message[1][1] < 1000)
        print ("Message " + (' ' * int(formatting1)) + str(ind + 1) +
              " with " + (' ' * int(formatting2)) + str(message[1][1]) + " votes, " +
              "twitted on " + str(message[1][2]) + ": " +
              ' '.join(message[1][0]))
