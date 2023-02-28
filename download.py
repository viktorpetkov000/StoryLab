# Import requests, BeautifulSoup and shutil libraries
import requests
from bs4 import BeautifulSoup
import shutil
import os

# Define the website url
url = "https://leagueoflegends.fandom.com/wiki/Azir/LoL/Audio"

# Get the html content of the website
response = requests.get(url)
html = response.text

# Parse the html using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the audio tags in the html
audio_tags = soup.find_all("audio")
folder_name = "char"
if not os.path.exists(folder_name): os.mkdir(folder_name)
# Loop through each audio tag and get its src attribute
for i, audio in enumerate(audio_tags):
    src = audio.get("src")
    # Download the src attribute as an .ogg file or print a message if it is None
    if src and "Original" in src:
        # Create a file name based on the index of the audio tag
        file_name = os.path.join(folder_name, f"audio_{i}.ogg")
        # Get the response from the src url
        r = requests.get(src, stream=True)
        # Open a file in write-binary mode and save the content of the response
        with open(file_name, "wb") as f:
            shutil.copyfileobj(r.raw, f)
        # Print a message indicating that the file was downloaded successfully
        print(f"Downloaded {file_name} from {src}")
    else:
        print("No src attribute found for this audio tag")