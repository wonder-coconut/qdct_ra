from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.extensions import UnitaryGate
from qiskit.circuit import Gate
from qiskit.circuit.library.standard_gates.u import UGate

import matplotlib.pyplot as plt
import math
import sys

def d_circuit(length):
    ancilla_reg = QuantumRegister(1,'ancilla')
    control_reg = QuantumRegister(length - 1,'control')
    qc = QuantumCircuit(ancilla_reg,control_reg)
    
    qc.u(math.pi/2,0,-math.pi/2,0)

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
