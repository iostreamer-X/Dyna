import json
import os

def handle(response):
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	title = entities['movieTitle'][0]['value']
	os.system('python pvi.py \''+title+'\'')
			
