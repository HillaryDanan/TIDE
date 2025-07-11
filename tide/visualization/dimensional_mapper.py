"""
Visualization tools for dimensional mapping of cognitive architectures.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict
from ..core.dimensional_space import DimensionalSpace

class DimensionalMapper:
    """
    Create scientific visualizations of dimensional organizations.
    """
    
    def __init__(self):
        self.space = DimensionalSpace()
        self.setup_style()
    
    def setup_style(self):
        """Set up clean, scientific visualization style"""
        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set_palette("husl")
    
    def create_architecture_comparison(self, elements: List[str] = None):
        """
        Create comparison visualization of how elements map across architectures.
        
        Args:
            elements: List of cognitive elements to map
        """
        if elements is None:
            elements = ['self', 'time', 'emotion', 'logic', 'social', 'structure']
        
        architectures = ['NT', 'ASD', 'ADHD']
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        for idx, arch in enumerate(architectures):
            ax = axes[idx]
            self._plot_architecture(ax, arch, elements)
            ax.set_title(f'{arch} Architecture', fontsize=14, fontweight='bold')
            ax.set_xlabel('Internal ← → External', fontsize=12)
            ax.set_ylabel('Dimension Strength', fontsize=12)
            ax.set_xlim(-0.1, 1.1)
            ax.set_ylim(-0.1, 1.1)
            
        plt.tight_layout()
        return fig
    
    def _plot_architecture(self, ax, architecture: str, elements: List[str]):
        """Plot single architecture's dimensional mapping"""
        positions = []
        labels = []
        
        for elem in elements:
            pos = self.space.compute_element_position(elem, architecture)
            positions.append(pos)
            labels.append(elem)
        
        positions = np.array(positions)
        
        # Create scatter plot with different colors for different element types
        colors = []
        for elem in elements:
            if elem in ['self', 'time']:
                colors.append('red')
            elif elem in ['emotion', 'social']:
                colors.append('blue')
            else:
                colors.append('green')
        
        scatter = ax.scatter(positions[:, 1], positions[:, 0], 
                           c=colors, s=200, alpha=0.7, edgecolors='black')
        
        # Add labels
        for i, label in enumerate(labels):
            ax.annotate(label, (positions[i, 1], positions[i, 0]),
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=10, fontweight='bold')
        
        # Add dimensional axis lines
        ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
        
        # Add legend for critical elements
        if architecture == 'NT':
            ax.text(0.02, 0.98, 'Self: Internal\nTime: External', 
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        elif architecture == 'ASD':
            ax.text(0.02, 0.98, 'Self: External\nTime: External', 
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        elif architecture == 'ADHD':
            ax.text(0.02, 0.98, 'Self: Internal\nTime: Internal', 
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    def create_integration_landscape(self):
        """
        Create 3D visualization of integration landscape for each architecture.
        Shows how self-time binding varies across dimensional space.
        """
        fig = plt.figure(figsize=(15, 5))
        
        architectures = ['NT', 'ASD', 'ADHD']
        for idx, arch in enumerate(architectures):
            ax = fig.add_subplot(1, 3, idx + 1, projection='3d')
            self._plot_integration_landscape(ax, arch)
            ax.set_title(f'{arch} Integration Landscape', fontsize=14)
        
        plt.tight_layout()
        return fig
    
    def _plot_integration_landscape(self, ax, architecture: str):
        """Plot 3D integration landscape for single architecture"""
        # Create grid
        internal = np.linspace(0, 1, 20)
        external = np.linspace(0, 1, 20)
        I, E = np.meshgrid(internal, external)
        
        # Compute integration strength at each point
        Z = np.zeros_like(I)
        for i in range(20):
            for j in range(20):
                # Simulate integration based on architecture
                if architecture == 'NT':
                    # Peak when self is internal and time is external
                    Z[i, j] = np.exp(-((I[i,j]-0.8)**2 + (E[i,j]-0.2)**2))
                elif architecture == 'ASD':
                    # Peak when both are external
                    Z[i, j] = np.exp(-((I[i,j]-0.2)**2 + (E[i,j]-0.2)**2))
                elif architecture == 'ADHD':
                    # Peak when both are internal but unstable
                    Z[i, j] = np.exp(-((I[i,j]-0.8)**2 + (E[i,j]-0.8)**2))
                    Z[i, j] += 0.2 * np.random.normal()  # Add noise
        
        # Create surface plot
        surf = ax.plot_surface(I, E, Z, cmap='viridis', alpha=0.8)
        ax.set_xlabel('Internal Dimension')
        ax.set_ylabel('External Dimension')
        ax.set_zlabel('Integration Strength')
