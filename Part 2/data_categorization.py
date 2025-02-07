import os
import json
import shutil

base = ""
json_file = "sky_classification_export.json"

with open(json_file, "r") as f:
    data = json.load(f)  # List of dictionaries

for photo in data:
    if "choice" not in photo:
        continue
    image_path = os.path.join(base, photo["image"])

    category_folder = os.path.join(base, "images", photo["choice"])
    os.makedirs(category_folder, exist_ok=True)

    if os.path.exists(image_path):
        shutil.move(image_path, os.path.join(category_folder))

print("Sorting complete.")
