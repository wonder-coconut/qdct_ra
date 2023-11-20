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
    op_gate = UnitaryGate(op_mat, label='dct/dst')
    return op_gate

def cnry(theta,n):
    theta_s = '%.2f'%theta
    cnry = QuantumCircuit(n + 1, name=f'cnry{theta_s}')
    theta /= math.pow(2,n-2)
    theta = -theta

    i = j = 0
    while(i < n):
        j = 0
        a = 0
        b = i
        temp = i - 1
        diff = 1
        while(j < math.pow(2,i)):

            if(i == 0):
                pass

            elif(i == 1):
                temp = i - 1
                cnry.cx(temp,i)

            else:
                cnry.cx(temp,i)
                c1 = temp + diff < a
                c2 = temp + diff >= b

                if(c1 and c2):
                    diff = 0
                elif c1:
                    diff = - diff
                elif c2:
                    diff = - diff
                
                temp += diff


            
            theta = -theta
            cnry.cry(theta,i,n)
            j += 1
        i += 1
    
    #cnry.draw(output = 'mpl')
    #plt.show()
    
    cnry_inst = cnry.to_instruction()
    return cnry_inst

def qc_gen(theta, length):
    
    pos_bits = int(math.log(length,2))
    n = 2 * pos_bits
    pos_reg = QuantumRegister(pos_bits,'position')
    phase_reg = QuantumRegister(1, 'grayscale')
    dct_reg = QuantumRegister(pos_bits + 1,'dct')
    qc = QuantumCircuit(pos_reg,phase_reg,dct_reg)
    
    #qc.x(0)
    #qc.x(1)
    
    qubits_frqi = []
    for qubit in pos_reg:
        qubits_frqi.append(qubit)
    for qubit in phase_reg:
        qubits_frqi.append(qubit)
    
    qubits_dct = []
    for qubit in dct_reg:
        qubits_dct.append(qubit)
    
    qc.barrier()
    
    qc.h(pos_reg)

    len_op = int(math.pow(2,n-2))
    qc.append(dct(len_op),qubits_dct)

    pos_id = 0

    for angle in theta:
        qc.barrier()
        pos_id_bin = decimal_to_binary(pos_id,pos_bits)

        i = 0
        while(i < pos_bits):
            if(pos_id_bin[i] == '1'):
                qc.x(pos_reg[pos_bits - 1 - i])
            i += 1
        
        qc.append(cnry(angle,pos_bits),qubits_frqi)

        i = 0
        while(i < pos_bits):
            if(pos_id_bin[i] == '1'):
                qc.x(pos_reg[pos_bits - 1 - i])
            i += 1
        pos_id += 1

    qc.barrier()
    return qc


length = int(sys.argv[1])
image = [int((i+1) * (256/length) - 1) for i in range(length)]
theta = [(pixel * (math.pi/(256*2))) for pixel in image]

qc = qc_gen(theta, length)
vector = qc_simulation_helper.simulate_vector(qc,1024,False)
#counts = simulate(qc,1024)
print(qc)
#vector = np.asarray(vector)
#for i in vector:
#    print(i)
#plot_distribution(counts)
#plt.show()