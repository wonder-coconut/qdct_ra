from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.extensions import UnitaryGate
from qiskit.circuit import Gate
from qiskit.circuit.library.standard_gates.u import UGate

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
    
    qc.u(math.pi/2,0,-math.pi/2,0)
    #b_gate = get_b_gate()
    #qc.append(b_gate,[0])

    #b_gate_transpose = b_gate.transpose()
    #b_gate_transpose.label = 'B_trans'
    #b_control_transpose = b_gate_transpose.control(length - 1)
    u_trans = UGate(math.pi/2,0,-math.pi/2).inverse()
    u_control_trans = u_trans.control(length - 1)

    control_parameter = [*range(1,length)]
    control_parameter.append(0)
    qc.append(u_control_trans, control_parameter)
    return qc

def simulate(qc,sim_shots):
    qc.measure_all()
    aer_sim = Aer.get_backend('qasm_simulator')
    job = execute(qc,aer_sim,shots = sim_shots)
    results = job.result()
    counts = results.get_counts()
    plot_distribution(counts)
    plt.show()

qc = d_circuit(int(sys.argv[1]))
qc = qc.decompose()
#print(qc)
try:
    sys.argv[2]
    simulate(qc,int(sys.argv[2]))
except:
    pass
