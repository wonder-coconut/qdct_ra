#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np
import math

#scripts
from image_parser import get_image_pixel_array, display_image

filepath = 'assets/test_8.jpg'
dim = 8
image = get_image_pixel_array(filepath,dim)

pos_bits = math.log(dim,2)
pos_reg = QuantumRegister(2*pos_bits,'position')
grayscale_reg = QuantumRegister(1,'grayscale')
c_reg = ClassicalRegister(2*pos_bits + 1,'measure')
qc = QuantumCircuit(grayscale_reg,pos_reg,c_reg)
print(qc)