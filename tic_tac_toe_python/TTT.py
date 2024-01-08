import tkinter as tk
from tkinter import messagebox

def check_for_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[row][0]['text']} wins!")
            reset_game()
            return
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[0][col]['text']} wins!")
            reset_game()
            return
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        messagebox.showinfo("Tic Tac Toe", f"Player {buttons[0][0]['text']} wins!")
        reset_game()
        return
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        messagebox.showinfo("Tic Tac Toe", f"Player {buttons[0][2]['text']} wins!")
        reset_game()
        return
    if all(buttons[row][col]['text'] != "" for row in range(3) for col in range(3)):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        reset_game()

def on_button_click(r, c):
    if buttons[r][c]['text'] == "" and not game_over.get():
        buttons[r][c]['text'] = "X" if player.get() == "O" else "O"
        player.set(buttons[r][c]['text'])
        check_for_winner()

def reset_game():
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ""
    player.set("X")
    game_over.set(False)

root = tk.Tk()
root.title("Tic Tac Toe")

player = tk.StringVar(value="X")
game_over = tk.BooleanVar(value=False)

buttons = [[tk.Button(root, text="", font='normal 20', width=5, height=2,
                      command=lambda r=row, c=col: on_button_click(r, c))
            for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col)

root.mainloop()
