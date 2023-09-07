import math
from image_parser import get_image_pixel_array,display_image, write_image_to_file

def print_mat(mat,dim):
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            if(isinstance(mat[i*dim + j],float)):
                print('%.2f'%mat[i*dim + j], end = '\t')
            else:
                print(mat[i*dim + j], end = '\t')
            j += 1
        print()
        i += 1

def mat_mult(mat1,mat2,dim):
    mat_res = [0]*dim*dim
    i = j = k = 0
    while(i < dim):
        j = 0
        while(j < dim):
            k = 0
            while(k < dim):
                mat_res[i*dim + j] += mat1[i*dim + k] * mat2[k*dim + j]
                k += 1
            j += 1
        i += 1
    return mat_res

def mat_div(mat1,mat2,dim,roundflag,multflag):
    mat_res = [0]*dim*dim
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            if(multflag):
                mat_res[i*dim + j] = mat1[i*dim + j]*mat2[i*dim + j]
            else:
                mat_res[i*dim + j] = mat1[i*dim + j]/mat2[i*dim + j]
            if(roundflag):
                mat_res[i*dim + j] = round(mat_res[i*dim + j])
            j += 1
        i += 1
    return mat_res

def transpose(mat,dim):
    mat_res = [0]*dim*dim
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            mat_res[i*dim + j] = mat[j*dim + i]
            j += 1
        i += 1
    return mat_res

def get_dct_matrix(dim):
    dct_mat = [0]*dim*dim
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            if(i == 0):
                #print('null',end='\t')
                temp = 1/math.sqrt(dim)
            else:
                theta = ((2*j+1)*i)/(2*dim)
                #print(theta, end='\t')
                temp = math.sqrt(2/dim)*math.cos(((2*j+1)*i*math.pi)/(2*dim))
            dct_mat[i*dim + j] = temp
            j += 1
        #print()
        i += 1
    #print('--------------')
    return dct_mat
