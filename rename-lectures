#!/bin/bash
#Josiah Bull - 22/05/2021
#A small script to rename lecture files to a more readable format.

for entry in "$PWD"/*.{mp4,m4v}
do
    if test -f "$entry"
    then
        f="${entry##*/}"
        if [ ${f:4:1} != "-" ] && [ ${f:2:1} != "-" ]
        then
            echo "File renamed: $f"
            mv "$entry" ${f:0:4}-${f:4:2}-${f:6:2}-${f:8}
        else
            echo "File already renamed: $f"
        fi
    fi
done
