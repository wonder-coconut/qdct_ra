import classical_dct

image_filepath = "assets/test_8.jpg"
dim = 8
#img = get_image_pixel_array(image_filepath,dim,False)
img = [16,11,10,16,24,40,51,61,12,12,14,19,26,58,60,55,14,13,16,24,40,57,69,56,14,17,22,29,51,87,80,62,18,22,37,56,68,109,103,77,24,35,55,64,81,104,113,92,49,64,78,87,103,121,120,101,72,92,95,98,112,100,103,99]
display_image(img,dim)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
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

display_image(mat_decoded,dim)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

op_filepath = f"assets/output_{dim}_cdct.png"
write_image_to_file(mat_decoded,dim,op_filepath)