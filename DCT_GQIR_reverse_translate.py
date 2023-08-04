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

def binary_to_dec(s,size):
    i = n = 0
    while(i < size):
        n += int(s[i])*pow(2,size - i - 1)
        i += 1
    return n

def parse_to_image_array(data,dim,pos_bits):
    data = data.split(':')
    image_data = []
    for token in data:
        image_data.append(token[len(token) - 17:len(token) - 1])
        
    image_data.pop()

    image_len = dim * dim
    image = [0] * len
    for pixel in image_data:
        pixel = pixel[::-1]
        pos = binary_to_dec(pixel[8:],2*pos_bits)
        val = binary_to_dec(pixel[:8],8)
        image[len - pos - 1] = val
        
    return image
    

f = open("outputs/op4")
dim = 16
counts = f.read()
image = parse_to_image_array(counts,dim,4)
display_image(image,dim)