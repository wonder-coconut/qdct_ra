import math
import sys

def b_coeff(k,n):
    b = 0
    if(k < 0 or k > n):
        b = 0
    elif(k == 0 or k == n):
        b = 1/math.sqrt(2)
    elif(k > 0 and k < n):
        b = 1
    return b

def get_dct_mat(transform_type, n):
    sqrt_coeff = math.sqrt(2/n)
    if(transform_type == 1):
        dim = n + 1
    else:
        dim = n
    
    mat_res = [0]*dim*dim
    
    i = j = 0

    while(i < dim):
        j = 0
        while(j < dim):
            if(transform_type == 1):
                mat_res[i*dim + j] = b_coeff(i,n) * b_coeff(j,n) * sqrt_coeff * math.cos((math.pi * i * j)/n)
            elif(transform_type == 2):
                mat_res[i*dim + j] = b_coeff(i,n) * sqrt_coeff * math.cos((math.pi * i * (j + 0.5))/n)
            elif(transform_type == 3): 
                mat_res[i*dim + j] = b_coeff(j,n) * sqrt_coeff * math.cos((math.pi * (i + 0.5) * j)/n)
            elif(transform_type == 4):
                mat_res[i*dim + j] = sqrt_coeff * math.cos((math.pi * (i + 0.5) * (j + 0.5))/n)
            j += 1
        i += 1

    return mat_res

def get_dst_mat(transform_type, n):
    sqrt_coeff = math.sqrt(2/n)
    if(transform_type == 1):
        dim = n - 1
    else:
        dim = n
    
    mat_res = [0]*dim*dim

    i = j = 0

    while(i < dim):
        j = 0
        while(j < dim):
            if(transform_type == 1):
                mat_res[i*dim + j] = sqrt_coeff * math.sin((math.pi * i * j)/n)
            elif(transform_type == 2):
                mat_res[i*dim + j] = b_coeff(i + 1,n) * sqrt_coeff * math.sin((math.pi * (i + 1) * (j + 0.5))/n)
            elif(transform_type == 3): 
                mat_res[i*dim + j] = b_coeff(j + 1,n) * sqrt_coeff * math.sin((math.pi * (i + 0.5) * (j + 1))/n)
            elif(transform_type == 4):
                mat_res[i*dim + j] = sqrt_coeff * math.sin((math.pi * (i + 0.5) * (j + 0.5))/n)
            j += 1
        i += 1
    
    return mat_res

def print_mat(mat):
    dim = int(math.sqrt(len(mat)))
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            print('{:.2f}'.format(mat[i*dim + j]), end='\t')
            j += 1
        print()
        i += 1