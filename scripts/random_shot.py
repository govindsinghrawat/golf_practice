import os
import random
import time
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Define a list of phrases
phrases = [
    "7:00",
    "8:00",
    "9:00",
    "10:00",
    "Full shot"
]

#sleep time
SLEEP=3.5

# Function to generate and save MP3 files
def generate_mp3_files(phrases, directory='../inputs/'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for index, phrase in enumerate(phrases, start=1):
        tts = gTTS(text=phrase, lang='en')
        audio_file = os.path.join(directory, f"{index}.mp3")
        tts.save(audio_file)
        print(f"Saved {audio_file}")

# Function to play a random MP3 file
def play_random_mp3(directory='../inputs/'):
    num_files = len(os.listdir(directory))
    random_index = random.randint(1, num_files)
    audio_file = os.path.join(directory, f"{random_index}.mp3")
    
    if os.path.exists(audio_file):
        audio = AudioSegment.from_mp3(audio_file)
        play(audio)
    else:
        print(f"File {audio_file} not found!")

# Example usage
if __name__ == "__main__":
    # Generate MP3 files (run this once when phrases change)
    generate_mp3_files(phrases)

    # Play a random MP3 file
    while True:
        play_random_mp3()
        time.sleep(SLEEP)  # Wait for 5 seconds before playing another random file

