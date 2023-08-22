#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library.standard_gates.x import XGate
import matplotlib.pyplot as plt
import math

#scripts
from classical_dct import get_dct_matrix,print_mat
from binary_helper import decimal_to_binary

def load(image,qc,i,dim,register_data):
   qc.h(register_data[2][0])
   cnx_gate = XGate().control(2*pos_bits)

   j = 0
   while(j < dim):
      qc.barrier()
      pixel_id = j*dim + i
      pixel = image[pixel_id]
      pixel_bin = decimal_to_binary(pixel,8)
      pixel_id_bin = decimal_to_binary(pixel_id,2*pos_bits)
      
      i_id = 0
      while(i_id < 2*pos_bits):
         if(pixel_id_bin[i_id] == '1'):
            qc.x(register_data[2][0][i_id])
         i_id += 1
      
      #f column vector
      print(pixel_bin)
      bin_id = 0
      for binary in pixel_bin:
         if(binary == '1'):
            control_parameter = [*range(register_data[2][1],register_data[2][1] + 2*pos_bits)]
            control_parameter.append(bin_id + register_data[3][1])
            qc.append(cnx_gate, control_parameter)
         bin_id += 1
      
      
      
      i_id = 0
      while(i_id < 2*pos_bits):
         if(pixel_id_bin[i_id] == '1'):
            qc.x(register_data[2][0][i_id])
         i_id += 1
      
      j += 1
   qc.barrier()
   qc.h(register_data[2][0])

def gen_qc(pos_bits,image,dim):
    
   alpha_reg = QuantumRegister(1,'alpha')
   alpha_reg_start = 0
   beta_reg = QuantumRegister(1,'beta')
   beta_reg_start = alpha_reg.size
   i_reg = QuantumRegister(2*pos_bits,'i')
   i_reg_start = beta_reg_start + beta_reg.size
   f_reg = QuantumRegister(8,'f')
   f_reg_start = i_reg_start + i_reg.size
   d_reg = QuantumRegister(8,'d')
   d_reg_start = f_reg_start + f_reg.size
   r1_reg = QuantumRegister(1,'r1')
   r1_reg_start = d_reg_start + d_reg.size
   r2_reg = QuantumRegister(1,'r2')
   r2_reg_start = r1_reg_start + r1_reg.size
   numqubits = r2_reg_start + r2_reg.size
   c_reg = ClassicalRegister(numqubits,'measure')
   
   register_data = [[alpha_reg,alpha_reg_start],[beta_reg,beta_reg_start],[i_reg,i_reg_start],[f_reg,f_reg_start],[d_reg,d_reg_start],[r1_reg,r1_reg_start],[r2_reg,r2_reg_start],c_reg,numqubits]

   '''
   indices:
   0  alpha
   1  beta
   2  i
   3  f
   4  d
   5  r1
   6  r2
   '''

   qc = QuantumCircuit(alpha_reg,beta_reg, i_reg, f_reg, d_reg, r1_reg, r2_reg)

   #load
   load(image,qc,0,dim,register_data)
   #load(image,qc,1,dim,register_data)

   print(qc)

dim = 2
dct = get_dct_matrix(dim)
pos_bits = int(math.log(dim,2))
image = [25,50,75,100]
gen_qc(pos_bits,image,dim)