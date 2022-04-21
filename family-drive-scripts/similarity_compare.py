from PIL import Image
import numpy as np
import imagehash
import os
import json

image_exts = ['.PNG', '.JPG', '.jpg', '.bmp', '.png']
start_dir = "/run/media/josiah/storage/main-disk/OldFamilyDrives/"
hash_size = 8

hashes = {}
dups = []

def walk(path):
    for file in os.scandir(path):
        if file.is_dir():
            walk(file)
        else:
            name, ext = os.path.splitext(file)
            if ext in image_exts:
                try:
                    with Image.open(file.path) as img:
                        temp_hash = imagehash(img, hash_size)
                        if temp_hash in hashes:
                            print("Found duplicate at {}, orignal path {}".format(file.path, hashes[temp_hash]))
                            dups.append({
                                "original_path": hashes[temp_hash],
                                "duplicate_path": file.path
                            })
                        else:
                            hashes[temp_hash] = file.path
                except:
                    print("ERROR: failed to process file {}".format(file.path))

walk(start_dir)
with open("img-similarity-dups.json", "w+") as writer:
    json.dump(dups, writer)