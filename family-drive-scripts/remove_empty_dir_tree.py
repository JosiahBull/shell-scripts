# Recursively loop through and remove any folders which are empty
import os
import sys

start_dir = "/run/media/josiah/storage/main-disk/OldFamilyDrives/"

def walk(path, count):
    files = os.listdir(path)
    if len(files) == 0:
        print("removing dir " + str(path))
        os.rmdir(path)
        count += 1
    else:
        for file in files:
            if os.path.isdir(os.path.join(path, file)):
                count += walk(os.path.join(path, file), count)
    return count

count = 1
while count != 0:
    count = 0
    walk(start_dir, count)