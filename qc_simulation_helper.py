from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.tools.visualization import plot_distribution, plot_bloch_multivector
import matplotlib.pyplot as plt

def simulate_res(qc, qc_shots, showdist):
    qc.measure_all()
    aer_sim = Aer.get_backend('qasm_simulator')
    counts = execute(qc,aer_sim,shots=qc_shots).result().get_counts()
    if(showdist):
        plot_distribution(counts)
        plt.show()
    return counts

def simulate_vector(qc, qc_shots, showbloch):
    aer_sim = Aer.get_backend('statevector_simulator')
    vector = execute(qc,aer_sim,shots=qc_shots).result().get_statevector()
    if(showbloch):
        plot_bloch_multivector(vector)
        plt.show()
    return vector

def simulate_unitary(qc,qc_shots):
    aer_sim = Aer.get_backend('unitary_simulator')
    job = execute(qc, aer_sim, shots=qc_shots)
    result = job.result()
    matrix = result.get_unitary(qc,3)
    return matrix