from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
import matplotlib.pyplot as plt
import math
import sys

def get_j_gate():
    coeff = 1/math.sqrt(2)
    j_matrix = [[complex(coeff,0),complex(0,-coeff)],[complex(0,-coeff),complex(coeff,0)]]
    j_gate = UnitaryGate(j_matrix,label = 'J')
    return j_gate

def j_circuit(length):
    ancilla_reg = QuantumRegister(1,'ancilla')
    control_reg = QuantumRegister(length - 1,'control')
    qc = QuantumCircuit(ancilla_reg,control_reg)
    
    j_control_gate = UGate(math.pi/2, -math.pi/2, math.pi/2).control(length - 1)
    
    control_parameter = [*range(1,length)]
    control_parameter.append(0)
    print(control_parameter)

    qc.append(j_control_gate,control_parameter)

    return qc

def simulate(qc,sim_shots):
    qc.measure_all()
    aer_sim = Aer.get_backend('qasm_simulator')
    job = execute(qc,aer_sim,shots = sim_shots)
    results = job.result()
    counts = results.get_counts()
    plot_distribution(counts)
    plt.show()