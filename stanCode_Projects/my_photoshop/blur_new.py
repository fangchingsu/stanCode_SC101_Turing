from simpleimage import SimpleImage

N_TIMES = 9


def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(N_TIMES):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(old_image):
    blurred = SimpleImage.blank(old_image.width,  old_image.height)
    for y in range(old_image.height):
        for x in range(old_image.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < old_image.width:
                        if 0 <= pixel_y < old_image.height:
                            pixel = old_image.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = r_sum/count
            new_pixel.green = g_sum/count
            new_pixel.blue = b_sum / count
    return blurred


if __name__ == '__main__':
    main()
