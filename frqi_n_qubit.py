from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

from binary_helper import binary_to_dec,decimal_to_binary
import qc_simulation_helper

def cnry(theta,n):
    theta_s = '%.2f'%theta
    cnry = QuantumCircuit(n + 1, name=f'cnry{theta_s}')
    theta /= math.pow(2,n-2)
    theta = -theta

    i = j = 0
    while(i < n):
        j = 0
        a = 0
        b = i
        temp = i - 1
        diff = 1
        while(j < math.pow(2,i)):

            if(i == 0):
                pass

            elif(i == 1):
                temp = i - 1
                cnry.cx(temp,i)

            else:
                cnry.cx(temp,i)
                c1 = temp + diff < a
                c2 = temp + diff >= b

                if(c1 and c2):
                    diff = 0
                elif c1:
                    diff = - diff
                elif c2:
                    diff = - diff
                
                temp += diff


            
            theta = -theta
            cnry.cry(theta,i,n)
            j += 1
        i += 1
    
    #cnry.draw(output = 'mpl')
    #plt.show()
    
    cnry_inst = cnry.to_instruction()
    return cnry_inst

def frqi(theta,length):

    pos_bits = int(math.log(length,2))
    pos_reg = QuantumRegister(pos_bits,'position')
    phase_reg = QuantumRegister(1,'grayscale')

    qubits = []
    for qubit in pos_reg:
        qubits.append(qubit)
    for qubit in phase_reg:
        qubits.append(qubit)

    qc = QuantumCircuit(pos_reg,phase_reg)
    qc.h(pos_reg)

    pos_id = 0

    for angle in theta:
        qc.barrier()
        pos_id_bin = decimal_to_binary(pos_id,pos_bits)

        i = 0
        while(i < pos_bits):
            if(pos_id_bin[i] == '1'):
                qc.x(pos_reg[pos_bits - 1 -i])
            i += 1

        qc.append(cnry(angle,pos_bits),qubits)

        i = 0
        while(i < pos_bits):
            if(pos_id_bin[i] == '1'):
                qc.x(pos_reg[pos_bits - 1 -i])
            i += 1
        pos_id += 1

    qc.barrier()
    return qc

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
        index = length - binary_to_dec(binary[1:pos_bits+1],pos_bits) - 1 #index reversal
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

length = int(sys.argv[1])
shots = int(sys.argv[2])
image = [int((i+1) * (256/length) - 1) for i in range(length)]

print(image)

theta = [(pixel * (math.pi/(256*2))) for pixel in image]
frqi_qc = frqi(theta,length)
vector = qc_simulation_helper.simulate_vector(frqi_qc,shots,False)
counts = qc_simulation_helper.simulate_res(frqi_qc,shots,False)
vector = np.asarray(vector)
for i in vector:
    print(i)
image_op = frqi_decode(counts,length)
print(image_op)