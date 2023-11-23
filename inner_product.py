from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.quantum_info.operators import Operator
from qiskit.tools.visualization import plot_distribution
import matplotlib.pyplot as plt

import qc_simulation_helper
import numpy as np

def op1():
    q_reg = QuantumRegister(3)
    op1 = QuantumCircuit(q_reg, name='op1')
    op1.x(2)
    op1.p(np.pi/4,2)
    print(op1)

    test = Operator(op1)
    return test

def op2():
    q_reg = QuantumRegister(3)
    op2 = QuantumCircuit(q_reg, name='op2')
    op2.h([0,1])
    op2.x(2)
    print(op2)

    test = Operator(op2)
    return test

q_reg = QuantumRegister(3,'state')
qubits = []
for qubit in q_reg:
    qubits.append(qubit)

qc = QuantumCircuit(q_reg)
qc.append(op1(),qubits)
qc.append(op2().transpose(),qubits)
print(qc)
#counts = qc_simulation_helper.simulate_res(qc,8192,True)
vector = qc_simulation_helper.simulate_vector(qc,8192,False)
vector = np.asarray(vector)
for i in vector:
    print(i)