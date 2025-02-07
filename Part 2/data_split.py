import os
import shutil
from sklearn.model_selection import train_test_split

base_dir = "images"
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")

# Create train and val folders
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Iterate over each category folder
for category in os.listdir(base_dir):
    category_path = os.path.join(base_dir, category)
    

    if not os.path.isdir(category_path) or category in ["train", "val"]:
        continue
    
    # Get all images in the category
    images = [img for img in os.listdir(category_path)]

    # Split images into train (80%) and val (20%)
    train_images, val_images = train_test_split(images, test_size=0.2)

    # Create category folders inside train and val
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(val_dir, category), exist_ok=True)

    # Move training images
    for img in train_images:
        shutil.move(os.path.join(category_path, img), os.path.join(train_dir, category, img))

    # Move validation images
    for img in val_images:
        shutil.move(os.path.join(category_path, img), os.path.join(val_dir, category, img))

print("done")
