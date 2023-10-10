#libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.circuit.library.standard_gates.x import XGate
from qiskit.circuit.library import QFT
import qiskit.quantum_info as qi
import sys
import math

#scripts
from C_matrix import get_C_gate
from J_matrix import get_j_gate
from lj_matrix import get_lj_gate
from kj_matrix import get_kj_gate
from permutation import permutation_gate

def qdct_2(q_size):
    q_reg = QuantumRegister(q_size)
    qc = QuantumCircuit(q_reg)

    #h
    qc.h(0)

    #permutation1
    for i in range(1, q_size):
        qc.cx(0,i)
    
    #qft
    qc = qc.compose(QFT(q_size, inverse=False), q_reg)

    #kj_gate
    for i in range(1,q_size):
        kj_gate = get_kj_gate(q_size,i).control(1)
        qc.append(kj_gate,[0,i])
    
    #lj_gate
    for i in range(1,q_size):
        lj_gate = get_lj_gate(q_size,i).control(1)
        lj_gate.ctrl_state = '0'
        qc.append(lj_gate,[0,i])
    
    #C_gate
    C_gate = get_C_gate(q_size)
    qc.append(C_gate,[0])

    #permutation2
    perm_gate = permutation_gate(q_size - 1).inverse()
    perm_gate.label = 'P_inv'
    perm_gate_control = perm_gate.control(1)
    control_parameter_p = [0]
    control_parameter_p.extend(range(1,q_size))
    qc.append(perm_gate_control,control_parameter_p)


    #permutation1
    for i in range(1, q_size):
        qc.cx(0,i)

    #B_trans_gate
    b_trans_gate = UGate(math.pi/2, math.pi/2, -math.pi)
    b_trans_gate.label = 'B'
    qc.append(b_trans_gate,[0])

    #J_gate
    j_control_gate = UGate(math.pi/2, -math.pi/2, math.pi/2)
    j_control_gate.label = 'J'
    j_control_gate = j_control_gate.control(q_size - 1)
    control_parameter_j = [*range(1,q_size)]
    control_parameter_j.append(0)

    control_state = ''
    for i in range(1,q_size):
        control_state += '0'

    j_control_gate.ctrl_state = control_state

    qc.append(j_control_gate,control_parameter_j)

    #permutation2
    qc.append(perm_gate_control,control_parameter_p)

    print(qc)

qdct_2(4)