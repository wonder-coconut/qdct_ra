from qiskit import QuantumRegister, QuantumCircuit, transpile, Aer
from qiskit.tools.visualization import circuit_drawer, plot_histogram
import matplotlib.pyplot as plt

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

#simulation backend
backendQasm = Aer.get_backend('qasm_simulator')

#image initialization
imagearray = [75,10,25,37]
image = []
for pixel in imagearray:
    image.append(decimal_to_binary(pixel,8))

#circuit
pixelMap = QuantumRegister(8,'pixelMap')
position = QuantumRegister(2,'pos')

qc = QuantumCircuit(pixelMap, position)
qc.h(position)

pixel_id = 0
for pixel in image:
    qc.barrier()
    pixel_id_bin = decimal_to_binary(pixel_id,2)

    if(pixel_id_bin[0] == '1'):
        qc.x(position[0])
    if(pixel_id_bin[1] == '1'):
        qc.x(position[1])
    
    bin_id = 0
    for bin in pixel:
        if(bin == '1'):
            qc.ccx(position[0],position[1],pixelMap[bin_id])
        bin_id += 1
    
    if(pixel_id_bin[0] == '1'):
        qc.x(position[0])
    if(pixel_id_bin[1] == '1'):
        qc.x(position[1])

    pixel_id += 1

print(qc)