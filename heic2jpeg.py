from PIL import Image
import pillow_heif
import os

print('Welcome to Heic2 converter')

input_file = input('Please enter the file path to the .heic pictures ? ')
if input_file not in ['.heic']:
    print('invalid format choose .heic format')

Image.open(input_file)

output_file = input ('Please enter the output file you would like to save it to ? ')

if output_file not in ['jpeg', 'png', 'jpg']:
    print('invalid request ')

for file in os.listdir(input_file):
    if file.lower().endswith('.heic'):
        
    



# import os
# from PIL import Image
# import pillow_heif

# # Function to convert HEIC files to another format
# def convert_heic_to_format(folder, format):
#     # Go through all files in the folder
#     for file in os.listdir(folder):
#         # If the file is a .heic file
#         if file.lower().endswith('.heic'):
#             heic_path = os.path.join(folder, file)  # Get full path to the file
#             image = Image.open(heic_path)  # Open the HEIC image
#             output_path = heic_path.rsplit('.', 1)[0] + '.' + format  # New file name with desired format
#             image.save(output_path, format=format.upper())  # Save it as the new format
#             print(f"Converted {file} to {output_path}")  # Let the user know

# # Folder with your HEIC files
# folder = "./heic_images"  # Put your folder path here

# # Format you want to convert to (e.g., 'jpeg', 'png')
# format = "jpeg"  # You can change this to "png" if you want

# # Call the function to convert the files
# convert_heic_to_format(folder, format)

