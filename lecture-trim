#!/bin/bash
#Josiah Bull - 23/05/2021
#A small script to automatically trim the first 45 seconds off lecture files from UoA

for entry in "$PWD"/*.{mp4,m4v}
do
 if test -f "$entry"
 then
  f="${entry##*/}"
  if [ ${f:0:3} != "tr-" ]
  then
   ffmpeg -y -hide_banner -loglevel error  -i "$f" -ss 45 -vcodec copy -acodec copy "output.${entry##*.}"
   rm "$f"
   mv "output.${entry##*.}" "tr-$f"
   echo "Removed first 45 sec on file: $f"
  else
   echo "File already trimmed: $f"
  fi
 fi
done
