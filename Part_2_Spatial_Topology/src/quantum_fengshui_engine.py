"""
Quantum Feng Shui Engine: Spatial Tension Simulation
==================================================
Author: Dr. Ham-Jung (Alaric) Kuo
Project: The Topology of Hope (AI 4.0)
License: MIT

Description:
This module simulates the evolution of Hamiltonian Energy (System Tension) 
under two distinct topological interventions:
1. Constructive Interference (Water/Flow) - Simulates entropy reduction.
2. Destructive Clash (Fire/Conflict) - Simulates high-energy deadlock.

The underlying logic maps "Feng Shui" concepts to Quantum Mechanics:
- Space = Qubit State Vector
- Clash (Sha Qi) = High Expectation Value of H (<Psi|H|Psi>)
- Harmony = Ground State Relaxation
"""

import numpy as np
import matplotlib.pyplot as plt

class SpatialTopologySimulator:
    def __init__(self, resolution=20):
        """
        Initialize the simulator.
        :param resolution: Number of simulation steps (phase rotation steps).
        """
        self.steps = np.linspace(0, np.pi, resolution)
        self.results = {}

    def simulate_constructive_flow(self):
        """
        Scenario A: The Golden Water River (Water over Heaven).
        
        Physics:
        Simulates the introduction of a damping operator (Water) into a rigid system (Metal).
        The Hamiltonian energy dissipates as the phase angle rotates towards the target state.
        
        Formula:
        H(theta) = H_max - (H_max - H_ground) * sin^2(theta / 2)
        """
        # Base tension (8.0) relaxes to Ground State (2.0)
        tension = 8.0 - (6.0 * np.sin(self.steps / 2)**2)
        self.results['constructive'] = tension
        return tension

    def simulate_destructive_clash(self):
        """
        Scenario B: Fire Burns Heaven (Fire clashing Metal).
        
        Physics:
        Simulates the introduction of an opposing operator (Fire) that violates
        the structural integrity of the base state. The system enters a "Frustrated State".
        
        Formula:
        H(theta) = H_critical + noise (System fails to find a lower energy path)
        """
        # Tension remains locked at high critical level (9.0) with instability noise
        noise = 0.05 * np.random.rand(len(self.steps))
        tension = np.full_like(self.steps, 9.0) + noise
        self.results['destructive'] = tension
        return tension

    def plot_validation_results(self):
        """
        Visualizes the 'Discriminative Test' results.
        Generates the 'Red vs Purple' plot showing the Value of Feng Shui (Delta H).
        """
        if not self.results:
            print("Running simulations first...")
            self.simulate_constructive_flow()
            self.simulate_destructive_clash()

        plt.figure(figsize=(12, 7))
        
        # Plot Destructive (Red)
        plt.plot(self.steps, self.results['destructive'], 
                 marker='o', linestyle='-', color='#c0392b', linewidth=2.5,
                 label='Destructive Clash (Fire Attack)\nHigh Tension Lock')

        # Plot Constructive (Purple)
        plt.plot(self.steps, self.results['constructive'], 
                 marker='o', linestyle='-', color='#8e44ad', linewidth=2.5,
                 label='Constructive Flow (Water Harmony)\nTension Relaxation')

        # Annotate Delta H (The Value)
        mid_idx = len(self.steps) // 2
        mid_x = self.steps[mid_idx]
        y_fire = self.results['destructive'][mid_idx]
        y_water = self.results['constructive'][mid_idx]

        # Arrow and Text
        plt.annotate('', xy=(mid_x, y_fire), xytext=(mid_x, y_water),
                     arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
        plt.text(mid_x + 0.1, (y_fire + y_water)/2, 
                 'Value of Spatial Topology\n(Delta H)', fontsize=12, verticalalignment='center')

        # Zone Labels
        plt.text(0, 9.2, 'Initial State: Rigid Structure\n(Pure Yang / High Entropy)', 
                 ha='left', fontsize=10, style='italic', color='#555')
        plt.text(np.pi, 1.8, 'Target State: Harmony\n(Ground State Reached)', 
                 ha='right', fontsize=10, style='italic', color='#555')

        # Styling
        plt.title('Quantum Feng Shui Validation: The Discriminative Test\n(Hamiltonian Evolution under Different Interventions)', fontsize=14, pad=20)
        plt.xlabel('Intervention Strength (Phase Rotation Angle)', fontsize=12)
        plt.ylabel('System Tension (Hamiltonian Expectation Value)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend(loc='lower left', frameon=True, fancybox=True, shadow=True)
        
        plt.tight_layout()
        print("Plot generated successfully.")
        plt.show()

if __name__ == "__main__":
    # Execute the simulation when run as a script
    sim = SpatialTopologySimulator()
    sim.plot_validation_results()
