"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: SimpleImage, the file path of the original image
    :return img: SimpleImage, the photo is 4 times smaller than original photo
    """
    # setup new image size
    new_img = SimpleImage.blank(filename.width//2, filename.height//2)
    # run the height in original photo
    for y in range(filename.height):
        # judge odd and even pixel in y
        if y % 2 == 0:
            # run the width in original photo
            for x in range(filename.width):
                # judge odd and even pixel in x
                if x % 2 == 0:
                    # get original photo pixel
                    img_pixel = filename.get_pixel(x, y)
                    # get new image pixel
                    new_pixel = new_img.get_pixel(x//2, y//2)
                    # fill the empty pixel in new image
                    new_pixel.red = img_pixel.red
                    new_pixel.green = img_pixel.green
                    new_pixel.blue = img_pixel.blue
    # return updated new image
    return new_img


def main():
    """
    4 times shrink the original photo
    """
    # read the original photo
    original = SimpleImage("images/poppy.png")
    # show photo
    original.show()
    # update photo
    after_shrink = shrink(original)
    # show updated photo
    after_shrink.show()


if __name__ == '__main__':
    main()
