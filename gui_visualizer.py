"""
GUI Visualizer using Pygame
Provides real-time step-by-step visualization of search algorithms
"""

import pygame
import sys
import time
from typing import Optional
import config
from grid_environment import GridEnvironment, SearchAlgorithms

class Button:
    """Simple button class for GUI controls"""
    
    def __init__(self, x, y, width, height, text, color=config.COLOR_BUTTON):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = config.COLOR_BUTTON_HOVER
        self.is_hovered = False
    
    def draw(self, screen, font):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, config.COLOR_TEXT, self.rect, 2)
        
        text_surface = font.render(self.text, True, config.COLOR_TEXT)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False


class GUIVisualizer:
    """Main GUI class for visualizing search algorithms"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption("GOOD PERFORMANCE TIME APP")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 20)
        
        # Grid and algorithms
        self.grid = GridEnvironment()
        self.search = SearchAlgorithms(self.grid)
        
        # Visualization state
        self.current_step = 0
        self.is_running = False
        self.is_complete = False
        self.selected_algorithm = 0
        self.animation_speed = config.ANIMATION_DELAY
        
        # Create buttons
        button_y = config.WINDOW_HEIGHT - 80
        button_width = 120
        button_spacing = 10
        start_x = 20
        
        self.buttons = {
            'run': Button(start_x, button_y, button_width, 40, 'Run'),
            'reset': Button(start_x + button_width + button_spacing, button_y, button_width, 40, 'Reset'),
            'next_algo': Button(start_x + 2 * (button_width + button_spacing), button_y, button_width, 40, 'Next Algo'),
            'speed_up': Button(start_x + 3 * (button_width + button_spacing), button_y, button_width, 40, 'Speed Up'),
            'slow_down': Button(start_x + 4 * (button_width + button_spacing), button_y, button_width, 40, 'Slow Down'),
        }
        
        self.last_update_time = time.time()
    
    def draw_grid(self):
        """Draw the grid with all cells"""
        grid_surface = pygame.Surface((config.GRID_COLS * config.CELL_SIZE, 
                                       config.GRID_ROWS * config.CELL_SIZE))
        grid_surface.fill(config.COLOR_BACKGROUND)
        
        # Get current visualization state
        frontier = set()
        explored = set()
        
        if self.is_running and self.current_step < len(self.search.frontier_history):
            frontier = set(self.search.frontier_history[self.current_step])
            explored = set(self.search.explored_history[self.current_step])
        elif self.is_complete:
            if len(self.search.explored_history) > 0:
                explored = set(self.search.explored_history[-1])
        
        # Draw cells
        for r in range(config.GRID_ROWS):
            for c in range(config.GRID_COLS):
                pos = (r, c)
                x = c * config.CELL_SIZE
                y = r * config.CELL_SIZE
                
                # Determine cell color
                if pos == self.grid.start:
                    color = config.COLOR_START
                elif pos == self.grid.target:
                    color = config.COLOR_TARGET
                elif pos in self.grid.walls:
                    color = config.COLOR_WALL
                elif pos in self.grid.dynamic_obstacles:
                    color = config.COLOR_DYNAMIC_OBSTACLE
                elif self.is_complete and pos in self.search.path:
                    color = config.COLOR_PATH
                elif pos in frontier:
                    color = config.COLOR_FRONTIER
                elif pos in explored:
                    color = config.COLOR_EXPLORED
                else:
                    color = config.COLOR_BACKGROUND
                
                # Draw cell
                pygame.draw.rect(grid_surface, color, (x, y, config.CELL_SIZE, config.CELL_SIZE))
                pygame.draw.rect(grid_surface, config.COLOR_GRID_LINE, 
                               (x, y, config.CELL_SIZE, config.CELL_SIZE), 1)
        
        self.screen.blit(grid_surface, (0, 0))
    
    def draw_info(self):
        """Draw information panel"""
        info_x = config.GRID_COLS * config.CELL_SIZE + 20
        info_y = 20
        
        # Algorithm name
        algo_text = config.ALGORITHMS[self.selected_algorithm]
        text_surface = self.font.render(algo_text, True, config.COLOR_TEXT)
        self.screen.blit(text_surface, (info_x, info_y))
        info_y += 40
        
        # Current step
        if self.is_running or self.is_complete:
            step_text = f"Step: {self.current_step}/{len(self.search.frontier_history)}"
            text_surface = self.small_font.render(step_text, True, config.COLOR_TEXT)
            self.screen.blit(text_surface, (info_x, info_y))
            info_y += 30
            
            # Nodes explored
            if self.current_step < len(self.search.explored_history):
                explored_count = len(self.search.explored_history[self.current_step])
            else:
                explored_count = len(self.search.explored_history[-1]) if self.search.explored_history else 0
            
            explored_text = f"Explored: {explored_count}"
            text_surface = self.small_font.render(explored_text, True, config.COLOR_TEXT)
            self.screen.blit(text_surface, (info_x, info_y))
            info_y += 30
            
            # Path length
            if self.is_complete and self.search.path:
                path_text = f"Path Length: {len(self.search.path)}"
                text_surface = self.small_font.render(path_text, True, config.COLOR_TEXT)
                self.screen.blit(text_surface, (info_x, info_y))
                info_y += 30
        
        # Speed
        info_y += 20
        speed_text = f"Speed: {self.animation_speed:.3f}s"
        text_surface = self.small_font.render(speed_text, True, config.COLOR_TEXT)
        self.screen.blit(text_surface, (info_x, info_y))
        info_y += 40
        
        # Legend
        info_y += 20
        legend_items = [
            ("Start (S)", config.COLOR_START),
            ("Target (T)", config.COLOR_TARGET),
            ("Wall", config.COLOR_WALL),
            ("Dynamic Obstacle", config.COLOR_DYNAMIC_OBSTACLE),
            ("Frontier", config.COLOR_FRONTIER),
            ("Explored", config.COLOR_EXPLORED),
            ("Path", config.COLOR_PATH),
        ]
        
        for label, color in legend_items:
            pygame.draw.rect(self.screen, color, (info_x, info_y, 20, 20))
            pygame.draw.rect(self.screen, config.COLOR_TEXT, (info_x, info_y, 20, 20), 1)
            text_surface = self.small_font.render(label, True, config.COLOR_TEXT)
            self.screen.blit(text_surface, (info_x + 30, info_y))
            info_y += 25
    
    def draw_buttons(self):
        """Draw all control buttons"""
        for button in self.buttons.values():
            button.draw(self.screen, self.small_font)
    
    def handle_events(self):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            # Handle button clicks
            for name, button in self.buttons.items():
                if button.handle_event(event):
                    if name == 'run':
                        self.run_algorithm()
                    elif name == 'reset':
                        self.reset()
                    elif name == 'next_algo':
                        self.next_algorithm()
                    elif name == 'speed_up':
                        self.animation_speed = max(0.001, self.animation_speed / 2)
                    elif name == 'slow_down':
                        self.animation_speed = min(1.0, self.animation_speed * 2)
        
        return True
    
    def run_algorithm(self):
        """Execute the selected algorithm"""
        if self.is_running:
            return
        
        # Reset grid dynamic obstacles
        self.grid.reset_dynamic_obstacles()
        
        # Run the selected algorithm
        self.is_running = True
        self.is_complete = False
        self.current_step = 0
        
        algorithm_methods = [
            self.search.bfs,
            self.search.dfs,
            self.search.ucs,
            self.search.dls,
            self.search.iddfs,
            self.search.bidirectional_search
        ]
        
        success = algorithm_methods[self.selected_algorithm]()
        
        if not success:
            print(f"Algorithm {config.ALGORITHMS[self.selected_algorithm]} failed to find a path!")
    
    def reset(self):
        """Reset the visualization"""
        self.grid = GridEnvironment()
        self.search = SearchAlgorithms(self.grid)
        self.current_step = 0
        self.is_running = False
        self.is_complete = False
    
    def next_algorithm(self):
        """Switch to the next algorithm"""
        self.selected_algorithm = (self.selected_algorithm + 1) % len(config.ALGORITHMS)
        self.reset()
    
    def update(self):
        """Update the visualization state"""
        if self.is_running and not self.is_complete:
            current_time = time.time()
            if current_time - self.last_update_time >= self.animation_speed:
                self.last_update_time = current_time
                self.current_step += 1
                
                if self.current_step >= len(self.search.frontier_history):
                    self.is_complete = True
                    self.is_running = False
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            
            # Draw everything
            self.screen.fill(config.COLOR_BACKGROUND)
            self.draw_grid()
            self.draw_info()
            self.draw_buttons()
            
            pygame.display.flip()
            self.clock.tick(config.FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    visualizer = GUIVisualizer()
    visualizer.run()
