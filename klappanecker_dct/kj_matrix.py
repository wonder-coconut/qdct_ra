from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.extensions import UnitaryGate
import matplotlib.pyplot as plt
import math
import numpy as np
import sys

def get_kj_gate(length, index):
    N = length
    theta = (2*math.pi)/(4*N)
    omega = complex(math.cos(theta), math.sin(theta))
    omega_conj = np.conj(omega)
    exponent = math.pow(2,index - 1)
    omega_exp = np.power(omega_conj,exponent)
    kj_matrix = [[1,0],[0,omega_exp]]
    kj_gate = UnitaryGate(kj_matrix,label = f'L{index}')
    return kj_gate

def circuit(length,index):
    qc = QuantumCircuit(length)
    for i in range(1,length):
        kj_gate = get_kj_gate(length,i).control(1)
        qc.append(kj_gate, [0,i])
    return qc

qc = circuit(4,1)
print(qc)