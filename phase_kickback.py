from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt

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

aer_sim = Aer.get_backend('aer_simulator')
job = execute(qc,aer_sim,shots=1024)
result = job.result()
counts = result_neqr.get_counts()
plot_histogram(counts)
plt.show()