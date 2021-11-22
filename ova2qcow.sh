#!/bin/bash
#Josiah Bull - 23/11/2021
#This is a script which will convert an ova file to qcow2
if [ -z "$1" ] && [ test -f "$1" ]
then
    echo "Invalid or no file provided."
else
    #Generate directory to hold conversion data
    echo "Attempting to open file " $1
    path="./${1}-conversiondata"
    mkdir -p "${path}"
    #Unzip files
    tar -xvf "./${1}" -C "${path}"
    files=( "${path}"/*.vmdk )
    #Convert to qcow
    qemu-img convert "${files[0]}" "${1}-img.qcow2"
    #Remove temporary files
    rm -rd "${path}"
fi
