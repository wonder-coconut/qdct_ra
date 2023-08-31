from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np
import math

from binary_helper import binary_to_dec,decimal_to_binary

def cnry(theta,n):
    theta_s = '%.2f'%theta
    cnry = QuantumCircuit(n + 1, name=f'cccry{theta_s}')
    theta /= 4
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
        #print('-=-=-=-=-=-')
        i += 1
    
    print(cnry)


cnry(math.pi/4,4)   