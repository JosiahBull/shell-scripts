# Change the absolute path on a scan

import os
import sys
import json

# Load data to be processed
input = {}
with open("oldfamilydrives.json", "r") as reader:
    input = json.load(reader)

# Do replace
for key, obj in input.items():
    for file in obj:
        file["path"] = file["path"].replace("/media/main-disk/", "/run/media/josiah/storage/main-disk/", 1)
    input[key] = obj

# Write Output
with open("replaced.json", "w+") as f:
    json.dump(input, f)
