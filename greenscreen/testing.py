import greenscreen
import os
from PIL import Image

# The function loads the images from the folder from the desktop


def load_images():
    global f_entries
    global b_entries
    f_entries = os.listdir('Desktop/img resource/foreground')
    b_entries = os.listdir('Desktop/img resource/background')

# The function returns the name of the file


def get_filename(file):
    return os.path.splitext(file)[0]

# The function creates Image objects and stores them in individual lists


def create_image_list():
    global foreground_images
    global background_images
    foreground_images = []
    background_images = []

    # Creates the image object for all of the images
    for foreground in f_entries[1:]:
        foreground = Image.open(foreground)
        foreground_images.append(foreground)

    for background in b_entries[1:]:
        background = Image.open(background)
        background_images.append(background)

# The function saves the new images using the green screen module


def save_image():
    version = 0
    idx = 1
    for foreground in foreground_images:
        for background in background_images:
            greenscreen.green_screen(
                foreground,
                background).save(
                "new" +
                get_filename(
                    f_entries[idx]) +
                str(version) +
                ".jpg",
                "JPEG")
            greenscreen.green_screen(foreground, background).show()
            version += 1
        idx += 1

# The main function


def main():
    load_images()
    create_image_list()
    save_image()
    print("Done!")


if __name__ == "__main__":
    main()
