import pygame
import numpy as np

pygame.init()

WIDTH, HEIGHT = 800, 800
SIDEBAR_WIDTH = 200
CELL_SIZE = 20
ROWS, COLS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
FPS = 5

screen = pygame.display.set_mode((WIDTH + SIDEBAR_WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

# Buttons
BUTTONS = [
    {"label": "Play", "rect": pygame.Rect(WIDTH + 20, 50, 160, 40)},
    {"label": "Grid", "rect": pygame.Rect(WIDTH + 20, 110, 160, 40)},
    {"label": "Random", "rect": pygame.Rect(WIDTH + 20, 170, 160, 40)},
    {"label": "Save", "rect": pygame.Rect(WIDTH + 20, 230, 160, 40)},
    {"label": "Load", "rect": pygame.Rect(WIDTH + 20, 290, 160, 40)},
    {"label": "Increase FPS", "rect": pygame.Rect(WIDTH + 20, 350, 160, 40)},
    {"label": "Decrease FPS", "rect": pygame.Rect(WIDTH + 20, 410, 160, 40)},
    {"label": "Clear", "rect": pygame.Rect(WIDTH + 20, 470, 160, 40)}
]

grid = np.zeros((ROWS, COLS), dtype=bool)
iteration_count = 0
show_grid = True

def draw_grid():
    if show_grid:
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_cells():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row, col]:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_sidebar(paused):
    pygame.draw.rect(screen, GRAY, (WIDTH, 0, SIDEBAR_WIDTH, HEIGHT))
    font = pygame.font.Font(None, 36)
    for button in BUTTONS:
        if button["label"] == "Play" or button["label"] == "Pause":
            button["label"] = "Pause" if not paused else "Play"
        pygame.draw.rect(screen, WHITE, button["rect"], border_radius=5)
        text = font.render(button["label"], True, BLACK)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)

    live_cells_count = np.sum(grid)
    count_text = font.render(f"Live Cells: {live_cells_count}", True, WHITE)
    screen.blit(count_text, (WIDTH + 20, 530))

    iteration_text = font.render(f"Iterations: {iteration_count}", True, WHITE)
    screen.blit(iteration_text, (WIDTH + 20, 570))

    fps_text = font.render(f"FPS: {FPS}", True, WHITE)
    screen.blit(fps_text, (WIDTH + 20, 610))

def check_button_click(pos):
    for button in BUTTONS:
        if button["rect"].collidepoint(pos):
            return button["label"]
    return None

def generate_random_grid():
    global grid
    grid = np.random.choice([False, True], size=(ROWS, COLS), p=[0.8, 0.2])

def save_grid():
    np.save("grid.npy", grid)
    print("Grid saved!")

def load_grid():
    global grid
    try:
        grid = np.load("grid.npy")
        print("Grid loaded!")
    except FileNotFoundError:
        print("No saved grid found.")

def clear_grid():
    global grid, iteration_count, FPS
    grid.fill(False)
    iteration_count = 0
    FPS = 5
    print("Grid cleared!")

def update_grid():
    global grid
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
    new_grid = np.copy(grid)
    for row in range(ROWS):
        for col in range(COLS):
            live_neighbors = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r, c]:
                    live_neighbors += 1
            if grid[row, col]:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row, col] = False
            else:
                if live_neighbors == 3:
                    new_grid[row, col] = True
    grid = new_grid

def main():
    global iteration_count, FPS, show_grid
    running = True
    paused = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if x < WIDTH:
                        grid[y // CELL_SIZE, x // CELL_SIZE] = not grid[y // CELL_SIZE, x // CELL_SIZE]
                    else: # SIDEBAR
                        action = check_button_click(event.pos)
                        if action == "Play" or action == "Pause":
                            paused = not paused
                        elif action == "Grid":
                            show_grid = not show_grid
                        elif action == "Random":
                            generate_random_grid()
                            iteration_count = 0
                        elif action == "Save":
                            save_grid()
                        elif action == "Load":
                            load_grid()
                        elif action == "Increase FPS":
                            FPS += 5
                        elif action == "Decrease FPS" and FPS > 5:
                            FPS -= 5
                        elif action == "Clear":
                            clear_grid()

        if not paused:
            update_grid()
            iteration_count += 1

        draw_cells()
        draw_grid()
        draw_sidebar(paused)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
