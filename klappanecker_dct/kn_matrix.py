from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.extensions import UnitaryGate
import matplotlib.pyplot as plt
import math
import sys

def get_kn_gate():
    