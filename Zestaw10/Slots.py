import tkinter as tk
from PIL import ImageTk, Image
import random

balance = 100 # starting balance
spin_cost = 10 # starting spin cost
min_spin_cost = 1
max_spin_cost = 50

def spin():
    global balance

    if balance < spin_cost:
        wynik_label.config(text="Insufficient funds!")
        return

    balance -= spin_cost

    result = [random.randint(1, 5) for _ in range(3)]

    n1.config(image=resized_images[result[0] - 1])
    n2.config(image=resized_images[result[1] - 1])
    n3.config(image=resized_images[result[2] - 1])

    if result[0] == result[1] and result[1] == result[2]:
        symbol = result[0]
        multiplier = get_multiplier(symbol)
        winnings_amount = multiplier * spin_cost
        balance += winnings_amount
        wynik_label.config(text=f"Jackpot! {multiplier}x - Win {winnings_amount}$")
    else:
        wynik_label.config(text="Try Again")

    update_balance()


def get_multiplier(symbol):
    multipliers = {
        1: 10,  # Cherries
        2: 15,  # Lemon
        3: 30,  # Watermelon
        4: 50,  # Seven
        5: 150  # Jackpot
    }
    return multipliers[symbol]

def update_balance():
    balance_label.config(text=f"Balance: ${balance}")


def increase_spin_cost():
    global spin_cost
    if spin_cost < max_spin_cost:
        spin_cost += 1
        spin_cost_label.config(text=f"Spin Cost: ${spin_cost}")


def decrease_spin_cost():
    global spin_cost
    if spin_cost > min_spin_cost:
        spin_cost -= 1
        spin_cost_label.config(text=f"Spin Cost: ${spin_cost}")


root = tk.Tk()
root.title('777MoneyMaker')
root.configure(width=800, height=800)

images = [
    Image.open("img/cherries.png"),
    Image.open("img/lemon.png"),
    Image.open("img/watermelon.png"),
    Image.open("img/seven.png"),
    Image.open("img/jackpot.png"),
]


def resize_image(image, width, height):
    return ImageTk.PhotoImage(image.resize((width, height)))


image_width = 150
image_height = 150
resized_images = [resize_image(img, image_width, image_height) for img in images]

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10)

n1 = tk.Label(main_frame, image=resized_images[0])
n2 = tk.Label(main_frame, image=resized_images[0])
n3 = tk.Label(main_frame, image=resized_images[0])

n1.grid(row=0, column=0)
n2.grid(row=0, column=1, columnspan=2)
n3.grid(row=0, column=3)

spin_cost_controls = tk.Frame(main_frame)
spin_cost_controls.grid(row=2, column=0)

increase_button = tk.Button(spin_cost_controls, text="+", font=("Arial", 16), command=increase_spin_cost)
increase_button.grid(row=0, column=0)

decrease_button = tk.Button(spin_cost_controls, text="-", font=("Arial", 16), command=decrease_spin_cost)
decrease_button.grid(row=0, column=1)

spin_cost_label = tk.Label(main_frame, text=f"Spin Cost: ${spin_cost}", font=("Arial", 16))
spin_cost_label.grid(row=2, column=3)

spin_button = tk.Button(main_frame, text="Spin", font=("Arial", 40), command=spin, width=10)
spin_button.grid(row=2, column=1, columnspan=2)

wynik_label = tk.Label(main_frame, text="", font=("Arial", 40))
wynik_label.grid(row=1, column=0, columnspan=4)

sidebar_frame = tk.Frame(root, width=200, bg='lightgray', height=400)
sidebar_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

sidebar_title = tk.Label(sidebar_frame, text="Winnings Table", font=("Arial", 16, "bold"), bg='lightgray')
sidebar_title.grid(row=0, column=0, padx=10, pady=10)

winnings_table = [
    ("Cherries x3", "10x"),
    ("Lemon x3", "15x"),
    ("Watermelon x3", "30x"),
    ("Seven x3", "50x"),
    ("Jackpot x3", "150x")
]

for i, (symbol, multiplier) in enumerate(winnings_table):
    tk.Label(sidebar_frame, text=f"{symbol}: {multiplier}", font=("Arial", 12), bg='lightgray').grid(row=i + 1,
                                                                                                     column=0, padx=10,
                                                                                                     pady=5, sticky="w")
balance_label = tk.Label(main_frame, text=f"Balance: ${balance}", font=("Arial", 16))
balance_label.grid(row=4, column=0, columnspan=4)

root.mainloop()
