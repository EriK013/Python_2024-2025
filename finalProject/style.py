class TkinterStyle:
    def __init__(self):
        self.bg_color = "#222222"
        self.button_style = {
            "bg": "#4CAF50",
            "highlightbackground": "#333333",
            "fg": "#FFFFFF",
            "font": ("Arial", 12, "bold"),
            "relief": "raised",
            "bd": 3
        }
        self.label_style = {
            "bg": self.bg_color,
            "fg": "#FFFFFF",
            "font": ("Arial", 12)
        }

    def style_button(self, button):
        for key, value in self.button_style.items():
            button[key] = value

    def style_label(self, label):
        for key, value in self.label_style.items():
            label[key] = value

    def style_frame(self, frame):
        frame.configure(bg=self.bg_color)
