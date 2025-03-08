import os
from PIL import Image


def is_corrupted(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()
            return False
    except Exception as e:
        return True


def move_corrupted_images(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if is_corrupted(source_path):
            destination_path = os.path.join(destination_folder, filename)
            os.rename(source_path, destination_path)
            print(f"Moved corrupted image: {filename}")


if __name__ == "__main__":
    source_folder = "/Users/santhiya/Documents/multimedia_mac/from_desktop"
    destination_folder = "output"

    move_corrupted_images(source_folder, destination_folder)
