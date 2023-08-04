from PIL import Image
from sty import bg, rs
from sty import Style, RgbBg

im = Image.open(r"assets/test3.jpg")
px = im.load()
i = j = 0
dim = 16
while(i < dim):
    j = 0
    while(j < dim):
        colour = im.getpixel((j,i))
        bw_colour = int((colour[0] + colour[1] + colour[2])/3)
        bg.pixel = Style(RgbBg(bw_colour, bw_colour, bw_colour))
        pix = bg.pixel + '  ' + bg.rs
        print(pix,end = '')
        #print(colour,end = '')
        j += 1
    print()
    i += 1