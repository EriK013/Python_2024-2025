# Conway's Game Of Life

A Python implementation of Conway's Game of Life with an interactive and visually appealing interface built using Tkinter.

## Features

This project enhances the classic Game of Life by providing a variety of functionalities, including:
- **Grid Navigation and Zoom**: Move around the grid and zoom in/out to explore different areas of the simulation.
- **Save and Load Grid States**: Save the current grid state to a file and load it later to continue where you left off.
- **Customizable Rules**: Modify the rules of the game (e.g., survival, birth conditions and neighborhood) for a personalized experience.
- **Control over speed**: Increase or decrease speed of the simulation.
- **Live cells and iteration count**: Keep track of current live cells on grid and the iteration count.
- **Dynamic Visualization**: Enjoy a graphical representation of the evolving grid.

## Project Structure

The project is organized as follows:
- *actions.py*  Handles actions such as grid updates and interactions 
- *main.py* Entry point of the application 
- *saved* Directory containing saved grid states
- *settings.py* Contains application settings and configurations
- *style.py* Defines graphical styles and appearance\

### How to run
``` 
git clone https://github.com/EriK013/Python_2024-2025.git
cd finalProject
python main.py
```

### How it works
1. Grid Navigation and Zoom: Use your mouse or keyboard shortcuts to pan and zoom in/out.
2. Saving and Loading: Save the current grid state using the provided save option. Load a previously saved state from the saved directory.
3. Customizing Rules: Access the settings menu to tweak survival and birth rules, providing a flexible way to experiment with new patterns.
4. Visualization: The grid dynamically updates based on the rules, showcasing the evolution of cells over time.


