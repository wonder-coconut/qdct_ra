from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, transpile, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt

def circuit(size):
    q_reg = QuantumRegister(size)
    qc = QuantumCircuit(q_reg)
    qc = qc.compose(QFT(size, inverse=False), q_reg)
    qc = qc.decompose()
    print(qc)
    return qc

def simulate_sv(qc):
    aer_sim = Aer.get_backend('qasm_simulator')
    qc.save_statevector()
    job = aer_sim.run(qc)
    result = job.result()
    statevector = result.get_statevector()
    plot_bloch_multivector(statevector)
    plt.show()

qc = circuit(5)
simulate(qc)