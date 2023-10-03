#libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_distribution
from qiskit.circuit.library.standard_gates.u import UGate
from qiskit.circuit.library.standard_gates.x import XGate
from qiskit.circuit.library import QFT
import sys
import math

#scripts
import D_matrix
import permutation
import qft

def qdct_1(q_size):
    q_reg = QuantumRegister(q_size)
    qc = QuantumCircuit(q_reg)

    #d_gate
    qc.u(math.pi/2,0,-math.pi/2,0)

    u_trans = UGate(math.pi/2,0,-math.pi/2).inverse()
    u_control = UGate(math.pi/2,0,-math.pi/2).control(q_size - 1)
    u_control_trans = u_trans.control(q_size - 1)

    control_parameter_d = [*range(1,q_size)]
    control_parameter_d.append(0)
    qc.append(u_control_trans, control_parameter_d)
    #end of d_gate

    #pi gate
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

    perm_gate = permutation.permutation_gate(q_size)
    qc.append(perm_gate,q_reg)
    #end of pi gate

    #qft
    qc = qc.compose(QFT(q_size, inverse=False), q_reg)
    #end of qft

    #pi inverse gate
    perm_gate_inv = perm_gate.inverse()
    qc.append(perm_gate_inv,q_reg)
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
    #end of pi inv

    #d inv
    qc.append(u_control,control_parameter_d)
    qc.append(u_trans,[0])
    #end of d inv
    
    
    print(qc)

qdct_1(int(sys.argv[1]))