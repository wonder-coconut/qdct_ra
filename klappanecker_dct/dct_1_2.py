#libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit import Gate
from qiskit.circuit.library import QFT

#scripts
from permutation import pi_circuit
from D_matrix import d_circuit

