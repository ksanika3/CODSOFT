import tkinter as tk
from tkinter import messagebox
import random
from tictactoe import TicTacToe, MinimaxAI

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='#2C3E50')  # Dark blue background
        
        # Game state
        self.game = TicTacToe()
        self.ai = MinimaxAI('O')
        self.current_player = 'X'  # Human player starts
        
        # Style configuration
        self.button_font = ('Helvetica', 20, 'bold')
        self.label_font = ('Helvetica', 16)
        self.button_size = 100
        
        # Create and configure the main frame
        self.main_frame = tk.Frame(root, bg='#2C3E50')
        self.main_frame.pack(padx=20, pady=20)
        
        # Create status label
        self.status_label = tk.Label(
            self.main_frame,
            text="Your turn (X)",
            font=self.label_font,
            bg='#2C3E50',
            fg='white'
        )
        self.status_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Create game board buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.main_frame,
                    text="",
                    font=self.button_font,
                    width=4,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col),
                    bg='#34495E',  # Darker blue for buttons
                    fg='white',
                    activebackground='#2980B9'  # Light blue when clicked
                )
                button.grid(row=i+1, column=j, padx=5, pady=5)
                self.buttons.append(button)
        
        # Create reset button
        self.reset_button = tk.Button(
            self.main_frame,
            text="New Game",
            font=self.label_font,
            command=self.reset_game,
            bg='#E74C3C',  # Red color for reset button
            fg='white',
            activebackground='#C0392B'
        )
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=(20, 0))

    def make_move(self, row, col):
        """Handle player's move and AI's response."""
        index = row * 3 + col
        
        # Check if the move is valid
        if self.game.board[index] != ' ' or self.current_player != 'X':
            return
        
        # Make player's move
        if self.game.make_move(index, 'X'):
            self.buttons[index].config(text='X', fg='#E74C3C')  # Red X
            self.update_status()
            
            # Check for game end
            if self.check_game_end():
                return
            
            # AI's turn
            self.root.after(500, self.make_ai_move)  # Add slight delay for better UX

    def make_ai_move(self):
        """Handle AI's move."""
        if not self.game.empty_squares():
            return
            
        # Get AI's move
        ai_move = self.ai.get_move(self.game)
        
        # Make AI's move
        if self.game.make_move(ai_move, 'O'):
            self.buttons[ai_move].config(text='O', fg='#3498DB')  # Blue O
            self.update_status()
            self.check_game_end()

    def update_status(self):
        """Update the status label."""
        if self.game.current_winner:
            if self.game.current_winner == 'X':
                self.status_label.config(text="You win! 🎉", fg='#2ECC71')
            else:
                self.status_label.config(text="AI wins! 🤖", fg='#E74C3C')
        elif not self.game.empty_squares():
            self.status_label.config(text="It's a tie! 🤝", fg='#F1C40F')
        else:
            self.status_label.config(
                text="Your turn (X)" if self.current_player == 'X' else "AI's turn (O)",
                fg='white'
            )

    def check_game_end(self):
        """Check if the game has ended and handle the result."""
        if self.game.current_winner or not self.game.empty_squares():
            if self.game.current_winner == 'X':
                messagebox.showinfo("Game Over", "Congratulations! You win! 🎉")
            elif self.game.current_winner == 'O':
                messagebox.showinfo("Game Over", "AI wins! Better luck next time! 🤖")
            else:
                messagebox.showinfo("Game Over", "It's a tie! 🤝")
            return True
        return False

    def reset_game(self):
        """Reset the game state."""
        self.game = TicTacToe()
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text="", state='normal')
        self.status_label.config(text="Your turn (X)", fg='white')

def main():
    root = tk.Tk()
    root.resizable(False, False)  # Disable window resizing
    app = TicTacToeGUI(root)
    
    # Center the window on the screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == '__main__':
    main() 