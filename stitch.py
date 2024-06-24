from PIL import Image
import os

def combine_images(image_sets, output_path):
    # Get the list of image names from the first set
    image_names = sorted(os.listdir(image_sets[0]))
    
    for image_name in image_names:
        # Get the full paths for the images to combine
        images = [Image.open(os.path.join(image_set, image_name)) for image_set in image_sets]
        
        # Create a new image with a width of 3240 pixels (1080 * 3) and a height of 1080 pixels
        combined_image = Image.new('RGB', (1080 * 3, 1080))

        # Paste the three images side by side
        for j, img in enumerate(images):
            combined_image.paste(img, (j * 1080, 0))

        # Save the combined image
        combined_image.save(os.path.join(output_path, f'combined_{image_name}'))
        print(image_name)

# Set the paths to the image sets and the output directory
set1_path = 'structuredTarget-24/images/scatter-cropped/'
set2_path = 'structuredTarget-21/images/scatter-cropped/' 
set3_path =  'structuredTarget-27/images/scatter-cropped/'
output_path = 'structuredTarget-nc5-60-a02p4/'

# List of image set paths
image_sets = [set1_path, set2_path, set3_path]

# Make sure the output directory exists
os.makedirs(output_path, exist_ok=True)

# Combine the images
combine_images(image_sets, output_path)

print('Done !')

