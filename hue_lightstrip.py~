import json
import os

def handle(response):
	xbackRelative = {'up':'-inc', 'down':'-dec'}
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	relative = dict.get(entities,'relative_adjustment','null')
	if relative != 'null':
		relativeValue = relative[0]['value']
		number = decoded['outcomes'][0]['entities']['number'][0]['value']
		os.system('xbacklight '+xbackRelative[relativeValue]+' '+str(number))	
	else:
		number = decoded['outcomes'][0]['entities']['number'][0]['value']
		os.system('xbacklight -set '+str(number))		
			    	
