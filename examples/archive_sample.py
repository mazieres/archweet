import json
import gzip
from twython import Twython
from twython import TwythonStreamer
from datetime import datetime

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Example: /home/mazieres/archive/twitter/
ARCHIVE_FOLDER = ""

global timestamp
timestamp = '-'.join([str(x) for x in datetime.utcnow().timetuple()[:5]])

global archive_file
archive_file = gzip.open('%stwitter_sample-%s.json.gz' % (ARCHIVE_FOLDER, timestamp), 'wb')


def archive(data, timestamp):
    new_timestamp = '-'.join([str(x) for x in datetime.utcnow().timetuple()[:5]])
    if timestamp == new_timestamp:
        archive_file.write(json.dumps(data, encoding='utf-8'))
    elif timestamp != new_timestamp:
        archive_file.close()
        globals()['timestamp'] = new_timestamp
        globals()['archive_file'] = gzip.open('%s/twitter_sample-%s.json.gz' % (ARCHIVE_FOLDER, new_timestamp), 'wb')
        archive_file.write(json.dumps(data, encoding='utf-8'))


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        archive(data, timestamp)
    
    def on_error(self, status_code, data):
        print status_code

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

if __name__ == '__main__':
    stream.statuses.sample()