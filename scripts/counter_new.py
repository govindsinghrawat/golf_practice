#!/usr/bin/env python3
import sys
import keyboard
import time
import random
from gtts import gTTS
import playsound
import os


class SoundProcessor:
  def __init__(self, start, end, sounds_dir='../sounds/counter/'):
    self.start=int(start)
    self.end=int(end)

    self.phrases=[ str(i) for i in range(self.start, self.end+1)]
    self.sounds_dir=sounds_dir


  def generate_sounds(self):
    ready_phrase="get ready!"
    ready_audio_file = self.sounds_dir+"ready.mp3"

    close_phrase="Practice ended! Great session"
    close_audio_file = self.sounds_dir+"close.mp3"

    if not os.path.exists(ready_audio_file):
      tts=gTTS(text=ready_phrase, lang='en')
      tts.save(ready_audio_file)
    
    if not os.path.exists(close_audio_file):
      tts=gTTS(text=close_phrase, lang='en')
      tts.save(close_audio_file)

    for p in self.phrases:
      audio_file = self.sounds_dir+p+".mp3"
      if not os.path.exists(audio_file):
        tts = gTTS(text=p, lang='en')
        tts.save(audio_file)

  def play_sound(self, mp3_file):
    playsound.playsound(mp3_file)
    


class GolfCounter:
  def __init__(self, start, end, ready_interval=4, rest_interval=4,sounds_dir='../sounds/counter/'):
    self.start=int(start)
    self.end=int(end)
    self.ready_interval=int(ready_interval)
    self.rest_interval=int(rest_interval)

    self.sounds_dir=sounds_dir


  def start_practice(self):
    for i in range(self.start, self.end+1):
      playsound.playsound(self.sounds_dir+"ready.mp3")
      time.sleep(self.ready_interval)
      print(str(i))
      playsound.playsound(self.sounds_dir+str(i)+".mp3")
      time.sleep(self.rest_interval)
    playsound.playsound(self.sounds_dir+"close.mp3")

    

def main(start, end, ready_interval, rest_interval):
  sp = SoundProcessor(start, end)
  gc = GolfCounter(start, end, ready_interval, rest_interval)
  print("Generating sounds...Please wait")
  sp.generate_sounds()
  print("Starting practice...")
  gc.start_practice()
  

if __name__ =='__main__':
  main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    

