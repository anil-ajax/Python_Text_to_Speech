# google text to speech library 
from gtts import gTTS 

# os library to play the converted audio 
import os 

# The text that you want to convert to audio 
txt = 'anil is here'

language = 'en'

obj = gTTS(text=txt, lang=language, slow=False) 

# convert and save to welcome.mp3
obj.save("welcome.mp3") 

# Playing the converted file. use "start"  command here as some other commands metioned on internet may not work
os.system("start welcome.mp3") 
