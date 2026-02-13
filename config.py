"""
Configuration file for AI Pathfinder
Contains all constants and settings for the application
"""

# Grid Settings
GRID_ROWS = 20
GRID_COLS = 20

# GUI Settings
CELL_SIZE = 30  # pixels
WINDOW_WIDTH = GRID_COLS * CELL_SIZE + 400  # Extra space for controls
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE + 100  # Extra space for info
FPS = 60

# Animation Settings
ANIMATION_DELAY = 0.05  # seconds between steps (adjustable)
FAST_MODE_DELAY = 0.01

# Dynamic Obstacles
DYNAMIC_OBSTACLE_PROBABILITY = 0.02  # 2% chance per step

# Depth Limit for DLS
DEPTH_LIMIT = 15

# Colors (R, G, B)
COLOR_BACKGROUND = (255, 255, 255)  # White
COLOR_GRID_LINE = (200, 200, 200)   # Light gray
COLOR_START = (0, 255, 0)           # Green
COLOR_TARGET = (255, 0, 0)          # Red
COLOR_WALL = (0, 0, 0)              # Black
COLOR_DYNAMIC_OBSTACLE = (128, 128, 128)  # Gray
COLOR_FRONTIER = (173, 216, 230)    # Light blue
COLOR_EXPLORED = (255, 255, 0)      # Yellow
COLOR_PATH = (128, 0, 128)          # Purple
COLOR_TEXT = (0, 0, 0)              # Black
COLOR_BUTTON = (100, 100, 255)      # Blue
COLOR_BUTTON_HOVER = (150, 150, 255)  # Light blue

# Movement directions (8-directional including all diagonals)
# Order: Up, Up-Right, Right, Down-Right, Down, Down-Left, Left, Up-Left
DIRECTIONS = [
    (-1, 0),   # Up
    (-1, 1),   # Up-Right
    (0, 1),    # Right
    (1, 1),    # Down-Right
    (1, 0),    # Down
    (1, -1),   # Down-Left
    (0, -1),   # Left
    (-1, -1),  # Up-Left
]

# Algorithm names
ALGORITHMS = [
    "BFS - Breadth-First Search",
    "DFS - Depth-First Search",
    "UCS - Uniform-Cost Search",
    "DLS - Depth-Limited Search",
    "IDDFS - Iterative Deepening DFS",
    "Bidirectional Search"
]
