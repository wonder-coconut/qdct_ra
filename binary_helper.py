def decimal_to_binary(num, limit):
    length = 8
    bin_s = ''

    while(num > 0):
        bin_s = str(num%2) + bin_s
        num = int(num/2)

    if(len(bin_s) > limit):
        print("error: overflow")
        return None
    
    padding = limit - len(bin_s)
    i = 0

    while(i < padding):
        i += 1
        bin_s = '0' + bin_s
    return bin_s

def binary_to_dec(s,size):
    i = n = 0
    while(i < size):
        n += int(s[i])*pow(2,size - i - 1)
        i += 1
    return n

#test comment