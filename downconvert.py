import urllib.request
from pydub import AudioSegment
from bs4 import BeautifulSoup
import os
# Get the character name from the user
char = str(input("Character name: "))

# Create a blacklist of words to filter out certain audio files
blacklist = {"laugh","death"}

# Create the URL for the character's audio files
url = "https://leagueoflegends.fandom.com/wiki/" + char + "/LoL/Audio"

# Create a folder for the character's audio files
folder_name = char
if not os.path.exists(folder_name): os.mkdir(folder_name)
os.chdir(folder_name)

# Open the URL and parse the HTML with BeautifulSoup
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

# Find all the audio tags on the page
audio_tags = soup.find_all('audio')

# Loop through each audio tag
for tag in audio_tags:
    file_url = tag.attrs['src']
    # Check if the file is an original file and contains the character name
    if "original" in file_url.lower() and char.lower() in file_url.lower():
      # Check if the file contains any words in the blacklist
      if not any(word.lower() in file_url.lower() for word in blacklist):
        # Get the file size to calculate the duration of the audio file
        request = urllib.request.Request(file_url, method='HEAD')
        response = urllib.request.urlopen(request)
        if response.getheader('Content-Length'):
            duration = int(int(response.getheader('Content-Length')) / 9600)
        # Only download files that are at least 4 seconds long
        if duration >= 4:
          file_name = file_url.split('/')[-1].split('=')[1]
          urllib.request.urlretrieve(file_url, file_name + ".ogg")
          print(f"Downloaded {file_url}")
print("done")

# Convert all the .ogg files to .wav files
cwd = os.getcwd()
files = os.listdir(cwd)
ogg_files = [f for f in files if f.endswith(".ogg")]
for ogg_file in ogg_files:
    sound = AudioSegment.from_ogg(ogg_file)
    wav_file = ogg_file.replace(".ogg", ".wav")
    sound.export(wav_file, format="wav")
    os.remove(ogg_file)
    print(f"Converted {ogg_file} to {wav_file}")
print("done")
