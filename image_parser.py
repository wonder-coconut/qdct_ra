from PIL import Image
from sty import bg, rs
from sty import Style, RgbBg

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

image = get_image_pixel_array("assets/test3.jpg",16)
print(image)