# AI Pathfinder - Uninformed Search Visualizer

A comprehensive visualization tool for 6 uninformed search algorithms with dynamic obstacle support and real-time GUI animation.

## 📖 Documentation

**📝 Read the full comprehensive report on Medium**: [AI Pathfinder - Comprehensive Report](https://medium.com/@amnasajjadashraf/ai-pathfinder-comprehensive-report-16fa80527a1d)

## 🎯 Features

- **6 Uninformed Search Algorithms**:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Uniform-Cost Search (UCS)
  - Depth-Limited Search (DLS)
  - Iterative Deepening DFS (IDDFS)
  - Bidirectional Search

- **Real-time Visualization**: Step-by-step animation showing how algorithms explore the grid
- **Dynamic Obstacles**: Random obstacles spawn during search, forcing re-planning
- **Interactive GUI**: Built with Pygame for smooth, responsive visualization
- **Color-coded Display**:
  - 🟢 Green: Start point (S)
  - 🔴 Red: Target point (T)
  - ⬛ Black: Static walls
  - ⬜ Gray: Dynamic obstacles
  - 🔵 Light Blue: Frontier nodes (waiting to be explored)
  - 🟡 Yellow: Explored nodes
  - 🟣 Purple: Final path

## 📋 Requirements

- Python 3.7+
- Pygame
- NumPy

## 🚀 Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install pygame numpy
   ```

## 🎮 Usage

### Running the Application

```bash
python main.py
```

Or run the GUI directly:
```bash
python gui_visualizer.py
```

### Controls

- **Run**: Execute the currently selected algorithm
- **Reset**: Clear the grid and generate a new random maze
- **Next Algo**: Switch to the next algorithm in the list
- **Speed Up**: Increase animation speed (faster visualization)
- **Slow Down**: Decrease animation speed (slower, more detailed view)

### Using Test Scenarios

To test specific scenarios (best-case, worst-case), modify `main.py` or `gui_visualizer.py`:

```python
from test_scenarios import TestScenarios

# In GUIVisualizer.__init__() or after creating grid:
self.grid.set_custom_walls(TestScenarios.get_complex_maze())
```

Available scenarios:
- `get_empty_grid()` - Best case for most algorithms
- `get_simple_maze()` - Simple corridor maze
- `get_complex_maze()` - Worst case for DFS
- `get_spiral_maze()` - Challenging for all algorithms
- `get_random_obstacles(density)` - Random obstacles

## 📁 Project Structure

```
ai_pathfinder/
├── main.py                 # Main entry point
├── gui_visualizer.py       # Pygame GUI implementation
├── grid_environment.py     # Grid and search algorithms
├── config.py              # Configuration constants
├── test_scenarios.py      # Pre-defined test grids
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Configuration

Edit `config.py` to customize:
- Grid size (default: 20x20)
- Cell size for visualization
- Animation speed
- Dynamic obstacle probability
- Depth limit for DLS
- Colors

## 🧪 Algorithm Details

### BFS (Breadth-First Search)
- **Strategy**: Explores level by level
- **Best Case**: Target is close to start
- **Worst Case**: Target is far away, explores entire grid

### DFS (Depth-First Search)
- **Strategy**: Explores as deep as possible before backtracking
- **Best Case**: Target is in the first explored path
- **Worst Case**: Many dead ends, explores unnecessary paths

### UCS (Uniform-Cost Search)
- **Strategy**: Expands lowest-cost nodes first
- **Best Case**: Straight diagonal path
- **Worst Case**: Complex maze with many turns

### DLS (Depth-Limited Search)
- **Strategy**: DFS with depth limit
- **Best Case**: Target within depth limit
- **Worst Case**: Target beyond depth limit (fails)

### IDDFS (Iterative Deepening DFS)
- **Strategy**: Repeatedly runs DLS with increasing depth
- **Best Case**: Target at shallow depth
- **Worst Case**: Target at maximum depth

### Bidirectional Search
- **Strategy**: Searches from both start and target simultaneously
- **Best Case**: Searches meet quickly in the middle
- **Worst Case**: Complex maze, searches explore large areas

## 📊 Dynamic Obstacles

The system randomly spawns obstacles during algorithm execution with a configurable probability (default: 2% per step). When an obstacle blocks the planned path, the algorithm must re-plan the route.

## 🎓 Assignment Compliance

This project fulfills all requirements for **AI2002 Assignment 1, Question 7**:
- ✅ All 6 uninformed search algorithms implemented
- ✅ 8-directional movement (including all diagonals)
- ✅ Dynamic obstacle system with re-planning
- ✅ GUI with step-by-step visualization
- ✅ Frontier, explored, and path visualization
- ✅ Real-time animation
- ✅ GUI title: "GOOD PERFORMANCE TIME APP"

## 👨‍💻 Author

-22F-3347 Amna Sajjad
-22F-3071 Shahzaib 

## 📝 License

This project is created for educational purposes.
