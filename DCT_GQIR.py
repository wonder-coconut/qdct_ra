from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import circuit_drawer, plot_histogram
from qiskit.circuit.library.standard_gates.x import XGate
import matplotlib.pyplot as plt
from PIL import Image
import math

#helper functions
def decimal_to_binary(num, limit):
    length = 8
    bin_s = ''

    while(num > 0):
        bin_s = str(num%2) + bin_s
        num = int(num/2)

    if(len(bin_s) > limit):
        print("error: overflow")
        return None
    
    padding = limit - len(bin_s)
    i = 0

    while(i < padding):
        i += 1
        bin_s = '0' + bin_s
    return bin_s

def get_image_pixel_array(filepath,dim):
    im = Image.open(filepath)
    image_array = []
    i = j = 0
    while(i < dim):
        j = 0
        while(j < dim):
            colour_pixel = im.getpixel((j,i))
            bw_pixel = int((colour_pixel[0] + colour_pixel[1] + colour_pixel[2])/3)
            image_array.append(decimal_to_binary(bw_pixel,8))
            j += 1
        i += 1
    return image_array

#image initialization
img_filepath = "assets/test3.jpg"
dim = 16
image = get_image_pixel_array(img_filepath,dim)

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
    for bin in pixel:
        if(bin == '1'):
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

qc.measure(range(8),range(8))

#simulate
aer_sim = Aer.get_backend('aer_simulator')
job = execute(qc,aer_sim,shots=16384)
result_neqr = job.result()
counts_neqr = result_neqr.get_counts()
print(qc)
print(counts_neqr)