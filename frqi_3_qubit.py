from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np
import math

def cccry(theta):
    theta_s = '%.2f'%theta
    cccry = QuantumCircuit(4, name=f'cccry{theta_s}')
    theta /= 2

    cccry.cry(theta,0,3)
    cccry.cx(0,1)
    cccry.cry(-theta,1,3)
    cccry.cx(0,1)
    cccry.cry(theta,1,3)
    cccry.cx(1,2)
    cccry.cry(-theta,2,3)
    cccry.cx(0,2)    
    cccry.cry(theta,2,3)
    cccry.cx(1,2)
    cccry.cry(-theta,2,3)
    cccry.cx(0,2)
    cccry.cry(theta,2,3)    
    
    cccry_inst = cccry.to_instruction() 
    return cccry_inst

pos_reg = QuantumRegister(3,'position')
phase_reg = QuantumRegister(1,'grayscale')
c_reg = ClassicalRegister(4,'measure')

qubits = []
for qubit in pos_reg:
    qubits.append(qubit)
for qubit in phase_reg:
    qubits.append(qubit)

qc = QuantumCircuit(pos_reg,phase_reg,c_reg)
qc.x(0)
qc.x(1)
qc.x(2)

qc.append(cccry(0),qubits)
qc.measure(range(4),range(4))
print(qc)

aer_sim = Aer.get_backend('qasm_simulator')
counts_frqi = execute(qc,aer_sim,shots=4096).result().get_counts()
plot_distribution(counts_frqi)
plt.show()