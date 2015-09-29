import json
import os

def handle(response):
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	on_off = entities['on_off'][0]['value']
	if on_off == 'on':
		os.system('rhythmbox-client --play')
	else:
		os.system('rhythmbox-client --pause')	
