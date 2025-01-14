import tkinter as tk
import random

def start_game():
    global current_player
    current_player = random.choice(players)
    info_label.config(text=f"{current_player}'s turn")
    for button in buttons:
        button.config(text="", state=tk.NORMAL)

def check_winner():
    for combo in winning_combinations:
        values = [buttons[i].cget("text") for i in combo]
        if values[0] != "" and values.count(values[0]) == 3:
            return values[0]
    return None

def button_click(index):
    global current_player

    if buttons[index].cget("text") == "":
        buttons[index].config(text=current_player, state=tk.DISABLED)
        winner = check_winner()
        if winner:
            info_label.config(text=f"{winner} wins!")
            for button in buttons:
                button.config(state=tk.DISABLED)
        elif all(button.cget("text") != "" for button in buttons):
            info_label.config(text="It's a draw!")
        else:
            current_player = "X" if current_player == "O" else "O"
            info_label.config(text=f"{current_player}'s turn")

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define players and initialize variables
players = ["X", "O"]
current_player = random.choice(players)
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Create UI elements
info_label = tk.Label(root, text=f"{current_player}'s turn", font=("Arial", 16))
info_label.pack(pady=10)

restart_button = tk.Button(root, text="Restart Game", command=start_game)
restart_button.pack(pady=5)

frame = tk.Frame(root)
frame.pack()

buttons = []
for i in range(9):
    button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the game
start_game()

root.mainloop()

