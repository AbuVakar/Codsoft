import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

        self.root = tk.Tk()
        self.root.title("Rock-Paper-Scissors Game")

        self.create_widgets()

    def create_widgets(self):
        self.label_instruction = ttk.Label(self.root, text="Choose Rock, Paper, or Scissors:")
        self.label_instruction.grid(row=0, column=0, columnspan=3, pady=10)

        self.button_rock = ttk.Button(self.root, text="Rock", command=lambda: self.play_game("rock"))
        self.button_rock.grid(row=1, column=0, padx=5)

        self.button_paper = ttk.Button(self.root, text="Paper", command=lambda: self.play_game("paper"))
        self.button_paper.grid(row=1, column=1, padx=5)

        self.button_scissors = ttk.Button(self.root, text="Scissors", command=lambda: self.play_game("scissors"))
        self.button_scissors.grid(row=1, column=2, padx=5)

        self.label_result = ttk.Label(self.root, text="")
        self.label_result.grid(row=2, column=0, columnspan=3, pady=10)

        self.label_score = ttk.Label(self.root, text="Score: User - 0, Computer - 0")
        self.label_score.grid(row=3, column=0, columnspan=3, pady=10)

        self.button_play_again = ttk.Button(self.root, text="Play Again", command=self.reset_game)
        self.button_play_again.grid(row=4, column=0, columnspan=3, pady=10)

    def play_game(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.label_result.config(text=f"User chose {user_choice}, Computer chose {computer_choice}. {result}")

        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self):
        self.label_score.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.label_result.config(text="")
        self.update_score()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.root.mainloop()
