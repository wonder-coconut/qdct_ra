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
    
    pi_inst = qc.to_gate(label='permutation')
    return pi_inst

def pi_circuit(length):

    qc = QuantumCircuit(length)

    i = 1
    while(i < length):
        qc.cx(0,i)
        i += 1

    pn_gate = permutation_gate(length - 1)
    pcn_gate = pn_gate.control(1)
    control_parameter = [*range(1,length)]
    control_parameter = [0] + control_parameter
    qc.append(pcn_gate,control_parameter)

    pi_gate = qc.to_gate(label='pi')
    return qc

def simulate(qc,sim_shots):
    qc.measure_all()
    aer_sim = Aer.get_backend('qasm_simulator')
    job = execute(qc,aer_sim,shots = sim_shots)
    results = job.result()
    counts = results.get_counts()
    plot_distribution(counts)
    plt.show()