import subprocess
import os
from mutagen.flac import FLAC
import glob

input_files = [os.path.basename(filepath) for
                filepath in glob.glob("IO/*.flac")]

for i in range(0, len(input_files)):
    input_files[i] = f"IO/{input_files[i]}"

tags = FLAC(input_files[0])
album_name = tags.get("album")[0]
artist = tags.get("artist")[0]
output_file = f'IO/{artist} - {album_name} [Full Album].flac'

ffmpeg_command = [
    'ffmpeg',
    '-y',
]

for file in input_files:
    ffmpeg_command.extend(['-i', file])

ffmpeg_command.extend([
    '-filter_complex', f'concat=n={len(input_files)}:v=0:a=1',
    '-c:a', 'flac',
    output_file
])

subprocess.run(ffmpeg_command)