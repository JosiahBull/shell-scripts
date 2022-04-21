# Remove duplicate items based on a dexy scan (matching sha256 hashes) between two directories

import os
import sys
import json

total_files = 0
moved_count = 0

# HOW TO USE:
# STEP 1: 
#   Arg1 - The files that are being merged (json)
#   Arg2 - The folder to compare against (json)
#   Arg3 - The folder to move "duplicate" files to (dir)
# STEP 2:
#   Do a test run!
# Step 3:
#   Uncomment line 45, and run it for reals


# Load merger data (data we want to merge FROM)
merger_path = sys.argv[1]
merger_data = {}
with open(merger_path, "r") as f:
    merger_data = json.load(f)

# Load static data (data we want to merge INTO)
static_path = sys.argv[2]
static_data = {}
with open(static_path, "r") as f:
    static_data = json.load(f)

# Find all instances where the merger file already exists in the target
duplicate_items = []
for hash, obj in merger_data.items():
    total_files += 1
    if hash in static_data:
        duplicate_items.append(obj)

# Carry out some action on each of those
move_dir = sys.argv[3]
for obj in duplicate_items:
    moved_count += 1
    for file in obj:
        source_dir = file["path"]
        dest_dir = move_dir + "/" + str(moved_count) + "-" + os.path.basename(source_dir)
        try:
            os.rename(source_dir, dest_dir)
        except:
            print("failed to move file")

with open("found_dups.json", "w+") as write_file:
    json.dump(duplicate_items, write_file)

print("Moved " + str(moved_count) + " hashes out of " + str(total_files) + " total hashes")