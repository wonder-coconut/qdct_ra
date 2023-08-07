#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import circuit_drawer, plot_histogram
from qiskit.circuit.library.standard_gates.x import XGate
import matplotlib.pyplot as plt
import math

#source files
from image_parser import *
from binary_helper import decimal_to_binary, binary_to_dec


#image initialization
img_filepath = "assets/test.jpg"
dim = 16
image = get_image_pixel_array(img_filepath,dim,binflag=True)
img_test = get_image_pixel_array(img_filepath,dim,binflag=False)
display_image(img_test,dim)

#simulation backend
backendQasm = Aer.get_backend('qasm_simulator')

#circuit
pos_bits = math.log(dim,2)
pixelMap = QuantumRegister(8,'pixelMap')
position = QuantumRegister(2*pos_bits,'position')
measure = ClassicalRegister(16,'measure')
qc = QuantumCircuit(pixelMap, position, measure)
qc.h(position)
c8x_gate = XGate().control(8)

pixel_id = 0
for pixel in image:
    qc.barrier()
    pixel_id_bin = decimal_to_binary(pixel_id,2*pos_bits)

    pos_id = 0
    while(pos_id < 2*pos_bits):
        if(pixel_id_bin[pos_id] == '1'):
            qc.x(position[pos_id])
        pos_id += 1

    bin_id = 0
    for binary in pixel:
        if(binary == '1'):
            control_parameter = [*range(8, 8 + int(2*pos_bits), 1)]
            control_parameter.append(bin_id)
            qc.append(c8x_gate, control_parameter)
        bin_id += 1
    
    pos_id = 0
    while(pos_id < 2*pos_bits):
        if(pixel_id_bin[pos_id] == '1'):
            qc.x(position[pos_id])
        pos_id += 1
    
    pixel_id += 1

qc.barrier()

qc.measure(range(16),range(16))

#simulate
aer_sim = Aer.get_backend('aer_simulator')
job = execute(qc,aer_sim,shots=16384)
result_neqr = job.result()
counts_neqr = result_neqr.get_counts()
#print(qc)
#print(counts_neqr)

#translate counts back to image
img_translate = parse_to_image_array(f'{counts_neqr}',dim,pos_bits) #pass counts data as string
display_image(img_translate,dim)