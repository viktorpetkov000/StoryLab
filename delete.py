import os

# Get the current working directory
cwd = os.getcwd()

# List all the files in the folder
files = os.listdir(cwd)

# Filter only the .ogg files
ogg_files = [f for f in files if f.endswith(".ogg")]

# Loop over the .ogg files and convert them to .wav files
for ogg_file in ogg_files:
    os.remove(ogg_file)