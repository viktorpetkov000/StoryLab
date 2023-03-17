import urllib.request
from pydub import AudioSegment
from bs4 import BeautifulSoup
import os
char = str(input("Character name: "))
blacklist = {"laugh","death"}
url = "https://leagueoflegends.fandom.com/wiki/" + char + "/LoL/Audio"
folder_name = char
if not os.path.exists(folder_name): os.mkdir(folder_name)
os.chdir(folder_name)
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
audio_tags = soup.find_all('audio')
for tag in audio_tags:
    file_url = tag.attrs['src']
    if "original" in file_url.lower() and char.lower() in file_url.lower():
      if not any(word.lower() in file_url.lower() for word in blacklist):
        request = urllib.request.Request(file_url, method='HEAD')
        response = urllib.request.urlopen(request)
        if response.getheader('Content-Length'):
            duration = int(int(response.getheader('Content-Length')) / 9600)
        if duration >= 4:
          file_name = file_url.split('/')[-1].split('=')[1]
          urllib.request.urlretrieve(file_url, file_name + ".ogg")
          print(f"Downloaded {file_url}")
print("done")

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
