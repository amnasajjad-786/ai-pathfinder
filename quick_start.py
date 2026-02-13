"""
Quick Start Script
Helps you quickly test different scenarios and algorithms
"""

from gui_visualizer import GUIVisualizer
from test_scenarios import TestScenarios

def main():
    print("=" * 60)
    print("AI PATHFINDER - Quick Start")
    print("=" * 60)
    print("\nSelect a test scenario:")
    print("1. Empty Grid (Best Case)")
    print("2. Simple Maze")
    print("3. Complex Maze (Worst Case for DFS)")
    print("4. Spiral Maze (Challenging)")
    print("5. Random Obstacles")
    print("6. Default Random Grid")
    
    choice = input("\nEnter choice (1-6): ").strip()
    
    visualizer = GUIVisualizer()
    
    if choice == "1":
        visualizer.grid.set_custom_walls(TestScenarios.get_empty_grid())
        print("Loaded: Empty Grid")
    elif choice == "2":
        visualizer.grid.set_custom_walls(TestScenarios.get_simple_maze())
        print("Loaded: Simple Maze")
    elif choice == "3":
        visualizer.grid.set_custom_walls(TestScenarios.get_complex_maze())
        print("Loaded: Complex Maze")
    elif choice == "4":
        visualizer.grid.set_custom_walls(TestScenarios.get_spiral_maze())
        print("Loaded: Spiral Maze")
    elif choice == "5":
        density = float(input("Enter obstacle density (0.0-1.0, default 0.3): ") or "0.3")
        visualizer.grid.set_custom_walls(TestScenarios.get_random_obstacles(density))
        print(f"Loaded: Random Obstacles (density={density})")
    else:
        print("Loaded: Default Random Grid")
    
    print("\nStarting GUI...")
    print("Use the buttons to:")
    print("  - Run: Execute algorithm")
    print("  - Next Algo: Switch algorithm")
    print("  - Speed Up/Down: Adjust animation")
    print("  - Reset: New random grid")
    print("=" * 60)
    
    visualizer.run()

if __name__ == "__main__":
    main()
