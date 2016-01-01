#!/usr/bin/python

import sys
import urllib
import json
import os

title = sys.argv[-1]
print(title)
query = urllib.urlencode({'q' : title+'soundcloud'})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' \
% (query)
search_results = urllib.urlopen(url)
json = json.loads(search_results.read())
results = json['responseData']['results']
link = results[0]['url']
print link
os.system('google-chrome '+link)
