import dct_dst
import sys
import numpy as np

def direct_sum(m1,m2,n):
    mat = [0]*4*n*n
    i = j = 0
    while(i < n):
        j = 0
        while(j < n):
            mat[i*2*n + j] = m1[i*n + j]
            mat[(i+n)*2*n + (j+n)] = m2[i*n + j]
            j += 1
        i += 1
    return mat
            

transform_type = int(sys.argv[1])
n = int(sys.argv[2])

dct = dst = 0

if(transform_type == 1):
    pass
elif(transform_type == 2 or transform_type == 3 or transform_type == 4):
    dct = dct_dst.get_dct_mat(transform_type,n)
    dst = dct_dst.get_dst_mat(transform_type,n)

mat = direct_sum(dct,dst,n)
dct_dst.print_mat(dct)
print('-=-=-=-=-=-=-=')
dct_dst.print_mat(dst)
print('-=-=-=-=-=-=-=')
dct_dst.print_mat(mat)