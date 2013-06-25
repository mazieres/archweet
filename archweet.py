#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from twython import Twython
from twython import TwythonStreamer

reload(sys)
sys.setdefaultencoding("utf-8")

'''
Use Python module Twython for querying Twitter API.
To log results, execute the script from terminal like this:
    
    python archweet.py | tee /path/to/your/file.json
    
For letting it run on a server without being logged, use screen, or:

    nohup python archweet.py | tee /path/to/your/file.json &
'''

# To get the following 4 credentials, got to https://dev.twitter.com/apps and create a new application and generate them.

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        print data
    
    def on_error(self, status_code, data):
        print status_code

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

if __name__ == '__main__':
    pass
    # Query Filter API, more details at https://dev.twitter.com/docs/api/1.1/post/statuses/filter
    # Example:
    # stream.statuses.filter(track=':),:(')
    
    # Query SAMPLE API, more detail at https://dev.twitter.com/docs/api/1.1/get/statuses/sample
    # Example:
    # stream.statuses.sample()
