"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: SimpleImage, the file path of the original image
    :return new_img: SimpleImage, photo height is 2 times larger than original photo and get its mirror photo
    """
    # setup new image size
    new_img = SimpleImage.blank(filename.width, filename.height * 2)
    # run the height and width in original photo
    for y in range(filename.height):
        for x in range(filename.width):
            # get original photo pixel
            img_pixel = filename.get_pixel(x, y)
            # get up and down pixel
            new_pixel1 = new_img.get_pixel(x, y)
            new_pixel2 = new_img.get_pixel(x, new_img.height-1-y)
            # fill the up empty pixel in new image
            new_pixel1.red = img_pixel.red
            new_pixel1.green = img_pixel.green
            new_pixel1.blue = img_pixel.blue
            # fill the down empty pixel in new image
            new_pixel2.red = img_pixel.red
            new_pixel2.green = img_pixel.green
            new_pixel2.blue = img_pixel.blue
    # return updated new image
    return new_img


def main():
    """
    read the original photo and get its mirror photo
    """
    # read the original photo
    original_mt = SimpleImage('images/mt-rainier.jpg')
    # show photo
    original_mt.show()
    # update photo
    reflected = reflect(original_mt)
    # show updated photo
    reflected.show()


if __name__ == '__main__':
    main()
