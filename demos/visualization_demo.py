"""
Demo: Visualize dimensional mappings across architectures
"""

from tide.visualization.dimensional_mapper import DimensionalMapper
import matplotlib.pyplot as plt

def main():
    print("=== TIDE Framework: Visualization Demo ===")
    print("Creating dimensional mapping visualizations...")
    
    mapper = DimensionalMapper()
    
    # Create architecture comparison
    fig1 = mapper.create_architecture_comparison()
    fig1.savefig('architecture_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: architecture_comparison.png")
    
    # Create integration landscape
    fig2 = mapper.create_integration_landscape()
    fig2.savefig('integration_landscape.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: integration_landscape.png")
    
    plt.show()

if __name__ == "__main__":
    main()
