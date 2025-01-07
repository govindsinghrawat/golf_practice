#!/usr/bin/env python3
import sys
import keyboard
import time
import random
from gtts import gTTS
import playsound
import os

# Define a list of phrases
start=int(sys.argv[1])
cap=int(sys.argv[2])
phrases = [ str(i) for i in range(start,cap+1) ]



def on_press(key):
    try:
        if key.char == 'q':  # Detect 'q' key press
            #print("You pressed 'q'!")
            return False  # Stop listener
    except AttributeError:
        pass

interval=int(sys.argv[3])  # Change this value to your desired interval

# Function to randomly select and speak a phrase
def say_random_phrase():
    #phrase = random.choice(phrases)
    ready_phrase="get ready!"
    tts=gTTS(text=ready_phrase, lang='en')
    ready_audio_file = "ready.mp3"
    tts.save(ready_audio_file)
    for p in phrases:

      tts = gTTS(text=p, lang='en')
      audio_file = "temp_audio.mp3"
      tts.save(audio_file)
      playsound.playsound(ready_audio_file)
      time.sleep(interval//2)
      print(p)
      playsound.playsound(audio_file)
      time.sleep(interval//2)
      os.remove(audio_file)  # Remove the temporary audio file
      #from pynput import keyboard
      #with keyboard.Listener(on_press=on_press) as listener:
      #listener.join()
      #keyboard.wait('q')

# Set the interval in seconds

# Main loop to continuously speak phrases at intervals
while True:
    say_random_phrase()
    time.sleep(interval)

