#!/usr/bin/python

import twitterKey
import json
import signal
import sys
import os
import sys
import socket
import subprocess
import tweepy
from twython import Twython, TwythonError
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

auth = OAuthHandler(twitterKey.APP_KEY, twitterKey.APP_SECRET)
auth.set_access_token(twitterKey.OAUTH_TOKEN, twitterKey.OAUTH_TOKEN_SECRET)

hastag = sys.argv[1]

class listener(StreamListener):
    
    def on_data(self, data):
        
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        for char in hastag:
            tweet = tweet.replace(char,"")
	    
        print("Listing New Tweet: {} | User: {}".format(tweet, username))
	
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.close()
        return True
		
    def on_error(self, status):
        print(status)

while 1:
      try:
	  print("Press Ctrl + c to Stop Listening")
	  print("Listening for Tweets That Contains: {}".format(hastag))
	  twitterStream = Stream(auth, listener())
	  twitterStream.filter(track=[hastag])
      except KeyboardInterrupt:
	  break

