from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.extensions import UnitaryGate
import matplotlib.pyplot as plt
import math

def get_b_gate():
    coeff = 1/math.sqrt(2)
    b_matrix = [[complex(coeff,0),complex(0,coeff)],[complex(coeff,0),complex(0,-coeff)]]
    b_gate = UnitaryGate(b_matrix, label='B')
    return b_gate

def circuit(length):
    ancilla_reg = QuantumRegister(1,'ancilla')
    control_reg = QuantumRegister(length - 1,'control')
    qc = QuantumCircuit(ancilla_reg,control_reg)
    
    b_gate = get_b_gate()
    b_trans_gate = b_gate.transpose()
    b_trans_gate.label = 'B_trans'
    b_control_trans = b_trans_gate.control(length - 1)

    control_parameter = [*range(1,length)]
    control_parameter.append(0)
    print(control_parameter)
    
    qc.append(b_gate,[0])
    qc.append(b_control_trans, control_parameter)
    
    return qc

qc = circuit(5)
print(qc)