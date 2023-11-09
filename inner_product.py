from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.quantum_info.operators import Operator
from qiskit.tools.visualization import plot_distribution
import matplotlib.pyplot as plt

def op1():
    q_reg = QuantumRegister(3)
    op1 = QuantumCircuit(q_reg, name='op1')
    op1.x(q_reg)
    op1.h(q_reg)
    print(op1)

    test = Operator(op1)
    return test

def op2():
    q_reg = QuantumRegister(3)
    op2 = QuantumCircuit(q_reg, name='op2')
    op2.h(0)
    op2.h(1)
    op2.h(2)
    print(op2)

    test = Operator(op2)
    return test

q_reg = QuantumRegister(3,'state')
c_reg = ClassicalRegister(3,'measure')
qubits = []
for qubit in q_reg:
    qubits.append(qubit)

qc = QuantumCircuit(q_reg,c_reg)
qc.append(op1(),qubits)
qc.append(op2().transpose(),qubits)

counts = qc_simulation_helper.simulate_res(qc,8192,True)

print(qc)