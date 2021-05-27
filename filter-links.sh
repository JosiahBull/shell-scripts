#!/bin/bash
#Josiah Bull - 27/05/2021
#Filters large csv/txt files to remove empty lines and invalid links that don't match the pattern we're looking for.

if [ -z "$1" ] && [ test -f "$1" ]
then
    echo "Invalid or no file provided."
else
    filename=${1##*/##*.}
    ext=${filename}
    #Create a tmpfile to store our filtered values.
    tmpfile=$(mktemp)
    trap "rm -f $tmpfile" 0 2 3 15
    currentLine=0

    #Read input file, and filter any that don't match.
    while IFS='' read -r line || [ -n "${line}" ]; do
        if [[ ${line:0:17} == "https://encrypted" ]] #This is the pattern we are matching.
        then
            echo "$line" >> $tmpfile
            currentLine=$(($currentLine + 1))
        fi
    done < "$1"

    #Remove unfiltered file and replace it with an empty file.
    rm "$1"
    touch "$1"

    #Fill file with filtered lines.
    while IFS='' read -r line || [ -n "${line}" ]; do
        currentLine=$(($currentLine - 1))
        if [ $currentLine == 0 ]
        then
            echo -n "$line" >> ${1}
        else
            echo "$line" >> ${1}
        fi
    done < "$tmpfile"
    
    #Remove tmp file.
    rm ${tmpfile}
fi