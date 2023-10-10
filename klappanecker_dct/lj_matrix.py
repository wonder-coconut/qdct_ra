from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.extensions import UnitaryGate
import matplotlib.pyplot as plt
import math
import numpy as np
import sys

def get_lj_gate(length, index):
    N = length
    theta = (2*math.pi)/(4*N)
    omega = complex(math.cos(theta), math.sin(theta))
    exponent = math.pow(2,index - 1)
    omega_exp = np.power(omega,exponent)
    lj_matrix = [[1,0],[0,omega_exp]]
    lj_gate = UnitaryGate(lj_matrix,label = f'L{index}')
    return lj_gate

def circuit(length):
    qc = QuantumCircuit(length)
    for i in range(1,length):
        lj_gate = get_lj_gate(length,i).control(1)
        lj_gate.ctrl_state = '0'
        qc.append(lj_gate, [0,i])
    return qc