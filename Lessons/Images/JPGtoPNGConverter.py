import sys
import os
from PIL import Image

image_folder = sys.argv[0]
output_folder = sys.argv[1]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{output_folder}{filename}.png', 'png')
    print('all done!')
    
