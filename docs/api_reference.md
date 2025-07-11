# TIDE API Reference

## Core Classes

### `CognitiveArchitecture`

The main class for creating and using cognitive architectures.

```python
from tide import CognitiveArchitecture

# Create an architecture
arch = CognitiveArchitecture(architecture_type='NT')
```

#### Parameters
- `architecture_type` (str): One of 'NT', 'ASD', 'ADHD'

#### Methods

##### `process_information(information: Dict[str, Any]) -> Dict[str, Any]`
Process information according to architecture-specific patterns.

```python
info = {
    'content': 'planning a project',
    'temporal_context': 'next month'
}
result = arch.process_information(info)
```

##### `get_behavioral_signature() -> Dict[str, float]`
Get observable behavioral metrics.

```python
signature = arch.get_behavioral_signature()
# Returns:
# {
#     'temporal_consistency': 0.6,
#     'processing_flexibility': 0.8,
#     'planning_horizon': 30,
#     'self_time_integration': 0.75
# }
```

### `DimensionalSpace`

Maps cognitive elements onto internal-external dimensions.

```python
from tide import DimensionalSpace

space = DimensionalSpace()
```

#### Methods

##### `compute_element_position(element: str, architecture: str) -> np.ndarray`
Get the dimensional position of a cognitive element.

```python
position = space.compute_element_position('self', 'ASD')
# Returns: [0.2, 0.8]  # [internal, external]
```

##### `compute_dimensional_distance(elem1: str, elem2: str, architecture: str) -> float`
Calculate distance between elements in dimensional space.

```python
distance = space.compute_dimensional_distance('self', 'time', 'NT')
```

### `IntegrationEngine`

Models self-time binding dynamics.

```python
from tide.core.integration import IntegrationEngine

engine = IntegrationEngine('NT')
```

#### Methods

##### `compute_integration(self_state: np.ndarray, time_state: np.ndarray) -> float`
Calculate integration strength (Φ).

```python
self_state = np.array([0.8, 0.2])
time_state = np.array([0.2, 0.8])
phi = engine.compute_integration(self_state, time_state)
```

##### `get_integration_stability() -> float`
Measure stability of integration over time.

```python
stability = engine.get_integration_stability()
```

## Visualization Tools

### `DimensionalMapper`

Create scientific visualizations of architectures.

```python
from tide.visualization import DimensionalMapper

mapper = DimensionalMapper()
```

#### Methods

##### `create_architecture_comparison(elements: List[str] = None)`
Generate comparison visualization across architectures.

```python
fig = mapper.create_architecture_comparison()
fig.savefig('comparison.png')
```

##### `create_integration_landscape()`
Create 3D integration landscape visualization.

```python
fig = mapper.create_integration_landscape()
```

## Example Workflows

### Basic Usage

```python
from tide import CognitiveArchitecture

# Create architectures
nt = CognitiveArchitecture('NT')
asd = CognitiveArchitecture('ASD')

# Process same information differently
info = {'content': 'schedule meeting', 'temporal_context': 'tomorrow'}

nt_result = nt.process_information(info)
asd_result = asd.process_information(info)

# Compare behavioral signatures
print(f"NT flexibility: {nt.get_behavioral_signature()['processing_flexibility']}")
print(f"ASD consistency: {asd.get_behavioral_signature()['temporal_consistency']}")
```

### Temporal Planning Demo

```python
from tide.examples import TemporalPlanningTask

# Create planners
nt_planner = TemporalPlanningTask('NT')
asd_planner = TemporalPlanningTask('ASD')

# Generate plans
nt_plan = nt_planner.plan_week()
asd_plan = asd_planner.plan_week()

# Measure consistency
nt_consistency = nt_planner.evaluate_plan_consistency()
asd_consistency = asd_planner.evaluate_plan_consistency()
```

### Visualization

```python
from tide.visualization import DimensionalMapper
import matplotlib.pyplot as plt

mapper = DimensionalMapper()

# Create and save visualizations
fig = mapper.create_architecture_comparison(
    elements=['self', 'time', 'emotion', 'logic']
)
fig.savefig('tide_dimensions.png', dpi=300)
plt.show()
```

## Configuration

Architecture configurations are stored in `tide.config`:

```python
from tide.config import ARCHITECTURE_CONFIGS

print(ARCHITECTURE_CONFIGS['ASD'])
# {
#     'self_dimension': 'external',
#     'time_dimension': 'external',
#     'integration_style': 'crystallized',
#     'processing_flexibility': 0.3,
#     'temporal_consistency': 0.9,
#     'planning_horizon': 90
# }
```

## Error Handling

```python
try:
    arch = CognitiveArchitecture('INVALID')
except ValueError as e:
    print(f"Error: {e}")
    # Use a valid architecture
    arch = CognitiveArchitecture('NT')
```
