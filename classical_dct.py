import math
from image_parser import get_image_pixel_array,display_image

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
                temp = 1/math.sqrt(dim)
            else:
                temp = math.sqrt(2/dim)*math.cos(((2*j+1)*i*math.pi)/(2*dim))
            dct_mat[i*dim + j] = temp
            j += 1
        i += 1
    return dct_mat

image_filepath = "assets/test_8.jpg"
dim = 8
img = get_image_pixel_array(image_filepath,dim,False)
display_image(img,dim)
img = [pixel - 128 for pixel in img]

#encoding
dct = get_dct_matrix(dim)
dct_trans = transpose(dct,dim)
q50 = [16,11,10,16,24,40,51,61,12,12,14,19,26,58,60,55,14,13,16,24,40,57,69,56,14,17,22,29,51,87,80,62,18,22,37,56,68,109,103,77,24,35,55,64,81,104,113,92,49,64,78,87,103,121,120,101,72,92,95,98,112,100,103,99]
mat_dct = mat_mult(mat_mult(dct,img,dim),dct_trans,dim)
mat_quant = mat_div(mat_dct,q50,dim,True,False)

#decoding
mat_unquant = mat_div(mat_quant,q50,dim,True,True)
mat_dct_inv = mat_mult(mat_mult(dct_trans,mat_unquant,dim),dct,dim)
mat_decoded = [(128 + round(pixel)) for pixel in mat_dct_inv]
