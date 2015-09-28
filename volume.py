import json
import os

def handle(response):
	currentVolume = int(os.popen('amixer sget Master').read().split()[-3].split('[')[1].split('%')[0])
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	relative = dict.get(entities,'relative_adjustment','null')
	if relative != 'null':
		relativeValue = relative[0]['value']
		number = decoded['outcomes'][0]['entities']['number'][0]['value']
		
		if relativeValue == 'up':
			currentVolume*=(1+number/100.0)
		else:
			currentVolume*=(1-number/100.0)
		
		currentVolume=int(round(currentVolume))		
		
		os.system('pactl -- set-sink-volume 0 '+str(currentVolume)+'%')	
	else:
		number = decoded['outcomes'][0]['entities']['number'][0]['value']
		currentVolume = number
		os.system('pactl -- set-sink-volume 0 '+str(currentVolume)+'%')		
			    	
