import os
import shutil
import random

def split_data(source, train_dest, val_dest, test_dest, train_size=0.7, val_size=0.15, test_size=0.15):
    images = os.listdir(source)
    random.shuffle(images)

    train_split = int(len(images) * train_size)
    val_split = train_split + int(len(images) * val_size)

    train_images = images[:train_split]
    val_images = images[train_split:val_split]
    test_images = images[val_split:]

    for img in train_images:
        shutil.copy(os.path.join(source, img), train_dest)
    
    for img in val_images:
        shutil.copy(os.path.join(source, img), val_dest)
    
    for img in test_images:
        shutil.copy(os.path.join(source, img), test_dest)

# Example: Splitting morph images
split_data("dataset/all_morphs", "dataset/train/morph", "dataset/val/morph", "dataset/test/morph")
split_data("dataset/all_not_morphs", "dataset/train/not_morph", "dataset/val/not_morph", "dataset/test/not_morph")
