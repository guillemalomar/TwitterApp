# Tweet Ranking Checker

*    Title: Tweet Ranking Checker         
*    Author: Guillem Nicolau Alomar Sitjes      
*    Date: August 27th, 2017                      
*    Code version: 1.0                         
*    Availability: Public                    

This is an app to check which have been your most successful tweets.

## Requirements
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

## Execution
To execute it, get in the main folder and run:

    python src/TwitterRanking.py

Then:    
1) insert the total number of tweets to analyze (the bigger this number is, the longer it will take to finish).
2) insert the length of the ranking to be shown.

The output will be a list with your top tweets (ordered by number of favs), your most replied users, your most used hashtags, and some statistics.

## Example output
This is the output of my account, analyzing the last 200 messages and obtaining the top 5 tweets, users replied and hashtags.
```
Insert total number of tweets to analyze:200
Insert length of ranking:5
% Tweets with at least one favourite in the last 200 tweets: 0.22
Average favs per tweet in the last 200 tweets: 1.495
Message   1 with  169 favs, twitted on 2016-12-22 21:09:17: 
Message   1 replies:   @9GAG
Message   1 links:     https://t.co/wTtORSO0mi
Message   2 with   47 favs, twitted on 2017-08-02 05:44:16: You might like this. OldSchool …
Message   2 replies:   @TukaramX @TolarianCollege @Davinnistrad @commanderinmtg @commandcast @angelicuriel
Message   2 links:     https://t.co/XxNCGrKPlX
Message   3 with   12 favs, twitted on 2017-03-04 22:07:01: One of the possible designs for a prize playmat at our OldSchool league. I'll order one for myself if we f …
Message   3 replies:   @mithmtg
Message   3 links:     https://t.co/Jj0NKV32Hm
Message   4 with   10 favs, twitted on 2017-03-21 20:14:23: I love fbb cards, glad to see someone else like me xD
Message   4 replies:   @LibrarianOfLeng
Message   4 links:     https://t.co/ivM1uMJc5d
Message   5 with    7 favs, twitted on 2017-08-21 04:39:54: Las leyes están hechas a medida de los gobernantes. Los afr …
Message   5 replies:   @seergiio0506 @platdescudella @norbertoweb @Indautxutik
Message   5 links:     https://t.co/lfqg1KLDUh
Most replied users in last 200 tweets ----------------------------------------
20 replies,@MissVakarian
16 replies,@TheWeirdWorld
12 replies,@eloyweb
10 replies,@9GAG
7 replies,@caricevhouten
Most used hashtags in last 200 tweets ----------------------------------------
3 times used,#Barcelona
2 times used,#oldschoolmtg
2 times used,#Cambrils
2 times used,#ramblas
2 times used,#LCOS
```

## Aknowledgements
I got inspired by this blog, check it out if you want to learn to do some more cool things!
https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
