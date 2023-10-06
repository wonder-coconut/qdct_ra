from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.extensions import UnitaryGate
import matplotlib.pyplot as plt
import math
import sys

def get_ln_gate(length):
    N = length
    theta = (2*math.pi)/(4*N)
    omega = complex(math.cos(theta), math.sin(theta))
    print(omega)

get_ln_gate(4)