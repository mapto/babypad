#!/bin/bash

# sudo apt-get install ffmpeg lame flac vorbis-tools

for x in sounds/*.mp3; do
  t=$(echo $x | sed 's/\.mp3$/.ogg/');
  ffmpeg -i $x -ar 48000 -vn -c:a libvorbis $t
done

