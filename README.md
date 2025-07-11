# TIDE: Temporal-Internal Dimensional Encoding

> Part of the [Cognitive Architectures for AI](https://github.com/HillaryDanan/cognitive-architectures-ai) research program


A neuroscience-inspired framework for understanding cognitive architecture patterns through dimensional organization of self-representation and temporal processing.

## Overview

TIDE demonstrates how different cognitive systems achieve information integration through distinct dimensional arrangements, inspired by findings from autism research showing alternative neural pathways for abstract concept processing (Levinson, 2021).

## Key Insight

Different cognitive architectures represent valid solutions to the fundamental challenge of integrating self-representation with temporal processing:

- **NT-TIDE** (Neurotypical): Dynamic balance between internal self and external time
- **ASD-TIDE** (Autism): Systematic alignment with both self and time in external dimension  
- **ADHD-TIDE** (ADHD): Unified but unstable integration in internal dimension

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

## Quick Start

```python
from tide import CognitiveArchitecture, DimensionalMapper

# Create architecture
nt_arch = CognitiveArchitecture('NT')
asd_arch = CognitiveArchitecture('ASD')

# Compare behavioral signatures
print(nt_arch.get_behavioral_signature())
print(asd_arch.get_behavioral_signature())

# Visualize dimensional mappings
mapper = DimensionalMapper()
fig = mapper.create_architecture_comparison()
fig.savefig('architecture_comparison.png')
```

## Applications

### 1. Cognitive Diversity in AI Systems
Different tasks benefit from different cognitive architectures:
- Systematic tasks → ASD-TIDE architecture
- Adaptive tasks → NT-TIDE architecture  
- Rapid response tasks → ADHD-TIDE architecture

### 2. Interpretable AI Behavior
The dimensional framework provides interpretable explanations for AI system behavior based on their cognitive architecture configuration.

### 3. Robust System Design
Multiple architectures working together create more robust systems than monolithic approaches.

## Theoretical Foundation

Based on empirical findings from neuroscience research:
- Alternative neural pathways achieve identical outcomes (Levinson, 2021)
- Dimensional reorganization explains behavioral differences
- Builds on previous work: [BIND](https://github.com/HillaryDanan/BIND), [Concrete-Overflow](https://github.com/HillaryDanan/concrete-overflow-detector)

## Documentation

- [Theoretical Foundation](docs/theoretical_foundation.md)
- [API Reference](docs/api_reference.md)
- [Tutorials](docs/tutorials/)

## Citation

If you use TIDE in your research, please cite:

```bibtex
@software{danan2025tide,
  author = {Danan, Hillary},
  title = {TIDE: Temporal-Internal Dimensional Encoding},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/HillaryDanan/TIDE}
}

@phdthesis{levinson2021neural,
  author = {Levinson, Hillary Jane},
  title = {The Neural Representation of Abstract Concepts in Typical and Atypical Cognition},
  school = {Rutgers University},
  year = {2021}
}
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contact

Hillary Danan - [GitHub](https://github.com/HillaryDanan)


## Interactive Demo

🚀 **[Try the Interactive TIDE Tool](https://hillarydanan.github.io/TIDE/tide_interactive.html)**

Explore how different cognitive architectures organize self-representation and temporal processing in real-time.


## Research Journey

This work represents the culmination of a research trajectory exploring information processing and cognitive architectures. See the [meta-repository overview](meta-repository.md) for the complete research journey from BIND through TIDE.


## Important Note on Terminology

I use diagnostic labels (NT, ASD, ADHD) throughout this framework as communication tools, not because I believe in rigid categorization. These terms represent observable patterns in cognitive organization, not fixed identities or disorders. See [DISCLAIMER.md](DISCLAIMER.md) for my full thoughts on labels and cognitive diversity.

TIDE demonstrates that different cognitive patterns are simply different solutions to the same challenges - each with unique strengths. The framework itself embodies the dynamic, fluid nature of cognition (hence "TIDE" - patterns that ebb and flow).
