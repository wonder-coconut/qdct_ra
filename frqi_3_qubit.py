from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np
import math

from binary_helper import binary_to_dec,decimal_to_binary

def cccry(theta):
    theta_s = '%.2f'%theta
    cccry = QuantumCircuit(4, name=f'cccry{theta_s}')
    theta /= 2

    cccry.cry(theta,0,3)
    cccry.cx(0,1)
    cccry.cry(-theta,1,3)
    cccry.cx(0,1)
    cccry.cry(theta,1,3)
    cccry.cx(1,2)
    cccry.cry(-theta,2,3)
    cccry.cx(0,2)    
    cccry.cry(theta,2,3)
    cccry.cx(1,2)
    cccry.cry(-theta,2,3)
    cccry.cx(0,2)
    cccry.cry(theta,2,3)
    
        
    
    cccry_inst = cccry.to_instruction() 
    return cccry_inst

def frqi(theta):
    pos_reg = QuantumRegister(3,'position')
    phase_reg = QuantumRegister(1,'grayscale')
    c_reg = ClassicalRegister(4,'measure')

    qubits = []
    for qubit in pos_reg:
        qubits.append(qubit)
    for qubit in phase_reg:
        qubits.append(qubit)

    qc = QuantumCircuit(pos_reg,phase_reg,c_reg)

    qc.h(0)
    qc.h(1)
    qc.h(2)

    pos_id = 0

    for angle in theta:
        qc.barrier()
        pos_id_bin = decimal_to_binary(pos_id,3)

        i = 0
        while(i < 3):
            if(pos_id_bin[i] == '1'):
                qc.x(pos_reg[2-i])
            i += 1

        qc.append(cccry(angle),qubits)

        i = 0
        while(i < 3):
            if(pos_id_bin[i] == '1'):
                qc.x(pos_reg[2-i])
            i += 1
        pos_id += 1

    qc.barrier()
    return qc

def simulate(qc, qc_shots):

    qc.measure(range(4),range(4))
    aer_sim = Aer.get_backend('qasm_simulator')
    counts_frqi = execute(qc,aer_sim,shots=qc_shots).result().get_counts()
    #plot_distribution(counts_frqi)
    #plt.show()
    return counts_frqi

def frqi_decode(counts_frqi,length):

    pos_bits = int(math.log(length,2))   
    counts = f'{counts_frqi}'
    counts = counts[1:len(counts)-1].split(',')
    limit = len(counts)

    image_data = [0 for i in range(length)]

    for i in range(limit):
        counts[i] = counts[i].strip()
        binary = counts[i][1:1 + pos_bits + 1]
        state = int(binary[0])
        index = length - binary_to_dec(binary[1:pos_bits+1],3) - 1 #index reversal
        amp = int(counts[i][counts[i].rfind(':') + 1:len(counts[i])].strip())/shots
        
        if(image_data[index] == 0):
            image_data[index] = {}
            image_data[index][0] = 0
            image_data[index][1] = 0
        image_data[index][state] = amp
        
    ouptut_image = []

    for pixel in image_data:
        
        n = math.log(length,2)/2
        a = math.pow(2,n)*math.sqrt(pixel[0])
        b = math.pow(2,n)*math.sqrt(pixel[1])
        
        if(a > 1):
            a = 1
        if(b > 1):
            b = 1
        
        theta1 = math.acos(a)
        theta2 = math.asin(b)

        theta_net = (theta1 + theta2)/2
        
        pixel_val = theta_net/(math.pi/2)*256
        ouptut_image.append(round(pixel_val))
    
    return ouptut_image

theta = [0,math.pi/8,math.pi/7,math.pi/6,math.pi/5,math.pi/4,math.pi/3,math.pi/2]
input_image = [int((angle*256*2)/math.pi) for angle in theta]
print(input_image)
length = 8
shots = 65536
frqi_qc = frqi(theta)
counts = simulate(frqi_qc, shots)
print(frqi_decode(counts,length))