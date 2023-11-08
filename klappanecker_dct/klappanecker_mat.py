import dct_dst
import sys
import numpy as np

def convert_to_2D(mat,n):
    net_mat = [ [0] *n for i in range(n)]
    i = j = 0
    while(i < n):
        j = 0
        while(j < n):
            net_mat[i][j] = mat[i*n + j]
            j += 1
        i += 1
    return net_mat

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
            
def get_klappanecker_mat(transform_type,n):
    dct = dst = 0
    if(transform_type == 1):
        pass
    elif(transform_type == 2 or transform_type == 3 or transform_type == 4):
        dct = dct_dst.get_dct_mat(transform_type,n)
        dst = dct_dst.get_dst_mat(transform_type,n)
        dst = np.dot(complex(0,1),dst)
    
    mat = direct_sum(dct,dst,n)
    mat = convert_to_2D(mat,2*n)
    return mat