# Work recursively through the directories finding every file type that is available
import os
import sys

start_dir = "/run/media/josiah/storage/main-disk/OldFamilyDrives/"

types = []

def walk(path):
    for file in os.scandir(path):
        if file.is_dir():
            walk(file)
        else:
            name, ext = os.path.splitext(file)
            if ext not in types:
                types.append(ext)


walk(start_dir)
print(types)