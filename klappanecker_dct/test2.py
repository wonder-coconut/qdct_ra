import numpy as np
import math

def print_mat(mat):
    for i in mat:
        for j in i:
            print('{:.2f}'.format(j),end = '\t')
        print()

def b(i,n):
    if(i < 0 or i > n):
        return 0
    elif (i == 0 or i == n):
        return math.sqrt(1/2)
    elif (i > 0 and i < n):
        return 1

def get_dct_1(n):
    mat = [[0 for i in range(n)] for j in range(n)]
    i = 0
    j = 0
    while(i < n):
        j = 0
        while(j < n):
            mat[i][j] = b(i,n)*b(j,n)*math.sqrt(2/(n-1))*math.cos((i*j*math.pi)/(n-1))
            j += 1
        i += 1
    
    dct = np.array(mat)
    return dct

n = 5
un = [[0 for i in range(n+1)] for i in range(2*n)]
un[0][0] = math.sqrt(2)
un[5][5] = math.sqrt(2)

for i in range(1,n):
    un[i][i] = 1
    un[2*n - i][i] = 1

f2n = [[0 for i in range(2*n)] for j in range(2*n)]

i = 0
while(i < 2*n):
    f2n[0][i] = 1
    f2n[i][0] = 1
    i += 1

i = 1
j = 1
while(i < 2*n):
    j = 1
    while(j < 2*n):
        theta = 2*i*j*math.pi/(2*n)
        omega = complex(math.cos(theta), math.sin(theta))
        f2n[i][j] = omega
        j += 1
    i += 1

Un = np.array(un)
Un_h = Un.T.conj()
F2n = np.array(f2n)
dct = get_dct_1(n+1)
#res = np.matmul(np.matmul(Un_h,F2n),Un)
print_mat(dct)
