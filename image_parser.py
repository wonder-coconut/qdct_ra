from PIL import Image
from sty import bg, rs
from sty import Style, RgbBg

def display_image(image,dim):
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            pixel_val = image[i * dim + j]
            bg.pixel = Style(RgbBg(pixel_val, pixel_val, pixel_val))
            pixel = bg.pixel + '  ' + bg.rs
            print(pixel, end = '')
            j += 1
        print()
        i += 1

def get_image_pixel_array(filepath,dim):
    im = Image.open(filepath)
    image_array = []
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            colour_pixel = im.getpixel((j,i))
            bw_pixel = int((colour_pixel[0] + colour_pixel[1] + colour_pixel[2])/3)
            image_array.append(bw_pixel)
            j += 1
        i += 1
    return image_array

dim = 16
image = get_image_pixel_array("assets/test3.jpg",dim)
display_image(image,dim)