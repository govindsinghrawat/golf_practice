#!/usr/bin/env python3
import keyboard
import time
import random
from gtts import gTTS
import playsound
import os

# Define a list of phrases
phrases = [
"367 yards",
"400 yards",
"366 yards",
"413 yards",
"519 yards",
"368 yards",
"359 yards",
"170 yards",
"349 yards",
"341 yards",
"160 yards",
"309 yards",
"414 yards",
"527 yards",
"415 yards",
"377 yards",
"449 yards",
"354 yards",
"168 yards",
"233 yards",
"423 yards",
"444 yards",
"432 yards",
"455 yards",
"466 yards",
"546 yards",
"565 yards",
"577 yards",
"457 yards",
"699 yards",
"646 yards",
"564 yards",
"169 yards",
"369 yards",
"384 yards",
"764 yards"
]


def on_press(key):
    try:
        if key.char == 'q':  # Detect 'q' key press
            #print("You pressed 'q'!")
            return False  # Stop listener
    except AttributeError:
        pass

interval=60000  # Change this value to your desired interval

# Function to randomly select and speak a phrase
def say_random_phrase():
    #phrase = random.choice(phrases)
    for p in phrases:
      print(p)

      tts = gTTS(text=p, lang='en')
      audio_file = "temp_audio.mp3"
      tts.save(audio_file)
      playsound.playsound(audio_file)
      time.sleep(interval)
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

