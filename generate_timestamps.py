from mutagen.flac import FLAC
import glob
import os
import math

audio_filenames = [os.path.basename(filepath) for
                filepath in glob.glob("IO/*.flac")]

length = 0

for file in audio_filenames:
  file_path = f"IO/{file}"
  audio = FLAC(file_path)
  length += audio.info.length
  ## optimisation: make the decision based on the full length MINUS the length of the last track (avoids formatting the timestamps in a wrong manner when the full album is just above an hour in length but the last track's timestamp isn't above 3600 seconds)

if length >= 3600:
  length = 0
  for file in audio_filenames:
    file_path = f"IO/{file}"
    audio = FLAC(file_path)

    track = audio.get("tracknumber")[0]
    title = audio.get("title")[0]

    print(f"{int(length/3600):02d}:{int((length-int(length/3600)*3600)/60):02d}:{math.floor((length-int(length/3600)*3600)-int((length-int(length/3600)*3600)/60)*60):02d} {int(track):02d}. {title}")
    length += audio.info.length
else:
  length = 0
  for file in audio_filenames:
    file_path = f"IO/{file}"
    audio = FLAC(file_path)

    track = audio.get("tracknumber")[0]
    title = audio.get("title")[0]

    print(f"{int((length-int(length/3600)*3600)/60):02d}:{math.floor((length-int(length/3600)*3600)-int((length-int(length/3600)*3600)/60)*60):02d} {int(track):02d}. {title}")
    length += audio.info.length