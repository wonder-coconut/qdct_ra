#general dimension image dct gqir but meant to be used only for low dimension image (2,4,8,16)

#packages
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library.standard_gates.x import XGate
import matplotlib.pyplot as plt
import math
import sys

#source scripts
from image_parser import *
from binary_helper import *


def neqr_gen_qc(img_filepath, dim):
    #image initialization
    image = get_image_pixel_array(img_filepath,dim,binflag=True)
    img_test = get_image_pixel_array(img_filepath,dim,binflag=False)
    #display_image(img_test,dim)
    #print(img_test)

    #simulation backend
    backendQasm = Aer.get_backend('qasm_simulator')

    #circuit
    pos_bits = int(math.log(dim,2))
    pixelMap = QuantumRegister(8,'pixelMap')
    position = QuantumRegister(2*pos_bits,'position')
    classic_bits = 2*pos_bits + 8
    measure = ClassicalRegister(classic_bits,'measure')
    qc = QuantumCircuit(pixelMap, position, measure)
    qc.h(position)
    cnx_gate = XGate().control(2*pos_bits)

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
                qc.append(cnx_gate, control_parameter)
            bin_id += 1

        pos_id = 0
        while(pos_id < 2*pos_bits):
            if(pixel_id_bin[pos_id] == '1'):
                qc.x(position[pos_id])
            pos_id += 1

        pixel_id += 1

    qc.barrier()
    return qc
    
def simulate(qc,dim,qc_shots=0):
    qc.measure(range(int(qc.width()/2)),range(int(qc.width()/2)))
    if(qc_shots == 0):
        qc_shots = dim*dim*9 #loss in dead pixels due to insufficient shots
    aer_sim = Aer.get_backend('aer_simulator')
    job = execute(qc,aer_sim,shots=qc_shots)
    result_neqr = job.result()
    counts_neqr = result_neqr.get_counts()
    plot_histogram(counts_neqr)
    return counts_neqr

def translate_to_image(counts_neqr,dim):
    #translate counts back to image
    pos_bits = int(math.log(dim,2))
    img_translate = parse_to_image_array(f'{counts_neqr}',dim,pos_bits) #pass counts data as string
    #print(img_translate)
    op_filepath = f"assets/output_{dim}_neqr.png"
    write_image_to_file(img_translate,dim,op_filepath)
