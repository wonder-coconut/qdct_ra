from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt
import math

image = [25,50,75,255]
theta = [(pixel * math.pi/2)/256 for pixel in image]
#theta = [math.pi/4,math.pi/3,math.pi/2,0]
qc = QuantumCircuit(3,3)
qc.h(0)
qc.h(1)

for pixel in range(4):
    
    qc.barrier()
    #pixel identification
    if(pixel%2 != 0):
        qc.x(0)
    if(int(pixel/2)%2 != 0):
        qc.x(1)
    
    #R(2theta) unitary operation
    qc.cry(theta[pixel],0,2)
    qc.cx(0,1)
    qc.cry(-theta[pixel],0,2)
    qc.cx(0,1)
    qc.cry(theta[pixel],0,2)
    
qc.barrier()
qc.measure(range(2),range(2))
print(qc)

aer_sim = Aer.get_backend('aer_simulator')
job = execute(qc,aer_sim,shots=8192)
result_neqr = job.result()
counts_neqr = result_neqr.get_counts()