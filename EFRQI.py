#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library.standard_gates.x import XGate
import matplotlib.pyplot as plt
import math

#source scripts
from image_parser import *
from binary_helper import *

#image initialization
img_filepath = "assets/test.jpg"
dim = 16
image = get_image_pixel_array(img_filepath,dim,binflag=True)
#img_test = get_image_pixel_array(img_filepath,dim,binflag=False)
#display_image(img_test,dim)

#simulation backend
backendQasm = Aer.get_backend('qasm_simulator')

#quantumcircuit
pos_bits = int(math.log(dim,2))
pixelMap = QuantumRegister(8,'pixelMap')
position = QuantumRegister(2*pos_bits,'position')
auxillary = QuantumRegister(1,'aux')
classic_bits = 2*pos_bits + 8
measure = ClassicalRegister(classic_bits,'measure')
qc = QuantumCircuit(pixelMap, auxillary, position, measure)

cnx_gate = XGate().control(2*pos_bits)

qc.h(position)

pixel_id = 0
for pixel in image:
    qc.barrier()
    pixel_id_bin = decimal_to_binary(pixel_id,2*pos_bits)

    control_parameter = [*range(9, 9 + 2*pos_bits,1)]
    control_parameter.append(8)

    pos_id = 0
    while(pos_id < 2*pos_bits):
        if(pixel_id_bin[pos_id] == '1'):
            qc.x(position[pos_id])
        pos_id += 1
    
    qc.append(cnx_gate, control_parameter)

    bin_id = 0
    for binary in pixel:
        if(binary == '1'):
            qc.cnot(8, bin_id)
        bin_id += 1

    qc.append(cnx_gate, control_parameter)

    pos_id = 0
    while(pos_id < 2*pos_bits):
        if(pixel_id_bin[pos_id] == '1'):
            qc.x(position[pos_id])
        pos_id += 1
    
    pixel_id += 1

qc.barrier()

qc.measure(range(8),range(8))

#simulate
aer_sim = Aer.get_backend('aer_simulator')
job = execute(qc,aer_sim,shots=16384)
result_neqr = job.result()
counts_neqr = result_neqr.get_counts()
#print(qc)
print(counts_neqr)