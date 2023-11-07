import classical_dct_dft
import sys

mat = classical_dct_dft.get_dct_matrix_2(int(sys.argv[1]))
classical_dct_dft.print_mat(mat,int(sys.argv[1]))