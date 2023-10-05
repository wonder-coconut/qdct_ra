#libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.circuit.library.standard_gates.x import XGate
from qiskit.circuit.library import QFT
import qiskit.quantum_info as qi
import sys
import math

def qdct_2(q_size):
    q_reg = QuantumRegister(q_size)
    qc = QuantumCircuit(q_reg)

    #h
    qc.h(0)

    #permutation
    i = 0
    while(i < q_size):
        if(q_size - i - 1 > 0):
            control_parameter_p = [*range(i + 1,q_size)]
            control_parameter_p.append(i)
            cnx = XGate().control(q_size - i - 1)
            qc.append(cnx,control_parameter_p)
        else:
            qc.x(i)
        i += 1
    
    #qft
    qc = qc.compose(QFT(q_size, inverse=False), q_reg)
    
    print(qc)

qdct_2(4)