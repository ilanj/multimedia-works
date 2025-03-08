import os
import shutil

from tqdm import tqdm


def get_filenames(path):
    return os.listdir(path)

def get_missed_files(original, converted):
    missing_files = [file for file in original if file not in converted]
    # missing_files = [file for file in converted_files_renamed if file not in original_files]
    print(missing_files)
    return  missing_files

def get_file_sizes(original_files, path):
    sum = 0
    for file in original_files:
        file = os.path.join(path, file)
        size = os.path.getsize(file)/1048576
        sum = sum + size
        print(file, size)
    print(sum/1024, " GB")

def copy_files(original_files, original_file_path, destination_path):
    for file in tqdm(original_files):
        destination_file = os.path.join(destination_path,file)
        file = os.path.join(original_file_path, file)
        shutil.copy(file, destination_file)

oppo = os.listdir("/Users/santhiya/Documents/multimedia/compressed/santhiya_vd/Photos from 2020")
iq = os.listdir("/Users/santhiya/Documents/multimedia/compressed/ilapiks_4/iqz3_images")
pool = oppo + iq

original_files_path = "/Users/santhiya/Documents/multimedia/DCIM/ila-619/Google Photos/Bin"
converted_files_path = "/Users/santhiya/Documents/multimedia/DCIM/ila-18/Drive/engagement/engagement/engagement"
destination_path = "/Users/santhiya/Documents/multimedia/DCIM/ila-619/Google Photos/oppo+iq/"

original_files = get_filenames(original_files_path)
# converted_files = get_filenames(converted_files_path)
converted_files_renamed = []

# for file in converted_files:
#     file = file.replace("_compressed_","")
#     converted_files_renamed.append(file)

get_missed_files(original_files, pool)
# get_file_sizes(original_files, original_files_path)
copy_files(get_missed_files(original_files, pool),
           original_files_path, destination_path)





