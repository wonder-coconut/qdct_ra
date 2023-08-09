from PIL import Image
from sty import bg, rs
from sty import Style, RgbBg
from binary_helper import *
import numpy

def write_image_to_file(image,dim,filepath):
    pixels = []
    i = j = 0
    while(i < dim):
        pixels.append([])
        j = 0
        while(j < dim):
            pixels[i].append(image[i * dim + j])
            j += 1
        i += 1
    
    img_array = numpy.array(pixels, dtype=numpy.uint8)
    
    new_image = Image.fromarray(img_array)
    new_image.save(filepath)

def display_image(image,dim):
#only works in terminal output
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

def get_image_pixel_array(filepath, dim, binflag):
    im = Image.open(filepath)
    fileformat = filepath[filepath.find('.'):]
    image_array = []
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            colour_pixel = im.getpixel((j,i))
            if(fileformat == '.png'):
                bw_pixel = colour_pixel
            else:
                bw_pixel = int((colour_pixel[0] + colour_pixel[1] + colour_pixel[2])/3)
            if(binflag):
                bw_pixel = decimal_to_binary(bw_pixel,8)
            image_array.append(bw_pixel)
            j += 1
        i += 1
    return image_array

def parse_to_image_array(data,dim,pos_bits):
    pos_bits = int(pos_bits)
    data = data.split(':')
    image_data = []
    for token in data:
        image_data.append(token[len(token) - (2*pos_bits + 8 + 1):len(token) - 1])
    image_data.pop()

    image_len = dim * dim
    image = [0] * image_len
    for pixel in image_data:
        pixel = pixel[::-1]
        pos = int(binary_to_dec(pixel[8:],2*pos_bits))
        val = int(binary_to_dec(pixel[:8],8))
        image[image_len - pos - 1] = val
        
    return image