#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import tweepy
from tweepy import OAuthHandler
import logging
logging.captureWarnings(True)


class Connection:
    def __init__(self):
        self.api = None

    def new_twitterapi_connection(self, consumer_key, consumer_secret, access_token, access_secret):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth)
