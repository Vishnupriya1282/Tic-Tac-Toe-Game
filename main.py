import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = "X"
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font="Arial 20 bold", width=25, height=10,
                                   command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                self.board[i][j] = button

    def click(self, row, col):
        if self.board[row][col]["text"] == "" and self.check_winner() is False:
            self.board[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                response = messagebox.askyesno("Tic Tac Toe", "Do you want to continue playing")
                if response:
                    self.reset_board()
                else:
                    self.root.destroy()
               
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
                response = messagebox.askyesno("Tic Tac Toe", "Do you want to continue playing")
                if response:
                    self.reset_board()
                else:
                    self.root.destroy()
               
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in range(3):
            if self.board[row][0]["text"] == self.board[row][1]["text"] == self.board[row][2]["text"] != "":
                return True
        for col in range(3):
            if self.board[0][col]["text"] == self.board[1][col]["text"] == self.board[2][col]["text"] != "":
                return True
        if self.board[0][0]["text"] == self.board[1][1]["text"] == self.board[2][2]["text"] != "":
            return True
        if self.board[0][2]["text"] == self.board[1][1]["text"] == self.board[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col]["text"] == "":
                    return False
        return True

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col]["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()



