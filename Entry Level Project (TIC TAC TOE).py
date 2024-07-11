import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def on_button_click(self, row, col):
        if self.board[row][col] == " " and self.current_player == "X":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X")
            if self.check_winner("X"):
                self.show_winner("You win!")
            elif self.is_draw():
                self.show_winner("It's a draw!")
            else:
                self.current_player = "O"
                self.ai_move()

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    self.board[row][col] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        self.board[best_move[0]][best_move[1]] = "O"
        self.buttons[best_move[0]][best_move[1]].config(text="O")
        if self.check_winner("O"):
            self.show_winner("AI wins!")
        elif self.is_draw():
            self.show_winner("It's a draw!")
        self.current_player = "X"

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        return [player, player, player] in win_conditions

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def show_winner(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
