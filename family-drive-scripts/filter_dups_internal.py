# Attempt to remove duplicate files within a folder, based on a dexy scan

import sys
import os
import json

# Where to move files
move_path = "/run/media/josiah/storage/duplicate/"

# Load merger data (data we want to merge FROM)
merger_path = "oldfamilydrives.json"
merger_data = {}
with open(merger_path, "r") as f:
    merger_data = json.load(f)

# Load all items with duplicates
to_remove = []
for hash, obj in merger_data.items():
    if len(obj) > 1:
        first = True
        for item in obj:
            if first:
                first = False
                continue #Skip the first item
            else:
                to_remove.append(item["path"])

# Filter those that no longer exist
to_remove_filtered = []
for path in to_remove:
    if os.path.exists(path):
        to_remove_filtered.append(path)

# We can now remove these links
count = 0
for item in to_remove_filtered:
    new_location = move_path + str(count) + "-" + os.path.basename(item)
    os.rename(item, new_location)
    count += 1