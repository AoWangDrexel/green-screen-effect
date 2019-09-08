from PIL import Image

# The function compares the areas of both images and returns the smaller
# height and width


def smaller_size(img1, img2):
    area1, area2 = get_area(img1), get_area(img2)
    if area1 < area2:
        return img1.size
    return img2.size

# The function returns the area of the image


def get_area(img):
    width, height = img.size
    return width * height

# The function returns the red, green, blue values of the pixel


def get_pixel(img, x, y):
    r, g, b = img.getpixel((x, y))
    return r, g, b

# The function takes the frontground image and replaces the green with the
# background pixels


def green_screen(img1, img2):

    # comparing both areas of the images and resizing the bigger image
    # so both images are the same size
    area = smaller_size(img1, img2)
    if get_area(img1) > get_area(img2):
        img1 = img1.resize(area)
    elif get_area(img1) < get_area(img2):
        img2 = img2.resize(area)

    # takes each pixel of frontground and see if the green value is greater than
    # the sum of the red and blue values, if they are, then replace the pixels with
    # pixels from the background
    px1 = img1.load()
    for x in range(area[0]):
        for y in range(area[1]):
            pixel = get_pixel(img1, x, y)
            if pixel[0] + pixel[2] < pixel[1]:
                px1[x, y] = get_pixel(img2, x, y)
    return img1


def main():
    fore = input("Foreground: ")

    # Creates the Image object for foreground and background
    # But checks inputs to prevent exceptions
    error1 = True
    error2 = True
    
    while error1:
        try:
            fore = Image.open(fore)
            error1 = False
        except (FileNotFoundError, OSError, AttributeError) as e:
            error1 = True
            e = str(e)
            if e == "'str' object has no attribute 'read'":
                print("No foreground image file input.")
            elif "[Errno 2] No such file or directory:" in e:
                print("Foreground image file is not found.")
            else:
                print("Foreground image file type is not supported. Convert image to JPEG.")
            fore = input("Foreground: ")
            
    back = input("Background: ")
    while error2:    
        try:
            back = Image.open(back)
            error2 = False
        except (FileNotFoundError, OSError, AttributeError) as e:
            error2 = True
            e = str(e)
            
            if e == "'str' object has no attribute 'read'":
                print("No background image file input.")
            elif "[Errno 2] No such file or directory:" in e:
                print("Background image file is not found. ")
            else:
                print("Background image file type is not supported. Convert image to JPEG. ")
            back = input("Background: ")
            
    new_image = green_screen(fore, back)

    # saves the new image
    new_image.save("new-image.jpg", "JPEG")
    print("Completed!")
    new_image.show()


if __name__ == "__main__":
    main()
