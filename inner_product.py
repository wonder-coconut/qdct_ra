from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt

register_len = 1
q0 = QuantumRegister(1,'q0')
r1 = QuantumRegister(register_len,'r1')
r2 = QuantumRegister(register_len,'r2')
cr = ClassicalRegister(1,'cr')
qc = QuantumCircuit(q0,r1,r2,cr)

qc.h(0)
qc.h(r1)
qc.x(r2)

for i in range(register_len):
    qc.cswap(0,i+1,i+register_len+1)

qc.h(0)
qc.measure(0,0)
print(qc)

aer_sim = Aer.get_backend('aer_simulator')
job = execute(qc,aer_sim,shots=4096)
result_neqr = job.result()
counts_neqr = result_neqr.get_counts()
plot_histogram(counts_neqr)
plt.show()

#qc.save_statevector()
#statevector= aer_sim.run(qc).result().get_statevector()
#fig = plot_bloch_multivector(statevector)
#plt.show()