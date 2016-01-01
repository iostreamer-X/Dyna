# Dyna
Linux Virtual Assistant

A basic virtual assistant powered by http://Wit.ai.

Dyna supports searching stuff on google, playing videos on youtube, volume & brightness control.
All you need to do is, say the right words. For example, saying "play lean on Major lazer" would fire up your browser
with the tune.

#Pre requisites

1. `sudo apt-get install libsox-dev`
2. `sudo apt-get install libsox2`
3. wit: `sudo pip install wit`
4. xbacklight: `sudo apt-get install xbacklight`

#Installation

1. `git clone https://github.com/iostreamer-X/Dyna.git`
2. `cd Dyna`
3. `python io.py`

#Notes

Depending on your OS you might have to change line 28 & 31 in io.py.
If no notification is appearing on your screen(Notification like 'Listening' or 'Processing')
then in lines 28 & 31, remove this part "pkill notify-osd && ", so that it looks like

28. `os.system("notify-send Listening")`
31. `os.system("notify-send Processing")`

#Commands

Dyna can do 4 things.

1. Modify brightness level
  * "set the brightness to 10%"
  * "increase the brightness by 20%"
  * "brightness 90%"

2. Modify Volume level
  * "set the volume to 10%"
  * "increase the volume by 20%"
  * "volume 90%"

3. Play Music. (If the song you asked for is not found in userName/Music, the song is played through soundcloud)
  * "play dropout slowly"
  * "play where are you now"

4. Search on Google
  * "How's the weather in Dubai"
  
#Demo

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/2Jy_rw5PW6Y/0.jpg)](http://www.youtube.com/watch?v=2Jy_rw5PW6Y)
