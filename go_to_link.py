import json
import os

def handle(response):
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	link = entities['url'][0]['value']
	os.system('google-chrome ' + link)
