import greenscreen
from PIL import Image
import os

# The function loads the images from the folder from the desktop
def load_images():
    global f_entries
    global b_entries
    f_entries = os.listdir('Desktop/foreground')
    b_entries = os.listdir('Desktop/background')

# The function returns the name of the file
def get_filename(file):
    return os.path.splitext(file)[0]

load_images()    
foreground_images = []
background_images = []

# Creates the image object for all of the images
for f in f_entries[1:]:
    f = Image.open(f)
    foreground_images.append(f)
    
for b in b_entries[1:]:
    b = Image.open(b)
    background_images.append(b)

# Using the green screen module to create the new images
version = 0
idx = 1
for f in foreground_images:
    for b in background_images:
        greenscreen.green_screen(f, b).save("new" + get_filename(f_entries[idx]) + str(version) + ".jpg", "JPEG")
        greenscreen.green_screen(f, b).show()
        version += 1
    idx += 1
