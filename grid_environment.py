"""
Grid Environment and Search Algorithms
Implements all 6 uninformed search algorithms with dynamic obstacle support
"""

import random
from collections import deque
from typing import List, Tuple, Set, Optional, Dict
import config

class GridEnvironment:
    """Represents the grid world with start, target, walls, and dynamic obstacles"""
    
    def __init__(self, rows: int = config.GRID_ROWS, cols: int = config.GRID_COLS):
        self.rows = rows
        self.cols = cols
        self.start = (1, 1)  # Start position (row, col)
        self.target = (rows - 2, cols - 2)  # Target position
        self.walls = set()  # Static walls
        self.dynamic_obstacles = set()  # Dynamic obstacles that appear during search
        self.generate_random_walls()
    
    def generate_random_walls(self, wall_probability: float = 0.2):
        """Generate random walls in the grid"""
        for r in range(self.rows):
            for c in range(self.cols):
                # Don't place walls on start, target, or borders
                if (r, c) == self.start or (r, c) == self.target:
                    continue
                if random.random() < wall_probability:
                    self.walls.add((r, c))
    
    def set_custom_walls(self, walls: Set[Tuple[int, int]]):
        """Set custom wall positions"""
        self.walls = walls.copy()
    
    def is_valid(self, pos: Tuple[int, int]) -> bool:
        """Check if position is valid (within bounds and not a wall)"""
        r, c = pos
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return False
        if pos in self.walls or pos in self.dynamic_obstacles:
            return False
        return True
    
    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighbors in the specified movement order"""
        r, c = pos
        neighbors = []
        for dr, dc in config.DIRECTIONS:
            new_pos = (r + dr, c + dc)
            if self.is_valid(new_pos):
                neighbors.append(new_pos)
        return neighbors
    
    def spawn_dynamic_obstacle(self):
        """Randomly spawn a dynamic obstacle"""
        if random.random() < config.DYNAMIC_OBSTACLE_PROBABILITY:
            # Find a random empty cell
            empty_cells = []
            for r in range(self.rows):
                for c in range(self.cols):
                    pos = (r, c)
                    if pos != self.start and pos != self.target and pos not in self.walls and pos not in self.dynamic_obstacles:
                        empty_cells.append(pos)
            
            if empty_cells:
                obstacle_pos = random.choice(empty_cells)
                self.dynamic_obstacles.add(obstacle_pos)
                return obstacle_pos
        return None
    
    def reset_dynamic_obstacles(self):
        """Clear all dynamic obstacles"""
        self.dynamic_obstacles.clear()


class SearchAlgorithms:
    """Implements all 6 uninformed search algorithms"""
    
    def __init__(self, grid: GridEnvironment):
        self.grid = grid
        self.frontier_history = []  # Track frontier nodes at each step
        self.explored_history = []  # Track explored nodes at each step
        self.path = []  # Final path
        self.dynamic_obstacle_spawned = []  # Track when obstacles spawn
    
    def reconstruct_path(self, came_from: Dict, current: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Reconstruct path from start to current using came_from dictionary"""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
    
    def bfs(self) -> bool:
        """Breadth-First Search"""
        self.frontier_history = []
        self.explored_history = []
        self.dynamic_obstacle_spawned = []
        
        queue = deque([self.grid.start])
        came_from = {}
        explored = set()
        
        while queue:
            # Spawn dynamic obstacle
            obstacle = self.grid.spawn_dynamic_obstacle()
            if obstacle:
                self.dynamic_obstacle_spawned.append(len(self.frontier_history))
            
            # Record current state
            self.frontier_history.append(list(queue))
            self.explored_history.append(explored.copy())
            
            current = queue.popleft()
            
            if current == self.grid.target:
                self.path = self.reconstruct_path(came_from, current)
                return True
            
            if current in explored:
                continue
            
            explored.add(current)
            
            for neighbor in self.grid.get_neighbors(current):
                if neighbor not in explored and neighbor not in queue:
                    queue.append(neighbor)
                    came_from[neighbor] = current
        
        return False
    
    def dfs(self) -> bool:
        """Depth-First Search"""
        self.frontier_history = []
        self.explored_history = []
        self.dynamic_obstacle_spawned = []
        
        stack = [self.grid.start]
        came_from = {}
        explored = set()
        
        while stack:
            # Spawn dynamic obstacle
            obstacle = self.grid.spawn_dynamic_obstacle()
            if obstacle:
                self.dynamic_obstacle_spawned.append(len(self.frontier_history))
            
            # Record current state
            self.frontier_history.append(stack.copy())
            self.explored_history.append(explored.copy())
            
            current = stack.pop()
            
            if current == self.grid.target:
                self.path = self.reconstruct_path(came_from, current)
                return True
            
            if current in explored:
                continue
            
            explored.add(current)
            
            # Add neighbors in reverse order so they're popped in correct order
            neighbors = self.grid.get_neighbors(current)
            for neighbor in reversed(neighbors):
                if neighbor not in explored and neighbor not in stack:
                    stack.append(neighbor)
                    came_from[neighbor] = current
        
        return False
    
    def ucs(self) -> bool:
        """Uniform-Cost Search"""
        self.frontier_history = []
        self.explored_history = []
        self.dynamic_obstacle_spawned = []
        
        # Priority queue: (cost, position)
        # Using list and sorting for simplicity
        frontier = [(0, self.grid.start)]
        came_from = {}
        cost_so_far = {self.grid.start: 0}
        explored = set()
        
        while frontier:
            # Spawn dynamic obstacle
            obstacle = self.grid.spawn_dynamic_obstacle()
            if obstacle:
                self.dynamic_obstacle_spawned.append(len(self.frontier_history))
            
            # Record current state
            self.frontier_history.append([pos for _, pos in frontier])
            self.explored_history.append(explored.copy())
            
            # Sort by cost and get lowest
            frontier.sort()
            current_cost, current = frontier.pop(0)
            
            if current == self.grid.target:
                self.path = self.reconstruct_path(came_from, current)
                return True
            
            if current in explored:
                continue
            
            explored.add(current)
            
            for neighbor in self.grid.get_neighbors(current):
                # Calculate cost (diagonal moves cost sqrt(2), straight moves cost 1)
                dr = abs(neighbor[0] - current[0])
                dc = abs(neighbor[1] - current[1])
                move_cost = 1.414 if (dr + dc) == 2 else 1.0
                new_cost = current_cost + move_cost
                
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    frontier.append((new_cost, neighbor))
                    came_from[neighbor] = current
        
        return False
    
    def dls(self, limit: int = config.DEPTH_LIMIT) -> bool:
        """Depth-Limited Search"""
        self.frontier_history = []
        self.explored_history = []
        self.dynamic_obstacle_spawned = []
        
        # Stack: (position, depth)
        stack = [(self.grid.start, 0)]
        came_from = {}
        explored = set()
        
        while stack:
            # Spawn dynamic obstacle
            obstacle = self.grid.spawn_dynamic_obstacle()
            if obstacle:
                self.dynamic_obstacle_spawned.append(len(self.frontier_history))
            
            # Record current state
            self.frontier_history.append([pos for pos, _ in stack])
            self.explored_history.append(explored.copy())
            
            current, depth = stack.pop()
            
            if current == self.grid.target:
                self.path = self.reconstruct_path(came_from, current)
                return True
            
            if current in explored or depth >= limit:
                continue
            
            explored.add(current)
            
            if depth < limit:
                neighbors = self.grid.get_neighbors(current)
                for neighbor in reversed(neighbors):
                    if neighbor not in explored:
                        stack.append((neighbor, depth + 1))
                        if neighbor not in came_from:
                            came_from[neighbor] = current
        
        return False
    
    def iddfs(self) -> bool:
        """Iterative Deepening Depth-First Search"""
        self.frontier_history = []
        self.explored_history = []
        self.dynamic_obstacle_spawned = []
        
        max_depth = self.grid.rows * self.grid.cols
        
        for depth_limit in range(max_depth):
            # Perform DLS at current depth
            stack = [(self.grid.start, 0)]
            came_from = {}
            explored = set()
            
            while stack:
                # Spawn dynamic obstacle
                obstacle = self.grid.spawn_dynamic_obstacle()
                if obstacle:
                    self.dynamic_obstacle_spawned.append(len(self.frontier_history))
                
                # Record current state
                self.frontier_history.append([pos for pos, _ in stack])
                self.explored_history.append(explored.copy())
                
                current, depth = stack.pop()
                
                if current == self.grid.target:
                    self.path = self.reconstruct_path(came_from, current)
                    return True
                
                if current in explored or depth >= depth_limit:
                    continue
                
                explored.add(current)
                
                if depth < depth_limit:
                    neighbors = self.grid.get_neighbors(current)
                    for neighbor in reversed(neighbors):
                        if neighbor not in explored:
                            stack.append((neighbor, depth + 1))
                            if neighbor not in came_from:
                                came_from[neighbor] = current
        
        return False
    
    def bidirectional_search(self) -> bool:
        """Bidirectional Search"""
        self.frontier_history = []
        self.explored_history = []
        self.dynamic_obstacle_spawned = []
        
        # Forward search from start
        queue_forward = deque([self.grid.start])
        came_from_forward = {}
        explored_forward = set()
        
        # Backward search from target
        queue_backward = deque([self.grid.target])
        came_from_backward = {}
        explored_backward = set()
        
        while queue_forward and queue_backward:
            # Spawn dynamic obstacle
            obstacle = self.grid.spawn_dynamic_obstacle()
            if obstacle:
                self.dynamic_obstacle_spawned.append(len(self.frontier_history))
            
            # Record current state (combine both frontiers)
            combined_frontier = list(queue_forward) + list(queue_backward)
            combined_explored = explored_forward.union(explored_backward)
            self.frontier_history.append(combined_frontier)
            self.explored_history.append(combined_explored)
            
            # Expand forward
            if queue_forward:
                current_f = queue_forward.popleft()
                
                if current_f in explored_backward:
                    # Found intersection!
                    path_forward = self.reconstruct_path(came_from_forward, current_f)
                    path_backward = self.reconstruct_path(came_from_backward, current_f)
                    path_backward.reverse()
                    self.path = path_forward[:-1] + path_backward
                    return True
                
                if current_f not in explored_forward:
                    explored_forward.add(current_f)
                    for neighbor in self.grid.get_neighbors(current_f):
                        if neighbor not in explored_forward and neighbor not in queue_forward:
                            queue_forward.append(neighbor)
                            came_from_forward[neighbor] = current_f
            
            # Expand backward
            if queue_backward:
                current_b = queue_backward.popleft()
                
                if current_b in explored_forward:
                    # Found intersection!
                    path_forward = self.reconstruct_path(came_from_forward, current_b)
                    path_backward = self.reconstruct_path(came_from_backward, current_b)
                    path_backward.reverse()
                    self.path = path_forward[:-1] + path_backward
                    return True
                
                if current_b not in explored_backward:
                    explored_backward.add(current_b)
                    for neighbor in self.grid.get_neighbors(current_b):
                        if neighbor not in explored_backward and neighbor not in queue_backward:
                            queue_backward.append(neighbor)
                            came_from_backward[neighbor] = current_b
        
        return False
