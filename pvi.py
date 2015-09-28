#!/usr/bin/python

import sys
from pygoogle import pygoogle
import os

title = sys.argv[-1]
print(title)
link = pygoogle(title+'youtube').get_urls()[0]
os.system('google-chrome '+link)
