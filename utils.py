import os

def count_images(folder):
    count = sum([len(files) for _, _, files in os.walk(folder)])
    return count

if __name__ == "__main__":
    print(f"Training images: {count_images('dataset/train')}")
    print(f"Validation images: {count_images('dataset/val')}")
    print(f"Test images: {count_images('dataset/test')}")
