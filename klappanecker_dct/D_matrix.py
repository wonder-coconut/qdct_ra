from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.extensions import UnitaryGate
from qiskit.circuit import Gate

import matplotlib.pyplot as plt
import math
import sys

def get_b_gate():
    coeff = 1/math.sqrt(2)
    b_matrix = [[complex(coeff,0),complex(0,coeff)],[complex(coeff,0),complex(0,-coeff)]]
    b_gate = UnitaryGate(b_matrix, label='B')
    return b_gate

def d_circuit(length):
    ancilla_reg = QuantumRegister(1,'ancilla')
    control_reg = QuantumRegister(length - 1,'control')
    qc = QuantumCircuit(ancilla_reg,control_reg)
    
    b_gate = get_b_gate()
    qc.append(b_gate,[0])

    b_gate_transpose = b_gate.transpose()
    b_gate_transpose.label = 'B_trans'
    b_control_transpose = b_gate_transpose.control(length - 1)


    control_parameter = [*range(1,length)]
    control_parameter.append(0)
    qc.append(b_control_transpose, control_parameter)
    return qc

qc = d_circuit(int(sys.argv[1]))
print(qc)
qc = qc.decompose()
print(qc)