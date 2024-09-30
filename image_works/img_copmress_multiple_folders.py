import os
import shutil

from PIL import Image
from time import sleep
from tqdm import tqdm
from video_works import compress_video
from joblib import Parallel, delayed

# configure max_width and height to alter size
def reduce_image_size(all_files, root_ip_folder, input_folder, root_op_folder, max_width, max_height):

    for input_file in tqdm(all_files):
        # Create the output folder if it doesn't exist
        output_file = os.path.join(root_op_folder, input_folder, input_file[len(root_ip_folder)+1:])
        output_dir = os.path.dirname(output_file)

        os.makedirs(output_dir, exist_ok=True)

        try:
            # Get the full path of the input image
            # input_image_path = os.path.join(input_file)

            # Open the image file
            extension = input_file.split('.')[-1]

            # skip the below formats
            if extension.lower() in ["opus", "m4a"]:
                continue

            if extension.lower() in ["mp4", "MP4", "mpg", "MPG", "AVI", "avi", "m4v", "mov", "MOV"]:
                # method call returns filename if passed and False if failed
                file_name = compress_video.compress_video(input_file, output_dir,size_upper_bound= 40 * 600)
                if file_name:
                    print("video is processed successfully", file_name)
                else:
                    print("video is copied as compression failed", input_file)
                    shutil.copy(input_file, output_file)
                continue

            if extension.lower() in ["pdf", "PDF", "gif", "xlsx", "docx", "xls", "txt", "mp3"]:
                shutil.copy(input_file, output_file)
                continue


            if extension not in ["DS_Store"]:
                image = Image.open(input_file)
                if image.mode == "RGBA":
                    # Convert RGBA to RGB (remove alpha channel)
                    image = image.convert("RGB")

                # Calculate the aspect ratio
                width, height = image.size
                aspect_ratio = width / height

                # Calculate the new dimensions while maintaining the aspect ratio
                if width > max_width or height > max_height:
                    if width > height:
                        new_width = max_width
                        new_height = int(max_width / aspect_ratio)
                    else:
                        new_height = max_height
                        new_width = int(max_height * aspect_ratio)
                else:
                    # No resizing necessary
                    new_width = width
                    new_height = height

                # Resize the image
                resized_image = image.resize((new_width, new_height))


                # Save the resized image
                resized_image.save(output_file)

        except Exception as error:
            shutil.copy(input_file, output_file)
            print("while processing {} exception happened {} so copied directly".format( input_file, error))

def read_files_in_directory(root_dir):
    all_files = []
    new_dirs = set()
    file_types = set()

    try:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                all_files.append(file_path)
                new_dirs.add(dirpath[len(root_dir):])
                file_types.add(filename.split(".")[-1])
        print("types of files are {}".format(file_types))
        return all_files, new_dirs
    except Exception as error:
        print(error)

def create_new_dirs(new_dirs, root_op_folder):
    for dir in new_dirs:
        path = os.path.join(root_op_folder, dir)
        if not os.path.exists(path):
            os.makedirs(path)


# Example usage
root_op_folder = "/Users/santhiya/Documents/multimedia_mac/compressed/"
input_folder = '/Users/santhiya/Documents/multimedia_mac/lucky_marriage'
root_ip_folder = input_folder.split("/")[-1]
# output_folder = '/Users/santhiya/Documents/multimedia/compressed/nikon_compressed'
# max_width = 960
# max_height = 720

# max_width = 480
# max_height = 360
#
# max_width = 1200
# max_height = 900

# max_width = 1440
# max_height = 1080

max_width = 1584
max_height = 1188

all_files, new_dirs = read_files_in_directory(input_folder)

# Parallel(n_jobs=5)(delayed(reduce_image_size)(os.path.join(input_folder, folder), output_folder, folder, max_width, max_height)
#                     for folder in folders)
reduce_image_size(all_files, input_folder, root_ip_folder, root_op_folder, max_width, max_height)
print("------------completed---------------")
