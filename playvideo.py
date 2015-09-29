import json
import os

def handle(response):
	decoded = json.loads(response)
	entities = decoded['outcomes'][0]['entities']
	isYoutube = decoded['outcomes'][0]['_text'].find('YouTube') != -1
	title = entities['movieTitle'][0]['value']
	if not isYoutube:
		local = os.popen('find /home/iostreamer/Music -iname "*'+title+'*"').read().strip('\n').split('\n')
		if local[0]=='':
			os.system('python pvi.py \''+title+'\'')
		else:
			cmd = 'rhythmbox-client --play-uri "file://'+local[0]+'"'
			os.system(cmd)
		
	else:
		os.system('python pvi.py \''+title+'\'')
			
