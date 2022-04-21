import os
import json

# FILTERING BASED on output from `similarity_compare.py`
# data_path = "img-similarity-dups.json"
# data = {}
# with open(data_path, "r") as f:
#     data = json.load(f)

# move_path = "/run/media/josiah/storage/duplicate/"
# count = 0
# for duplicate in data:
#     new_location = move_path + str(count) + "-" + os.path.basename(duplicate["duplicate_path"])
#     os.rename(duplicate["duplicate_path"], new_location)
#     count += 1

move_dir = "/run/media/josiah/storage/duplicate/duplicate (already exists in 2019 backup)/"

# FILTERING BASED on output from `similarity-finder.rs`
photos_path = "similarity_finder_photos.json"
photos_data = {}
with open(photos_path, "r") as f:
    photos_data = json.load(f)

drive_path = "similarity_finder_oldfamilydrives.json"
drive_data = {}
with open(drive_path, "r") as f:
    drive_data = json.load(f)

count = 0
for hash, obj in drive_data.items():
    if hash in photos_data:
        for image in obj:
            dest_dir = move_dir + "/" + str(count) + "-" + os.path.basename(image["path"])
            os.rename(image["path"], dest_dir)
            count += 1

print("Moved " + str(count) + " files")