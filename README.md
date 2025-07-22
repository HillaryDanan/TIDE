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

## 🌐 Part of the AI Architecture Research Suite

This tool is part of a comprehensive empirical framework for analyzing AI cognitive architectures through measurable patterns.

### 🧠 The Complete Framework

**📊 Data Collection & Analysis Pipeline:**
- [TIDE-analysis](https://github.com/HillaryDanan/TIDE-analysis) - Automated empirical data engine
- [Pattern Analyzer](https://github.com/HillaryDanan/pattern-analyzer) - Comprehensive analysis suite (14+ tools)
- [TIDE-Resonance](https://hillarydanan.github.io/TIDE-resonance/) - Central research platform & demos

**🔬 Core Theoretical Frameworks:**
- [TIDE Framework](https://github.com/HillaryDanan/TIDE) - Temporal-Internal Dynamics Engine
- [BIND](https://github.com/HillaryDanan/BIND) - Boundary Interface & Neurodiversity Dynamics
- [Information Atoms](https://github.com/HillaryDanan/information-atoms) - Alternative to tokenization

**🛠️ Specialized Analysis Tools:**
- [Concrete Overflow Detector](https://github.com/HillaryDanan/concrete-overflow-detector) - Neural pathway analysis
- [Hexagonal Pattern Suite](https://github.com/HillaryDanan/hexagonal-consciousness-suite) - Efficiency patterns
- [Game Theory Trust Suite](https://github.com/HillaryDanan/game-theory-trust-suite) - Cooperation dynamics
- [Cognitive Architectures](https://github.com/HillaryDanan/cognitive-architectures-ai) - NT/ASD/ADHD patterns
- [Hexagonal Vision Research](https://github.com/HillaryDanan/hexagonal-vision-research) - Visual processing

### 🎯 Live Demonstrations

Experience the frameworks in action:
- [🌊 TIDE-Resonance Platform](https://hillarydanan.github.io/TIDE-resonance/) - Main research hub
- [🔍 Pattern Analysis Dashboard](https://hillarydanan.github.io/pattern-analyzer/) - Live results
- [🎮 Interactive Resonance Explorer](https://hillarydanan.github.io/TIDE-resonance/interactive_resonance.html)
- [🧪 Advanced Analysis Tools](https://hillarydanan.github.io/TIDE-resonance/advanced_explorer.html)
- [🔄 BIND Systems Visualizer](https://hillarydanan.github.io/BIND/bind_systems_interactive.html)
- [📊 TIDE Interactive](https://hillarydanan.github.io/TIDE/tide_interactive.html)
- [📋 Contribute Data](https://hillarydanan.github.io/TIDE-resonance/collect.html)

### 🚀 Start Here

1. **New to the framework?** Start with [TIDE-Resonance](https://hillarydanan.github.io/TIDE-resonance/) for an overview
2. **Want to analyze AI responses?** Try the [Pattern Analyzer Demo](https://github.com/HillaryDanan/pattern-analyzer/tree/main/examples)
3. **Interested in the theory?** Read about [TIDE Framework](https://github.com/HillaryDanan/TIDE) and [BIND](https://github.com/HillaryDanan/BIND)
4. **Have data to contribute?** Use our [data collection tool](https://hillarydanan.github.io/TIDE-resonance/collect.html)

### 💡 The Vision

This ecosystem represents a new approach to understanding AI through:
- **Empirical measurement** of cognitive patterns
- **Multiple integrated tools** providing converging evidence
- **Neuroscience-grounded** frameworks based on real fMRI research
- **Open source** collaboration for reproducible science

Built with 💜 by [Hillary Danan](https://github.com/HillaryDanan) | Bridging neuroscience and AI research
