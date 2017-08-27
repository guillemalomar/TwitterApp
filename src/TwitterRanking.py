#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import tweepy
import os
import sys
from collections import defaultdict
sys.path.append("../src/TextParser")
sys.path.append("../src/Connection")
from Connect import Connection
from TextParser import preprocess


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

    ready = False
    while not ready:
        total_tweets_checked = raw_input("Insert total number of tweets to analyze:")
        ready = check_input(total_tweets_checked)

    ready = False
    while not ready:
        limit = raw_input("Insert length of ranking:")
        ready = check_input(limit)

    my_connection = Connection()
    my_connection.new_twitterapi_connection(consumer_key, consumer_secret, access_token, access_secret)

    messages_liked = 0
    message_favs = {}
    total_favs = 0
    total_replies = []
    total_hashtags = []
    for status in tweepy.Cursor(my_connection.api.user_timeline).items(int(total_tweets_checked)):
        if status.favorite_count > 0:
            message_favs[status.id] = preprocess(status.text), status.favorite_count, str(status.created_at)
            messages_liked += 1
            total_favs += status.favorite_count
        for entry in preprocess(status.text):
            if entry.startswith('@'):
                total_replies.append(entry)
            elif entry.startswith('#'):
                total_hashtags.append(entry)

    print ("% Tweets with at least one favourite in the last " +
          str(total_tweets_checked) + " tweets: " +
          str(float(messages_liked) / float(total_tweets_checked)))

    print ("Average favs per tweet in the last " +
          str(total_tweets_checked) + " tweets: " +
          str(float(total_favs) / float(total_tweets_checked)))

    list_of_messages = message_favs.items()
    list_of_messages.sort(key=lambda x: x[1][1], reverse=True)
    for ind, message in enumerate(list_of_messages):
        if ind == int(limit):
            break
        formatting1 = int((ind + 1) < 10) + int((ind + 1) < 100)
        formatting2 = int(message[1][1] < 10) + int(message[1][1] < 100) + int(message[1][1] < 1000)
        message_text = []
        message_replies = []
        message_links = []
        message_hashtags = []
        last_entry = ''
        for entry in message[1][0]:
            if 'http' in entry:
                message_links.append(entry)
            elif entry.startswith('@'):
                message_replies.append(entry)
            elif entry.startswith('#'):
                message_hashtags.append(entry)
            elif entry in ['.', ',', '(', ')', '?', '¿', '!', '¡', '{', '}', '[', ']'] or last_entry in ['(', '[', '¡', '¿', '{']:
                message_text.append(message_text.pop() + entry)
            else:
                message_text.append(entry)
            last_entry = entry
        print ("Message " + (' ' * int(formatting1)) + str(ind + 1) +
              " with " + (' ' * int(formatting2)) + str(message[1][1]) + " favs, " +
              "twitted on " + str(message[1][2]) + ": " +
              ' '.join(message_text))
        if len(message_replies) > 0:
              print "Message " + (' ' * int(formatting1)) + str(ind + 1) + " replies:  ", ' '.join(message_replies)
        if len(message_links) > 0:
              print "Message " + (' ' * int(formatting1)) + str(ind + 1) + " links:    ", ' '.join(message_links)
        if len(message_hashtags) > 0:
              print "Message " + (' ' * int(formatting1)) + str(ind + 1) + " hashtags: ", ' '.join(message_hashtags)

    print "Most replied users in last " + str(total_tweets_checked) + " tweets ----------------------------------------"
    counts = defaultdict(int)
    for x in total_replies:
        counts[x] += 1
    for entry in sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:int(limit)]:
        print str(entry[1]) + " replies," + str(entry[0])

    print "Most used hashtags in last " + str(total_tweets_checked) + " tweets ----------------------------------------"
    counts = defaultdict(int)
    for x in total_hashtags:
        counts[x] += 1
    for entry in sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:int(limit)]:
        print str(entry[1]) + " times used," + str(entry[0])
