import wit
import time
import json
import os
import thread
import hue_lightstrip
import volume
import playvideo
import search
import go_to_link
import music_control

context = 'null'
if __name__ == '__main__':
	def handle_response(response):
    		decoded = json.loads(response)
		body = decoded['_text']
		if body is not None:
			confidence = decoded['outcomes'][0]['confidence']
			intent = decoded['outcomes'][0]['intent']
			if confidence >= 0.67:
				exec(intent+'.handle(response)')


	wit.init()

	while True:
		os.system("pkill notify-osd && notify-send Listening")
		wit.voice_query_start('O66U5BV3JAAAZ7YENBNJVHTWN2DXGZ3Z')
		time.sleep(5)
		os.system("pkill notify-osd && notify-send Processing")
		response = wit.voice_query_stop()
		try:
			thread.start_new_thread(handle_response,(response,))
		except:
			print "Dafaq"

	wit.close()
