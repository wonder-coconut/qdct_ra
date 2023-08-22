from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt
import math

image = [25,50,75,255]
theta = [(pixel * math.pi/2)/256 for pixel in image]

qc = QuantumCircuit(3,3)

qc.h(0)
qc.h(1)

qc.barrier()
#Pixel 1

qc.cry(theta[0],0,2)
qc.cx(0,1)
qc.cry(-theta[0],1,2)
qc.cx(0,1)
qc.cry(theta[0],1,2)

qc.barrier()
#Pixel 2

qc.x(1)

qc.cry(theta[1],0,2)
qc.cx(0,1)
qc.cry(-theta[1],1,2)
qc.cx(0,1)
qc.cry(theta[1],1,2)

qc.barrier()
#pixel 3
qc.x(1)
qc.x(0)
qc.cry(theta[2],0,2)
qc.cx(0,1)
qc.cry(-theta[2],1,2)
qc.cx(0,1)
qc.cry(theta[2],1,2)


qc.barrier()
#pixel 4
qc.x(1)

qc.cry(theta[3],0,2)
qc.cx(0,1)
qc.cry(-theta[3],1,2)
qc.cx(0,1)
qc.cry(theta[3],1,2)

#qc.measure([2],[2])

print(qc)
print(theta)

aer_sim = Aer.get_backend('qasm_simulator')
qc.save_statevector()
statevector = aer_sim.run(qc)
statevector = statevector.result()

#job = execute(qc,aer_sim,shots=65536)
#result_neqr = job.result()
#counts_neqr = result_neqr.get_counts()
#print(counts_neqr)