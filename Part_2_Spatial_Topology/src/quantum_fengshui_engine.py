"""
Quantum Feng Shui Simulation: Harmony vs. Deadlock
Author: Alaric Kuo (A&J Management Consulting)
Description:
    This script uses Qiskit to model two different organizational transformation strategies:
    1. Water Flow (Harmony): Targeted intervention leading to a ground state.
    2. Fire Clash (Deadlock): Brute-force intervention leading to a high-tension lock.
"""
!pip install qiskit qiskit-aer
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp, Statevector

def define_frustrated_hamiltonian():
    """
    Defines an 'Antiferromagnetic' Hamiltonian.
    Physics: Neighboring qubits with SAME state (00 or 11) increase energy (Tension).
             Neighboring qubits with DIFFERENT state (01 or 10) decrease energy (Harmony).
    """
    interactions = []
    num_qubits = 6
    # Coefficient +1.0 means 'Same State' adds energy (Penalty)
    for i in range(num_qubits - 1):
        # Format: IIZZII (ZZ interaction between neighbor i and i+1)
        op_str = "I" * (num_qubits - 1 - i - 1) + "ZZ" + "I" * i
        interactions.append((op_str, 1.0))
    
    return SparsePauliOp.from_list(interactions)

def create_water_flow_circuit(mix_angle):
    """
    Strategy A: Water Flow (Smart Intervention)
    Action: Only rotate ODD indices to create an alternating pattern (0-1-0-1...).
    Result: Perfectly aligns with the Hamiltonian's preference for difference.
    """
    qc = QuantumCircuit(6)
    # Apply rotation only to indices 1, 3, 5
    qc.rx(mix_angle, 1)
    qc.rx(mix_angle, 3)
    qc.rx(mix_angle, 5)
    return qc

def create_fire_clash_circuit(mix_angle):
    """
    Strategy B: Fire Clash (Brute Force / Deadlock)
    Action: Rotate ALL qubits simultaneously.
    Result: Although the state changes, the structure remains uniform (All 0s -> All 1s).
            The internal tension (neighbor conflict) is never resolved.
    """
    qc = QuantumCircuit(6)
    # Apply rotation to ALL indices
    for i in range(6):
        qc.rx(mix_angle, i)
    return qc

def run_simulation():
    print("Initializing Quantum Simulation...")
    
    # 1. Setup Parameters
    angles = np.linspace(0, np.pi, 25) # Simulate from 0 to 180 degrees
    tension_water = []
    tension_fire = []
    hamiltonian = define_frustrated_hamiltonian()
    
    # Offset to normalize initial tension to a visible scale (e.g., 10)
    base_energy_offset = 5.0 

    # 2. Execution Loop
    for angle in angles:
        # --- Simulating Water Strategy ---
        qc_w = create_water_flow_circuit(angle)
        state_w = Statevector.from_instruction(qc_w)
        # Calculate Expectation Value <H>
        energy_w = state_w.expectation_value(hamiltonian).real + base_energy_offset
        tension_water.append(energy_w)
        
        # --- Simulating Fire Strategy ---
        qc_f = create_fire_clash_circuit(angle)
        state_f = Statevector.from_instruction(qc_f)
        energy_f = state_f.expectation_value(hamiltonian).real + base_energy_offset
        tension_fire.append(energy_f)

    return angles, tension_water, tension_fire

def plot_results(angles, tension_water, tension_fire):
    plt.figure(figsize=(10, 6))

    # Plot Water Curve (Harmony)
    plt.plot(angles, tension_water, 'o-', color='#8e44ad', linewidth=3, label='Water Flow (Targeted / Harmony)')

    # Plot Fire Curve (Deadlock)
    plt.plot(angles, tension_fire, 's-', color='#c0392b', linewidth=3, label='Fire Clash (Brute Force / Deadlock)')

    # Annotations
    plt.annotate('Ground State Reached\n(Trust Established)', 
                 xy=(np.pi, tension_water[-1]), 
                 xytext=(2.0, 2), 
                 arrowprops=dict(facecolor='#8e44ad', shrink=0.05),
                 fontsize=10, color='#8e44ad', weight='bold')

    plt.annotate('Transformation Deadlock\n(High Tension Persists)', 
                 xy=(np.pi, tension_fire[-1]), 
                 xytext=(1.8, 8.5), 
                 arrowprops=dict(facecolor='#c0392b', shrink=0.05),
                 fontsize=10, color='#c0392b', weight='bold')

    plt.title('Quantum Simulation: Effort vs. Structural Impact', fontsize=14)
    plt.xlabel('Intervention Intensity (Phase Angle)', fontsize=12)
    plt.ylabel('System Tension (Hamiltonian Energy)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Save the plot
    output_filename = 'quantum_deadlock_simulation.png'
    plt.savefig(output_filename, dpi=300)
    print(f"Simulation complete. Graph saved as {output_filename}")
    plt.show()

if __name__ == "__main__":
    angles, t_water, t_fire = run_simulation()
    plot_results(angles, t_water, t_fire)
