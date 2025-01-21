from tkinter import ttk
import settings
from style import TkinterStyle
from finalProject.actions import *
from tkinter.colorchooser import askcolor
import re

class App(tk.Frame):
    def __init__(self):
        self.WIDTH, self.HEIGHT = settings.WIDTH, settings.HEIGHT
        self.CELL_SIZE = settings.CELL_SIZE
        self.CELL_COLOR = settings.CELL_COLOR
        self.CELL_OUTLINE_COLOR = settings.CELL_OUTLINE_COLOR
        self.GRID_COLOR = settings.GRID_COLOR
        super().__init__()
        self.SIDEBAR_WIDTH = settings.SIDEBAR_WIDTH
        self.FPS = settings.FPS
        self.show_grid = False
        self.paused = True
        self.iteration = 0
        self.zoom_level = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.settings_popup = None
        self.grid = np.zeros((self.WIDTH // self.CELL_SIZE, self.HEIGHT // self.CELL_SIZE), dtype=bool)
        self.initUI()

    def initUI(self):
        style = TkinterStyle()
        self.master.title('Game of Life')
        self.master.geometry("5000x5000")
        self.pack(fill=tk.BOTH, expand=True)
        style.style_frame(self)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(5, weight=1)

        self.iteration_label = tk.Label(self, text=f'Iterations: {self.iteration}')
        style.style_label(self.iteration_label)
        self.iteration_label.grid(sticky=tk.W, pady=5, padx=5)

        self.canvas = tk.Canvas(self, bg='black')
        draw_grid(self)
        self.canvas.grid(row=1, column=0, columnspan=2, rowspan=5, padx=5, pady=5, sticky=tk.E + tk.W + tk.S + tk.N)
        self.canvas.bind("<Button-1>", lambda event: left_click(self, event))
        self.canvas.bind("<B3-Motion>", lambda event: right_drag(self, event))
        self.canvas.bind("<Button-4>", lambda event: zoom_in(self, event))
        self.canvas.bind("<Button-5>", lambda event: zoom_out(self, event))
        self.canvas.bind("<ButtonPress-3>", lambda event: self.start_drag(event))

        righbar = tk.Frame(self)
        style.style_frame(righbar)
        righbar.grid(row=1, column=3)

        pbn = tk.Button(righbar, text='Play/Pause', width=settings.SIDEBAR_WIDTH, command=lambda: play(self))
        style.style_button(pbn)
        pbn.pack()

        gbn = tk.Button(righbar, text='Grid', width=settings.SIDEBAR_WIDTH, command=lambda: show_hide_grid(self))
        style.style_button(gbn)
        gbn.pack()

        rbn = tk.Button(righbar, text='Random', width=settings.SIDEBAR_WIDTH, command=lambda: generate_random_grid(self))
        style.style_button(rbn)
        rbn.pack()

        cbn = tk.Button(righbar, text='Clear', width=settings.SIDEBAR_WIDTH, command=lambda: clear(self))
        style.style_button(cbn)
        cbn.pack()

        footbar = tk.Frame(self)
        style.style_frame(footbar)
        footbar.grid(row=6, column=0)

        ifbn = tk.Button(footbar, text='+FPS', command=lambda: increase_fps(self))
        style.style_button(ifbn)
        ifbn.pack(side=tk.LEFT)

        dfbn = tk.Button(footbar, text='-FPS', command=lambda: decrease_fps(self))
        style.style_button(dfbn)
        dfbn.pack(side=tk.LEFT)

        sbn = tk.Button(footbar, text='Save', command=lambda: save_pressed(self))
        style.style_button(sbn)
        sbn.pack(side=tk.LEFT)

        lbn = tk.Button(footbar, text='Load', command=lambda: load_pressed(self))
        style.style_button(lbn)
        lbn.pack(side=tk.LEFT)

        self.fps_label = tk.Label(footbar, text=f'FPS: {self.FPS}')
        style.style_label(self.fps_label)
        self.fps_label.pack(side=tk.LEFT, padx=10)

        self.lvc = tk.Label(footbar, text=f'Live Cells: {np.sum(self.grid)}')
        style.style_label(self.lvc)
        self.lvc.pack(side=tk.LEFT, padx=10)

        setbn = tk.Button(self, text='Settings', width=settings.SIDEBAR_WIDTH, pady=3, command=self.open_settings)
        style.style_button(setbn)
        setbn.grid(row=6, column=3)

    def start_drag(self, event):
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y

    def open_settings(self):
        if self.settings_popup is None:
            self.settings_popup = tk.Toplevel(self)
            self.settings_popup.title("Settings")
            self.settings_popup.geometry("400x400")

            notebook = ttk.Notebook(self.settings_popup)

            # GAME RULES TAB
            game_rules_tab = ttk.Frame(notebook)
            notebook.add(game_rules_tab, text="Game Rules")

            tk.Label(game_rules_tab, text="Set Game Rules", font=("Arial", 14)).pack(pady=10)

            tk.Label(game_rules_tab, text="Birth Rules (e.g., 3):").pack(anchor=tk.W, padx=10)
            birth_rules_entry = tk.Entry(game_rules_tab)
            birth_rules_entry.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(game_rules_tab, text="Survival Rules (e.g., 2,3):").pack(anchor=tk.W, padx=10)
            survival_rules_entry = tk.Entry(game_rules_tab)
            survival_rules_entry.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(game_rules_tab, text="Neighborhood").pack(anchor=tk.W, padx=10)
            survival_rules_combobox = ttk.Combobox(game_rules_tab, values=settings.DISTANCE_OPTIONS)
            survival_rules_combobox.pack(fill=tk.X, padx=10, pady=5)

            save_rules_button = tk.Button(
                game_rules_tab, text="Save Rules",
                command=lambda: self.update_game_rules(birth_rules_entry.get(), survival_rules_entry.get(),
                                                       survival_rules_combobox.get())
            )
            save_rules_button.pack(pady=10)


            # COLOR TAB
            display_tab = ttk.Frame(notebook)
            notebook.add(display_tab, text="Display")

            tk.Label(display_tab, text="Display Settings", font=("Arial", 14)).pack(pady=10)

            tk.Label(display_tab, text="Cell Color:").pack(anchor=tk.W, padx=10)
            cell_color_button = tk.Button(display_tab, text="Pick Cell Color",
                                          command=lambda: self.pick_color("CELL_COLOR"))
            cell_color_button.pack(pady=5)

            tk.Label(display_tab, text="Cell Outline Color:").pack(anchor=tk.W, padx=10)
            cell_outline_color_button = tk.Button(display_tab, text="Pick Cell Outline Color",
                                                  command=lambda: self.pick_color("CELL_OUTLINE_COLOR"))
            cell_outline_color_button.pack(pady=5)

            tk.Label(display_tab, text="Grid Color:").pack(anchor=tk.W, padx=10)
            grid_color_button = tk.Button(display_tab, text="Pick Grid Color",
                                          command=lambda: self.pick_color("GRID_COLOR"))
            grid_color_button.pack(pady=5)

            notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

            self.settings_popup.protocol("WM_DELETE_WINDOW", self.close_settings)
        else:
            self.settings_popup.lift()

    def close_settings(self):
        self.settings_popup.destroy()
        self.settings_popup = None

    def pick_color(self, color_attribute):
        color_code = askcolor(title=f"Pick {color_attribute}")[1]
        if color_code:
            setattr(settings, color_attribute, color_code)
            print(f"{color_attribute} set to {color_code}")

    def update_game_rules(self, birth_rules, survival_rules, neighborhood_type):
        pattern = r'^\d+(\s*,\s*\d+)*$'

        if re.match(pattern, birth_rules):
            settings.BIRTH = [int(x.strip()) for x in birth_rules.split(",")]
            print(f"Updated Birth Rules: {settings.BIRTH}")
        else:
            print("Invalid Birth Rules entered. Please enter valid integers separated by commas.")

        if re.match(pattern, survival_rules):
            settings.SURVIVAL = [int(x.strip()) for x in survival_rules.split(",")]
            print(f"Updated Survival Rules: {settings.SURVIVAL}")
        else:
            print("Invalid Survival Rules entered. Please enter valid integers separated by commas.")

        if neighborhood_type == "Moore":
            settings.DIRECTIONS = settings.DIRECTIONS_MOORE
            print(f"Updated Neighborhood: {settings.DIRECTIONS}")
        elif neighborhood_type == "Von Neumann":
            settings.DIRECTIONS = settings.DIRECTIONS_NEUMANN
            print(f"Updated Neighborhood: {settings.DIRECTIONS}")

    def game_loop(self):
        self.canvas.delete('all')
        draw_cells(self)
        if not self.paused:
            update_grid(self)
            self.iteration += 1
            self.iteration_label.config(text=f'Iteration: {self.iteration}')
            self.lvc.config(text=f'Live Cells: {np.sum(self.grid)}')
        draw_grid(self)
        self.after(1000 // self.FPS, self.game_loop)



def main():
    root = tk.Tk()
    app = App()
    app.game_loop()
    root.mainloop()

if __name__ == '__main__':
    main()