import os
from PIL import Image
from time import sleep
from tqdm import tqdm

# configure max_width and height to alter size
def reduce_image_size(input_folder, output_folder, max_width, max_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the files in the input folder
    for filename in tqdm(os.listdir(input_folder)):
        # Get the full path of the input image
        filename = "IMG-20171126-WA0008.jpg"
        try:
            input_image_path = os.path.join(input_folder, filename)

            # Open the image file
            extension = input_image_path.split('.')[-1]
            if extension not in ["DS_Store", "mp4"]:
                image = Image.open(input_image_path)
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

                # Get the output path for the resized image
                output_image_path = os.path.join(output_folder, filename)

                # Save the resized image
                resized_image.save(output_image_path)
        except Exception as error:
            print("while processing {} exception happened {}".format( filename, error))

# Example usage
input_folder = '/Users/santhiya/Documents/multimedia/DCIM/Takeout/GooglePhotos/Photosfrom2017'
output_folder = '/Users/santhiya/Documents/multimedia/compressed/test_delete'
max_width = 2400
max_height = 1800

reduce_image_size(input_folder, output_folder, max_width, max_height)
print("------------completed---------------")
