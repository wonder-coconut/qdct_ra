from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library.standard_gates.x import XGate

import matplotlib.pyplot as plt
import math

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
    
    pi_inst = qc.to_instruction().control(1)
    return pi_inst

length = 9
qc = QuantumCircuit(length)
pn_gate = permutation_gate(length - 1)
control_parameter = [0]
control_parameter.append(*range(1,length))
qc.append(pn_gate,control_parameter)
print(qc)