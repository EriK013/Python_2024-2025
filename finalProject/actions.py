import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np
import settings

#Game Functions
def update_grid(app_instance):
    directions = settings.DIRECTIONS
    new_grid = np.copy(app_instance.grid)
    for row in range(app_instance.grid.shape[0]):
        for col in range(app_instance.grid.shape[1]):
            live_neighbors = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (0 <= r < app_instance.grid.shape[0] and 0 <= c < app_instance.grid.shape[1]
                        and app_instance.grid[r, c]):
                    live_neighbors += 1
            if app_instance.grid[row, col]:
                if live_neighbors not in settings.SURVIVAL:
                    new_grid[row, col] = False
            else:
                if live_neighbors in settings.BIRTH:
                    new_grid[row, col] = True
    app_instance.grid = new_grid

def generate_random_grid(app_instance):
    grid = np.random.choice([False, True], size=(app_instance.grid.shape[0], app_instance.grid.shape[1]),
                            p=[0.8, 0.2])
    app_instance.grid = grid


def show_hide_grid(app_instance):
    app_instance.show_grid = not app_instance.show_grid


def draw_cells(app_instance):
    app_instance.canvas.delete('all')
    size = app_instance.CELL_SIZE * app_instance.zoom_level
    for row in range(0, app_instance.grid.shape[0]):
        for col in range(0, app_instance.grid.shape[1]):
            if app_instance.grid[row][col]:
                x1 = col * size + app_instance.offset_x
                y1 = row * size + app_instance.offset_y
                x2 = x1 + size
                y2 = y1 + size
                app_instance.canvas.create_rectangle(x1, y1, x2, y2, fill=settings.CELL_COLOR, outline=settings.CELL_OUTLINE_COLOR)
    draw_grid(app_instance)

def draw_grid(app_instance):
    app_instance.canvas.delete('grid')
    if app_instance.show_grid:
        app_instance.canvas.delete("grid")
        size = app_instance.CELL_SIZE * app_instance.zoom_level
        width, height = app_instance.canvas.winfo_width(), app_instance.canvas.winfo_height()

        start_col = max(0, int(-app_instance.offset_x // size))
        end_col = min(app_instance.grid.shape[1], int((width - app_instance.offset_x) // size) + 1)
        start_row = max(0, int(-app_instance.offset_y // size))
        end_row = min(app_instance.grid.shape[0], int((height - app_instance.offset_y) // size) + 1)

        # Draw only the visible grid lines
        for col in range(start_col, end_col):
            x = col * size + app_instance.offset_x
            app_instance.canvas.create_line(x, 0, x, height, fill=settings.GRID_COLOR, tags="grid")
        for row in range(start_row, end_row):
            y = row * size + app_instance.offset_y
            app_instance.canvas.create_line(0, y, width, y, fill=settings.GRID_COLOR, tags="grid")
            
def play(app_instance):
    app_instance.paused = not app_instance.paused

# Grid controls
def left_click(app_instance, event):
    size = app_instance.CELL_SIZE * app_instance.zoom_level
    col = int((event.x - app_instance.offset_x) / size)
    row = int((event.y - app_instance.offset_y) / size)
    if 0 <= row < app_instance.grid.shape[0] and 0 <= col < app_instance.grid.shape[1]:
        app_instance.grid[row][col] = not app_instance.grid[row][col]
        draw_cells(app_instance)


def right_drag(app_instance, event):
    dx = event.x - app_instance.last_mouse_x
    dy = event.y - app_instance.last_mouse_y
    app_instance.offset_x += dx
    app_instance.offset_y += dy
    app_instance.last_mouse_x = event.x
    app_instance.last_mouse_y = event.y
    draw_cells(app_instance)

def zoom_in(app_instance, event):
    zoom_factor = 1.1
    zoom(zoom_factor, app_instance,event)

def zoom_out(app_instance, event):
    zoom_factor = 0.9
    zoom(zoom_factor, app_instance,event)

def zoom(zoom_factor, app_instance,event):
    app_instance.zoom_level *= zoom_factor

    mouse_x = event.x
    mouse_y = event.y
    app_instance.offset_x = mouse_x - zoom_factor * (mouse_x - app_instance.offset_x)
    app_instance.offset_y = mouse_y - zoom_factor * (mouse_y - app_instance.offset_y)

    draw_cells(app_instance)

# Window functions
def save_pressed(app_instance):
    filename = tk.simpledialog.askstring("Save file", "Enter file name: ")
    if filename:
        os.makedirs("saved", exist_ok=True)
        filepath = os.path.join("saved", filename + ".npy")
        np.save(filepath, app_instance.grid)
        tk.messagebox.showinfo("Game of Life", f"Grid {filename}.np saved!")

def load_pressed(app_instance):
    filename = tk.simpledialog.askstring("Load file", "Enter file name: ")
    filepath = os.path.join("saved", filename + ".npy")
    try:
        app_instance.grid = np.load(filepath)
        tk.messagebox.showinfo("Game of Life", f"Grid {filename}.npy loaded!")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")


def increase_fps(app_instance):
    if app_instance.FPS < settings.MAX_FPS:
        app_instance.FPS += 5
        app_instance.fps_label.config(text=f"FPS: {app_instance.FPS}")

def decrease_fps(app_instance):
    if app_instance.FPS > 5:
        app_instance.FPS -= 5
        app_instance.fps_label.config(text=f"FPS: {app_instance.FPS}")

def clear(app_instance):
    app_instance.grid.fill(False)
    app_instance.FPS = 5
    app_instance.iteration = 0
    app_instance.fps_label.config(text=f"FPS: {app_instance.FPS}")
    app_instance.iteration_label.config(text=f"Iteration: {app_instance.iteration}")
    app_instance.lvc.config(text=f'Live Cells: {0}')

