from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt

import qc_simulation_helper

qreg = QuantumRegister(2,'test')
creg = ClassicalRegister(2,'test_c')
qc = QuantumCircuit(qreg,creg)

qc.x(0)
qc.x(1)

def test1(qc):
    qc.cx(1,0)

def test2(qc):
    qc.h(qreg)
    qc.cx(0,1)
    qc.h(qreg)

test2(qc)
qc.measure(qreg,creg)
print(qc)

counts = qc_simulation_helper.simulate_res(qc,1024,True)