#!/usr/bin/env python3

import time
import random
from gtts import gTTS
import playsound
import os

# Define a list of phrases
phrases = [
"9 o'clock!",
"6 o'clock!",
"7 o'clock!",
"8 o'clock!",
"10 o'clock!",
"11 o'clock!"
]

# Function to randomly select and speak a phrase
def say_random_phrase():
    phrase = random.choice(phrases)
    print(phrase)

    tts = gTTS(text=phrase, lang='en')
    audio_file = "temp_audio.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)  # Remove the temporary audio file

# Set the interval in seconds
interval = 5  # Change this value to your desired interval

# Main loop to continuously speak phrases at intervals
while True:
    say_random_phrase()
    time.sleep(interval)

