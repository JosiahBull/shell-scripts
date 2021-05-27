#!/bin/bash
#Josiah Bull - 27/05/2021
# This script will automatically merge all files of a provided extension in a directory to an output file, or if no output file is provided then to the first file it finds.
# Usage: merge-file.sh :extension :output_file :delete

# Check search param has been provided.
if [ -z "$1" ]
then
    echo "No file type provided."
else
    # Set save file.
    save="$2"
    # Loop over all files of the search type in the directory
    for entry in "$PWD"/*."$1"
    do
        # Check that the file we're about to merge isn't the output file.
        if ! [ $entry == $save ]
        then
            f="${entry##*/}"

            if [ -z "$2" ] && [ -z $save ]
            then
                echo "Using file ${entry} as save file."
                save=$entry
            else
                echo "$(<$entry)" >> "$save"
            fi
            
            echo "Merged file: $f"
            
            if [ "$3" == "y" ]
            then
                rm "$entry"
            fi
        fi
    done
fi

echo "Files merged succesfully."

