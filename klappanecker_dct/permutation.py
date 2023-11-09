from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.x import XGate

import matplotlib.pyplot as plt
import math
import sys

def permutation_gate(length):
    qc = QuantumCircuit(length)
    i = 0
    while(i < length):
        if(length - i - 1 > 0):
            control_parameter = [*range(i + 1,length)]
            control_parameter.append(i)
            cnx = XGate().control(length - i - 1)
            qc.append(cnx,control_parameter)
        else:
            qc.x(i)
        i += 1
        
    perm_gate = qc.to_gate(label='permutation')
    return perm_gate