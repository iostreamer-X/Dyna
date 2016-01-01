# Dyna
Linux Virtual Assistant

A basic virtual assistant powered by http://Wit.ai.

Dyna supports searching stuff on google, playing videos on youtube, volume & brightness control.
All you need to do is, say the right words. For example, saying "play lean on Major lazer" would fire up your browser
with the tune.

#Pre requisites

1. sudo apt-get install libsox-dev
2. sudo apt-get install libsox2
3. wit: sudo pip install wit
4. xbacklight: sudo apt-get install xbacklight

#Installation

1. `git clone https://github.com/iostreamer-X/Dyna.git`
2. cd Dyna
3. python io.py

#Notes

Depending on your OS you might have to change line 28 & 31 in io.py.
If no notification is appearing on your screen(Notification like 'Listening' or 'Processing')
then in lines 28 & 31, remove this part "pkill notify-osd && ", so that it looks like

28. `os.system("notify-send Listening")`
31. `os.system("notify-send Processing")`

#[Demo](https://www.youtube.com/watch?v=2Jy_rw5PW6Y)
