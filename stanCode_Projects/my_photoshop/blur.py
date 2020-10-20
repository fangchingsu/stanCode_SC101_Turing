"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage

# CONSTANT
N_TIMES = 9


def blur(img):
    """
    :param img: SimpleImage , the file path of the original image
    :return new_img: SimpleImage, get the average pixel from each side of original image and save to new image
    """
    # setup new image size
    new_img = SimpleImage.blank(img.width, img.height)
    # run the height and width in original photo
    for y in range(img.height):
        for x in range(img.width):
            # get new image pixel
            new_pixel = new_img.get_pixel(x, y)
            count = 0
            # declare variable
            x1_y = x1_y1 = x1_y2 = x_y = x_y1 = x_y2 = x2_y = x2_y1 = x2_y2 = new_img.get_pixel(x, y)
            # judge x position
            if x - 1 >= 0:
                x1_y = img.get_pixel(x - 1, y)
                count += 1
                # judge y position
                if y - 1 >= 0:
                    x1_y1 = img.get_pixel(x - 1, y - 1)
                    count += 1
                # judge y position
                if y + 1 < img.height:
                    x1_y2 = img.get_pixel(x - 1, y + 1)
                    count += 1
            # judge x position
            if x == x:
                x_y = img.get_pixel(x, y)
                count += 1
                # judge y position
                if y - 1 >= 0:
                    x_y1 = img.get_pixel(x, y - 1)
                    count += 1
                # judge y position
                if y + 1 < img.height:
                    x_y2 = img.get_pixel(x, y + 1)
                    count += 1
            # judge x position
            if x + 1 < img.width:
                x2_y = img.get_pixel(x + 1, y)
                count += 1
                # judge y position
                if y - 1 >= 0:
                    x2_y1 = img.get_pixel(x + 1, y - 1)
                    count += 1
                # judge y position
                if y + 1 < img.height:
                    x2_y2 = img.get_pixel(x + 1, y + 1)
                    count += 1
            # calculate new image pixel and save to new image pixel
            new_pixel.red = (x1_y.red + x1_y1.red + x1_y2.red + x_y.red + x_y1.red + x_y2.red + x2_y.red + x2_y1.red +
                             x2_y2.red) / count
            new_pixel.green = (x1_y.green + x1_y1.green + x1_y2.green + x_y.green + x_y1.green + x_y2.green +
                               x2_y.green + x2_y1.green + x2_y2.green) / count
            new_pixel.blue = (x1_y.blue + x1_y1.blue + x1_y2.blue + x_y.blue + x_y1.blue + x_y2.blue + x2_y.blue +
                              x2_y1.blue + x2_y2.blue) / count
    # return updated new image
    return new_img


def main():
    """
    change the constant number to blur n times of the original photo
    """
    # read the original photo
    old_img = SimpleImage("images/smiley-face.png")
    # show photo
    old_img.show()
    # update photo
    blurred_img = blur(old_img)
    # update photo n+1 times
    for i in range(N_TIMES):
        blurred_img = blur(blurred_img)
    # show updated photo
    blurred_img.show()


if __name__ == '__main__':
    main()
