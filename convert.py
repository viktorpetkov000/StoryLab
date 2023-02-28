import os
from pydub import AudioSegment

# Get the current working directory
cwd = os.getcwd()

# List all the files in the folder
files = os.listdir(cwd)

# Filter only the .ogg files
ogg_files = [f for f in files if f.endswith(".ogg")]

# Loop over the .ogg files and convert them to .wav files
for ogg_file in ogg_files:
    sound = AudioSegment.from_ogg(ogg_file)
    wav_file = ogg_file.replace(".ogg", ".wav")
    sound.export(wav_file, format="wav")
    os.remove(ogg_file)