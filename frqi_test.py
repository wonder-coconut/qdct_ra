from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt
import math

from binary_helper import binary_to_dec

#image = [0,100,200,255]
#theta = [(pixel * math.pi/2)/256 for pixel in image]
theta = [math.pi/2,math.pi/4,math.pi/8,0]
image = [(angle*256)/(math.pi/2) for angle in theta]
print(f"original image: {image}")

qc = QuantumCircuit(3,3)

qc.h(0)
qc.h(1)

qc.barrier()
#Pixel 1

qc.cry(theta[0],0,2)
qc.cx(0,1)
qc.cry(-theta[0],1,2)
qc.cx(0,1)
qc.cry(theta[0],1,2)

qc.barrier()
#Pixel 2

qc.x(1)

qc.cry(theta[1],0,2)
qc.cx(0,1)
qc.cry(-theta[1],1,2)
qc.cx(0,1)
qc.cry(theta[1],1,2)

qc.barrier()
#pixel 3
qc.x(1)
qc.x(0)
qc.cry(theta[2],0,2)
qc.cx(0,1)
qc.cry(-theta[2],1,2)
qc.cx(0,1)
qc.cry(theta[2],1,2)


qc.barrier()
#pixel 4
qc.x(1)

qc.cry(theta[3],0,2)
qc.cx(0,1)
qc.cry(-theta[3],1,2)
qc.cx(0,1)
qc.cry(theta[3],1,2)

qc.measure(range(3),range(3))

#print(qc)
#print(theta)

aer_sim = Aer.get_backend('qasm_simulator')
#qc.save_statevector()
#statevector = aer_sim.run(qc)
#statevector = statevector.result()

job = execute(qc,aer_sim,shots=65536)
result_neqr = job.result()
counts_neqr = result_neqr.get_counts()
plot_distribution(counts_neqr)
plt.show()

counts = f'{counts_neqr}'
counts = counts[1:len(counts)-1].split(',')
shots = 65536
dim = 2
limit = len(counts)
image_data = [0 for i in range(dim * dim)]

i = 0
while(i < limit):
    counts[i] = (counts[i]).strip()
    binary = counts[i][1:4]
    state = int(binary[0])
    pos = binary[1:len(binary)]
    pos = pos[::-1]
    amp = int(counts[i][counts[i].rfind(':') + 1:len(counts[i])].strip())/shots
    index = binary_to_dec(pos,2)
    if(image_data[index] == 0):
        image_data[index] = {}
        image_data[index][0] = 0
        image_data[index][1] = 0
    image_data[index][state] = amp
    i += 1

image = []
for pixel in image_data:
    a = pixel[0]
    b = pixel[1]
    s = math.sqrt(a*a + b*b)
    a = a/s
    b = b/s
    theta1 = math.acos(math.sqrt(a))
    theta2 = math.asin(math.sqrt(b))
    theta_net = (theta1 + theta2)/2
    pixel_val = theta_net/(math.pi/2) * 256
    image.append(round(pixel_val))

print(f"final image: {image}")