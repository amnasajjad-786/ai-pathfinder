"""
GUI Visualizer using Pygame - Modern Pinterest Style
Provides real-time step-by-step visualization with beautiful card-based design
"""

import pygame
import sys
import time
from typing import Optional
import config
from grid_environment import GridEnvironment, SearchAlgorithms

def draw_rounded_rect(surface, color, rect, radius=10):
    """Draw a rounded rectangle"""
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_card(surface, x, y, width, height, color=config.COLOR_CARD_BG):
    """Draw a card with shadow effect"""
    # Shadow
    shadow_rect = pygame.Rect(x + 4, y + 4, width, height)
    draw_rounded_rect(surface, config.COLOR_SHADOW, shadow_rect, 12)
    # Card
    card_rect = pygame.Rect(x, y, width, height)
    draw_rounded_rect(surface, color, card_rect, 12)
    return card_rect

class ModernButton:
    """Modern Pinterest-style button with rounded corners and hover effects"""
    
    def __init__(self, x, y, width, height, text, color=config.COLOR_BUTTON, icon=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = config.COLOR_BUTTON_HOVER
        self.is_hovered = False
        self.icon = icon
    
    def draw(self, screen, font):
        # Determine color
        color = self.hover_color if self.is_hovered else self.color
        
        # Draw button with rounded corners
        draw_rounded_rect(screen, color, self.rect, 8)
        
        # Draw text
        text_surface = font.render(self.text, True, (255, 255, 255))
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
    """Main GUI class with modern Pinterest-style design"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption("GOOD PERFORMANCE TIME APP")
        self.clock = pygame.time.Clock()
        
        # Modern fonts
        self.title_font = pygame.font.Font(None, 32)
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 20)
        self.tiny_font = pygame.font.Font(None, 16)
        
        # Grid and algorithms
        self.grid = GridEnvironment()
        self.search = SearchAlgorithms(self.grid)
        
        # Visualization state
        self.current_step = 0
        self.is_running = False
        self.is_complete = False
        self.selected_algorithm = 0
        self.animation_speed = config.ANIMATION_DELAY
        
        # Create modern buttons
        button_y = config.WINDOW_HEIGHT - 70
        button_width = 110
        button_height = 45
        button_spacing = 15
        start_x = 30
        
        self.buttons = {
            'run': ModernButton(start_x, button_y, button_width, button_height, '▶ Run', config.COLOR_BUTTON),
            'reset': ModernButton(start_x + button_width + button_spacing, button_y, button_width, button_height, '↻ Reset', (239, 68, 68)),
            'next_algo': ModernButton(start_x + 2 * (button_width + button_spacing), button_y, button_width, button_height, '→ Next', config.COLOR_ACCENT),
            'speed_up': ModernButton(start_x + 3 * (button_width + button_spacing), button_y, 80, button_height, '⚡ Fast', (52, 211, 153)),
            'slow_down': ModernButton(start_x + 3 * (button_width + button_spacing) + 95, button_y, 80, button_height, '🐢 Slow', (251, 146, 60)),
        }
        
        self.last_update_time = time.time()
    
    def draw_grid(self):
        """Draw the grid with modern styling"""
        grid_x = 30
        grid_y = 100
        grid_width = config.GRID_COLS * config.CELL_SIZE
        grid_height = config.GRID_ROWS * config.CELL_SIZE
        
        # Draw card background for grid
        draw_card(self.screen, grid_x - 10, grid_y - 10, grid_width + 20, grid_height + 20)
        
        # Get current visualization state
        frontier = set()
        explored = set()
        
        if self.is_running and self.current_step < len(self.search.frontier_history):
            frontier = set(self.search.frontier_history[self.current_step])
            explored = set(self.search.explored_history[self.current_step])
        elif self.is_complete:
            if len(self.search.explored_history) > 0:
                explored = set(self.search.explored_history[-1])
        
        # Draw cells with rounded corners
        for r in range(config.GRID_ROWS):
            for c in range(config.GRID_COLS):
                pos = (r, c)
                x = grid_x + c * config.CELL_SIZE
                y = grid_y + r * config.CELL_SIZE
                
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
                    color = config.COLOR_CARD_BG
                
                # Draw cell with slight rounding
                cell_rect = pygame.Rect(x + 1, y + 1, config.CELL_SIZE - 2, config.CELL_SIZE - 2)
                draw_rounded_rect(self.screen, color, cell_rect, 4)
    
    def draw_header(self):
        """Draw modern header with algorithm name"""
        # Header card
        header_card = draw_card(self.screen, 30, 20, config.GRID_COLS * config.CELL_SIZE + 20, 60)
        
        # Algorithm name
        algo_text = config.ALGORITHMS[self.selected_algorithm]
        text_surface = self.title_font.render(algo_text, True, config.COLOR_TEXT)
        text_rect = text_surface.get_rect(center=(header_card.centerx, header_card.centery))
        self.screen.blit(text_surface, text_rect)
    
    def draw_stats_panel(self):
        """Draw statistics panel with modern card design"""
        panel_x = config.GRID_COLS * config.CELL_SIZE + 80
        panel_y = 100
        panel_width = 320
        
        # Main stats card
        card_y = panel_y
        draw_card(self.screen, panel_x, card_y, panel_width, 200)
        
        # Title
        title = self.font.render("Statistics", True, config.COLOR_TEXT)
        self.screen.blit(title, (panel_x + 20, card_y + 15))
        
        y_offset = card_y + 55
        
        if self.is_running or self.is_complete:
            # Current step
            step_text = f"Step: {self.current_step}/{len(self.search.frontier_history)}"
            text_surface = self.small_font.render(step_text, True, config.COLOR_TEXT)
            self.screen.blit(text_surface, (panel_x + 20, y_offset))
            y_offset += 30
            
            # Nodes explored
            if self.current_step < len(self.search.explored_history):
                explored_count = len(self.search.explored_history[self.current_step])
            else:
                explored_count = len(self.search.explored_history[-1]) if self.search.explored_history else 0
            
            explored_text = f"Explored: {explored_count} nodes"
            text_surface = self.small_font.render(explored_text, True, config.COLOR_TEXT)
            self.screen.blit(text_surface, (panel_x + 20, y_offset))
            y_offset += 30
            
            # Path length
            if self.is_complete and self.search.path:
                path_text = f"Path Length: {len(self.search.path)}"
                text_surface = self.small_font.render(path_text, True, config.COLOR_ACCENT)
                self.screen.blit(text_surface, (panel_x + 20, y_offset))
                y_offset += 30
        
        # Speed indicator
        speed_text = f"Speed: {self.animation_speed:.3f}s"
        text_surface = self.small_font.render(speed_text, True, config.COLOR_TEXT)
        self.screen.blit(text_surface, (panel_x + 20, y_offset))
        
        # Legend card
        legend_y = card_y + 230
        draw_card(self.screen, panel_x, legend_y, panel_width, 340)
        
        # Legend title
        legend_title = self.font.render("Legend", True, config.COLOR_TEXT)
        self.screen.blit(legend_title, (panel_x + 20, legend_y + 15))
        
        # Legend items
        legend_items = [
            ("Start (S)", config.COLOR_START),
            ("Target (T)", config.COLOR_TARGET),
            ("Wall", config.COLOR_WALL),
            ("Dynamic Obstacle", config.COLOR_DYNAMIC_OBSTACLE),
            ("Frontier", config.COLOR_FRONTIER),
            ("Explored", config.COLOR_EXPLORED),
            ("Final Path", config.COLOR_PATH),
        ]
        
        y_offset = legend_y + 55
        for label, color in legend_items:
            # Color box with rounded corners
            box_rect = pygame.Rect(panel_x + 20, y_offset, 30, 30)
            draw_rounded_rect(self.screen, color, box_rect, 6)
            
            # Label
            text_surface = self.small_font.render(label, True, config.COLOR_TEXT)
            self.screen.blit(text_surface, (panel_x + 60, y_offset + 5))
            y_offset += 40
    
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
            self.draw_header()
            self.draw_grid()
            self.draw_stats_panel()
            self.draw_buttons()
            
            pygame.display.flip()
            self.clock.tick(config.FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    visualizer = GUIVisualizer()
    visualizer.run()
