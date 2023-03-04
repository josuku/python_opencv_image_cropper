import cv2
import sys
from os import path
from pathlib import Path

if len(sys.argv) <= 1:
    sys.exit('file path is not included')

file_path = sys.argv[1]

if not path.exists(file_path): 
    sys.exit('file path doesnt exist')

# Load the larger image
img = cv2.imread(file_path)

# get dimensions of image
dimensions = img.shape

# number of images in x and y axis
images_x = 5
images_y = 6
print(str(images_x) + ' horizontal images')
print(str(images_y) + ' vertical images')

# height, width, number of channels in image
h = img.shape[0]/images_y
w = img.shape[1]/images_x
channels = img.shape[2]
print('Image Dimension    : ',dimensions)
print('Image Height       : ',h)
print('Image Width        : ',w)
print('Number of Channels : ',channels)

x = 0
y = 0
for i in range(images_y):
    for j in range(images_x):
        # set end positions
        new_y = int(y + h)
        new_x = int(x + w)
        print(' -  image:(' + str(i) + ',' + str(j) + ') new_x:' + str(new_x) + ' new_y:' + str(new_y)) 

        # Crop the smaller image from the larger image
        roi = img[y:new_y, x:new_x]

        # set new end position to x
        x = int(x + w)
  
        # Save the cropped image to a file
        name = Path(file_path).stem
        filename = 'mini_' + name + '_' + str(i) + '-' + str(j) + '.jpg'
        cv2.imwrite('./' + filename, roi)

    # reset x position and set new y position
    x = 0
    y = int(y + h)

