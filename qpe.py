#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library import QFT
import matplotlib.pyplot as plt
from math import pi

count_reg = QuantumRegister(5,'counters')
state_reg = QuantumRegister(1,'state')
c_reg = ClassicalRegister(count_reg.size,'measure')
qc = QuantumCircuit(count_reg,state_reg,c_reg)
qc.x(state_reg)
qc.h(count_reg)

repeat = 1
for counter in count_reg:
    i = 0
    while(i < repeat):
        qc.cp(2*pi/3,counter,state_reg)
        i += 1
    repeat *= 2

qc = qc.compose(QFT(count_reg.size, inverse=True), count_reg)
qc.measure(count_reg,c_reg)
print(qc)

aer_sim = Aer.get_backend('aer_simulator')
job = execute(qc,aer_sim,shots=4096)
result_neqr = job.result()
counts_neqr = result_neqr.get_counts()
plot_histogram(counts_neqr)
plt.show()