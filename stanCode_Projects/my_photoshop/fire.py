"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage

# Constant
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: SimpleImage, the file path of the original image
    :return filename: updated image
    """
    # run the pixel in photo
    for pixel in filename:
        # calculate average pixel in photo
        avg = (pixel.red + pixel.green + pixel.blue)/3
        # judge fire
        if pixel.red > avg*HURDLE_FACTOR:
            # change pixel value
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # change pixel value
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    # return updated photo
    return filename


def main():
    """
    detect the fire and change it to red
    let others part to grayscale
    """
    # read the original photo
    original_fire = SimpleImage('images/greenland-fire.png')
    # show photo
    original_fire.show()
    # update photo
    highlighted_fire = highlight_fires(original_fire)
    # show updated photo
    highlighted_fire.show()


if __name__ == '__main__':
    main()
