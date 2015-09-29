import json
import os

def handle(response):
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	title = entities['search_query'][0]['value']
	if decoded['_text'].find('what') != -1:
		os.system('google-chrome google.co.in/search?q='+'\''+decoded['_text']+'\'')	
	else:
		os.system('google-chrome google.co.in/search?q='+'\''+title+'\'')
