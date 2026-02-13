"""
AI Pathfinder - Main Entry Point
Uninformed Search Algorithms Visualizer
"""

from gui_visualizer import GUIVisualizer

def main():
    """Main entry point for the application"""
    print("=" * 60)
    print("AI PATHFINDER - Uninformed Search Visualizer")
    print("=" * 60)
    print("\nControls:")
    print("  - Run: Execute the selected algorithm")
    print("  - Reset: Clear the grid and start over")
    print("  - Next Algo: Switch to the next algorithm")
    print("  - Speed Up/Slow Down: Adjust animation speed")
    print("\nAlgorithms:")
    print("  1. BFS - Breadth-First Search")
    print("  2. DFS - Depth-First Search")
    print("  3. UCS - Uniform-Cost Search")
    print("  4. DLS - Depth-Limited Search")
    print("  5. IDDFS - Iterative Deepening DFS")
    print("  6. Bidirectional Search")
    print("\nStarting GUI...")
    print("=" * 60)
    
    visualizer = GUIVisualizer()
    visualizer.run()

if __name__ == "__main__":
    main()
