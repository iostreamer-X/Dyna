import wit
import time
import json
import os
import hue_lightstrip
import volume

context = 'null'
def handle_response(response):
    	decoded = json.loads(response)
	body = decoded['_text']
	if body is not None:
		confidence = decoded['outcomes'][0]['confidence']
		intent = decoded['outcomes'][0]['intent']
		if confidence >= 0.7:
			exec(intent+'.handle(response)')


wit.init()

while True:
	os.system("pkill notify-osd && notify-send Listening")
	wit.voice_query_start('O66U5BV3JAAAZ7YENBNJVHTWN2DXGZ3Z')
	time.sleep(5)
	os.system("pkill notify-osd && notify-send Processing")
	response = wit.voice_query_stop()
	handle_response(response)

wit.close()
