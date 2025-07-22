import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False  

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", width=10, height=3, font=("Arial", 18, "bold"),
                               bg="white", command=lambda i=i: self.on_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Reset Button
        self.reset_button = tk.Button(self.master, text="Reset", font=("Arial", 14),command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

    def on_click(self, index):
        if self.board[index] == " " and not self.game_over:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, 
                                       bg="#FF0000" if self.current_player == "X" else "#0000FF")  # Change color

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.highlight_winner()
                self.game_over = True
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                                (0, 4, 8), (2, 4, 6)]  
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                self.winning_combo = combo  
                return True
        return False

    def highlight_winner(self):
        for index in self.winning_combo:
            self.buttons[index].config(bg="#90EE90")  # Highlight winning buttons in green

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ", bg="white")  

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
