"""
Test Scenarios for AI Pathfinder
Pre-defined grids for testing best-case and worst-case scenarios
"""

from typing import Set, Tuple
import config

class TestScenarios:
    """Collection of test scenarios for different algorithms"""
    
    @staticmethod
    def get_empty_grid() -> Set[Tuple[int, int]]:
        """Empty grid - best case for most algorithms"""
        return set()
    
    @staticmethod
    def get_simple_maze() -> Set[Tuple[int, int]]:
        """Simple maze with a clear path"""
        walls = set()
        # Create a simple corridor
        for r in range(5, 15):
            walls.add((r, 10))
        # Add opening
        walls.remove((10, 10))
        return walls
    
    @staticmethod
    def get_complex_maze() -> Set[Tuple[int, int]]:
        """Complex maze - worst case for DFS"""
        walls = set()
        # Create multiple corridors and dead ends
        for r in range(2, 18):
            if r % 4 != 0:
                walls.add((r, 5))
                walls.add((r, 10))
                walls.add((r, 15))
        
        # Create openings
        for r in [4, 8, 12, 16]:
            if (r, 5) in walls:
                walls.remove((r, 5))
            if (r, 10) in walls:
                walls.remove((r, 10))
            if (r, 15) in walls:
                walls.remove((r, 15))
        
        return walls
    
    @staticmethod
    def get_spiral_maze() -> Set[Tuple[int, int]]:
        """Spiral maze - challenging for most algorithms"""
        walls = set()
        # Create a spiral pattern
        for i in range(3, 17):
            walls.add((3, i))
            walls.add((17, i))
            walls.add((i, 3))
            walls.add((i, 17))
        
        for i in range(5, 15):
            walls.add((5, i))
            walls.add((15, i))
            walls.add((i, 5))
            walls.add((i, 15))
        
        for i in range(7, 13):
            walls.add((7, i))
            walls.add((13, i))
            walls.add((i, 7))
            walls.add((i, 13))
        
        # Create openings for the spiral
        walls.discard((3, 3))
        walls.discard((5, 17))
        walls.discard((7, 5))
        walls.discard((9, 15))
        walls.discard((11, 7))
        walls.discard((13, 13))
        
        return walls
    
    @staticmethod
    def get_random_obstacles(density: float = 0.3) -> Set[Tuple[int, int]]:
        """Random obstacles with specified density"""
        import random
        walls = set()
        for r in range(config.GRID_ROWS):
            for c in range(config.GRID_COLS):
                if random.random() < density:
                    walls.add((r, c))
        return walls
    
    @staticmethod
    def get_best_case_bfs() -> Set[Tuple[int, int]]:
        """Best case for BFS - straight line to target"""
        return set()
    
    @staticmethod
    def get_worst_case_bfs() -> Set[Tuple[int, int]]:
        """Worst case for BFS - target at the end of exploration"""
        walls = set()
        # Force BFS to explore most of the grid
        for c in range(1, config.GRID_COLS - 1):
            for r in range(1, config.GRID_ROWS - 2):
                if c % 2 == 0:
                    walls.add((r, c))
        return walls
    
    @staticmethod
    def get_best_case_dfs() -> Set[Tuple[int, int]]:
        """Best case for DFS - straight path in the first direction"""
        return set()
    
    @staticmethod
    def get_worst_case_dfs() -> Set[Tuple[int, int]]:
        """Worst case for DFS - many dead ends"""
        return TestScenarios.get_complex_maze()
    
    @staticmethod
    def get_best_case_bidirectional() -> Set[Tuple[int, int]]:
        """Best case for Bidirectional - meets in the middle quickly"""
        return set()
    
    @staticmethod
    def get_worst_case_bidirectional() -> Set[Tuple[int, int]]:
        """Worst case for Bidirectional - complex maze"""
        return TestScenarios.get_spiral_maze()


# Example usage
if __name__ == "__main__":
    scenarios = TestScenarios()
    print("Available test scenarios:")
    print("1. Empty Grid (Best case for most)")
    print("2. Simple Maze")
    print("3. Complex Maze (Worst case for DFS)")
    print("4. Spiral Maze (Challenging)")
    print("5. Random Obstacles")
    print("\nTo use these scenarios, import them in your main application:")
    print("from test_scenarios import TestScenarios")
    print("grid.set_custom_walls(TestScenarios.get_complex_maze())")
