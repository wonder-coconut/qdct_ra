#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library import QFT
import matplotlib.pyplot as plt
from math import pi

import qc_simulation_helper

counters = 5
count_reg = QuantumRegister(counters,'counters')
state_reg = QuantumRegister(1,'state')
c_reg = ClassicalRegister(count_reg.size,'measure')
qc = QuantumCircuit(count_reg,state_reg,c_reg)
qc.x(state_reg)
qc.h(count_reg)

i = j = N = 0
i = 1
j = 1
N = 8
theta = ((2*j + 1)*i*pi)/(2*N)

repeat = 1
for counter in count_reg:
    i = 0
    while(i < repeat):
        qc.cp(theta,counter,state_reg)
        i += 1
    repeat *= 2

qc = qc.compose(QFT(count_reg.size, inverse=True), count_reg)
qc.measure(count_reg,c_reg)
#print(qc)

counts = qc_simulation_helper.simulate_res(qc,4096,False)