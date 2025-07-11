# Getting Started with TIDE

## Installation

```bash
pip install tide-framework
```

Or install from source:

```bash
git clone https://github.com/HillaryDanan/TIDE.git
cd TIDE
pip install -e .
```

## Your First TIDE Program

Let's explore how different cognitive architectures process information:

```python
from tide import CognitiveArchitecture

# Create a neurotypical architecture
nt_brain = CognitiveArchitecture('NT')

# Create an ASD architecture  
asd_brain = CognitiveArchitecture('ASD')

# Give them the same planning task
task = {
    'content': 'organize a birthday party',
    'temporal_context': 'next week'
}

# See how they process it differently
nt_result = nt_brain.process_information(task)
asd_result = asd_brain.process_information(task)

print("NT approach:", nt_result)
print("ASD approach:", asd_result)
```

## Understanding the Dimensions

TIDE maps cognitive elements onto two dimensions:

- **Internal**: Fluid, emotional, experiential
- **External**: Structured, logical, systematic

Let's see where different elements live:

```python
from tide import DimensionalSpace

space = DimensionalSpace()

# Where does 'self' live for each architecture?
for arch in ['NT', 'ASD', 'ADHD']:
    position = space.compute_element_position('self', arch)
    print(f"{arch} self position: Internal={position[0]:.1f}, External={position[1]:.1f}")
```

## Visualizing Architectures

Create beautiful visualizations to understand the differences:

```python
from tide.visualization import DimensionalMapper
import matplotlib.pyplot as plt

mapper = DimensionalMapper()

# Compare all three architectures
fig = mapper.create_architecture_comparison()
plt.show()

# Save for your presentation
fig.savefig('my_tide_visualization.png', dpi=300, bbox_inches='tight')
```

## Temporal Planning Example

See how different architectures approach planning:

```python
from tide.examples import TemporalPlanningTask

# Create an ADHD planner
adhd_planner = TemporalPlanningTask('ADHD')

# Generate a week plan
plan = adhd_planner.plan_week()

print("ADHD Planning Style:")
for day, activities in plan.items():
    print(f"\n{day}:")
    for activity in activities:
        print(f"  - {activity}")
```

Expected output:
```
ADHD Planning Style:

TODAY:
  - NOW: work
  - Maybe later: exercise
  - If time: social

Monday:
  - probably something
  - will figure it out
```

## Measuring Integration

How well do self and time bind together?

```python
from tide.core.integration import IntegrationEngine
import numpy as np

# Create integration engine for each architecture
for arch_type in ['NT', 'ASD', 'ADHD']:
    engine = IntegrationEngine(arch_type)
    
    # Simulate some integration measurements
    for _ in range(10):
        self_state = np.random.rand(2)
        time_state = np.random.rand(2)
        phi = engine.compute_integration(self_state, time_state)
    
    stability = engine.get_integration_stability()
    print(f"{arch_type} integration stability: {stability:.2f}")
```

## Next Steps

1. **Explore examples**: Check out `demos/` for more complex examples
2. **Framework**: See [Theoretical Foundation](../theoretical_foundation.md)
3. **Build**: Use TIDE to model cognitive diversity in your AI systems
4. **Contribute**: Open to collaboration

## Quick Reference

```python
# The three architectures
architectures = ['NT', 'ASD', 'ADHD']

# Key differences
# NT:  Self=Internal, Time=External, Integration=Dynamic
# ASD: Self=External, Time=External, Integration=Crystallized  
# ADHD: Self=Internal, Time=Internal, Integration=Collapsed

# Behavioral patterns
# NT:  Flexible, moderate planning, adaptive
# ASD: Consistent, extended planning, systematic
# ADHD: Immediate, minimal planning, intense
```

Happy exploring! 🧠✨
