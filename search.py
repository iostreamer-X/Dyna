import json
import os

def handle(response):
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	title = entities['search_query'][0]['value']
	os.system('google-chrome google.co.in/search?q='+'\''+title+'\'')
