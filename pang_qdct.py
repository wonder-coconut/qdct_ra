#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library.standard_gates.x import XGate
import matplotlib.pyplot as plt
import math

def gen_qc():
    
   alpha_reg = QuantumRegister(1,'alpha')
   beta_reg = QuantumRegister(1,'beta')
   i_reg = QuantumRegister(1,'i')
   f_reg = QuantumRegister(1,'f')
   d_reg = QuantumRegister(1,'d')
   r1_reg = QuantumRegister(1,'r1')
   r2_reg = QuantumRegister(1,'r2')
   numqubits = alpha_reg.size + beta_reg.size + i_reg.size + f_reg.size + d_reg.size + r1_reg.size + r2_reg.size
   c_reg = ClassicalRegister(numqubits,'measure')

   qc = QuantumCircuit(alpha_reg,beta_reg, i_reg, f_reg, d_reg, r1_reg, r2_reg)
   print(qc)

gen_qc()