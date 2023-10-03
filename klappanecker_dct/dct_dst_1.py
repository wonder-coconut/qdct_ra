#libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit import Gate
from qiskit.circuit.library import QFT
import sys

#scripts
from permutation import pi_circuit
from D_matrix import d_circuit
from qft import qft_circuit

def qdct_1(q_size):
    q_reg = QuantumRegister(q_size)
    qc = QuantumCircuit(q_reg)

    d_gate = d_circuit(q_size)
    d_gate = d_gate.to_gate(label='D')
    pi_gate = pi_circuit(q_size)
    pi_gate = pi_gate.to_gate(label='pi')
    qft_gate = qft_circuit(q_size)
    qft_gate = qft_gate.to_gate(label='qft')
    
    qc.append(d_gate,q_reg)
    qc.append(pi_gate,q_reg)
    qc.append(qft_gate,q_reg)

    pi_gate_inv = pi_gate.inverse()
    pi_gate_inv.label = 'pi_trans'
    d_gate_inv = d_gate.inverse()
    d_gate_inv.label = 'D_trans'

    qc.append(pi_gate_inv,q_reg)
    qc.append(d_gate_inv,q_reg)
    print(qc)

qdct_1(int(sys.argv[1]))