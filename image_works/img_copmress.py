import os
from PIL import Image

# configure max_width and height to alter size
def reduce_image_size(input_folder, output_folder, max_width, max_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the files in the input folder
    for filename in os.listdir(input_folder):
        # Get the full path of the input image
        input_image_path = os.path.join(input_folder, filename)

        # Open the image file
        image = Image.open(input_image_path)

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

# Example usage
input_folder = '/Users/santhiya/Documents/multimedia/DCIM/Camera/images'
output_folder = '/Users/santhiya/Documents/multimedia/compressed'
max_width = 2400
max_height = 1800

reduce_image_size(input_folder, output_folder, max_width, max_height)
