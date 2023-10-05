from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.extensions import UnitaryGate
import matplotlib.pyplot as plt
import math
import numpy as np
import sys

def get_C_gate(length):

    N = length
    theta = (2*math.pi)/(4*N)
    omega = complex(math.cos(theta), math.sin(theta))
    omega_conj = np.conj(omega)
    
    C_matrix = [[1,0],[0,omega_conj]]
    C_gate = UnitaryGate(C_matrix,label='C')
    qc = QuantumCircuit(1)
    qc.append(C_gate,[0])

get_C_gate(int(sys.argv[1]))