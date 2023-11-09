from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np
import math

from binary_helper import binary_to_dec
import qc_simulation_helper

def mcry(theta):

    theta_s = '%.2f'%theta
    mcry_reg = QuantumRegister(3)
    mcry = QuantumCircuit(mcry_reg, name=f'mcry({theta_s})')
    
    mcry.cry(theta,mcry_reg[2],mcry_reg[0])
    mcry.cx(mcry_reg[2],mcry_reg[1])
    mcry.cry(-theta,mcry_reg[1],mcry_reg[0])
    mcry.cx(mcry_reg[2],mcry_reg[1])
    mcry.cry(theta,mcry_reg[1],mcry_reg[0])

    mcry_inst = mcry.to_instruction()
    return mcry_inst


def mary(theta):

    theta_s = '%.2f'%theta
    mary_reg = QuantumRegister(3)
    mary = QuantumCircuit(mary_reg, name=f'mary({theta_s})')

    theta /= 2

    mary.ry(theta,mary_reg[0])
    mary.cx(mary_reg[1],mary_reg[0])
    mary.ry(-theta,mary_reg[0])
    mary.cx(mary_reg[2],mary_reg[0])
    mary.ry(theta,mary_reg[0])
    mary.cx(mary_reg[1],mary_reg[0])
    mary.ry(-theta,mary_reg[0])
    mary.cx(mary_reg[2],mary_reg[0])

    mary_inst = mary.to_instruction()
    return mary_inst

def regular_frqi(theta):

    pos_reg = QuantumRegister(2,'position')
    grayscale_reg = QuantumRegister(1,'grayscale')
    c_reg = ClassicalRegister(3)

    qc = QuantumCircuit(grayscale_reg,pos_reg,c_reg)
    qc.h(pos_reg)
    qc.append(mcry(theta[0]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.x(pos_reg[0])
    qc.append(mcry(theta[1]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.x(pos_reg)
    qc.append(mcry(theta[2]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.x(pos_reg[0])
    qc.append(mcry(theta[3]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.measure(range(3),range(3))
    return qc

def improved_frqi(theta):

    pos_reg = QuantumRegister(2,'position')
    grayscale_reg = QuantumRegister(1,'grayscale')
    c_reg = ClassicalRegister(3)

    qc = QuantumCircuit(grayscale_reg,pos_reg,c_reg)
    qc.h(pos_reg)
    qc.append(mary(theta[0]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.x(pos_reg[0])
    qc.append(mary(theta[1]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.x(pos_reg)
    qc.append(mary(theta[2]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.x(pos_reg[0])
    qc.append(mary(theta[3]),[grayscale_reg[0],pos_reg[0],pos_reg[1]])

    qc.measure(range(3),range(3))
    return qc

def frqi_decode(counts_frqi,shots,dim):

    counts = f'{counts_frqi}'
    counts = counts[1:len(counts)-1].split(',')
    limit = len(counts)
    image_data = [0 for i in range(dim * dim)]

    for i in range(limit):
        counts[i] = counts[i].strip()
        binary = counts[i][1:1 + dim + 1]
        state = int(binary[dim])
        index = binary_to_dec(binary[0:dim],2)
        amp = int(counts[i][counts[i].rfind(':') + 1:len(counts[i])].strip())/shots
        
        if(image_data[index] == 0):
            image_data[index] = {}
            image_data[index][0] = 0
            image_data[index][1] = 0
        image_data[index][state] = amp

    image = []

    for pixel in image_data:
        
        n = dim/2
        a = math.pow(2,n)*math.sqrt(pixel[0])
        b = math.pow(2,n)*math.sqrt(pixel[1])
        
        if(a > 1):
            a = 1
        if(b > 1):
            b = 1
        theta1 = math.acos(a)
        theta2 = math.asin(b)

        theta_net = (theta1 + theta2)/2
        
        pixel_val = theta_net/(math.pi/2) * 256
        image.append(round(pixel_val))
    
    return image

theta = [math.pi/16,math.pi/8,math.pi/4,math.pi/2]
image = [int((angle*256*2)/math.pi) for angle in theta]
shots = 16384
print(image)
frqi_qc = regular_frqi(theta)
counts = qc_simulation_helper.simulate_res(frqi_qc,shots,False)
image = frqi_decode(counts,shots,2)
print(image)