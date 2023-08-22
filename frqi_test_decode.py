from binary_helper import binary_to_dec
import math

counts = "{'101': 8144, '001': 8319, '111': 16240, '110': 2476, '000': 16384, '010': 13973}"
counts = counts[1:len(counts)-1].split(',')
shots = 65536
dim = 2
limit = len(counts)
image_data = [0 for i in range(dim * dim)]

i = 0
j = 0
while(i < limit):
    counts[i] = (counts[i]).strip()
    binary = counts[i][1:4]
    state = int(binary[0])
    pos = binary[1:len(binary)]
    pos = pos[::-1]
    amp = int(counts[i][counts[i].rfind(':') + 1:len(counts[i])].strip())/shots
    index = binary_to_dec(pos,2)
    if(image_data[index] == 0):
        image_data[index] = {}
        image_data[index][0] = 0
        image_data[index][1] = 0
    image_data[index][state] = amp
    i += 1

for pixel in image_data:
    a = pixel[0]
    b = pixel[1]
    s = math.sqrt(a*a + b*b)
    a = a/s
    b = b/s

    theta = math.acos(a)
    pixel_val = theta/(math.pi/2) * 256
    print(pixel_val)