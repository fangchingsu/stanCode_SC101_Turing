"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimepleImage, the file path of the background image
    :param figure_img: SimepleImage, green screen figure image
    :return figure_img: SimepleImage, the green screen pixels are replaced by pixels background image
    """
    # run the pixel in background image
    for y in range(background_img.height):
        for x in range(background_img.width):
            # get figure image pixel
            figure = figure_img.get_pixel(x, y)
            # find greenscale
            if figure.green > figure.red * 2 or figure.green > figure.blue * 2:
                # get background image pixel
                background = background_img.get_pixel(x, y)
                # update figure pixel
                figure.red = background.red
                figure.blue = background.blue
                figure.green = background.green
    # return updated photo
    return figure_img


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop a person onto any background
    """
    # read the background image
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    # read the figure image
    figure = SimpleImage("images/ReyGreenScreen.png")
    # combine 2 photo
    result = combine(space_ship, figure)
    # show updated photo
    result.show()


if __name__ == '__main__':
    main()
