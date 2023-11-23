from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.extensions import UnitaryGate
import sys
import math
import matplotlib.pyplot as plt
import numpy as np

import klappanecker_mat
import qc_simulation_helper
from binary_helper import binary_to_dec,decimal_to_binary


def print_mat(mat):
    for i in mat:
        for j in i:
            print('{:.2f}'.format(j),end='\t')
        print()

def dct(n):
    op_mat = klappanecker_mat.get_klappanecker_mat(2,n)
    print_mat(op_mat)
    op_gate = UnitaryGate(op_mat, label='dct/dst')
    return op_gate

def qc_gen(n):
    
    qc = QuantumCircuit(n)
        
    len_op = int(math.pow(2,n-1))
    dct_op = dct(len_op)
    dct_op_transpose = dct_op.transpose()
    dct_op_transpose.label = 'dct/dst_trans'
    qc.append(dct_op_transpose,[*range(n)])
    return qc

def simulate(qc,qc_shots):
    aer_sim = Aer.get_backend('unitary_simulator')
    job = execute(qc, aer_sim, shots=qc_shots)
    result = job.result()
    print(result.get_unitary(qc,3))


qc = qc_gen(int(sys.argv[1]))
#vector = qc_simulation_helper.simulate_vector(qc,1024,False)
#counts = simulate(qc,1024)
print(qc)
simulate(qc,8192)
#vector = np.asarray(vector)
#for i in vector:
#    print(i)
#plot_distribution(counts)
#plt.show()