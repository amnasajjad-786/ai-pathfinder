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

# Colors (R, G, B) - Modern Pinterest Style
COLOR_BACKGROUND = (250, 250, 252)  # Soft off-white
COLOR_GRID_LINE = (230, 230, 235)   # Very light gray
COLOR_START = (52, 211, 153)        # Emerald green
COLOR_TARGET = (239, 68, 68)        # Vibrant red
COLOR_WALL = (71, 85, 105)          # Slate gray
COLOR_DYNAMIC_OBSTACLE = (156, 163, 175)  # Medium gray
COLOR_FRONTIER = (147, 197, 253)    # Sky blue
COLOR_EXPLORED = (253, 224, 71)     # Warm yellow
COLOR_PATH = (167, 139, 250)        # Purple
COLOR_TEXT = (30, 41, 59)           # Dark slate
COLOR_BUTTON = (99, 102, 241)       # Indigo
COLOR_BUTTON_HOVER = (129, 140, 248)  # Light indigo
COLOR_CARD_BG = (255, 255, 255)     # Pure white
COLOR_SHADOW = (203, 213, 225)      # Light shadow
COLOR_ACCENT = (236, 72, 153)       # Pink accent

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
