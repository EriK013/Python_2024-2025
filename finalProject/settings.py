# WINDOW SETTINGS
WIDTH, HEIGHT = 2000, 2000 # DIMENSIONS OF GRID SO GAME BOARD
SIDEBAR_WIDTH = 10
CELL_SIZE = 20 # SIZE OF ONE CELL
FPS = 5 # STARTING FPS
MAX_FPS = 120

# Game rules
SURVIVAL = [2, 3] # How many cells to survive
BIRTH = [3] # How many cells to produce another cell
DIRECTIONS_MOORE = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
DIRECTIONS_NEUMANN = [(0,1) , (1, 0), (0, -1), (-1, 0)]
DIRECTIONS = DIRECTIONS_MOORE
DISTANCE_OPTIONS = ['Moore', 'Von Neumann']

# COLOR SETTINGS
CELL_COLOR =  '#ffffff'
CELL_OUTLINE_COLOR = '#ffffff'
GRID_COLOR = '#ffffff'
