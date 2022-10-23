import os,json
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import time
try:
    mixer.init()
except:
    pass
class Files:
    SUSPICIOUS_TEXT='suspicioustext.mp3'
    SUSPICIOUS_CALL='suspiciouscall.mp3'
    CONNECTION_LOST='connectionlost.mp3'
    ERROR='error.mp3'
    CONNECTED='monitored.mp3'

def run(file:Files):
    try:
        with open('config.json','r')as f:
            if json.load(f)['notification']:
                sound = mixer.Sound('assets/notification.mp3')
                sound.play()
                time.sleep(2)
                sound = mixer.Sound('assets/'+file)
                sound.play()
    except:
        print('Error with notification/playing sound')
